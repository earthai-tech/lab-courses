# MEN 4338 week 10: change of support, block kriging and grade-tonnage curves.
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, toolbox_cell

NB = 'MEN4338_W10_block_kriging_grade_tonnage.ipynb'
DATA = ['bassam_samples.csv', 'bassam_truth_grid.csv']

BASE = (">>> import numpy as _np, pandas as _pd\n>>> _s = _pd.read_csv('bassam_samples.csv'); _x, _y, _v = (_s[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n"
        ">>> _T = _pd.read_csv('bassam_truth_grid.csv')['au_gpt'].to_numpy().reshape(100, 120)\n"
        ">>> _B = _T.reshape(20, 5, 24, 5).mean(axis=(1, 3))\n"
        ">>> def _gb(dx, dy):\n"
        "...     t = _np.radians(45); u = dx * _np.sin(t) + dy * _np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n"
        "...     h = _np.sqrt(u ** 2 + (2 * w) ** 2); r = _np.minimum(h / 300, 1)\n"
        "...     return _np.where(h > 0, 0.06 + 0.20 * (1.5 * r - 0.5 * r ** 3), 0.0)\n"
        ">>> def _disc(xc, yc, size, n):\n"
        "...     o = (_np.arange(n) + 0.5) / n * size - size / 2; px, py = _np.meshgrid(xc + o, yc + o)\n"
        "...     return px.ravel(), py.ravel()\n"
        ">>> def _gbar(size, n=5):\n"
        "...     px, py = _disc(0, 0, size, n)\n"
        "...     return float(_gb(px[:, None] - px[None, :], py[:, None] - py[None, :]).mean())\n"
        ">>> def _okb(xc, yc, size=50, nd=4, nmax=16):\n"
        "...     k = _np.argsort(_np.hypot(_x - xc, _y - yc))[:nmax]; xs, ys = _x[k], _y[k]; m = len(k)\n"
        "...     px, py = _disc(xc, yc, size, nd)\n"
        "...     A = _np.ones((m + 1, m + 1)); A[m, m] = 0; A[:m, :m] = _gb(xs[:, None] - xs[None, :], ys[:, None] - ys[None, :])\n"
        "...     b = _np.ones(m + 1); b[:m] = _gb(xs[:, None] - px[None, :], ys[:, None] - py[None, :]).mean(axis=1)\n"
        "...     s = _np.linalg.solve(A, b)\n"
        "...     return float(s[:m] @ _v[k]), float(s[:m] @ b[:m] + s[m] - _gbar(size, nd))\n")
TESTS = {
 "q1": [(BASE + ">>> bool(blocks_true.shape == (20, 24) and _np.allclose(blocks_true, _B))\nTrue",
         "blocks_true = T.reshape(20, 5, 24, 5).mean(axis=(1, 3)): each 50 m block is the mean of 5 × 5 truth cells."),
        (BASE + ">>> bool(abs(var_points - _T.var()) < 1e-12 and abs(var_blocks - _B.var()) < 1e-12 and abs(f_ratio - _B.var() / _T.var()) < 1e-12)\nTrue",
         "var_points = T.var(), var_blocks = blocks_true.var(), f_ratio = var_blocks / var_points."),
        (BASE + ">>> bool(abs(blocks_true.mean() - _T.mean()) < 1e-9)\nTrue", "Changing the support does not change the mean.")],
 "q2": [(BASE + ">>> _px, _py = _disc(100., 200., 50, 4)\n>>> _o = discretise(100., 200., 50, 4)\n"
         ">>> bool(_np.allclose(_np.sort(_o[0]), _np.sort(_px)) and _np.allclose(_np.sort(_o[1]), _np.sort(_py)) and len(_o[0]) == 16)\nTrue",
         "discretise(xc, yc, size, n): n × n points at the centres of n × n sub-cells, e.g. offsets ±6.25 and ±18.75 m for size 50, n 4."),
        (BASE + ">>> bool(abs(gamma_bar(gamma_bassam, 50, 5) - _gbar(50, 5)) < 1e-9 and abs(gbar_50 - _gbar(50, 5)) < 1e-9)\nTrue",
         "gamma_bar: mean of γ over ALL pairs of discretisation points (including a point with itself); gbar_50 with size 50, n 5."),
        (">>> bool(abs(block_var_model - (0.26 - gbar_50)) < 1e-9)\nTrue",
         "Krige's relation: dispersion variance of the blocks = total sill (0.26) - gbar_50.")],
 "q3": [(BASE + ">>> bool(all(abs(ok_block(a, b, 50, x, y, au, gamma_bassam)[0] - _okb(a, b)[0]) < 1e-6 and abs(ok_block(a, b, 50, x, y, au, gamma_bassam)[1] - _okb(a, b)[1]) < 1e-6 for a, b in [(325., 475.), (625., 225.), (1175., 975.)]))\nTrue",
         "Right-hand side = mean of γ between sample i and the 4 × 4 block points; block variance = Σλ b̄ + μ - γ̄(block).")],
 "q4": [(BASE + ">>> bool(bk_map.shape == (20, 24) and bk_var.shape == (20, 24))\nTrue", "bk_map and bk_var: one value per 50 m block, rows = north (20), columns = east (24)."),
        (BASE + ">>> bool(all(abs(bk_map[r, c] - _okb(25 + 50 * c, 25 + 50 * r)[0]) < 1e-6 for r, c in [(0, 0), (7, 11), (19, 23), (12, 3)]))\nTrue",
         "Block (r, c) has its centre at (25 + 50 c, 25 + 50 r)."),
        (BASE + ">>> bool(abs(bk_mse - _np.mean((bk_map - _B) ** 2)) < 1e-9)\nTrue", "bk_mse = mean((bk_map - blocks_true)**2).")],
 "q5": [(">>> import numpy as _np\n>>> bool(_np.allclose(cutoffs, _np.arange(0, 2.01, 0.25)))\nTrue", "cutoffs = np.arange(0, 2.01, 0.25)."),
        (">>> import numpy as _np\n>>> _t = _np.array([(bk_map >= c).sum() * 67500 / 1e6 for c in cutoffs])\n"
         ">>> _g = _np.array([bk_map[bk_map >= c].mean() if (bk_map >= c).any() else _np.nan for c in cutoffs])\n"
         ">>> bool(_np.allclose(tonnes_mt, _t) and _np.allclose(grade_above, _g, equal_nan=True))\nTrue",
         "One block = 50 × 50 × 10 m × 2.7 t/m³ = 67 500 t. tonnes_mt: tonnage of blocks with estimate >= cutoff (Mt); grade_above: their mean grade."),
        (">>> import numpy as _np\n>>> _t = _np.array([(blocks_true >= c).sum() * 67500 / 1e6 for c in cutoffs])\n>>> bool(_np.allclose(tonnes_true_mt, _t))\nTrue",
         "tonnes_true_mt: the same tonnage curve for blocks_true."),
        (">>> import numpy as _np\n>>> bool(abs(metal_koz - (bk_map[bk_map >= 1.0] * 67500).sum() / 31.1035 / 1000) < 1e-6)\nTrue",
         "metal_koz: gold contained in the blocks estimated >= 1.0 g/t, in thousands of troy ounces (1 oz = 31.1035 g).")],
}

def notebook():
    cells = [
        header(10, 'Change of support, block kriging and grade–tonnage', NB, '''
        A mine does not dig points: it digs **blocks** (here 50 m × 50 m × 10 m), and sends each block to the mill or
        to the waste dump. Block grades are averages, so they vary **less** than point grades: this is the
        **support effect**. Ignoring it is a classic error: a selection made on point-like estimates promises
        a tonnage that the mine never delivers.

        **What you will practise:** support and dispersion variance · Krige's relation · the average variogram
        $\\bar\\gamma$ · block kriging · grade–tonnage curves · contained metal.
        '''),
        setup_cell('w10', DATA, TESTS),
        otter_cell(),
        toolbox_cell('models', 'kriging'),
        code('''
        import pandas as pd
        import matplotlib.pyplot as plt

        def gamma_bassam(dx, dy):
            return spherical(aniso_h(dx, dy, 45, 300, 150), 0.06, 0.20, 300)   # total sill 0.26

        samples = pd.read_csv("bassam_samples.csv")
        x, y, au = samples["x"].to_numpy(), samples["y"].to_numpy(), samples["au_gpt"].to_numpy()
        T = pd.read_csv("bassam_truth_grid.csv")["au_gpt"].to_numpy().reshape(100, 120)   # 10 m cells
        '''),
        md('''
        ## 1. The support effect

        Average the true 10 m cells into 50 m blocks and compare the histograms: same mean, smaller spread.
        '''),
        code('''
        B = T.reshape(20, 5, 24, 5).mean(axis=(1, 3))
        plt.hist(T.ravel(), bins=50, density=True, alpha=0.5, label="10 m cells")
        plt.hist(B.ravel(), bins=30, density=True, alpha=0.5, label="50 m blocks")
        plt.xlabel("Au (g/t)"); plt.legend(); plt.show()
        print("share above 1.5 g/t:", (T >= 1.5).mean().round(3), "(cells)", (B >= 1.5).mean().round(3), "(blocks)")
        '''),
        md('''
        ## 2. The average variogram and Krige's relation

        The mean of $\\gamma$ over all pairs of points inside a block $v$ is $\\bar\\gamma(v, v)$. It is computed by
        **discretising** the block into $n \\times n$ points. Krige's relation links the variances of the supports:

        $$D^2(v \\mid D) = D^2(\\cdot \\mid D) - \\bar\\gamma(v, v)$$

        For a deposit much larger than the range, $D^2(\\cdot \\mid D)$ is the total sill. The larger the block, the
        larger $\\bar\\gamma(v,v)$, the smaller the variance of the blocks.

        ## 3. Block kriging

        Same system as point kriging, but the right-hand side uses the average variogram between each sample and the
        block, $\\bar\\gamma(\\mathbf{x}_i, v)$, and the variance becomes

        $$\\sigma^2_{OK}(v) = \\sum_i \\lambda_i \\bar\\gamma(\\mathbf{x}_i, v) + \\mu - \\bar\\gamma(v, v)$$

        ## 4. Grade–tonnage curves

        For each cut-off $z_c$: the tonnage of blocks with grade $\\ge z_c$, and their mean grade. These two curves
        drive the choice of the cut-off and the size of the mine.

        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. Point and block variances

        Store the true 50 m blocks in `blocks_true` (shape 20 × 24), the variance of the 10 m cells in `var_points`,
        that of the blocks in `var_blocks`, and their ratio in `f_ratio`.
        ''', '''
        blocks_true = ...
        var_points = ...
        var_blocks = ...
        f_ratio = ...
        var_points, var_blocks, f_ratio
        '''),
        *question('q2', '''
        ### Q2. Discretisation and $\\bar\\gamma$

        Write `discretise(xc, yc, size, n)` returning the arrays `(px, py)` of the $n \\times n$ points at the centres
        of the sub-cells of a square block of side `size` centred on `(xc, yc)`. Then write
        `gamma_bar(gamma, size, n=5)`, the mean of `gamma` over all pairs of these points. Store
        `gbar_50 = gamma_bar(gamma_bassam, 50, 5)` and the dispersion variance of 50 m blocks predicted by the model,
        `block_var_model` = 0.26 − `gbar_50`.
        ''', '''
        def discretise(xc, yc, size, n):
            ...

        def gamma_bar(gamma, size, n=5):
            ...

        gbar_50 = ...
        block_var_model = ...
        gbar_50, block_var_model
        '''),
        *question('q3', '''
        ### Q3. Block kriging

        Write `ok_block(xc, yc, size, x, y, v, gamma, nd=4, nmax=16)` returning `(estimate, variance)` for the block,
        using the `nmax` samples closest to the block centre and $nd \\times nd$ discretisation points.
        ''', '''
        def ok_block(xc, yc, size, x, y, v, gamma, nd=4, nmax=16):
            ...

        ok_block(625., 225., 50, x, y, au, gamma_bassam), ok_point(625., 225., x, y, au, gamma_bassam)
        '''),
        *question('q4', '''
        ### Q4. The block model

        Krig every 50 m block (centre `(25 + 50*c, 25 + 50*r)`): `bk_map` and `bk_var`, shape 20 × 24. Store the mean
        squared error against the true blocks in `bk_mse`.
        ''', '''
        bk_map = np.zeros((20, 24))
        bk_var = np.zeros((20, 24))
        ...
        bk_mse = ...
        bk_mse
        '''),
        *question('q5', '''
        ### Q5. Grade–tonnage

        With `cutoffs = np.arange(0, 2.01, 0.25)` and 67 500 t per block, compute for the kriged blocks the tonnage
        above each cut-off in Mt (`tonnes_mt`) and the mean grade above (`grade_above`), and the true tonnage curve
        `tonnes_true_mt`. Store the gold contained in the blocks estimated ≥ 1.0 g/t in thousands of ounces
        (`metal_koz`). Plot the curves. At which cut-offs does the kriged block model over- or under-state tonnage?
        ''', '''
        cutoffs = ...
        tonnes_mt = ...
        grade_above = ...
        tonnes_true_mt = ...
        metal_koz = ...
        metal_koz
        '''),
        *closing('''
        ### Going further (not checked)

        * Compute the tonnage above 1.5 g/t from the **point** kriging map of week 9 (20 m nodes) as if each node were a
          block. Why is it different from the 50 m block result?
        * Compute `gamma_bar` for blocks of 10, 25, 50, 100 m and plot the block dispersion variance against block size.
        '''),
    ]
    save_notebook(NB, 'w10', cells)

def build():
    write_tests('w10', TESTS)
    notebook()
    return f'{NB} written'
