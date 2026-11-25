# MEN 4338 week 12: indicator geostatistics, probability of exceeding a cut-off.
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, toolbox_cell

NB = 'MEN4338_W12_indicator_kriging.ipynb'
DATA = ['bassam_samples.csv', 'bassam_truth_grid.csv']

BASE = (">>> import numpy as _np, pandas as _pd\n>>> _s = _pd.read_csv('bassam_samples.csv'); _x, _y, _v = (_s[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n"
        ">>> _i = (_v > 1.0).astype(float); _gm = (_s['campaign'] == 'grid').to_numpy()\n"
        ">>> def _w(x, y, c):\n...     k = _np.floor(x / c).astype(int) * 100000 + _np.floor(y / c).astype(int)\n"
        "...     _, inv, cnt = _np.unique(k, return_inverse=True, return_counts=True); w = 1.0 / cnt[inv]\n...     return w / w.sum()\n"
        ">>> def _gi(dx, dy):\n"
        "...     t = _np.radians(45); u = dx * _np.sin(t) + dy * _np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n"
        "...     h = _np.sqrt(u ** 2 + (w * 280 / 130) ** 2); r = _np.minimum(h / 280, 1)\n"
        "...     return _np.where(h > 0, 0.08 + 0.17 * (1.5 * r - 0.5 * r ** 3), 0.0)\n"
        ">>> def _ik(x0, y0):\n"
        "...     k = _np.argsort(_np.hypot(_x - x0, _y - y0))[:16]; xs, ys = _x[k], _y[k]\n"
        "...     A = _np.ones((17, 17)); A[16, 16] = 0; A[:16, :16] = _gi(xs[:, None] - xs[None, :], ys[:, None] - ys[None, :])\n"
        "...     b = _np.ones(17); b[:16] = _gi(xs - x0, ys - y0)\n"
        "...     return float(_np.clip(_np.linalg.solve(A, b)[:16] @ _i[k], 0, 1))\n"
        ">>> _T = _pd.read_csv('bassam_truth_grid.csv')['au_gpt'].to_numpy().reshape(100, 120)[1::2, 1::2]\n")
TESTS = {
 "q1": [(BASE + ">>> bool(_np.array_equal(_np.asarray(ind_1, float), _i))\nTrue", "ind_1 = (au > 1.0).astype(float): 1 above the cut-off, 0 below."),
        (BASE + ">>> bool(abs(p_naive - _i.mean()) < 1e-12 and abs(p_declus - (_w(_x, _y, 50) * _i).sum()) < 1e-12)\nTrue",
         "p_naive = mean of the indicator; p_declus = declustered mean with 50 m cells."),
        (BASE + ">>> bool(sorted(props) == [0.5, 1.0, 1.5] and all(abs(props[c] - (_w(_x, _y, 50) * (_v > c)).sum()) < 1e-12 for c in props))\nTrue",
         "props maps each cut-off 0.5, 1.0, 1.5 to the declustered proportion of samples above it.")],
 "q2": [(BASE + ">>> bool(_np.allclose(g_ind, exp_variogram(_x[_gm], _y[_gm], _i[_gm], 50, 10)[1]))\nTrue",
         "g_ind: omnidirectional variogram of ind_1 on the grid holes, lag 50 m, 10 lags."),
        (BASE + ">>> _p = _i[_gm].mean()\n>>> bool(abs(ind_sill - _p * (1 - _p)) < 1e-12)\nTrue", "The variance of an indicator is p(1 - p), with p its mean on the grid holes.")],
 "q3": [(BASE + ">>> _t = [(312., 457.), (641., 213.), (906., 782.)]\n>>> bool(_np.allclose(ik_targets, [_ik(*t) for t in _t]))\nTrue",
         "ik_targets: ok_point on ind_1 with gamma_ind (16 neighbours), clipped to [0, 1] with np.clip."),
        (">>> bool(all(0 <= p <= 1 for p in ik_targets))\nTrue", "Probabilities must lie between 0 and 1.")],
 "q4": [(BASE + ">>> bool(prob_map.shape == (50, 60) and all(abs(prob_map[r, c] - _ik(15 + 20 * c, 15 + 20 * r)) < 1e-9 for r, c in [(0, 0), (20, 30), (49, 59), (8, 44)]))\nTrue",
         "prob_map[r, c]: clipped indicator kriging at (15 + 20 c, 15 + 20 r)."),
        (">>> bool(abs(ha_above_05 - (prob_map > 0.5).sum() * 400 / 10000) < 1e-9)\nTrue",
         "Each node stands for 20 m × 20 m = 400 m²; 1 ha = 10 000 m².")],
 "q5": [(BASE + ">>> bool(abs(true_frac - (_T > 1.0).mean()) < 1e-12 and abs(expected_frac - prob_map.mean()) < 1e-12)\nTrue",
         "true_frac = share of truth_nodes above 1 g/t; expected_frac = mean of prob_map."),
        (BASE + ">>> bool(abs(misclass - ((prob_map > 0.5) != (_T > 1.0)).mean()) < 1e-12)\nTrue",
         "misclass: share of nodes where (prob_map > 0.5) disagrees with (truth_nodes > 1.0).")],
}

def notebook():
    cells = [
        header(12, 'Indicator kriging: the probability of ore', NB, '''
        A mine manager rarely asks "what is the grade here?". The real question is **"what is the chance that this
        block is ore?"**. Indicator geostatistics answers it directly. Code each sample 1 if it is above the cut-off,
        0 otherwise; kriging these 0/1 values gives a **probability**. No assumption on the shape of the histogram is
        needed, and extreme grades no longer dominate.

        **What you will practise:** indicator coding · declustered proportions · indicator variograms · indicator
        kriging · order-relation corrections · probability maps and risk.
        '''),
        setup_cell('w12', DATA, TESTS),
        otter_cell(),
        toolbox_cell('variogram', 'models', 'declus', 'kriging'),
        code('''
        import pandas as pd
        import matplotlib.pyplot as plt

        samples = pd.read_csv("bassam_samples.csv")
        x, y, au = samples["x"].to_numpy(), samples["y"].to_numpy(), samples["au_gpt"].to_numpy()
        is_grid = (samples["campaign"] == "grid").to_numpy()
        T = pd.read_csv("bassam_truth_grid.csv")["au_gpt"].to_numpy().reshape(100, 120)
        '''),
        md('''
        ## 1. Indicators

        $$i(\\mathbf{x}; z_c) = \\begin{cases} 1 & z(\\mathbf{x}) > z_c \\\\ 0 & \\text{otherwise} \\end{cases}$$

        The (declustered) mean of an indicator is the proportion of the deposit above the cut-off. Its variance is
        $p(1-p)$, which is also the sill of its variogram.

        ## 2. Indicator kriging (IK)

        Ordinary kriging of the indicators with the **indicator variogram** gives, at each location, an estimate of
        $P\\{Z(\\mathbf{x}) > z_c \\mid \\text{data}\\}$. Because kriging weights can be negative, the result can fall
        slightly outside $[0, 1]$: clip it (an *order-relation correction*). With several cut-offs, the probabilities
        must also decrease as the cut-off increases.

        The indicator variogram at 1 g/t on the Bassam grid holes is modelled by `gamma_ind`: nugget 0.08 +
        spherical 0.17, range 280 m along N045 and 130 m along N135.
        '''),
        code('''
        def gamma_ind(dx, dy):
            return spherical(aniso_h(dx, dy, 45, 280, 130), 0.08, 0.17, 280)
        '''),
        md('''
        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. Indicators and proportions

        Store the indicator of `au > 1.0` as floats in `ind_1`, its plain mean in `p_naive` and its declustered mean
        (50 m cells) in `p_declus`. Then build the dictionary `props` with the declustered proportion above 0.5, 1.0
        and 1.5 g/t.
        ''', '''
        ind_1 = ...
        p_naive = ...
        p_declus = ...
        props = ...
        p_naive, p_declus, props
        '''),
        *question('q2', '''
        ### Q2. Indicator variogram

        On the grid holes, compute the omnidirectional indicator variogram (lag 50 m, 10 lags) in `g_ind` and the
        indicator variance $p(1-p)$ in `ind_sill` (with $p$ = mean of `ind_1` on the grid holes). Plot them with the
        model `gamma_ind` along N045 and N135.
        ''', '''
        g_ind = ...
        ind_sill = ...
        '''),
        *question('q3', '''
        ### Q3. Probability at three points

        Store in `ik_targets` the probability of exceeding 1 g/t at (312, 457), (641, 213) and (906, 782): `ok_point`
        on `ind_1` with `gamma_ind` and 16 neighbours, clipped to $[0, 1]$.
        ''', '''
        ik_targets = ...
        ik_targets
        '''),
        *question('q4', '''
        ### Q4. Probability map

        Krig the probability on the week 9 nodes (`np.meshgrid(np.arange(15, 1200, 20), np.arange(15, 1000, 20))`)
        into `prob_map` (shape 50 × 60, clipped), draw it, and store in `ha_above_05` the area in hectares where the
        probability is above 0.5.
        ''', '''
        gx, gy = np.meshgrid(np.arange(15, 1200, 20), np.arange(15, 1000, 20))
        prob_map = ...
        ha_above_05 = ...
        ha_above_05
        '''),
        *question('q5', '''
        ### Q5. How good are the probabilities?

        With `truth_nodes = T[1::2, 1::2]`: store the true share of nodes above 1 g/t in `true_frac`, the expected
        share from the probabilities (`prob_map.mean()`) in `expected_frac`, and the share of nodes misclassified by
        the rule "ore if probability > 0.5" in `misclass`.
        ''', '''
        truth_nodes = T[1::2, 1::2]
        true_frac = ...
        expected_frac = ...
        misclass = ...
        true_frac, expected_frac, misclass
        '''),
        *closing('''
        ### Going further (not checked)

        * Check calibration: group the nodes by probability (0–0.1, 0.1–0.2, …) and compute the true share of ore in
          each group. A well-calibrated map gives about 0.15 in the 0.1–0.2 group, and so on.
        * Krig the indicators at 0.5 and 1.5 g/t too (use the same model for simplicity). Are the three probabilities
          always in decreasing order? Fix the nodes where they are not.
        '''),
    ]
    save_notebook(NB, 'w12', cells)

def build():
    write_tests('w12', TESTS)
    notebook()
    return f'{NB} written'
