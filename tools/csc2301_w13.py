# CSC 2301 week 13: simulation, Monte Carlo estimate of oil in place (STOIIP) with P90 / P50 / P10.
# Built by tools/make_csc2301.py, which imports this file and calls build().
from make_csc2301 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing

NB = 'CSC2301_W13_monte_carlo_stoiip.ipynb'

N = 100_000
REF = (">>> import numpy as _np\n>>> _r = _np.random.default_rng(999)\n>>> _n = 400_000\n"
       ">>> _A = _r.triangular(8, 12, 18, _n); _h = _np.clip(_r.normal(25, 4, _n), 5, None)\n"
       ">>> _p = _r.uniform(0.18, 0.26, _n); _s = _r.uniform(0.20, 0.40, _n)\n"
       ">>> _S = _A * 1e6 * _h * _p * (1 - _s) / 1.25 * 6.2898 / 1e6\n")
TESTS = {
 "q1": [(">>> bool(abs(stoiip_mmbbl(1.0, 10.0, 0.2, 0.25, 1.2) - 7.86225) < 1e-6)\nTrue",
         "STOIIP (MMbbl) = A(km²) × 10⁶ × h × φ × (1 − Sw) / Bo × 6.2898 / 10⁶."),
        (">>> bool(abs(base_case - stoiip_mmbbl(12, 25, 0.22, 0.30, 1.25)) < 1e-9)\nTrue", "base_case uses the most likely values of the table.")],
 "q2": [(">>> import numpy as _np\n>>> _v = stoiip_mmbbl(_np.array([1.0, 2.0]), _np.array([10.0, 10.0]), 0.2, _np.array([0.25, 0.5]), 1.2)\n"
         ">>> bool(_np.allclose(_v, [7.86225, 10.483]))\nTrue",
         "stoiip_mmbbl must work on arrays too: only arithmetic, no if, no loop, no math module."),
        (">>> import numpy as _np\n>>> bool(isinstance(u, _np.ndarray) and u.shape == (5,) and (u >= 0).all() and (u < 1).all())\nTrue",
         "u = rng.uniform(0, 1, 5) with rng = np.random.default_rng(13).")],
 "q3": [(">>> bool(all(len(x) == 100_000 for x in (area, h, phi, sw)))\nTrue", "Draw N = 100_000 values for each parameter (size=N)."),
        (">>> bool(area.min() >= 8 and area.max() <= 18 and abs(area.mean() - 38 / 3) < 0.05)\nTrue",
         "area: rng.triangular(8, 12, 18, N), in km²."),
        (">>> bool(h.min() >= 5 and abs(h.mean() - 25) < 0.1 and 3.8 < h.std() < 4.2)\nTrue",
         "h: rng.normal(25, 4, N), then np.clip(h, 5, None) so that no thickness is below 5 m."),
        (">>> bool(phi.min() >= 0.18 and phi.max() <= 0.26 and sw.min() >= 0.20 and sw.max() <= 0.40 and abs(phi.mean() - 0.22) < 0.002 and abs(sw.mean() - 0.30) < 0.002)\nTrue",
         "phi: rng.uniform(0.18, 0.26, N); sw: rng.uniform(0.20, 0.40, N)."),
        (REF + ">>> bool(len(stoiip) == 100_000 and abs(stoiip.mean() / _S.mean() - 1) < 0.01)\nTrue",
         "stoiip = stoiip_mmbbl(area, h, phi, sw, 1.25): one STOIIP per draw.")],
 "q4": [(">>> import numpy as _np\n>>> bool(_np.allclose([p90, p50, p10], _np.percentile(stoiip, [10, 50, 90])))\nTrue",
         "Industry convention: P90 is the value exceeded 90 % of the time, i.e. the 10th percentile: np.percentile(stoiip, [10, 50, 90])."),
        (REF + ">>> bool(p90 < p50 < p10 and abs(p50 / _np.percentile(_S, 50) - 1) < 0.015)\nTrue", "p90 < p50 < p10.")],
 "q5": [(">>> bool(abs(prob_200 - float((stoiip >= 200).mean())) < 1e-12)\nTrue",
         "The probability is the share of draws with stoiip >= 200: (stoiip >= 200).mean()."),
        (REF + ">>> bool(abs(prob_200 - (_S >= 200).mean()) < 0.01)\nTrue", "prob_200 is a fraction between 0 and 1, not a percentage."),
        (">>> bool(len(ax_mc.patches) >= 10 and len(ax_mc.lines) >= 3 and 'MMbbl' in ax_mc.get_xlabel())\nTrue",
         "Histogram of stoiip in ax_mc, three vertical lines (ax_mc.axvline) at P90, P50, P10, x label with the unit MMbbl.")],
}

def notebook():
    cells = [
        header(13, 'Simulation: Monte Carlo oil in place', NB, '''
        Before drilling, nobody knows the exact size of a reservoir: the area, the thickness and the porosity are
        only known as **ranges**. A single "best guess" hides the risk. **Monte Carlo simulation** draws thousands
        of possible reservoirs at random, computes the oil in place of each, and turns the results into the
        figures every petroleum company reports: **P90, P50, P10**. The same method sizes ore bodies, schedules
        projects and prices risk.

        **What you will practise:** `np.random.default_rng` and a seed · uniform, normal and triangular draws ·
        a vectorised model · percentiles · probabilities as averages of a mask · a histogram with markers.
        '''),
        setup_cell('w13', [], TESTS),
        otter_cell(),
        md('''
        ## 1. Random numbers you can reproduce

        A **generator** with a **seed** gives the same "random" numbers every time: your results can be checked.
        '''),
        code('''
        import numpy as np
        import matplotlib.pyplot as plt

        rng = np.random.default_rng(42)
        print(rng.uniform(0, 1, 3))          # 3 values, any value in [0, 1) equally likely
        print(rng.normal(25, 4, 3))          # mean 25, standard deviation 4
        print(rng.triangular(8, 12, 18, 3))  # min 8, most likely 12, max 18
        '''),
        code('''
        rng = np.random.default_rng(1)
        fig, axes = plt.subplots(1, 3, figsize=(11, 3))
        for ax, (name, x) in zip(axes, [("uniform(0.18, 0.26)", rng.uniform(0.18, 0.26, 20_000)),
                                        ("normal(25, 4)", rng.normal(25, 4, 20_000)),
                                        ("triangular(8, 12, 18)", rng.triangular(8, 12, 18, 20_000))]):
            ax.hist(x, bins=50)
            ax.set_title(name)
        plt.tight_layout()
        plt.show()
        '''),
        md('''
        ## 2. More draws, steadier answers

        The mean of many random draws settles down as their number grows (law of large numbers).
        That is why we use 100 000 draws, not 10.
        '''),
        code('''
        rng = np.random.default_rng(7)
        for n in [10, 100, 1_000, 10_000, 100_000]:
            print(f"{n:>7} draws: mean of a uniform(0, 1) = {rng.uniform(0, 1, n).mean():.4f}")
        '''),
        md('''
        ## 3. The model

        **Stock-tank oil initially in place**, in millions of barrels:

        $$STOIIP = \\frac{A \\times 10^6 \\times h \\times \\phi \\times (1 - S_w)}{B_o} \\times \\frac{6.2898}{10^6}$$

        $A$ area (km²), $h$ net thickness (m), $\\phi$ porosity, $S_w$ water saturation, $B_o$ formation volume
        factor (reservoir m³ per stock-tank m³), 6.2898 barrels per m³.

        | parameter | distribution | values |
        |---|---|---|
        | area $A$ (km²) | triangular | min 8, most likely 12, max 18 |
        | thickness $h$ (m) | normal, no value below 5 | mean 25, std 4 |
        | porosity $\\phi$ | uniform | 0.18 – 0.26 |
        | water saturation $S_w$ | uniform | 0.20 – 0.40 |
        | $B_o$ | fixed | 1.25 |

        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. The deterministic answer

        Write `stoiip_mmbbl(area_km2, h_m, phi, sw, bo)` and store in `base_case` the STOIIP with the most likely
        values (A = 12, h = 25, φ = 0.22, Sw = 0.30, Bo = 1.25).
        ''', '''
        def stoiip_mmbbl(area_km2, h_m, phi, sw, bo):
            ...

        base_case = ...
        base_case
        '''),
        *question('q2', '''
        ### Q2. Ready for arrays

        If your function only uses `+ - * /`, it already works on NumPy arrays: try it below with two arrays.
        Then create `rng = np.random.default_rng(13)` and store five uniform draws between 0 and 1 in `u`.
        ''', '''
        print(stoiip_mmbbl(np.array([10.0, 14.0]), np.array([20.0, 30.0]), 0.22, 0.30, 1.25))

        rng = ...
        u = ...
        u
        '''),
        *question('q3', '''
        ### Q3. 100 000 possible reservoirs

        With `rng` and `N = 100_000`, draw `area`, `h`, `phi` and `sw` following the table (clip `h` at 5 m with
        `np.clip`), then compute `stoiip` for every draw in **one line**.
        ''', '''
        N = 100_000
        area = ...
        h = ...
        phi = ...
        sw = ...
        stoiip = ...
        stoiip.mean(), stoiip.min(), stoiip.max()
        '''),
        *question('q4', '''
        ### Q4. P90, P50, P10

        The industry reports **P90** (a value exceeded with 90 % probability: the low, "proved-like" case),
        **P50** (the median) and **P10** (the high case). P90 is therefore the **10th percentile**.
        Store them in `p90`, `p50`, `p10` with one call to `np.percentile`. Is `base_case` close to `p50`?
        ''', '''
        p90, p50, p10 = ...
        print(f"P90 {p90:.0f}  P50 {p50:.0f}  P10 {p10:.0f} MMbbl   (base case {base_case:.0f})")
        '''),
        *question('q5', '''
        ### Q5. Risk for the manager

        The development is economic if STOIIP ≥ 200 MMbbl. Store in `prob_200` the probability of that (a
        fraction). Then draw the histogram of `stoiip` in `fig_mc, ax_mc` (50 bins), with a vertical line at P90,
        P50 and P10 (`ax_mc.axvline`), the x axis labelled `STOIIP (MMbbl)` and a legend.
        ''', '''
        prob_200 = ...

        fig_mc, ax_mc = plt.subplots(figsize=(7, 4))
        ...
        plt.show()
        prob_200
        '''),
        *closing('''
        ### Going further (not checked)

        * Which parameter matters most? Replace one range at a time by its most likely value and see how much
          P10 − P90 shrinks (a "tornado" analysis).
        * Run the simulation with 100 draws, five times with different seeds. How much does P50 move? And with 100 000?
        '''),
    ]
    save_notebook(NB, 'w13', cells)

def build():
    write_tests('w13', TESTS)
    notebook()
    return f'{NB} written (no data file: the inputs are distributions)'
