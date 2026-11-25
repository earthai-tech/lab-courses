# MEN 4338 week 13: sequential Gaussian simulation and the uncertainty of a resource.
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, toolbox_cell

NB = 'MEN4338_W13_sequential_gaussian_simulation.ipynb'
DATA = ['bassam_samples.csv']

NS = (">>> import numpy as _np, pandas as _pd\n>>> from scipy.stats import norm as _norm\n"
      ">>> _s = _pd.read_csv('bassam_samples.csv'); _v = _s['au_gpt'].to_numpy()\n"
      ">>> def _ns(v):\n...     r = _np.argsort(_np.argsort(v)); return _norm.ppf((r + 0.5) / len(v))\n")
GN = (">>> def _gn(dx, dy):\n"
      "...     t = _np.radians(45); u = dx * _np.sin(t) + dy * _np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n"
      "...     h = _np.sqrt(u ** 2 + (2 * w) ** 2); r = _np.minimum(h / 300, 1)\n"
      "...     return _np.where(h > 0, 0.15 + 0.85 * (1.5 * r - 0.5 * r ** 3), 0.0)\n"
      ">>> def _sk(x0, y0, xs, ys, vs):\n"
      "...     C = 1 - _gn(xs[:, None] - xs[None, :], ys[:, None] - ys[None, :]); c0 = 1 - _gn(xs - x0, ys - y0)\n"
      "...     lam = _np.linalg.solve(C, c0); return float(lam @ vs), float(1 - lam @ c0)\n")
TESTS = {
 "q1": [(NS + ">>> bool(_np.allclose(nscore(_np.array([3., 1, 2, 10])), _norm.ppf([0.625, 0.125, 0.375, 0.875])))\nTrue",
         "Rank the values (0 = smallest), then y = norm.ppf((rank + 0.5) / n)."),
        (NS + ">>> bool(_np.allclose(y_ns, _ns(_v)) and abs(y_ns.mean()) < 1e-9)\nTrue", "y_ns = nscore(au): mean 0 and variance close to 1.")],
 "q2": [(NS + ">>> bool(_np.allclose(back_transform(_ns(_v), _v), _v))\nTrue",
         "back_transform(y, v) = np.interp(y, np.sort(nscore(v)), np.sort(v)): it must give the data back exactly."),
        (NS + ">>> bool(_np.allclose(back_transform(_np.array([-9., 9.]), _v), [_v.min(), _v.max()]))\nTrue",
         "Beyond the extreme normal scores, np.interp keeps the minimum and maximum grade.")],
 "q3": [(NS + GN + ">>> _xs = _np.array([0., 60, 0, 100]); _ys = _np.array([0., 0, 50, 100]); _vs = _np.array([0.5, -0.2, 1.1, 0.3])\n"
         ">>> _o = sk_normal(30., 20., _xs, _ys, _vs, gamma_ns)\n>>> bool(abs(_o[0] - _sk(30., 20., _xs, _ys, _vs)[0]) < 1e-9 and abs(_o[1] - _sk(30., 20., _xs, _ys, _vs)[1]) < 1e-9)\nTrue",
         "Simple kriging with mean 0 and sill 1: C = 1 - γ; λ = solve(C, c0); mean = λ · values; variance = 1 - λ · c0."),
        (NS + GN + ">>> _xs = _np.array([0., 60]); _ys = _np.array([0., 0]); _vs = _np.array([0.5, -0.2])\n"
         ">>> bool(abs(sk_normal(5000., 5000., _xs, _ys, _vs, gamma_ns)[0]) < 1e-9 and abs(sk_normal(5000., 5000., _xs, _ys, _vs, gamma_ns)[1] - 1) < 1e-9)\nTrue",
         "Far from all data, SK returns the mean (0) and the full variance (1).")],
 "q4": [(">>> bool(reals.shape == (20, 33, 40))\nTrue", "reals: 20 realisations on 33 rows × 40 columns (30 m nodes)."),
        (NS + ">>> bool(reals.min() >= _v.min() - 1e-9 and reals.max() <= _v.max() + 1e-9)\nTrue", "Back-transform each realisation to grades: values stay within the data range."),
        (">>> import numpy as _np\n>>> bool(0.85 < reals.mean() < 1.25 and _np.mean([r.var() for r in reals]) > 0.12)\nTrue",
         "Each realisation should have a mean near 1 g/t and a variance close to that of the data (no smoothing).")],
 "q5": [(">>> import numpy as _np\n>>> _t = _np.array([(r >= 1.0).sum() * 24300 / 1e6 for r in reals])\n>>> bool(_np.allclose(tonnage_mt, _t))\nTrue",
         "One 30 m node = 30 × 30 × 10 m × 2.7 t/m³ = 24 300 t. tonnage_mt[k]: tonnage of nodes >= 1.0 g/t in realisation k (Mt)."),
        (">>> import numpy as _np\n>>> bool(_np.allclose([t_p90, t_p50, t_p10], _np.percentile(tonnage_mt, [10, 50, 90])))\nTrue",
         "P90 = 10th percentile (the value exceeded in 90 % of the realisations), P50 = median, P10 = 90th percentile."),
        (">>> import numpy as _np\n>>> bool(prob_ore.shape == (33, 40) and _np.allclose(prob_ore, (reals >= 1.0).mean(axis=0)))\nTrue",
         "prob_ore: share of the realisations above 1.0 g/t at each node.")],
}

def notebook():
    cells = [
        header(13, 'Sequential Gaussian simulation', NB, '''
        Kriging gives the best estimate at each point, but a kriged map is too smooth to look like the real deposit:
        its histogram is too narrow, and summing kriged values does not tell how uncertain the total tonnage is.
        **Simulation** draws many equally probable versions of the deposit, each honouring the data, the histogram
        and the variogram. Their spread **is** the uncertainty. This is how banks and boards are told that a
        resource is "18 Mt, between 15 and 21 Mt with 80 % confidence".

        **What you will practise:** the normal-score transform · simple kriging in Gaussian space · the sequential
        algorithm (random path, conditioning on simulated nodes) · back-transform · probability maps · P90/P50/P10.
        '''),
        setup_cell('w13', DATA, TESTS),
        otter_cell(),
        toolbox_cell('models'),
        code('''
        import pandas as pd
        import matplotlib.pyplot as plt
        from scipy.stats import norm

        samples = pd.read_csv("bassam_samples.csv")
        x, y, au = samples["x"].to_numpy(), samples["y"].to_numpy(), samples["au_gpt"].to_numpy()

        def gamma_ns(dx, dy):
            """Variogram of the normal scores (sill 1): nugget 0.15 + spherical 0.85, 300 m along N045, 150 m along N135."""
            return spherical(aniso_h(dx, dy, 45, 300, 150), 0.15, 0.85, 300)
        '''),
        md('''
        ## 1. Why a Gaussian transform?

        The algorithm relies on a property of the multi-Gaussian model: the conditional distribution at a node given
        its neighbours is **normal**, with mean and variance given by **simple kriging**. Grades are not normal, so we
        first map them onto a standard normal distribution by **ranks** (normal scores), simulate, and map back.

        $$y_i = G^{-1}\\!\\left(\\frac{r_i + 0.5}{n}\\right)$$

        where $r_i$ is the rank of $z_i$ (0 for the smallest) and $G^{-1}$ is `norm.ppf`.

        ## 2. The sequential algorithm

        1. Transform the data to normal scores.
        2. Visit the grid nodes in a **random order**.
        3. At each node: simple-krige (mean 0, sill 1) from the nearest data **and previously simulated nodes**;
           draw a value from $N(y^*_{SK}, \\sigma^2_{SK})$; add it to the conditioning data.
        4. Back-transform all nodes to grades.

        A different random seed gives a different, equally probable, realisation.

        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. Normal scores

        Write `nscore(v)` returning the normal scores of an array (ranks with `np.argsort(np.argsort(v))`). Store the
        normal scores of `au` in `y_ns` and plot their histogram.
        ''', '''
        def nscore(v):
            ...

        y_ns = ...
        y_ns.mean(), y_ns.var()
        '''),
        *question('q2', '''
        ### Q2. Back-transform

        Write `back_transform(yv, v)` mapping normal scores `yv` back to grades with `np.interp`, using the pairs
        (sorted normal scores of `v`, sorted `v`).
        ''', '''
        def back_transform(yv, v):
            ...

        np.allclose(back_transform(y_ns, au), au)
        '''),
        *question('q3', '''
        ### Q3. Simple kriging in Gaussian space

        Write `sk_normal(x0, y0, xs, ys, vs, gamma)` returning `(mean, variance)` of simple kriging with mean 0 and
        sill 1 from the points `(xs, ys)` with normal-score values `vs`.
        ''', '''
        def sk_normal(x0, y0, xs, ys, vs, gamma):
            ...

        sk_normal(30., 20., np.array([0., 60, 0]), np.array([0., 0, 50]), np.array([0.5, -0.2, 1.1]), gamma_ns)
        '''),
        md('''
        ## 3. The simulation engine

        The function below is complete: it uses your `sk_normal`. Read it line by line, then run it.
        '''),
        code('''
        def sgs(gx, gy, xd, yd, yd_ns, gamma, seed, nmax=12):
            """One realisation in normal scores on the nodes (gx, gy) (1D arrays), conditioned on (xd, yd, yd_ns)."""
            rng = np.random.default_rng(seed)
            px, py, pv = list(xd), list(yd), list(yd_ns)          # conditioning points: data + simulated nodes
            out = np.zeros(len(gx))
            for node in rng.permutation(len(gx)):                 # random path
                ax, ay, av = np.array(px), np.array(py), np.array(pv)
                k = np.argsort(np.hypot(ax - gx[node], ay - gy[node]))[:nmax]
                m, v = sk_normal(gx[node], gy[node], ax[k], ay[k], av[k], gamma)
                out[node] = rng.normal(m, np.sqrt(max(v, 0.0)))
                px.append(gx[node]); py.append(gy[node]); pv.append(out[node])
            return out

        GX, GY = np.meshgrid(np.arange(15, 1200, 30), np.arange(15, 1000, 30))   # 33 rows x 40 columns
        print(GX.shape)
        '''),
        *question('q4', '''
        ### Q4. Twenty realisations

        Run `sgs` with seeds 0 to 19 on the nodes `GX.ravel(), GY.ravel()`, back-transform each realisation to grades
        and reshape it to `GX.shape`. Store them in `reals` (shape 20 × 33 × 40). This takes from a few seconds to a minute. Draw two
        realisations side by side: same data, different deposits.
        ''', '''
        reals = ...
        reals.shape
        '''),
        *question('q5', '''
        ### Q5. Uncertainty on the resource

        Each 30 m node stands for 24 300 t. Store in `tonnage_mt` the tonnage above 1.0 g/t of each realisation (Mt),
        the P90, P50 and P10 in `t_p90, t_p50, t_p10` (P90 = 10th percentile), and the probability map
        `prob_ore` = share of realisations above 1.0 g/t at each node. Draw the histogram of `tonnage_mt` and the map.
        ''', '''
        tonnage_mt = ...
        t_p90, t_p50, t_p10 = ...
        prob_ore = ...
        t_p90, t_p50, t_p10
        '''),
        *closing('''
        ### Going further (not checked)

        * Average the 20 realisations node by node (the "E-type" map) and compare it with a kriging map: which one is smoother?
        * Compare `prob_ore` with the indicator kriging map of week 12.
        * How much do P90 and P10 move with 50 realisations instead of 20?
        '''),
    ]
    save_notebook(NB, 'w13', cells)

def build():
    write_tests('w13', TESTS)
    notebook()
    return f'{NB} written'
