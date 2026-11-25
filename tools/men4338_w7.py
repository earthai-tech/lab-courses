# MEN 4338 week 7: review mini-project, from raw copper intervals to a validated variogram model (Copper South).
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, toolbox_cell

NB = 'MEN4338_W7_review_copper_south.ipynb'
DATA = ['copper_south_intervals.csv', 'copper_south_collars.csv']

COMP = (">>> import pandas as _pd, numpy as _np\n>>> _iv = _pd.read_csv('copper_south_intervals.csv').dropna(subset=['cu_pct'])\n"
        ">>> _iv['_l'] = _iv['to_m'] - _iv['from_m']; _iv['_gl'] = _iv['cu_pct'] * _iv['_l']\n"
        ">>> _t = _iv.groupby('hole_id')[['_gl', '_l']].sum(); _c = (_t['_gl'] / _t['_l']).rename('_cu')\n"
        ">>> _co = _pd.read_csv('copper_south_collars.csv').merge(_c, left_on='hole_id', right_index=True)\n"
        ">>> _x, _y, _v = (_co[c].to_numpy() for c in ('x', 'y', '_cu'))\n")
W = (">>> def _w(x, y, c):\n...     k = _np.floor(x / c).astype(int) * 100000 + _np.floor(y / c).astype(int)\n"
     "...     _, inv, cnt = _np.unique(k, return_inverse=True, return_counts=True); w = 1.0 / cnt[inv]\n...     return w / w.sum()\n")
SPH = (">>> def _sph(h, c0, c, a):\n...     r = _np.minimum(_np.asarray(h, float) / a, 1)\n"
       "...     return _np.where(_np.asarray(h) > 0, c0 + c * (1.5 * r - 0.5 * r ** 3), 0.0)\n")
TESTS = {
 "q1": [(COMP + ">>> _m = cs.set_index('hole_id')\n>>> bool(len(cs) == len(_co) and _np.allclose(_m.loc[_co['hole_id'], 'cu_pct'].to_numpy(), _v))\nTrue",
         "cs: one row per hole with hole_id, x, y and its length-weighted composite cu_pct (missing assays ignored)."),
        (COMP + ">>> bool(_np.allclose(cs.set_index('hole_id').loc[_co['hole_id'], ['x', 'y']].to_numpy(), _co[['x', 'y']].to_numpy()))\nTrue",
         "Merge the composites with copper_south_collars.csv to get x and y.")],
 "q2": [(COMP + ">>> bool(abs(naive_cu - _v.mean()) < 1e-9)\nTrue", "naive_cu = plain mean of the composites."),
        (COMP + W + ">>> bool(abs(declus_cu - (_w(_x, _y, 60) * _v).sum()) < 1e-9)\nTrue", "declus_cu: declustered mean with 60 m cells (the drilling grid)."),
        (COMP + W + ">>> bool(abs(prop_above_05 - (_w(_x, _y, 60) * (_v > 0.5)).sum()) < 1e-9)\nTrue",
         "prop_above_05: declustered proportion of composites above 0.5 % Cu = sum of the weights of those samples.")],
 "q3": [(COMP + ">>> _h, _g, _n = exp_variogram(_x, _y, _v, 60, 10)\n>>> bool(_np.allclose(g_cu, _g) and _np.allclose(n_cu, _n) and _np.allclose(h_cu, _h))\nTrue",
         "h_cu, g_cu, n_cu = exp_variogram(x, y, cu, 60, 10) on all the composites."),
        (COMP + ">>> bool(abs(var_cu - _v.var(ddof=1)) < 1e-12)\nTrue", "var_cu: sample variance of the composites (ddof=1).")],
 "q4": [(COMP + SPH + ">>> _h, _g, _n = exp_variogram(_x, _y, _v, 60, 10)\n"
         ">>> _b = min(_np.sum(_n * (_g - _sph(_h, c0, c, a)) ** 2) for c0 in _np.arange(0, 0.0601, 0.005) for c in _np.arange(0.05, 0.2501, 0.01) for a in range(60, 601, 20))\n"
         ">>> bool(_np.sum(_n * (_g - _sph(_h, *cu_params)) ** 2) <= _b * (1 + 1e-9))\nTrue",
         "Grid search c0 0..0.06 (step 0.005), c 0.05..0.25 (step 0.01), a 60..600 m (step 20) minimising the weighted SSE."),
        (">>> bool(len(cu_params) == 3)\nTrue", "cu_params = (c0, c, a).")],
 "q5": [(COMP + ">>> def _idw(x0, y0, x, y, v):\n...     d = _np.hypot(x - x0, y - y0); k = _np.argsort(d)[:8]; w = 1 / d[k] ** 2\n...     return (w * v[k]).sum() / w.sum()\n"
         ">>> _e = _np.array([_idw(_x[i], _y[i], _np.delete(_x, i), _np.delete(_y, i), _np.delete(_v, i)) - _v[i] for i in range(len(_v))])\n"
         ">>> bool(abs(cu_cv_me - _e.mean()) < 1e-9 and abs(cu_cv_mse - (_e ** 2).mean()) < 1e-9)\nTrue",
         "Leave-one-out IDW (power 2, 8 nearest): cu_cv_me = mean error, cu_cv_mse = mean squared error."),
        (">>> bool(isinstance(summary, dict) and {'declustered_mean', 'nugget', 'sill', 'range_m', 'cv_mse'} <= set(summary))\nTrue",
         "summary is a dictionary with the keys declustered_mean, nugget, sill, range_m, cv_mse."),
        (">>> bool(abs(summary['sill'] - (cu_params[0] + cu_params[1])) < 1e-9 and summary['range_m'] == cu_params[2] and summary['cv_mse'] == cu_cv_mse)\nTrue",
         "sill = c0 + c (the total sill), range_m = a, cv_mse = cu_cv_mse.")],
}

def notebook():
    cells = [
        header(7, 'Review mini-project: Copper South', NB, '''
        Half-way through the semester: time to run the whole workflow on a deposit you have never seen. Copper South
        is a porphyry-style copper prospect (synthetic): 800 m × 600 m, drilled on a 60 m grid, plus one east–west
        infill line at 30 m across the middle. The laboratory sent raw intervals.

        You will go from the raw intervals to a validated variogram model, and summarise the result in a small table
        as you would in a technical report. Every step is a skill from weeks 1 to 6.

        **What you will practise:** compositing · declustering · declustered proportions · experimental variogram ·
        model fitting · cross-validation · reporting.
        '''),
        setup_cell('w7', DATA, TESTS),
        otter_cell(),
        toolbox_cell('variogram', 'models', 'declus', 'idw'),
        code('''
        import pandas as pd
        import matplotlib.pyplot as plt

        intervals = pd.read_csv("copper_south_intervals.csv")
        collars = pd.read_csv("copper_south_collars.csv")
        print(intervals.shape, collars.shape)
        intervals.head()
        '''),
        md('''
        **Reminders.** Composite = length-weighted mean of the assayed intervals. Declustered statistics use
        `cell_weights(x, y, cell)`. A declustered **proportion** is the sum of the weights of the samples that satisfy
        the condition. A lag is reliable with at least 30 pairs.

        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. Composites with coordinates

        Build the DataFrame `cs` with one row per hole and the columns `hole_id`, `x`, `y`, `cu_pct` (the composite).
        Then plot a location map coloured by grade.
        ''', '''
        cs = ...
        cs.head()
        '''),
        *question('q2', '''
        ### Q2. Declustered statistics

        Store the plain mean in `naive_cu`, the declustered mean with 60 m cells in `declus_cu`, and the declustered
        proportion of composites above 0.5 % Cu in `prop_above_05`.
        ''', '''
        x, y, cu = cs["x"].to_numpy(), cs["y"].to_numpy(), cs["cu_pct"].to_numpy()
        naive_cu = ...
        declus_cu = ...
        prop_above_05 = ...
        naive_cu, declus_cu, prop_above_05
        '''),
        *question('q3', '''
        ### Q3. Experimental variogram

        Compute the omnidirectional variogram of the composites with lag 60 m and 10 lags (`h_cu, g_cu, n_cu`) and
        the sample variance `var_cu`. Plot it. Check the directions N000 and N090 quickly: is an isotropic model
        acceptable here?
        ''', '''
        h_cu, g_cu, n_cu = ...
        var_cu = ...
        '''),
        *question('q4', '''
        ### Q4. Fit a spherical model

        Find `cu_params = (c0, c, a)` minimising the weighted SSE over $c_0$ = 0 to 0.06 (step 0.005), $c$ = 0.05 to
        0.25 (step 0.01), $a$ = 60 to 600 m (step 20). Plot the model over the experimental points.
        ''', '''
        cu_params = ...
        cu_params
        '''),
        *question('q5', '''
        ### Q5. Validate and report

        Cross-validate IDW (power 2, 8 nearest composites) by leave-one-out: store the mean error in `cu_cv_me` and the
        MSE in `cu_cv_mse`. Then fill the dictionary `summary` with the keys `declustered_mean`, `nugget`, `sill`
        (total: $c_0 + c$), `range_m` and `cv_mse`, and print it as a small table.
        ''', '''
        cu_cv_me = ...
        cu_cv_mse = ...
        summary = {
            "declustered_mean": ...,
            "nugget": ...,
            "sill": ...,
            "range_m": ...,
            "cv_mse": ...,
        }
        pd.Series(summary)
        '''),
        *closing('''
        ### Going further (not checked)

        * Is the copper grade higher on the infill line than elsewhere? Was the line placed on a rich zone?
        * Write the five numbers of `summary` in two sentences, as in the executive summary of a report.
        '''),
    ]
    save_notebook(NB, 'w7', cells)

def build():
    write_tests('w7', TESTS)
    notebook()
    return f'{NB} written'
