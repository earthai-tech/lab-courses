# MEN 4338 week 9: kriging a map, kriging variance map, cross-validation and conditional bias.
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, toolbox_cell

NB = 'MEN4338_W9_kriging_maps_validation.ipynb'
DATA = ['bassam_samples.csv', 'bassam_truth_grid.csv']

BASE = (">>> import numpy as _np, pandas as _pd\n>>> _s = _pd.read_csv('bassam_samples.csv'); _x, _y, _v = (_s[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n"
        ">>> _T = _pd.read_csv('bassam_truth_grid.csv')['au_gpt'].to_numpy().reshape(100, 120)[1::2, 1::2]\n"
        ">>> def _gb(dx, dy):\n"
        "...     t = _np.radians(45); u = dx * _np.sin(t) + dy * _np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n"
        "...     h = _np.sqrt(u ** 2 + (2 * w) ** 2); r = _np.minimum(h / 300, 1)\n"
        "...     return _np.where(h > 0, 0.06 + 0.20 * (1.5 * r - 0.5 * r ** 3), 0.0)\n"
        ">>> def _ok(x0, y0, x, y, v, n=16):\n"
        "...     k = _np.argsort(_np.hypot(x - x0, y - y0))[:n]; xs, ys = x[k], y[k]; m = len(k)\n"
        "...     A = _np.ones((m + 1, m + 1)); A[m, m] = 0; A[:m, :m] = _gb(xs[:, None] - xs[None, :], ys[:, None] - ys[None, :])\n"
        "...     b = _np.ones(m + 1); b[:m] = _gb(xs - x0, ys - y0); s = _np.linalg.solve(A, b)\n"
        "...     return float(s[:m] @ v[k]), float(s[:m] @ b[:m] + s[m])\n")
NODES = [(0, 0), (10, 17), (25, 40), (33, 5), (49, 59)]
TESTS = {
 "q1": [(">>> import numpy as _np\n>>> bool(gx.shape == (50, 60) and gy.shape == (50, 60) and gx[0, 0] == 15 and gx[0, -1] == 1195 and gy[-1, 0] == 995)\nTrue",
         "gx, gy = np.meshgrid(np.arange(15, 1200, 20), np.arange(15, 1000, 20)): 50 rows (north) by 60 columns (east)."),
        (">>> bool(n_nodes == 3000)\nTrue", "n_nodes = gx.size.")],
 "q2": [(BASE + f">>> bool(ok_map.shape == (50, 60) and ok_varmap.shape == (50, 60))\nTrue", "ok_map and ok_varmap have the shape of gx."),
        (BASE + f">>> bool(all(abs(ok_map[r, c] - _ok(15 + 20 * c, 15 + 20 * r, _x, _y, _v)[0]) < 1e-6 and abs(ok_varmap[r, c] - _ok(15 + 20 * c, 15 + 20 * r, _x, _y, _v)[1]) < 1e-6 for r, c in {NODES}))\nTrue",
         "Each node: ok_point(gx[r, c], gy[r, c], x, y, au, gamma_bassam, nmax=16).")],
 "q3": [(BASE + ">>> bool(abs(mse_ok_truth - _np.mean((ok_map - _T) ** 2)) < 1e-9)\nTrue",
         "truth_nodes = T[1::2, 1::2] (the truth cells under the nodes); mse_ok_truth = mean((ok_map - truth_nodes)**2)."),
        (BASE + ">>> def _idw(x0, y0):\n...     d = _np.hypot(_x - x0, _y - y0); k = _np.argsort(d)[:12]; w = 1 / d[k] ** 2\n...     return (w * _v[k]).sum() / w.sum()\n"
         f">>> bool(all(abs(idw_map[r, c] - _idw(15 + 20 * c, 15 + 20 * r)) < 1e-9 for r, c in {NODES}))\nTrue",
         "idw_map: idw_estimate (power 2, 12 samples) at every node."),
        (BASE + ">>> bool(abs(mse_idw_truth - _np.mean((idw_map - _T) ** 2)) < 1e-9 and abs(smoothing - ok_map.var() / _T.var()) < 1e-9)\nTrue",
         "mse_idw_truth likewise for IDW; smoothing = ok_map.var() / truth_nodes.var().")],
 "q4": [(BASE + ">>> _e = []; _z = []\n>>> for i in range(len(_v)):\n...     m = _np.arange(len(_v)) != i\n...     est, var = _ok(_x[i], _y[i], _x[m], _y[m], _v[m])\n"
         "...     _e.append(est - _v[i]); _z.append((est - _v[i]) ** 2 / var)\n"
         ">>> bool(_np.allclose(ok_cv_err, _e) and abs(ok_cv_mse - _np.mean(_np.square(_e))) < 1e-9 and abs(ok_cv_msse - _np.mean(_z)) < 1e-9)\nTrue",
         "Leave-one-out OK (16 neighbours): ok_cv_err = estimate - true; ok_cv_mse = mean squared error; ok_cv_msse = mean of err² / kriging variance."),
        (">>> bool(0.5 < ok_cv_msse < 2)\nTrue", "The mean standardised squared error should be close to 1 if the variogram model is right.")],
 "q5": [(BASE + ">>> bool(abs(slope_ok - _np.polyfit(ok_map.ravel(), _T.ravel(), 1)[0]) < 1e-9 and abs(slope_idw - _np.polyfit(idw_map.ravel(), _T.ravel(), 1)[0]) < 1e-9)\nTrue",
         "Slope of the regression of the TRUE values on the estimates: np.polyfit(estimates, truth, 1)[0]."),
        (">>> bool(len(axes_maps) == 3 and all(len(a.images) >= 1 for a in axes_maps))\nTrue",
         "Draw truth_nodes, ok_map and ok_varmap side by side with imshow in axes_maps (3 axes).")],
}

def notebook():
    cells = [
        header(9, 'Kriging maps and validation', NB, '''
        Last week we kriged single points. A mine plan needs a **map**: an estimate on every node of a grid, and the
        kriging variance that says where the map can be trusted. Because we know the true Bassam grades, we can also
        check what textbooks claim: kriging is the best linear estimator, it smooths, and it has less
        **conditional bias** than IDW.

        **What you will practise:** kriging on a grid · variance maps · comparison with the truth · smoothing ·
        cross-validation with standardised errors · conditional bias (slope of regression).
        '''),
        setup_cell('w9', DATA, TESTS),
        otter_cell(),
        toolbox_cell('models', 'idw', 'kriging'),
        code('''
        import pandas as pd
        import matplotlib.pyplot as plt

        def gamma_bassam(dx, dy):
            return spherical(aniso_h(dx, dy, 45, 300, 150), 0.06, 0.20, 300)

        samples = pd.read_csv("bassam_samples.csv")
        x, y, au = samples["x"].to_numpy(), samples["y"].to_numpy(), samples["au_gpt"].to_numpy()
        T = pd.read_csv("bassam_truth_grid.csv")["au_gpt"].to_numpy().reshape(100, 120)
        print(ok_point(600, 500, x, y, au, gamma_bassam))
        '''),
        md('''
        ## 1. From points to maps

        A map is just kriging repeated on every node. Each node has its own neighbourhood (here the 16 closest
        samples), so the computation is a loop. 3000 nodes take a few seconds.

        The kriging variance map shows the drilling pattern: low near holes, high in the gaps and at the edges.
        It does **not** show where grades are high: it depends on geometry only.

        ## 2. Smoothing and conditional bias

        Kriging estimates are **smoother** than reality: their variance is smaller than the true variance, because
        each estimate is an average. For mine planning the important property is that, among the blocks
        **estimated** at a given grade, the true grades are on average that same grade. Regress the true values on the
        estimates: a slope of 1 means no conditional bias; a slope below 1 means high estimates are too high and low
        estimates too low, which sends ore to the waste dump and waste to the mill.

        ## 3. Standardised errors

        If the variogram is right, the kriging variance predicts the size of the errors. In cross-validation the
        **mean standardised squared error** $\\frac1n\\sum e_i^2/\\sigma^2_{OK,i}$ should be close to 1.

        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. The grid

        Build the nodes `gx, gy` of a 20 m grid with `np.meshgrid(np.arange(15, 1200, 20), np.arange(15, 1000, 20))`
        (they fall on the centres of the truth cells) and store their number in `n_nodes`.
        ''', '''
        gx, gy = ...
        n_nodes = ...
        gx.shape, n_nodes
        '''),
        *question('q2', '''
        ### Q2. Kriging every node

        Fill `ok_map` and `ok_varmap` (same shape as `gx`) with `ok_point(..., gamma_bassam, nmax=16)`.
        ''', '''
        ok_map = np.zeros(gx.shape)
        ok_varmap = np.zeros(gx.shape)
        ...
        ok_map.mean(), ok_varmap.min(), ok_varmap.max()
        '''),
        *question('q3', '''
        ### Q3. Compare with the truth

        `truth_nodes = T[1::2, 1::2]` are the true grades under the nodes. Store `mse_ok_truth`. Make the IDW map
        `idw_map` (power 2, 12 samples) on the same nodes and store `mse_idw_truth`. Store `smoothing` =
        variance of `ok_map` / variance of `truth_nodes`.
        ''', '''
        truth_nodes = T[1::2, 1::2]
        mse_ok_truth = ...
        idw_map = ...
        mse_idw_truth = ...
        smoothing = ...
        mse_ok_truth, mse_idw_truth, smoothing
        '''),
        *question('q4', '''
        ### Q4. Cross-validation of kriging

        Leave-one-out with OK (16 neighbours): store the errors in `ok_cv_err`, the MSE in `ok_cv_mse` and the mean
        standardised squared error in `ok_cv_msse`. Compare `ok_cv_mse` with the IDW value of week 6.
        ''', '''
        ok_cv_err = ...
        ok_cv_mse = ...
        ok_cv_msse = ...
        ok_cv_mse, ok_cv_msse
        '''),
        *question('q5', '''
        ### Q5. Conditional bias and maps

        Store the slope of the regression of the true values on the estimates for kriging (`slope_ok`) and for IDW
        (`slope_idw`) with `np.polyfit(estimates.ravel(), truth_nodes.ravel(), 1)[0]`. Then draw `truth_nodes`,
        `ok_map` and `ok_varmap` side by side: `fig_maps, axes_maps = plt.subplots(1, 3, figsize=(15, 4))`.
        ''', '''
        slope_ok = ...
        slope_idw = ...

        fig_maps, axes_maps = plt.subplots(1, 3, figsize=(15, 4))
        ...
        plt.show()
        slope_ok, slope_idw
        '''),
        *closing('''
        ### Going further (not checked)

        * Krig with 4, 8, 16 and 32 neighbours. How do `mse_ok_truth` and `slope_ok` change? Small neighbourhoods
          increase conditional bias.
        * Plot the absolute error |ok_map − truth| against `ok_varmap`. Does a high kriging variance mean a large error?
        '''),
    ]
    save_notebook(NB, 'w9', cells)

def build():
    write_tests('w9', TESTS)
    notebook()
    return f'{NB} written'
