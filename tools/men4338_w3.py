# MEN 4338 week 3: spatial continuity, h-scatterplots and the experimental variogram.
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing

NB = 'MEN4338_W3_experimental_variogram.ipynb'
DATA = ['bassam_samples.csv']

RS = (">>> import pandas as _pd, numpy as _np\n>>> _s = _pd.read_csv('bassam_samples.csv')\n"
      ">>> _g = _s[_s['campaign'] == 'grid']\n")
REF = (">>> def _vg(x, y, v, lag, nlags):\n"
       "...     x, y, v = (_np.asarray(a, float) for a in (x, y, v))\n"
       "...     i, j = _np.triu_indices(len(v), 1)\n"
       "...     d = _np.hypot(x[j] - x[i], y[j] - y[i]); sq = 0.5 * (v[j] - v[i]) ** 2\n"
       "...     out = []\n"
       "...     for k in range(1, nlags + 1):\n"
       "...         m = _np.abs(d - k * lag) < lag / 2\n"
       "...         out.append((d[m].mean() if m.any() else _np.nan, sq[m].mean() if m.any() else _np.nan, int(m.sum())))\n"
       "...     return [_np.array(c) for c in zip(*out)]\n")
TESTS = {
 "q1": [(RS + ">>> _n = len(_g)\n>>> bool(n_pairs == _n * (_n - 1) // 2)\nTrue",
         "With n grid holes there are n(n-1)/2 distinct pairs."),
        (RS + ">>> _x, _y = _g['x'].to_numpy(), _g['y'].to_numpy()\n>>> _i, _j = _np.triu_indices(len(_x), 1)\n"
         ">>> _d = _np.hypot(_x[_j] - _x[_i], _y[_j] - _y[_i])\n>>> bool(len(dist) == len(_d) and _np.allclose(_np.sort(dist), _np.sort(_d)))\nTrue",
         "dist holds the distance of every pair of grid holes (use np.triu_indices(n, 1) and np.hypot)."),
        (RS + ">>> _x, _y = _g['x'].to_numpy(), _g['y'].to_numpy()\n>>> _i, _j = _np.triu_indices(len(_x), 1)\n"
         ">>> bool(abs(max_dist - _np.hypot(_x[_j] - _x[_i], _y[_j] - _y[_i]).max()) < 1e-9)\nTrue", "max_dist is the largest pair distance.")],
 "q2": [(RS + ">>> _x, _y, _v = (_g[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n>>> _i, _j = _np.triu_indices(len(_x), 1)\n"
         ">>> _d = _np.hypot(_x[_j] - _x[_i], _y[_j] - _y[_i]); _m = (_d >= 40) & (_d < 60)\n"
         ">>> bool(n_pairs_50 == int(_m.sum()) and len(tail) == len(head) == int(_m.sum()))\nTrue",
         "Keep the pairs with 40 <= d < 60 m; tail and head are the two grades of each kept pair."),
        (RS + ">>> _x, _y, _v = (_g[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n>>> _i, _j = _np.triu_indices(len(_x), 1)\n"
         ">>> _d = _np.hypot(_x[_j] - _x[_i], _y[_j] - _y[_i]); _m = (_d >= 40) & (_d < 60)\n"
         ">>> bool(abs(gamma_50 - 0.5 * ((_v[_j][_m] - _v[_i][_m]) ** 2).mean()) < 1e-9)\nTrue",
         "gamma_50 = 0.5 * mean((head - tail)**2) over these pairs."),
        (RS + ">>> _x, _y, _v = (_g[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n>>> _i, _j = _np.triu_indices(len(_x), 1)\n"
         ">>> _d = _np.hypot(_x[_j] - _x[_i], _y[_j] - _y[_i]); _m = (_d >= 40) & (_d < 60)\n"
         ">>> bool(abs(rho_50 - _np.corrcoef(_v[_i][_m], _v[_j][_m])[0, 1]) < 1e-6)\nTrue",
         "rho_50 = np.corrcoef(tail, head)[0, 1].")],
 "q3": [(">>> import numpy as _np\n>>> _h, _gm, _n = exp_variogram(_np.array([0., 10, 20, 30]), _np.zeros(4), _np.array([1., 2, 4, 7]), 10, 3)\n"
         ">>> bool(_np.allclose(_n, [3, 2, 1]) and _np.allclose(_gm, [7 / 3, 8.5, 18]) and _np.allclose(_h, [10, 20, 30]))\nTrue",
         "Class k (1..nlags) holds the pairs with |d - k*lag| < lag/2; return (mean distance, semivariance, number of pairs) as arrays."),
        (RS + REF + ">>> _r = _vg(_g['x'], _g['y'], _g['au_gpt'], 50, 12)\n>>> _o = exp_variogram(_g['x'].to_numpy(), _g['y'].to_numpy(), _g['au_gpt'].to_numpy(), 50, 12)\n"
         ">>> bool(all(_np.allclose(a, b, equal_nan=True) for a, b in zip(_o, _r)))\nTrue",
         "Your function gives different values on the grid holes: check the class rule and the 0.5 factor.")],
 "q4": [(RS + REF + ">>> _r = _vg(_g['x'], _g['y'], _g['au_gpt'], 50, 12)\n>>> bool(_np.allclose(g_grid, _r[1]) and _np.allclose(h_grid, _r[0]))\nTrue",
         "h_grid, g_grid, n_grid = exp_variogram(...) on the grid holes only, lag 50 m, 12 lags."),
        (RS + REF + ">>> _r = _vg(_s['x'], _s['y'], _s['au_gpt'], 50, 12)\n>>> bool(_np.allclose(g_all, _r[1]))\nTrue",
         "h_all, g_all, n_all = exp_variogram(...) on all samples (grid + infill), lag 50 m, 12 lags."),
        (RS + ">>> bool(abs(var_grid - _g['au_gpt'].var()) < 1e-9 and abs(var_all - _s['au_gpt'].var()) < 1e-9)\nTrue",
         "var_grid and var_all: sample variances (pandas .var()) of the grid holes and of all samples.")],
 "q5": [(">>> import numpy as _np\n>>> bool(_np.array_equal(reliable, n_grid >= 30))\nTrue", "reliable = n_grid >= 30 (a boolean array)."),
        (">>> bool(len(ax_vg.lines) >= 2 and 'm' in ax_vg.get_xlabel())\nTrue",
         "Plot g_grid against h_grid with markers, a dashed horizontal line at var_grid (ax_vg.axhline) and an x label with the unit."),
        (">>> import numpy as _np\n>>> bool(abs(nugget_guess - g_grid[0]) < 1e-12 and abs(sill_guess - var_grid) < 1e-12)\nTrue",
         "nugget_guess = g_grid[0] (first lag), sill_guess = var_grid.")],
}

def notebook():
    cells = [
        header(3, 'Spatial continuity: h-scatterplots and the variogram', NB, '''
        Two holes 25 m apart usually have similar grades; two holes 500 m apart do not. The **variogram** measures
        how quickly that similarity is lost with distance. It is the central tool of geostatistics: kriging,
        simulation and the classification of resources all start from it.

        **What you will practise:** pairs of samples and their distances · h-scatterplots · the semivariance
        $\\gamma(h)$ · lag classes and tolerances · reading nugget, sill and range · the effect of clustered data.
        '''),
        setup_cell('w3', DATA, TESTS),
        otter_cell(),
        md('''
        ## 1. Pairs of samples

        With $n$ samples there are $n(n-1)/2$ pairs. NumPy gives all of them at once with `np.triu_indices`.
        '''),
        code('''
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        samples = pd.read_csv("bassam_samples.csv")
        grid = samples[samples["campaign"] == "grid"]          # the regular 50 m campaign
        x, y, au = grid["x"].to_numpy(), grid["y"].to_numpy(), grid["au_gpt"].to_numpy()

        i, j = np.triu_indices(4, 1)
        print("pairs of 4 samples:", list(zip(i, j)))
        '''),
        md('''
        ## 2. h-scatterplots

        Take every pair separated by roughly a distance $h$, and plot the grade at one end (*tail*) against the
        grade at the other (*head*). Close pairs fall near the 1:1 line; distant pairs scatter.
        '''),
        code('''
        i, j = np.triu_indices(len(x), 1)
        d = np.hypot(x[j] - x[i], y[j] - y[i])

        fig, axes = plt.subplots(1, 3, figsize=(12, 4))
        for ax, h in zip(axes, [50, 150, 400]):
            m = np.abs(d - h) < 10
            ax.scatter(au[i][m], au[j][m], s=4, alpha=0.4)
            ax.plot([0, 4], [0, 4], "k--", lw=0.8)
            r = np.corrcoef(au[i][m], au[j][m])[0, 1]
            ax.set_title(f"h ≈ {h} m · {m.sum()} pairs · r = {r:.2f}")
            ax.set_xlabel("tail (g/t)"); ax.set_ylabel("head (g/t)")
        plt.tight_layout(); plt.show()
        '''),
        md('''
        ## 3. The semivariogram

        The moment of inertia of the h-scatterplot about the 1:1 line is the **semivariance**:

        $$\\gamma(h) = \\frac{1}{2N(h)} \\sum_{(i,j)\\,:\\,d_{ij} \\approx h} \\left(z_i - z_j\\right)^2$$

        Data are never exactly $h$ apart, so pairs are grouped into **lag classes**: class $k$ holds the pairs with
        $|d - k \\cdot lag| < lag/2$. Plot $\\gamma$ against the mean distance of each class and read:

        * the **nugget** $c_0$: the jump at the origin (assay error, very short-scale variability),
        * the **sill**: the plateau, close to the variance of the data,
        * the **range** $a$: the distance where the plateau is reached; beyond it, samples are unrelated.
        '''),
        md('''
        ---
        ## Exercises

        Q1 to Q3 use the **grid holes** only (`x`, `y`, `au` defined above).
        '''),
        *question('q1', '''
        ### Q1. All the pairs

        Store the number of pairs in `n_pairs`, the distance of every pair in the array `dist` and the largest
        distance in `max_dist`.
        ''', '''
        n_pairs = ...
        dist = ...
        max_dist = ...
        n_pairs, max_dist
        '''),
        *question('q2', '''
        ### Q2. One lag by hand

        Keep the pairs with $40 \\le d < 60$ m. Store their number in `n_pairs_50`, the two grades of each pair in
        `tail` (first sample) and `head` (second sample), the semivariance in `gamma_50` and the correlation
        coefficient of the h-scatterplot in `rho_50`.
        ''', '''
        m = ...
        n_pairs_50 = ...
        tail = ...
        head = ...
        gamma_50 = ...
        rho_50 = ...
        n_pairs_50, gamma_50, rho_50
        '''),
        *question('q3', '''
        ### Q3. The experimental variogram

        Write `exp_variogram(x, y, v, lag, nlags)` returning three arrays of length `nlags`: the mean distance of
        the pairs in each class, the semivariance, and the number of pairs (use `np.nan` for an empty class).
        Class $k = 1 \\dots nlags$ holds the pairs with $|d - k \\cdot lag| < lag/2$.
        ''', '''
        def exp_variogram(x, y, v, lag, nlags):
            ...

        exp_variogram(np.array([0., 10, 20, 30]), np.zeros(4), np.array([1., 2, 4, 7]), 10, 3)
        '''),
        *question('q4', '''
        ### Q4. Grid holes versus all holes

        Compute the variogram with lag 50 m and 12 lags:

        * on the grid holes: `h_grid, g_grid, n_grid`,
        * on all samples (grid + infill): `h_all, g_all, n_all`.

        Store the variances `var_grid` and `var_all` (pandas `.var()`). Plot both variograms. Why is the variogram
        of all samples higher and more erratic? (Think about where the infill holes are, and about the
        *proportional effect*: in rich zones grades also vary more.)
        ''', '''
        h_grid, g_grid, n_grid = ...
        h_all, g_all, n_all = ...
        var_grid = ...
        var_all = ...
        '''),
        *question('q5', '''
        ### Q5. Read the variogram

        A lag with fewer than 30 pairs is not reliable: store `reliable = n_grid >= 30`. Plot `g_grid` against
        `h_grid` in `fig_vg, ax_vg` with markers, a dashed horizontal line at `var_grid`, axis labels with units.
        Store your first reading of the nugget (`nugget_guess = g_grid[0]`) and of the sill (`sill_guess = var_grid`),
        and write down the range you see.
        ''', '''
        reliable = ...

        fig_vg, ax_vg = plt.subplots(figsize=(7, 4))
        ...
        plt.show()

        nugget_guess = ...
        sill_guess = ...
        '''),
        *closing('''
        ### Going further (not checked)

        * Draw the **variogram cloud**: every pair as a point (distance, half squared difference). Which pairs are the
          extreme ones?
        * Change the lag to 25 m on the grid holes. Why are half of the classes nearly empty?
        '''),
    ]
    save_notebook(NB, 'w3', cells)

def build():
    write_tests('w3', TESTS)
    notebook()
    return f'{NB} written'
