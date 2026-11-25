# MEN 4338 week 6: classical estimators (nearest neighbour, inverse distance) and cross-validation.
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing

NB = 'MEN4338_W6_idw_cross_validation.ipynb'
DATA = ['bassam_samples.csv', 'bassam_truth_grid.csv']

RS = (">>> import pandas as _pd, numpy as _np\n>>> _s = _pd.read_csv('bassam_samples.csv')\n"
      ">>> _x, _y, _v = (_s[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n")
IDW = (">>> def _idw(x0, y0, x, y, v, p=2, nmax=12):\n"
       "...     d = _np.hypot(x - x0, y - y0); k = _np.argsort(d)[:nmax]\n"
       "...     if d[k[0]] < 1e-9: return float(v[k[0]])\n"
       "...     w = 1 / d[k] ** p\n"
       "...     return float((w * v[k]).sum() / w.sum())\n"
       ">>> def _cv(p):\n"
       "...     e = []\n"
       "...     for i in range(len(_v)):\n"
       "...         m = _np.arange(len(_v)) != i\n"
       "...         e.append(_idw(_x[i], _y[i], _x[m], _y[m], _v[m], p, 12) - _v[i])\n"
       "...     return _np.array(e)\n")
TARGETS = "[(312.0, 457.0), (641.0, 213.0), (906.0, 782.0), (152.0, 933.0), (1083.0, 97.0)]"
TESTS = {
 "q1": [(">>> import numpy as _np\n>>> bool(nearest_estimate(1.0, 1.0, _np.array([0., 5, 2]), _np.array([0., 5, 2]), _np.array([10., 20, 30])) == 10.0)\nTrue",
         "Return the value of the closest sample (np.argmin of the distances)."),
        (RS + ">>> _d = _np.hypot(_x - 500, _y - 500)\n>>> bool(abs(nn_500 - _v[_np.argmin(_d)]) < 1e-12)\nTrue", "nn_500 = nearest_estimate(500, 500, x, y, au).")],
 "q2": [(RS + IDW + ">>> bool(all(abs(idw_estimate(a, b, _x, _y, _v) - _idw(a, b, _x, _y, _v)) < 1e-9 for a, b in [(500, 500), (33, 870), (1190, 10)]))\nTrue",
         "Default power 2 and the 12 nearest samples: w_i = 1 / d_i**power, estimate = sum(w v) / sum(w)."),
        (RS + IDW + ">>> bool(abs(idw_estimate(500, 500, _x, _y, _v, power=1, nmax=30) - _idw(500, 500, _x, _y, _v, 1, 30)) < 1e-9)\nTrue",
         "Use the power and nmax arguments."),
        (">>> import numpy as _np\n>>> bool(idw_estimate(5.0, 5.0, _np.array([5., 0]), _np.array([5., 0]), _np.array([3., 9])) == 3.0)\nTrue",
         "At a sample location (distance 0) return that sample's value instead of dividing by zero.")],
 "q3": [(RS + IDW + f">>> _t = {TARGETS}\n>>> bool(_np.allclose(idw_at_targets, [_idw(a, b, _x, _y, _v) for a, b in _t]))\nTrue",
         "idw_at_targets: idw_estimate (power 2, 12 samples) at each of the 5 targets, in order."),
        (f">>> import pandas as _pd, numpy as _np\n>>> _tg = _pd.read_csv('bassam_truth_grid.csv')\n>>> _t = {TARGETS}\n"
         ">>> _tv = [_tg['au_gpt'].to_numpy()[_np.argmin(_np.hypot(_tg['x'] - a, _tg['y'] - b))] for a, b in _t]\n"
         ">>> bool(_np.allclose(true_at_targets, _tv))\nTrue",
         "true_at_targets: the au_gpt of the truth-grid cell centre closest to each target."),
        (">>> import numpy as _np\n>>> bool(abs(mae_targets - _np.mean(_np.abs(_np.array(idw_at_targets) - _np.array(true_at_targets)))) < 1e-9)\nTrue",
         "mae_targets = mean absolute error of the 5 estimates.")],
 "q4": [(RS + IDW + ">>> _e = _cv(2)\n>>> bool(len(cv_err) == len(_v) and _np.allclose(cv_err, _e))\nTrue",
         "Leave-one-out: for each sample i, estimate it from all the OTHER samples (power 2, 12 nearest), error = estimate - true value."),
        (">>> import numpy as _np\n>>> bool(abs(cv_me - _np.mean(cv_err)) < 1e-12 and abs(cv_mse - _np.mean(_np.asarray(cv_err) ** 2)) < 1e-12)\nTrue",
         "cv_me = mean error (bias), cv_mse = mean squared error."),
        (RS + IDW + ">>> _e = _cv(2)\n>>> bool(abs(cv_rho - _np.corrcoef(_v + _e, _v)[0, 1]) < 1e-9)\nTrue",
         "cv_rho = correlation between the cross-validation estimates and the true values.")],
 "q5": [(RS + IDW + ">>> _m = {p: float(_np.mean(_cv(p) ** 2)) for p in (1, 2, 3)}\n>>> bool(sorted(cv_mse_by_power) == [1, 2, 3] and all(abs(cv_mse_by_power[p] - _m[p]) < 1e-9 for p in _m))\nTrue",
         "cv_mse_by_power maps 1, 2, 3 to the leave-one-out MSE (12 nearest samples)."),
        (">>> bool(best_power == min(cv_mse_by_power, key=cv_mse_by_power.get))\nTrue", "best_power: the power with the smallest MSE.")],
}

def notebook():
    cells = [
        header(6, 'Classical estimators and cross-validation', NB, f'''
        Before kriging, engineers estimated grades with simple geometric rules: take the **nearest** sample, or
        an **inverse-distance** weighted average. They are still used, as quick checks and in many mine software
        defaults. This week we program them, and learn how to judge any estimator with **cross-validation**: hide
        one sample, estimate it from the others, compare.

        For Bassam we can go further: we know the true grades (`bassam_truth_grid.csv`, one value per 10 m cell),
        which a real mine never does.

        **What you will practise:** nearest neighbour · inverse distance weighting (IDW) · search neighbourhood ·
        leave-one-out cross-validation · bias, mean squared error, correlation.
        '''),
        setup_cell('w6', DATA, TESTS),
        otter_cell(),
        code('''
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        samples = pd.read_csv("bassam_samples.csv")
        truth = pd.read_csv("bassam_truth_grid.csv")
        x, y, au = samples["x"].to_numpy(), samples["y"].to_numpy(), samples["au_gpt"].to_numpy()
        T = truth["au_gpt"].to_numpy().reshape(100, 120)      # rows = north, columns = east
        print(len(samples), "samples;", T.shape, "truth cells; true mean", T.mean().round(3))
        '''),
        md('''
        ## 1. Every estimator is a weighted average

        $$z^*(\\mathbf{x}_0) = \\sum_{i=1}^{n} \\lambda_i \\, z(\\mathbf{x}_i), \\qquad \\sum_i \\lambda_i = 1$$

        * **Nearest neighbour (polygons):** weight 1 for the closest sample, 0 for the others.
        * **Inverse distance:** $\\lambda_i \\propto 1/d_i^{\\,p}$, usually $p = 2$, over the $n_{max}$ closest samples.

        Neither uses the variogram: they ignore the nugget, the anisotropy and the redundancy between clustered
        samples. Kriging (week 8) fixes all three.
        '''),
        md('''
        ## 2. Cross-validation

        For each sample $i$: remove it, estimate it from the others, record the error $e_i = z^*_i - z_i$. Then:

        | statistic | ideal | tells you |
        |---|---|---|
        | mean error $\\bar e$ | 0 | global bias |
        | mean squared error $\\overline{e^2}$ | small | precision |
        | correlation $\\rho(z^*, z)$ | close to 1 | how well the estimates follow reality |

        Cross-validation compares estimators on the **same** data. It is not a proof that the model is right.

        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. Nearest neighbour

        Write `nearest_estimate(x0, y0, x, y, v)` returning the value of the closest sample. Store the estimate at
        (500, 500) in `nn_500`.
        ''', '''
        def nearest_estimate(x0, y0, x, y, v):
            ...

        nn_500 = ...
        nn_500
        '''),
        *question('q2', '''
        ### Q2. Inverse distance

        Write `idw_estimate(x0, y0, x, y, v, power=2, nmax=12)` using the `nmax` closest samples. If a sample sits
        exactly at the target (distance 0), return its value.
        ''', '''
        def idw_estimate(x0, y0, x, y, v, power=2, nmax=12):
            ...

        idw_estimate(500, 500, x, y, au)
        '''),
        *question('q3', f'''
        ### Q3. Compare with the truth

        `targets = {TARGETS}`. Store the IDW estimates (power 2, 12 samples) in `idw_at_targets`, the true grades in
        `true_at_targets` (the value of the closest truth-grid cell centre), and the mean absolute error in `mae_targets`.
        ''', f'''
        targets = {TARGETS}
        idw_at_targets = ...
        true_at_targets = ...
        mae_targets = ...
        list(zip(idw_at_targets, true_at_targets)), mae_targets
        '''),
        *question('q4', '''
        ### Q4. Leave-one-out cross-validation

        Cross-validate IDW (power 2, 12 samples) on all samples. Store the errors (estimate − true) in `cv_err`
        (same order as `samples`), the mean error in `cv_me`, the mean squared error in `cv_mse` and the correlation
        between estimates and true values in `cv_rho`. Plot estimates against true values.
        ''', '''
        cv_err = ...
        cv_me = ...
        cv_mse = ...
        cv_rho = ...
        cv_me, cv_mse, cv_rho
        '''),
        *question('q5', '''
        ### Q5. Which power?

        Repeat the cross-validation for powers 1, 2 and 3. Store the MSE of each in the dictionary
        `cv_mse_by_power` and the best power in `best_power`. What happens to the estimates when the power is very
        large?
        ''', '''
        cv_mse_by_power = {}
        ...
        best_power = ...
        cv_mse_by_power, best_power
        '''),
        *closing('''
        ### Going further (not checked)

        * Estimate every 10 m cell of the bench by IDW and draw the map next to the truth (`plt.imshow(T, origin="lower")`).
          Which one is smoother? Compare the variance of the estimates with the variance of the truth.
        * Do the cross-validation errors depend on the campaign (grid or infill)?
        '''),
    ]
    save_notebook(NB, 'w6', cells)

def build():
    write_tests('w6', TESTS)
    notebook()
    return f'{NB} written'
