# MEN 4338 week 8: ordinary kriging at a point (system, weights, kriging variance, screening, nugget).
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, toolbox_cell

NB = 'MEN4338_W8_ordinary_kriging_point.ipynb'
DATA = ['bassam_samples.csv']

GB = (">>> import numpy as _np\n>>> def _gb(dx, dy):\n"
      "...     t = _np.radians(45); u = dx * _np.sin(t) + dy * _np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n"
      "...     h = _np.sqrt(u ** 2 + (2 * w) ** 2); r = _np.minimum(h / 300, 1)\n"
      "...     return _np.where(h > 0, 0.06 + 0.20 * (1.5 * r - 0.5 * r ** 3), 0.0)\n"
      ">>> def _sys(xs, ys, x0, y0, g):\n"
      "...     n = len(xs); A = _np.ones((n + 1, n + 1)); A[n, n] = 0\n"
      "...     A[:n, :n] = g(xs[:, None] - xs[None, :], ys[:, None] - ys[None, :])\n"
      "...     b = _np.ones(n + 1); b[:n] = g(xs - x0, ys - y0)\n"
      "...     return A, b\n")
TOY = (">>> _xs = _np.array([100., 150, 120, 200]); _ys = _np.array([100., 120, 170, 160]); _vs = _np.array([1.2, 0.8, 1.5, 2.1])\n")
OKP = (">>> import pandas as _pd\n>>> _s = _pd.read_csv('bassam_samples.csv'); _x, _y, _v = (_s[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n"
       ">>> def _okp(x0, y0):\n"
       "...     k = _np.argsort(_np.hypot(_x - x0, _y - y0))[:16]\n"
       "...     A, b = _sys(_x[k], _y[k], x0, y0, _gb); s = _np.linalg.solve(A, b)\n"
       "...     return float(s[:16] @ _v[k]), float(s[:16] @ b[:16] + s[16])\n")
TESTS = {
 "q1": [(GB + TOY + ">>> _A, _b = _sys(_xs, _ys, 140., 140., _gb)\n>>> A, b = ok_matrices(_xs, _ys, 140., 140., gamma_bassam)\n"
         ">>> bool(A.shape == (5, 5) and b.shape == (5,) and _np.allclose(A, _A) and _np.allclose(b, _b))\nTrue",
         "A = [[Γ, 1], [1ᵀ, 0]] with Γ[i, j] = γ(x_i - x_j, y_i - y_j); b = [γ(x_i - x0, y_i - y0)..., 1]."),
        (GB + TOY + ">>> A, b = ok_matrices(_xs, _ys, 140., 140., gamma_bassam)\n>>> bool(_np.allclose(_np.diag(A)[:4], 0) and A[4, 4] == 0 and _np.allclose(A, A.T))\nTrue",
         "The diagonal of Γ is γ(0) = 0, the corner is 0 and A is symmetric.")],
 "q2": [(GB + TOY + ">>> _A, _b = _sys(_xs, _ys, 140., 140., _gb); _s = _np.linalg.solve(_A, _b)\n"
         ">>> bool(_np.allclose(weights, _s[:4]) and abs(mu - _s[4]) < 1e-9)\nTrue",
         "Solve A [λ, μ] = b with np.linalg.solve: weights = first 4 values, mu = the last one."),
        (">>> bool(abs(sum(weights) - 1) < 1e-9)\nTrue", "The ordinary kriging weights add up to 1 (unbiasedness).")],
 "q3": [(GB + TOY + ">>> _A, _b = _sys(_xs, _ys, 140., 140., _gb); _s = _np.linalg.solve(_A, _b)\n"
         ">>> bool(abs(ok_est - _s[:4] @ _vs) < 1e-9)\nTrue", "ok_est = sum(weights * values)."),
        (GB + TOY + ">>> _A, _b = _sys(_xs, _ys, 140., 140., _gb); _s = _np.linalg.solve(_A, _b)\n"
         ">>> bool(abs(ok_var - (_s[:4] @ _b[:4] + _s[4])) < 1e-9)\nTrue", "Kriging variance: σ²_OK = Σ λ_i γ(x_i - x0) + μ."),
        (">>> bool(0 < ok_var < 0.26 * 2)\nTrue", "The kriging variance is positive and of the order of the sill.")],
 "q4": [(">>> import numpy as _np\n>>> bool(_np.allclose(weights_nugget, 0.25))\nTrue",
         "With a pure nugget model every sample is equally (un)informative: each weight is 1/n."),
        (">>> bool(abs(ok_var_nugget - 1.25) < 1e-9)\nTrue", "Pure nugget of sill 1: σ²_OK = 1 + 1/n."),
        (GB + ">>> _xs = _np.array([140., 160, 165]); _ys = _np.array([140., 160, 165])\n>>> _A, _b = _sys(_xs, _ys, 140., 140., _gb)\n"
         ">>> bool(_np.allclose(weights_screen, _np.linalg.solve(_A, _b)[:3]))\nTrue",
         "weights_screen: OK weights with gamma_bassam for samples at (140,140), (160,160), (165,165) and target (140,140)."),
        (">>> bool(abs(weights_screen[0] - 1) < 1e-9)\nTrue", "A sample exactly at the target gets weight 1: kriging is an exact interpolator.")],
 "q5": [(GB + OKP + ">>> _t = [(312., 457.), (641., 213.), (906., 782.)]\n>>> bool(all(abs(a - _okp(*t)[0]) < 1e-6 and abs(b - _okp(*t)[1]) < 1e-6 for (a, b), t in zip(ok_targets, _t)))\nTrue",
         "ok_targets: list of (estimate, variance) from ok_point(x0, y0, x, y, au, gamma_bassam, nmax=16) at the 3 targets."),
        (GB + OKP + ">>> bool(abs(var_far - _okp(1190., 990.)[1]) < 1e-6 and var_far > max(v for _, v in ok_targets))\nTrue",
         "var_far: kriging variance at the corner (1190, 990), far from the infill: it should be larger.")],
}

def notebook():
    cells = [
        header(8, 'Ordinary kriging at a point', NB, '''
        Kriging is a weighted average like IDW, but the weights come from the **variogram**. They are the weights that
        make the estimate **unbiased** and the estimation **error variance as small as possible**. In exchange we get
        something IDW cannot give: the **kriging variance**, a measure of how reliable each estimate is.

        **What you will practise:** the ordinary kriging system · solving it with NumPy · the kriging variance ·
        the screening effect · exactness · the effect of the nugget.
        '''),
        setup_cell('w8', DATA, TESTS),
        otter_cell(),
        toolbox_cell('models'),
        code('''
        import pandas as pd
        import matplotlib.pyplot as plt

        def gamma_bassam(dx, dy):
            """Bassam model (week 5): nugget 0.06 + spherical 0.20, ranges 300 m (N045) and 150 m (N135)."""
            return spherical(aniso_h(dx, dy, 45, 300, 150), 0.06, 0.20, 300)

        samples = pd.read_csv("bassam_samples.csv")
        x, y, au = samples["x"].to_numpy(), samples["y"].to_numpy(), samples["au_gpt"].to_numpy()
        '''),
        md('''
        ## 1. The ordinary kriging system

        We look for $z^* = \\sum_i \\lambda_i z_i$ with $\\sum_i \\lambda_i = 1$ (no bias when the mean is unknown)
        that minimises the error variance. With a Lagrange multiplier $\\mu$ for the constraint, the solution is
        the linear system

        $$
        \\begin{bmatrix} \\gamma_{11} & \\cdots & \\gamma_{1n} & 1 \\\\ \\vdots & & \\vdots & \\vdots \\\\
        \\gamma_{n1} & \\cdots & \\gamma_{nn} & 1 \\\\ 1 & \\cdots & 1 & 0 \\end{bmatrix}
        \\begin{bmatrix} \\lambda_1 \\\\ \\vdots \\\\ \\lambda_n \\\\ \\mu \\end{bmatrix} =
        \\begin{bmatrix} \\gamma_{10} \\\\ \\vdots \\\\ \\gamma_{n0} \\\\ 1 \\end{bmatrix}
        $$

        where $\\gamma_{ij} = \\gamma(\\mathbf{x}_i - \\mathbf{x}_j)$ and $\\gamma_{i0} = \\gamma(\\mathbf{x}_i - \\mathbf{x}_0)$.
        The **kriging variance** is

        $$\\sigma^2_{OK} = \\sum_i \\lambda_i \\gamma_{i0} + \\mu$$

        It depends on the geometry of the data and on the variogram, **not on the grade values**.

        ## 2. What the weights do

        * Samples **closer** to the target, measured in the anisotropic distance, get more weight.
        * Samples **hidden behind** another sample get little weight (screening effect).
        * **Clustered** samples share the weight of one sample: kriging declusters by itself.
        * Weights can be slightly **negative** when there is strong screening.
        '''),
        code('''
        xs = np.array([100., 150, 120, 200]); ys = np.array([100., 120, 170, 160])
        vs = np.array([1.2, 0.8, 1.5, 2.1]); x0, y0 = 140., 140.
        plt.figure(figsize=(4, 4))
        plt.scatter(xs, ys, s=60); plt.scatter([x0], [y0], marker="x", s=80, c="red")
        for k, (a, b) in enumerate(zip(xs, ys)): plt.annotate(f"{k}: {vs[k]}", (a + 3, b + 3))
        plt.gca().set_aspect("equal"); plt.title("4 samples and the target"); plt.show()
        '''),
        md('''
        ---
        ## Exercises

        Q1 to Q3 use the 4 samples above (`xs`, `ys`, `vs`) and the target `(x0, y0)`.
        '''),
        *question('q1', '''
        ### Q1. Build the system

        Write `ok_matrices(xs, ys, x0, y0, gamma)` returning `(A, b)` as defined above. `gamma(dx, dy)` is a variogram
        model of the separation vector, such as `gamma_bassam`.

        *Hint:* `xs[:, None] - xs[None, :]` gives the matrix of all differences.
        ''', '''
        def ok_matrices(xs, ys, x0, y0, gamma):
            ...

        A, b = ok_matrices(xs, ys, x0, y0, gamma_bassam)
        np.round(A, 3), np.round(b, 3)
        '''),
        *question('q2', '''
        ### Q2. Solve it

        Solve the system: store the 4 weights in `weights` and the Lagrange multiplier in `mu`. Which sample gets the
        largest weight? Is it the closest one in plain distance?
        ''', '''
        sol = ...
        weights = ...
        mu = ...
        np.round(weights, 3), mu
        '''),
        *question('q3', '''
        ### Q3. Estimate and kriging variance

        Store the estimate in `ok_est` and the kriging variance in `ok_var`.
        ''', '''
        ok_est = ...
        ok_var = ...
        ok_est, ok_var
        '''),
        *question('q4', '''
        ### Q4. Nugget, screening and exactness

        1. With a **pure nugget** model of sill 1, `gamma_nugget = lambda dx, dy: np.where(np.hypot(dx, dy) > 0, 1.0, 0.0)`,
           compute the weights of the 4 samples (`weights_nugget`) and the kriging variance (`ok_var_nugget`).
           What does kriging become?
        2. With `gamma_bassam`, compute the weights `weights_screen` for three samples at (140, 140), (160, 160) and
           (165, 165), and the target (140, 140). What happens to the first weight, and why?
        ''', '''
        gamma_nugget = lambda dx, dy: np.where(np.hypot(dx, dy) > 0, 1.0, 0.0)
        weights_nugget = ...
        ok_var_nugget = ...

        weights_screen = ...
        weights_nugget, ok_var_nugget, np.round(weights_screen, 4)
        '''),
        *question('q5', '''
        ### Q5. Kriging the Bassam data

        Write `ok_point(x0, y0, x, y, v, gamma, nmax=16)` that krigs a point from its `nmax` closest samples and
        returns `(estimate, variance)`. Store in `ok_targets` the results at (312, 457), (641, 213) and (906, 782),
        and in `var_far` the kriging variance at (1190, 990).
        ''', '''
        def ok_point(x0, y0, x, y, v, gamma, nmax=16):
            ...

        ok_targets = ...
        var_far = ...
        ok_targets, var_far
        '''),
        *closing('''
        ### Going further (not checked)

        * Move the target along a line from (0, 500) to (1200, 500) and plot the kriging variance. Where is it lowest?
        * Replace `gamma_bassam` by an isotropic model (range 225 m) at (641, 213). How do the weights change?
        '''),
    ]
    save_notebook(NB, 'w8', cells)

def build():
    write_tests('w8', TESTS)
    notebook()
    return f'{NB} written'
