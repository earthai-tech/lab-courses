# CSC 2301 week 14: final project, from a raw well log to a pay summary, a figure and an uncertainty range.
# Built by tools/make_csc2301.py, which imports this file and calls build().
import random
from make_csc2301 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, write_csv

NB = 'CSC2301_W14_final_project_kw3.ipynb'
DATA = 'well_log_kw3.csv'
NULL = -999.25

# (top, base, kind): oil sands, a water sand (low RT), a tight limestone, shales elsewhere
LAYERS = [(1812.0, 1821.5, 'oil'), (1840.0, 1843.0, 'oil'), (1866.0, 1880.0, 'water'), (1902.0, 1909.0, 'lime'),
          (1931.0, 1946.5, 'oil'), (1958.0, 1958.5, 'oil'), (1985.0, 1992.0, 'water'), (2020.0, 2031.0, 'oil')]

def make_data():
    rnd = random.Random(2314)
    rows, d = [], 1800.0
    while d <= 2060.0 + 1e-9:
        kind = next((k for t, b, k in LAYERS if t <= d < b), 'shale')
        if kind == 'oil':
            gr, rhob, rt = rnd.gauss(38, 6), rnd.gauss(2.29, 0.03), rnd.lognormvariate(3.4, 0.35)
        elif kind == 'water':
            gr, rhob, rt = rnd.gauss(40, 6), rnd.gauss(2.28, 0.03), rnd.lognormvariate(0.9, 0.25)
        elif kind == 'lime':
            gr, rhob, rt = rnd.gauss(24, 5), rnd.gauss(2.62, 0.03), rnd.lognormvariate(4.2, 0.3)
        else:
            gr, rhob, rt = rnd.gauss(112, 12), rnd.gauss(2.50, 0.04), rnd.lognormvariate(1.2, 0.3)
        vals = [f'{max(gr, 8):.1f}', f'{rhob:.3f}', f'{rt:.2f}']
        if rnd.random() < 0.035:                      # tool problem: LAS null value
            vals[rnd.randrange(3)] = f'{NULL}'
        rows.append({'depth_m': f'{d:.1f}', 'gr_api': vals[0], 'rhob_g_cc': vals[1], 'rt_ohmm': vals[2]})
        d = round(d + 0.5, 1)
    write_csv(DATA, rows)
    return rows

REF = '''>>> import numpy as _np, pandas as _pd
>>> _L = _pd.read_csv('well_log_kw3.csv').replace(-999.25, _np.nan)
>>> _L['vsh'] = ((_L['gr_api'] - 20) / (140 - 20)).clip(0, 1)
>>> _L['phi'] = ((2.65 - _L['rhob_g_cc']) / (2.65 - 1.0)).clip(0, 0.40)
>>> _L['pay'] = (_L['vsh'] < 0.35) & (_L['phi'] >= 0.12) & (_L['rt_ohmm'] >= 15)
>>> def _zones(d, p, min_m=1.0):
...     out, top, last = [], None, None
...     for x, q in list(zip(d, p)) + [(None, False)]:
...         if q and top is None:
...             top = x
...         if not q and top is not None:
...             if last + 0.5 - top >= min_m:
...                 out.append((top, last + 0.5))
...             top = None
...         last = x
...     return out
>>> _Z = _zones(list(_L['depth_m']), list(_L['pay']))
>>> _net = sum(b - t for t, b in _Z)
>>> _phi_pay = _L.loc[_L['pay'], 'phi'].mean()
'''
MC = ('>>> _r = _np.random.default_rng(999); _n = 400_000\n'
      '>>> _S = _r.triangular(2, 4, 7, _n) * 1e6 * _net * _np.clip(_r.normal(_phi_pay, 0.02, _n), 0.05, 0.35) * (1 - _r.uniform(0.25, 0.45, _n)) / 1.2 * 6.2898 / 1e6\n'
      '>>> _P = _np.percentile(_S, [10, 50, 90])\n')
TESTS = {
 "q1": [(">>> import pandas as _pd\n>>> bool(isinstance(log, _pd.DataFrame) and len(log) == len(_pd.read_csv('well_log_kw3.csv')))\nTrue",
         "log: the whole file read with pd.read_csv, one row per depth (do not drop rows in log)."),
        (REF + ">>> bool(not (log[['gr_api', 'rhob_g_cc', 'rt_ohmm']] == -999.25).any().any() and int(log[['gr_api', 'rhob_g_cc', 'rt_ohmm']].isna().sum().sum()) == int(_L[['gr_api', 'rhob_g_cc', 'rt_ohmm']].isna().sum().sum()))\nTrue",
         "Replace the null code -999.25 by NaN: log = log.replace(-999.25, np.nan)."),
        (REF + ">>> bool(n_bad == int(_L[['gr_api', 'rhob_g_cc', 'rt_ohmm']].isna().any(axis=1).sum()))\nTrue", "n_bad: the number of DEPTHS (rows) with at least one missing value: log.isna().any(axis=1).sum().")],
 "q2": [(">>> import pandas as _pd, numpy as _np\n>>> _t = _pd.DataFrame({'gr_api': [10.0, 80.0, 30.0, _np.nan], 'rhob_g_cc': [2.30, 2.40, 2.00, 2.30], 'rt_ohmm': [40.0, 40.0, 5.0, 40.0]})\n"
         ">>> _e = evaluate(_t)\n>>> [round(float(x), 3) for x in _e['vsh'].fillna(-1)], [round(float(x), 3) for x in _e['phi']], [bool(x) for x in _e['pay']]\n"
         "([0.0, 0.5, 0.083, -1.0], [0.212, 0.152, 0.394, 0.212], [True, False, False, False])",
         "vsh = (GR − 20) / (140 − 20) clipped 0–1; phi = (2.65 − RHOB) / 1.65 clipped 0–0.40; pay = vsh < 0.35 & phi ≥ 0.12 & RT ≥ 15. A missing value is never pay."),
        (">>> import pandas as _pd\n>>> _t = _pd.DataFrame({'gr_api': [10.0], 'rhob_g_cc': [2.3], 'rt_ohmm': [40.0]})\n>>> _e = evaluate(_t)\n>>> list(_t.columns)\n['gr_api', 'rhob_g_cc', 'rt_ohmm']",
         "evaluate must return a NEW table (work on df.copy()) and leave its input unchanged."),
        (REF + ">>> bool(_np.array_equal(kw3['pay'].values, _L['pay'].values) and _np.allclose(kw3['phi'], _L['phi'], equal_nan=True))\nTrue",
         "kw3 = evaluate(log): the whole well, including the depths with missing values.")],
 "q3": [(">>> pay_zones([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0], [True, True, True, False, True, False, True])\n[(1.0, 2.5)]",
         "A zone is a run of consecutive pay samples: top = first depth, base = last depth + 0.5 m. Zones thinner than min_m (1.0 m) are dropped."),
        (">>> pay_zones([1.0, 1.5, 2.0, 2.5], [True, True, False, False], min_m=0.5)\n[(1.0, 2.0)]", "min_m is a parameter with default 1.0."),
        (REF + ">>> bool([(float(a), float(b)) for a, b in zones] == [(float(a), float(b)) for a, b in _Z] and abs(net_pay_m - _net) < 1e-9)\nTrue",
         "zones = pay_zones(kw3['depth_m'], kw3['pay']); net_pay_m = sum of (base − top) over the zones."),
        (REF + ">>> bool(abs(phi_pay - _phi_pay) < 1e-9)\nTrue", "phi_pay: mean porosity of the pay samples: kw3.loc[kw3['pay'], 'phi'].mean().")],
 "q4": [(">>> bool(len(fig_kw3.axes) == 3 and fig_kw3.axes[0].yaxis_inverted())\nTrue", "Three tracks sharing depth (plt.subplots(1, 3, sharey=True)), depth increasing downwards."),
        (">>> bool(fig_kw3.axes[2].get_xscale() == 'log')\nTrue", "Resistivity is always shown on a logarithmic scale: ax.set_xscale('log')."),
        (">>> bool(len(fig_kw3.axes[0].patches) >= len(zones))\nTrue", "Shade each pay zone in the GR track with ax.axhspan(top, base, color=..., alpha=0.3)."),
        (">>> import os\n>>> bool(os.path.exists('kw3_logs.png') and os.path.getsize('kw3_logs.png') > 20000)\nTrue",
         "Save the figure as kw3_logs.png (dpi=150, bbox_inches='tight').")],
 "q5": [(REF + MC + ">>> bool(len(stoiip) == 100_000 and p90 < p50 < p10 and all(abs(a / b - 1) < 0.02 for a, b in zip((p90, p50, p10), _P)))\nTrue",
         "100 000 draws: area triangular(2, 4, 7) km², h = net_pay_m, phi normal(phi_pay, 0.02) clipped 0.05–0.35, Sw uniform(0.25, 0.45), Bo 1.2. P90 is the 10th percentile."),
        (REF + ">>> _want = f'KW-3: {len(zones)} pay zones, net pay {net_pay_m:.1f} m, mean porosity {phi_pay:.3f}, STOIIP P90 {p90:.1f} / P50 {p50:.1f} / P10 {p10:.1f} MMbbl'\n"
               ">>> bool(open('kw3_summary.txt', encoding='utf-8').read().strip() == _want)\nTrue",
         "kw3_summary.txt: one line, exactly in the format shown, built from your own variables.")],
}

def notebook():
    cells = [
        header(14, 'Final project: evaluating well KW-3', NB, f'''
        Well KW-3 has just reached total depth. The logging company sent the raw file `{DATA}` (synthetic): gamma ray,
        bulk density and deep resistivity every 0.5 m from 1800 to 2060 m. Some samples are missing (the tool wrote
        the null code `-999.25`). Your team must tell the asset manager, **in one notebook and a 5-minute
        presentation**: where the pay is, how thick it is, and how much oil it may hold.

        Every part reuses the course: reading and cleaning (W4, W6, W10), functions (W3, W11), masks (W8),
        runs of intervals (W7), figures (W9), Monte Carlo (W13).

        **Deliverables:** this notebook with all checks passing, `kw3_logs.png`, `kw3_summary.txt`, and 4 slides
        (see the end of the notebook).
        '''),
        setup_cell('w14', [DATA], TESTS),
        otter_cell(),
        md('''
        ## The rules of the evaluation

        | quantity | formula | parameters |
        |---|---|---|
        | shale volume | $V_{sh} = (GR - 20) / (140 - 20)$, clipped to 0–1 | clean line 20 API, shale line 140 API |
        | porosity | $\\phi = (2.65 - \\rho_b) / (2.65 - 1.0)$, clipped to 0–0.40 | sandstone matrix, water |
        | **pay** | $V_{sh} < 0.35$ **and** $\\phi \\ge 0.12$ **and** $R_t \\ge 15$ Ω·m | a missing value is never pay |
        | pay zone | consecutive pay samples, at least 1.0 m thick | each sample = 0.5 m |

        A sand with **low resistivity** is porous but full of salt water: it is not pay. Look for it in the figure.

        Start by looking at the file.
        '''),
        code(f'''
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        raw = pd.read_csv("{DATA}")
        print(raw.shape)
        raw.head()
        '''),
        code('''
        raw.describe()     # what is strange in the min row?
        '''),
        md('''
        ---
        ## Project tasks
        '''),
        *question('q1', '''
        ### Q1. Load and clean

        Read the file into `log` and replace the null code `-999.25` by `np.nan` (keep **every** row: the depths must
        stay regular). Store in `n_bad` the number of depths with at least one missing value.
        ''', '''
        log = ...
        n_bad = ...
        n_bad, len(log)
        '''),
        *question('q2', '''
        ### Q2. A petrophysics function

        Write `evaluate(df)` that returns a **copy** of the table with three new columns: `vsh`, `phi` and `pay`
        (Boolean), following the rules above. No loop: column operations, `.clip`, `&`. Then `kw3 = evaluate(log)`.

        *Note:* a comparison with `NaN` is `False`, so a sample with a missing value is automatically not pay.
        ''', '''
        def evaluate(df):
            """Add vsh, phi and pay columns to a copy of a log table."""
            out = df.copy()
            ...
            return out

        kw3 = evaluate(log)
        kw3.head()
        '''),
        *question('q3', '''
        ### Q3. Pay zones

        Write `pay_zones(depths, pay, min_m=1.0)` that returns the list of zones `(top_m, base_m)`: runs of consecutive
        pay samples, with `top` = first depth and `base` = last depth + 0.5 m, keeping only zones at least `min_m` thick.
        (It is the week 7 intercept algorithm again.) Then store:

        * `zones = pay_zones(kw3["depth_m"], kw3["pay"])`
        * `net_pay_m`: total thickness of the zones
        * `phi_pay`: mean porosity of the pay samples

        Look at your zones: are two of them separated by **one missing sample**? Say in your presentation whether
        you would report them as one zone, and why.
        ''', '''
        def pay_zones(depths, pay, min_m=1.0):
            ...

        zones = ...
        net_pay_m = ...
        phi_pay = ...
        zones, net_pay_m, phi_pay
        '''),
        *question('q4', '''
        ### Q4. The log display

        Build `fig_kw3` with **three tracks** sharing depth: GR, RHOB and RT. Depth downwards, every axis labelled with
        its unit, **RT on a logarithmic scale**, and each pay zone shaded in the GR track with
        `ax.axhspan(top, base, color="gold", alpha=0.3)` (you may shade all tracks). Give it a title and save it as
        `kw3_logs.png` (150 dpi, `bbox_inches="tight"`).
        ''', '''
        fig_kw3, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(9, 10))
        ...
        plt.show()
        '''),
        *question('q5', '''
        ### Q5. How much oil? With uncertainty

        Run a Monte Carlo of 100 000 draws with `rng = np.random.default_rng(14)`:

        | parameter | distribution |
        |---|---|
        | area (km²) | triangular: min 2, most likely 4, max 7 |
        | thickness h (m) | fixed: `net_pay_m` |
        | porosity | normal(`phi_pay`, 0.02), clipped to 0.05–0.35 |
        | Sw | uniform(0.25, 0.45) |
        | Bo | fixed: 1.2 |

        Store the results in `stoiip` (MMbbl, your week 13 formula) and `p90, p50, p10`. Then write
        `kw3_summary.txt`, one line exactly in this format (your numbers):

        ```
        KW-3: 4 pay zones, net pay 40.5 m, mean porosity 0.218, STOIIP P90 51.2 / P50 76.4 / P10 107.3 MMbbl
        ```
        ''', '''
        rng = np.random.default_rng(14)
        N = 100_000
        ...
        stoiip = ...
        p90, p50, p10 = ...

        line = ...
        with open("kw3_summary.txt", "w", encoding="utf-8") as f:
            f.write(line + "\\n")
        print(line)
        '''),
        md('''
        ---
        ## The presentation (5 minutes, 4 slides)

        Present to the "asset manager" as a team. One idea per slide, numbers with units:

        1. **The data and its problems**: what the file contained, how many bad depths, what you did about them.
        2. **The method**: the three pay rules, in plain words; why the low-resistivity sand is not pay.
        3. **The result**: your `kw3_logs.png` figure, the pay zones and the net pay.
        4. **The uncertainty and your recommendation**: P90 / P50 / P10, which parameter worries you most, and what you
           would measure next (a core? a test? a seismic survey?).

        Be ready for one question about your code: any line of the notebook.
        '''),
        *closing('''
        ### Going further (not checked)

        * Change the resistivity cut-off from 15 to 10 and to 25 Ω·m. How sensitive is the net pay? Show it in one small table.
        * Move `evaluate` and `pay_zones` into your `geotools.py` from week 11 and import them.
        * Which parameter widens the P10 − P90 range most? Fix each one at its most likely value in turn.
        '''),
    ]
    save_notebook(NB, 'w14', cells)

def build():
    rows = make_data()
    write_tests('w14', TESTS)
    notebook()
    return f'{len(rows)} log samples; {NB} written'
