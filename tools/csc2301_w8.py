# CSC 2301 week 8: NumPy arrays, vectorised calculations and masks on a full well log.
# Built by tools/make_csc2301.py, which imports this file and calls build().
import random
from make_csc2301 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, write_csv

NB = 'CSC2301_W8_numpy_well_log.ipynb'
DATA = 'well_log_kw2.csv'

def make_data():
    rnd = random.Random(2308)
    rows, d, kind, left = [], 2100.0, 'shale', 0
    while d <= 2400.0 + 1e-9:
        if left <= 0:
            kind = {'shale': 'sand', 'sand': rnd.choice(['shale', 'shale', 'limestone']), 'limestone': 'shale'}[kind]
            left = rnd.choice([6, 8, 10, 14, 20])
        if kind == 'sand':
            gr, rhob, rt = rnd.gauss(40, 8), rnd.gauss(2.30, 0.04), rnd.lognormvariate(3.0, 0.5)
        elif kind == 'limestone':
            gr, rhob, rt = rnd.gauss(25, 6), rnd.gauss(2.58, 0.04), rnd.lognormvariate(4.0, 0.4)
        else:
            gr, rhob, rt = rnd.gauss(105, 12), rnd.gauss(2.52, 0.04), rnd.lognormvariate(1.2, 0.3)
        rows.append({'depth_m': f'{d:.1f}', 'gr_api': f'{max(gr, 8):.1f}', 'rhob_g_cc': f'{rhob:.3f}', 'rt_ohmm': f'{rt:.2f}'})
        d = round(d + 0.5, 1); left -= 0.5
    write_csv(DATA, rows)
    return rows

READ = (">>> import numpy as _np\n>>> _a = _np.loadtxt('well_log_kw2.csv', delimiter=',', skiprows=1)\n"
        ">>> _d, _g, _r, _t = _a[:, 0], _a[:, 1], _a[:, 2], _a[:, 3]\n>>> _phi = (2.65 - _r) / (2.65 - 1.0)\n")
TESTS = {
 "q1": [(">>> import numpy as _np\n>>> bool(isinstance(gr, _np.ndarray) and isinstance(rhob, _np.ndarray))\nTrue", "gr and rhob must be NumPy arrays (not lists)."),
        (READ + ">>> bool(abs(mean_gr - _g.mean()) < 1e-9 and abs(max_rhob - _r.max()) < 1e-9)\nTrue", "Use the array methods .mean() and .max() (or np.mean, np.max).")],
 "q2": [(READ + ">>> bool(phi_d.shape == _r.shape and _np.allclose(phi_d, _phi))\nTrue",
         "Density porosity: (2.65 - rhob) / (2.65 - 1.0), computed on the whole array at once, no loop.")],
 "q3": [(READ + ">>> bool(sand.dtype == bool and _np.array_equal(sand, _g < 60))\nTrue", "sand is a Boolean array: gr < 60."),
        (READ + ">>> bool(n_sand == int((_g < 60).sum()) and abs(sand_phi_mean - _phi[_g < 60].mean()) < 1e-9)\nTrue",
         "Count with .sum() on the mask; average the porosity of the sand samples only: phi_d[sand].mean().")],
 "q4": [(READ + ">>> bool(_np.allclose(vsh, _np.clip((_g - 25) / (130 - 25), 0, 1)))\nTrue",
         "V_sh = (GR - 25) / (130 - 25), clipped to 0–1 with np.clip, no loop.")],
 "q5": [(READ + ">>> _v = _np.clip((_g - 25) / (130 - 25), 0, 1)\n>>> _pay = (_v < 0.35) & (_phi >= 0.10) & (_t >= 10)\n"
               ">>> bool(abs(net_pay_m - 0.5 * _pay.sum()) < 1e-9)\nTrue",
         "Pay: vsh < 0.35 AND phi_d ≥ 0.10 AND rt ≥ 10 ohm·m. Combine masks with & and brackets; each sample is 0.5 m."),
        (READ + ">>> _v = _np.clip((_g - 25) / (130 - 25), 0, 1)\n>>> _pay = (_v < 0.35) & (_phi >= 0.10) & (_t >= 10)\n"
               ">>> bool(abs(top_pay_m - _d[_pay][0]) < 1e-9)\nTrue", "top_pay_m is the depth of the shallowest pay sample: depth[pay][0].")],
}

def notebook():
    cells = [
        header(8, 'NumPy arrays: calculations on a whole log', NB, '''
        A modern well log has tens of thousands of samples. Loops work, but they are slow to write and slow to run.
        **NumPy** stores numbers in **arrays** and applies a formula to every element at once.
        The data are four logs from well KW-2 (synthetic), every 0.5 m from 2100 to 2400 m: gamma ray (GR),
        bulk density (RHOB) and deep resistivity (RT).

        **What you will practise:** creating arrays · element-wise arithmetic · `mean`, `max`, `sum` ·
        Boolean masks · `&` and `|` · `np.clip`, `np.where` · indexing with a mask.
        '''),
        setup_cell('w8', [DATA], TESTS),
        otter_cell(),
        md('''
        ## 1. From a list to an array
        '''),
        code('''
        import numpy as np

        values = [2.31, 2.45, 2.52, 2.28]
        a = np.array(values)
        print(a * 2)               # every element times 2
        print(a - 1.0)
        print(a.mean(), a.max(), a.shape, a.dtype)
        print([v * 2 for v in values])   # the same with a list needs a loop
        '''),
        md('''
        ## 2. Loading the log

        `np.loadtxt` reads a table of numbers into a 2-D array. Column `k` is `table[:, k]`.
        '''),
        code(f'''
        table = np.loadtxt("{DATA}", delimiter=",", skiprows=1)
        print(table.shape)          # (rows, columns)
        depth = table[:, 0]
        print(depth[:5], depth[-1])
        '''),
        md('''
        ## 3. Masks: choosing elements with a condition

        A comparison on an array gives a **Boolean array**. Use it to count, or to select.
        '''),
        code('''
        x = np.array([45.0, 110.0, 38.0, 95.0, 52.0])
        clean = x < 60
        print(clean)                 # [ True False  True False  True]
        print(clean.sum())           # True counts as 1 -> 3
        print(x[clean])              # only the selected values
        print(x[(x > 40) & (x < 100)])   # & = and, | = or; brackets are required
        print(np.where(x < 60, "sand", "shale"))
        print(np.clip(np.array([-0.2, 0.5, 1.3]), 0, 1))
        '''),
        md('''
        ---
        ## Exercises

        From now on, **no `for` loop** over the samples: use array operations.
        '''),
        *question('q1', '''
        ### Q1. The arrays

        From `table`, create the arrays `gr` (column 1), `rhob` (column 2) and `rt` (column 3). Store the mean GR
        in `mean_gr` and the highest density in `max_rhob`.
        ''', '''
        gr = ...
        rhob = ...
        rt = ...
        mean_gr = ...
        max_rhob = ...
        mean_gr, max_rhob
        '''),
        *question('q2', '''
        ### Q2. Density porosity

        For a sandstone (grain density 2.65 g/cm³) filled with water (1.0 g/cm³), porosity from the density log is

        $$\\phi_D = \\frac{2.65 - \\rho_b}{2.65 - 1.0}$$

        Compute `phi_d` for every sample in one line.
        ''', '''
        phi_d = ...
        phi_d[:5]
        '''),
        *question('q3', '''
        ### Q3. Sand samples

        Create the mask `sand` (GR < 60), count the sand samples in `n_sand`, and store in `sand_phi_mean` the mean
        density porosity of the sand samples only.
        ''', '''
        sand = ...
        n_sand = ...
        sand_phi_mean = ...
        n_sand, sand_phi_mean
        '''),
        *question('q4', '''
        ### Q4. Shale volume, vectorised

        In week 2 you wrote `vshale` with `if`. Now compute it for the whole log at once, with this well's clean
        and shale lines: $V_{sh} = (GR - 25) / (130 - 25)$, clipped to 0–1 with `np.clip`. Store it in `vsh`.
        ''', '''
        vsh = ...
        vsh.min(), vsh.max()
        '''),
        *question('q5', '''
        ### Q5. Net pay

        A sample is **pay** when `vsh < 0.35` **and** `phi_d >= 0.10` **and** `rt >= 10` ohm·m (high resistivity:
        hydrocarbons, not salt water). Build the mask `pay`, store the pay thickness in `net_pay_m`
        (0.5 m per sample) and the depth of the shallowest pay sample in `top_pay_m`.
        ''', '''
        pay = ...
        net_pay_m = ...
        top_pay_m = ...
        net_pay_m, top_pay_m
        '''),
        *closing('''
        ### Going further (not checked)

        * Time the two ways with `%timeit`: a Python loop computing `phi_d`, and the array formula.
        * With `np.diff` on the pay mask (as integers), find where each pay zone starts and ends.
        '''),
    ]
    save_notebook(NB, 'w8', cells)

def build():
    rows = make_data()
    write_tests('w8', TESTS)
    notebook()
    return f'{len(rows)} log samples; {NB} written'
