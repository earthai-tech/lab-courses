# MEN 4338 week 14: final project, a mineral resource estimate for the Kossou gold prospect.
# The checks verify consistency (composites, declustering, the student's own model by cross-validation, block model,
# resource table); the geological choices are the student's and are assessed in the report. No model answer here.
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, toolbox_cell

NB = 'MEN4338_W14_final_project_kossou.ipynb'
DATA = ['kossou_intervals.csv', 'kossou_collars.csv']

COMP = (">>> import pandas as _pd, numpy as _np\n>>> _iv = _pd.read_csv('kossou_intervals.csv').dropna(subset=['au_gpt'])\n"
        ">>> _iv['_l'] = _iv['to_m'] - _iv['from_m']; _iv['_gl'] = _iv['au_gpt'] * _iv['_l']\n"
        ">>> _t = _iv.groupby('hole_id')[['_gl', '_l']].sum(); _c = (_t['_gl'] / _t['_l']).rename('_au')\n"
        ">>> _co = _pd.read_csv('kossou_collars.csv').merge(_c, left_on='hole_id', right_index=True)\n"
        ">>> _x, _y, _v = (_co[c].to_numpy() for c in ('x', 'y', '_au'))\n")
TESTS = {
 "q1": [(COMP + ">>> _m = ks.set_index('hole_id')\n>>> bool(len(ks) == len(_co) and _np.allclose(_m.loc[_co['hole_id'], 'au_gpt'].to_numpy(), _v) and _np.allclose(_m.loc[_co['hole_id'], 'x'].to_numpy(), _x))\nTrue",
         "ks: one row per hole with hole_id, x, y and the 8 m bench composite au_gpt (length-weighted, missing assays ignored)."),
        (COMP + ">>> bool(n_holes == len(_co) and abs(sampled_m - _iv['_l'].sum()) < 1e-6)\nTrue",
         "n_holes = number of holes; sampled_m = total length of assayed intervals.")],
 "q2": [(COMP + ">>> _i, _j = _np.triu_indices(len(_x), 1); _d = _np.full((len(_x), len(_x)), _np.inf)\n"
         ">>> _d[_i, _j] = _d[_j, _i] = _np.hypot(_x[_j] - _x[_i], _y[_j] - _y[_i])\n"
         ">>> _m = ks.set_index('hole_id').loc[_co['hole_id']]\n"
         ">>> bool(_np.array_equal(_np.asarray(_m['is_infill'], bool), _d.min(axis=1) < 40))\nTrue",
         "ks['is_infill'] is True for the holes whose nearest neighbour is closer than 40 m."),
        (COMP + ">>> _k = _np.floor(_x / 50).astype(int) * 100000 + _np.floor(_y / 50).astype(int)\n"
         ">>> _, _inv, _cnt = _np.unique(_k, return_inverse=True, return_counts=True); _w = 1 / _cnt[_inv]; _w = _w / _w.sum()\n"
         ">>> bool(abs(ks_naive_mean - _v.mean()) < 1e-9 and abs(ks_declus_mean - (_w * _v).sum()) < 1e-9)\nTrue",
         "ks_naive_mean: plain mean; ks_declus_mean: declustered mean with 50 m cells.")],
 "q3": [(">>> import numpy as _np\n>>> bool({'c0', 'c', 'azimuth', 'a_major', 'a_minor'} <= set(ks_model) and float(gamma_ks(0.0, 0.0)) == 0.0)\nTrue",
         "ks_model is a dictionary with c0, c, azimuth, a_major, a_minor, and gamma_ks(dx, dy) is your model (γ(0) = 0)."),
        (">>> import numpy as _np\n>>> bool(abs(float(gamma_ks(1e5, 0.0)) - (ks_model['c0'] + ks_model['c'])) < 1e-6 and ks_model['a_major'] >= ks_model['a_minor'] > 0)\nTrue",
         "Far away gamma_ks must equal the total sill c0 + c; a_major >= a_minor."),
        (COMP + ">>> _e = []\n>>> for _i in range(len(_v)):\n...     _k = _np.argsort(_np.hypot(_x - _x[_i], _y - _y[_i]))[1:17]; _xs, _ys = _x[_k], _y[_k]\n"
         "...     _A = _np.ones((17, 17)); _A[16, 16] = 0; _A[:16, :16] = gamma_ks(_xs[:, None] - _xs[None, :], _ys[:, None] - _ys[None, :])\n"
         "...     _b = _np.ones(17); _b[:16] = gamma_ks(_xs - _x[_i], _ys - _y[_i]); _s = _np.linalg.solve(_A, _b)\n"
         "...     _e.append(((_s[:16] @ _v[_k]) - _v[_i]) ** 2 / (_s[:16] @ _b[:16] + _s[16]))\n"
         ">>> bool(0.7 < _np.mean(_e) < 1.4)\nTrue",
         "Leave-one-out kriging with your model gives a mean standardised squared error outside 0.7–1.4: revise the nugget, sill or ranges.")],
 "q4": [(">>> bool(ks_blocks.shape == (16, 20) and ks_block_var.shape == (16, 20))\nTrue",
         "50 m blocks over 1000 m × 800 m: 16 rows (north) × 20 columns (east)."),
        (COMP + ">>> bool(all(abs(ks_blocks[r, c] - ok_block(25 + 50 * c, 25 + 50 * r, 50, _x, _y, _v, gamma_ks)[0]) < 1e-6 for r, c in [(0, 0), (8, 10), (15, 19)]))\nTrue",
         "Block (r, c) centred on (25 + 50 c, 25 + 50 r): ok_block(..., 50, x, y, au, gamma_ks) with the default nd=4, nmax=16.")],
 "q5": [(">>> import numpy as _np\n>>> _o = (ks_blocks >= 0.8)\n>>> bool(abs(resource['tonnes_mt'].sum() - _o.sum() * 54000 / 1e6) < 1e-6)\nTrue",
         "One block = 50 × 50 × 8 m × 2.7 t/m³ = 54 000 t; the categories together hold every block estimated >= 0.8 g/t."),
        (">>> import numpy as _np\n>>> bool(list(resource['category']) == ['Measured', 'Indicated', 'Inferred'])\nTrue",
         "resource has one row per category, in the order Measured, Indicated, Inferred."),
        (">>> import numpy as _np\n>>> _ok = resource['tonnes_mt'] > 0\n"
         ">>> bool(_np.allclose(resource.loc[_ok, 'metal_koz'], resource.loc[_ok, 'tonnes_mt'] * 1e6 * resource.loc[_ok, 'grade_gpt'] / 31.1035 / 1000))\nTrue",
         "metal_koz = tonnes × grade / 31.1035 / 1000 for each category."),
        (">>> import numpy as _np\n>>> _o = ks_blocks >= 0.8\n>>> bool(abs(resource['metal_koz'].sum() - (ks_blocks[_o] * 54000).sum() / 31.1035 / 1000) < 1e-6)\nTrue",
         "The total metal must equal the metal of all blocks >= 0.8 g/t.")],
}

def notebook():
    cells = [
        header(14, 'Final project: resource estimate for Kossou', NB, '''
        You are the geostatistician of a junior mining company. The Kossou gold prospect (synthetic) has been
        drilled with RC holes on a 50 m grid, plus an infill pattern on the best zone. Each hole samples an **8 m
        bench**. The board wants a **mineral resource estimate** at a cut-off of 0.8 g/t, classified into
        Measured, Indicated and Inferred, before deciding on a feasibility study.

        This notebook gives the steps and checks the consistency of your numbers. The geological choices (variogram
        model, classification rule) are yours: justify them in the report.

        **Deliverables:** this notebook (all checks passing) · a 6–8 page report · a 10-minute presentation.
        '''),
        setup_cell('w14', DATA, TESTS),
        otter_cell(),
        toolbox_cell('variogram', 'models', 'declus', 'kriging', 'block'),
        code('''
        import pandas as pd
        import matplotlib.pyplot as plt

        intervals = pd.read_csv("kossou_intervals.csv")
        collars = pd.read_csv("kossou_collars.csv")
        print(intervals.shape, collars.shape)
        '''),
        md('''
        ## Project steps

        | step | weeks | output |
        |---|---|---|
        | 1. Composites and data check | 1–2 | `ks`, location map, histogram |
        | 2. Clustering and declustered statistics | 2 | `is_infill`, declustered mean |
        | 3. Variography and model | 3–5 | directional variograms, `ks_model`, `gamma_ks` |
        | 4. Validation | 6, 9 | cross-validation (mean standardised squared error near 1) |
        | 5. Block model | 8–10 | 50 m blocks, estimates and block kriging variances |
        | 6. Classification and resource table | 10 | Measured / Indicated / Inferred at 0.8 g/t |

        **Classification.** A common rule uses the block kriging variance (or the distance to the data): blocks with a
        low variance are **Measured**, intermediate **Indicated**, the rest **Inferred**. Choose two thresholds,
        e.g. from the variance of blocks fully inside the infill pattern and inside the 50 m grid, and justify them.

        ---
        ## Checked steps
        '''),
        *question('q1', '''
        ### Q1. Composites

        Build `ks` (columns `hole_id`, `x`, `y`, `au_gpt`: the 8 m bench composite of each hole). Store `n_holes` and
        `sampled_m` (total length of assayed intervals).
        ''', '''
        ks = ...
        n_holes = ...
        sampled_m = ...
        n_holes, sampled_m
        '''),
        *question('q2', '''
        ### Q2. Clustering and declustering

        Add a boolean column `ks["is_infill"]`: True when the nearest other hole is closer than 40 m. Store the plain
        mean in `ks_naive_mean` and the declustered mean with 50 m cells in `ks_declus_mean`.
        ''', '''
        x, y, au = ks["x"].to_numpy(), ks["y"].to_numpy(), ks["au_gpt"].to_numpy()
        ks["is_infill"] = ...
        ks_naive_mean = ...
        ks_declus_mean = ...
        ks_naive_mean, ks_declus_mean
        '''),
        *question('q3', '''
        ### Q3. Your variogram model

        Study the directional variograms of the **grid** holes (`~ks["is_infill"]`), choose an anisotropic spherical
        model and store it in `ks_model = {"c0": ..., "c": ..., "azimuth": ..., "a_major": ..., "a_minor": ...}`.
        Define `gamma_ks(dx, dy)` from it. The check cross-validates your model on all holes (16 neighbours): the mean
        standardised squared error must be between 0.7 and 1.4.
        ''', '''
        ks_model = {"c0": ..., "c": ..., "azimuth": ..., "a_major": ..., "a_minor": ...}

        def gamma_ks(dx, dy):
            ...
        '''),
        *question('q4', '''
        ### Q4. Block model

        Krig the 50 m blocks (16 rows × 20 columns, block `(r, c)` centred on `(25 + 50*c, 25 + 50*r)`) with
        `ok_block(..., 50, x, y, au, gamma_ks)`. Store `ks_blocks` and `ks_block_var`. Map both.
        ''', '''
        ks_blocks = np.zeros((16, 20))
        ks_block_var = np.zeros((16, 20))
        ...
        '''),
        *question('q5', '''
        ### Q5. Resource table

        Classify the blocks with your two variance thresholds and build the DataFrame `resource` with the rows
        `Measured`, `Indicated`, `Inferred` (in that order) and the columns `category`, `tonnes_mt`, `grade_gpt`,
        `metal_koz`, for the blocks estimated ≥ 0.8 g/t (54 000 t per block, 31.1035 g per ounce).
        ''', '''
        t_measured = ...
        t_indicated = ...
        resource = ...
        resource
        '''),
        *closing('''
        ### For the report (not checked)

        * Grade–tonnage curves for cut-offs 0 to 2 g/t, and the sensitivity of the resource to the cut-off.
        * A sequential Gaussian simulation (week 13) of the bench: P90 / P50 / P10 of the tonnage above 0.8 g/t.
          Is the Measured + Indicated tonnage inside that range?
        * Risks and recommendations: where would you drill next, and why?
        '''),
    ]
    save_notebook(NB, 'w14', cells)

def build():
    write_tests('w14', TESTS)
    notebook()
    return f'{NB} written'
