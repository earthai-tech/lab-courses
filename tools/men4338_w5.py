# MEN 4338 week 5: variogram models, fitting and the anisotropic model of the Bassam deposit.
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, toolbox_cell

NB = 'MEN4338_W5_variogram_models_fitting.ipynb'
DATA = ['bassam_samples.csv']

SPH = (">>> import numpy as _np\n>>> def _sph(h, c0, c, a):\n...     h = _np.asarray(h, float); r = _np.minimum(h / a, 1)\n"
       "...     return _np.where(h > 0, c0 + c * (1.5 * r - 0.5 * r ** 3), 0.0)\n")
VG = (">>> import pandas as _pd\n>>> _s = _pd.read_csv('bassam_samples.csv'); _g = _s[_s['campaign'] == 'grid']\n"
      ">>> _h, _gm, _n = exp_variogram(_g['x'], _g['y'], _g['au_gpt'], 50, 12)\n")
GRID = (">>> _best = min(_np.sum(_n * (_gm - _sph(_h, c0, c, a)) ** 2) for c0 in _np.arange(0, 0.151, 0.01) for c in _np.arange(0.05, 0.301, 0.01) for a in range(50, 501, 10))\n")
TESTS = {
 "q1": [(SPH + ">>> _h = _np.array([0, 10, 50, 99.9, 100, 250])\n>>> bool(_np.allclose(spherical(_h, 0.1, 0.5, 100), _sph(_h, 0.1, 0.5, 100)))\nTrue",
         "spherical: c0 + c (1.5 h/a - 0.5 (h/a)^3) for h < a, c0 + c beyond, and exactly 0 at h = 0."),
        (">>> bool(float(spherical(0.0, 0.1, 0.5, 100)) == 0.0 and abs(float(spherical(1e-9, 0.1, 0.5, 100)) - 0.1) < 1e-6)\nTrue",
         "γ(0) = 0 but γ jumps to the nugget c0 as soon as h > 0: use np.where(h > 0, ..., 0.0).")],
 "q2": [(">>> import numpy as _np\n>>> _h = _np.array([0., 30, 100, 300])\n"
         ">>> bool(_np.allclose(exponential(_h, 0.1, 0.5, 100), _np.where(_h > 0, 0.1 + 0.5 * (1 - _np.exp(-3 * _h / 100)), 0)))\nTrue",
         "exponential with practical range a: c0 + c (1 - exp(-3h/a)), and 0 at h = 0."),
        (">>> import numpy as _np\n>>> _h = _np.array([0., 30, 100, 300])\n"
         ">>> bool(_np.allclose(gaussian(_h, 0.1, 0.5, 100), _np.where(_h > 0, 0.1 + 0.5 * (1 - _np.exp(-3 * (_h / 100) ** 2)), 0)))\nTrue",
         "gaussian with practical range a: c0 + c (1 - exp(-3 (h/a)^2)), and 0 at h = 0."),
        (">>> bool(abs(float(exponential(100.0, 0, 1, 100)) - 0.95) < 0.001)\nTrue", "At the practical range the model reaches 95 % of the sill: 1 - exp(-3) ≈ 0.95.")],
 "q3": [(SPH + VG + ">>> bool(_np.allclose(h_exp, _h) and _np.allclose(g_exp, _gm) and _np.allclose(n_exp, _n))\nTrue",
         "h_exp, g_exp, n_exp = exp_variogram(x, y, au, 50, 12) on the grid holes."),
        (SPH + VG + ">>> bool(abs(wsse((0.05, 0.2, 250), _h, _gm, _n) - _np.sum(_n * (_gm - _sph(_h, 0.05, 0.2, 250)) ** 2)) < 1e-9)\nTrue",
         "wsse(params, h, g, n) = sum of n * (g - spherical(h, c0, c, a))**2 with params = (c0, c, a).")],
 "q4": [(SPH + VG + GRID + ">>> bool(wsse(best_params, _h, _gm, _n) <= _best * (1 + 1e-9))\nTrue",
         "Search c0 in 0..0.15 (step 0.01), c in 0.05..0.30 (step 0.01), a in 50..500 m (step 10) and keep the triple with the smallest wsse."),
        (">>> bool(len(best_params) == 3 and all(p >= 0 for p in best_params))\nTrue", "best_params = (c0, c, a), all non-negative."),
        (">>> bool(abs(nugget_ratio - best_params[0] / (best_params[0] + best_params[1])) < 1e-9)\nTrue",
         "nugget_ratio = c0 / (c0 + c): the share of the variance that is not spatially structured.")],
 "q5": [(">>> import numpy as _np\n>>> bool(_np.allclose(aniso_h(_np.array([0., 100, 70.71067811865476]), _np.array([100., 0, 70.71067811865476]), 0, 300, 100), [100, 300, 223.60679774997897]))\nTrue",
         "Rotate (dx, dy) into the major (u) and minor (w) axes, then h = sqrt(u² + (w · a_major / a_minor)²)."),
        (">>> import numpy as _np\n>>> bool(abs(float(aniso_h(70.71067811865476, 70.71067811865476, 45, 300, 150)) - 100) < 1e-6 and abs(float(aniso_h(-70.71067811865476, 70.71067811865476, 45, 300, 150)) - 200) < 1e-6)\nTrue",
         "For azimuth 45: u = dx sin(45°) + dy cos(45°) runs along N045, w = dx cos(45°) - dy sin(45°) along N135."),
        (SPH + ">>> _t = _np.radians(45)\n>>> def _ah(dx, dy):\n...     u = dx * _np.sin(_t) + dy * _np.cos(_t); w = dx * _np.cos(_t) - dy * _np.sin(_t)\n...     return _np.sqrt(u ** 2 + (w * 2) ** 2)\n"
         ">>> _dx = _np.array([0., 50, -80, 120]); _dy = _np.array([0., 50, 80, -10])\n>>> bool(_np.allclose(gamma_bassam(_dx, _dy), _sph(_ah(_dx, _dy), 0.06, 0.20, 300)))\nTrue",
         "gamma_bassam(dx, dy) = spherical(aniso_h(dx, dy, 45, 300, 150), 0.06, 0.20, 300).")],
}

def notebook():
    cells = [
        header(5, 'Variogram models and fitting', NB, '''
        The experimental variogram is only known at a few lags, and kriging needs $\\gamma(h)$ at **every** distance
        and direction. We therefore fit a **model**: a smooth function from a small family of shapes that are
        mathematically safe (they never give a negative kriging variance). This week ends with the model of the
        Bassam deposit that we will use for estimation from week 8.

        **What you will practise:** nugget, spherical, exponential and Gaussian models · practical range ·
        nested structures · weighted least-squares fitting · anisotropic models.
        '''),
        setup_cell('w5', DATA, TESTS),
        otter_cell(),
        toolbox_cell('variogram'),
        md('''
        ## 1. The standard models

        | model | $\\gamma(h)$ for $h > 0$ | behaviour near 0 |
        |---|---|---|
        | nugget | $c_0$ | discontinuous |
        | spherical | $c_0 + c\\left(\\tfrac32 \\tfrac{h}{a} - \\tfrac12 \\tfrac{h^3}{a^3}\\right)$ if $h < a$, else $c_0 + c$ | linear: most grades |
        | exponential | $c_0 + c\\,(1 - e^{-3h/a})$ | linear, reaches the sill only asymptotically |
        | Gaussian | $c_0 + c\\,(1 - e^{-3h^2/a^2})$ | parabolic: very smooth variables (topography, thickness) |

        and $\\gamma(0) = 0$ always. For the exponential and Gaussian models $a$ is the **practical range**: the
        distance where 95 % of the sill is reached.

        Several structures can be added (**nested** model), e.g. nugget + short-range spherical + long-range spherical.
        '''),
        code('''
        import pandas as pd
        import matplotlib.pyplot as plt

        h = np.linspace(0, 400, 401)
        r = np.minimum(h / 200, 1)
        sph = np.where(h > 0, 0.05 + 0.2 * (1.5 * r - 0.5 * r ** 3), 0)
        exp_ = np.where(h > 0, 0.05 + 0.2 * (1 - np.exp(-3 * h / 200)), 0)
        gau = np.where(h > 0, 0.05 + 0.2 * (1 - np.exp(-3 * (h / 200) ** 2)), 0)
        plt.figure(figsize=(7, 4))
        for g, lab in [(sph, "spherical"), (exp_, "exponential"), (gau, "Gaussian")]:
            plt.plot(h, g, label=lab)
        plt.axvline(200, ls=":", color="grey"); plt.axhline(0.25, ls="--", color="grey")
        plt.xlabel("h (m)"); plt.ylabel("γ(h)"); plt.legend(); plt.title("c0 = 0.05, c = 0.2, a = 200 m")
        plt.show()
        '''),
        md('''
        ## 2. Fitting

        Fitting "by eye" is still common, and a good habit to check any automatic fit. An automatic fit minimises the
        **weighted sum of squared errors**, giving more weight to lags with many pairs:

        $$WSSE(c_0, c, a) = \\sum_k N(h_k)\\,\\big(\\hat\\gamma(h_k) - \\gamma_{model}(h_k)\\big)^2$$

        Always look at the result: a perfect numerical fit with a silly range is still silly.
        '''),
        code('''
        samples = pd.read_csv("bassam_samples.csv")
        grid = samples[samples["campaign"] == "grid"]
        x, y, au = grid["x"].to_numpy(), grid["y"].to_numpy(), grid["au_gpt"].to_numpy()
        '''),
        md('''
        ## 3. Anisotropic models

        A geometric anisotropy is modelled by **rescaling distances**: rotate the separation vector into the major
        ($u$) and minor ($w$) axes, stretch the minor component by $a_{max}/a_{min}$, and apply an isotropic model
        with range $a_{max}$:

        $$u = \\Delta x \\sin\\theta + \\Delta y \\cos\\theta, \\quad w = \\Delta x \\cos\\theta - \\Delta y \\sin\\theta, \\quad
        h' = \\sqrt{u^2 + \\left(w \\, a_{max}/a_{min}\\right)^2}$$

        with $\\theta$ the azimuth of the major direction.

        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. The spherical model

        Write `spherical(h, c0, c, a)`, working on numbers and arrays, with $\\gamma(0) = 0$.
        ''', '''
        def spherical(h, c0, c, a):
            ...

        spherical(np.array([0, 50, 100, 200, 300]), 0.05, 0.2, 200)
        '''),
        *question('q2', '''
        ### Q2. Exponential and Gaussian

        Write `exponential(h, c0, c, a)` and `gaussian(h, c0, c, a)` with the practical-range convention, and
        $\\gamma(0) = 0$.
        ''', '''
        def exponential(h, c0, c, a):
            ...

        def gaussian(h, c0, c, a):
            ...

        exponential(200.0, 0, 1, 200), gaussian(200.0, 0, 1, 200)
        '''),
        *question('q3', '''
        ### Q3. The fitting criterion

        Compute the experimental variogram of the grid holes, lag 50 m and 12 lags: `h_exp, g_exp, n_exp`.
        Write `wsse(params, h, g, n)` returning the weighted sum of squared errors of a spherical model with
        `params = (c0, c, a)`.
        ''', '''
        h_exp, g_exp, n_exp = ...

        def wsse(params, h, g, n):
            ...

        wsse((0.05, 0.2, 250), h_exp, g_exp, n_exp)
        '''),
        *question('q4', '''
        ### Q4. Best spherical model

        Search all combinations of $c_0$ from 0 to 0.15 (step 0.01), $c$ from 0.05 to 0.30 (step 0.01) and $a$
        from 50 to 500 m (step 10) and keep the one with the smallest `wsse` in `best_params = (c0, c, a)`.
        Store `nugget_ratio` = $c_0 / (c_0 + c)$. Plot the experimental points and the fitted model.

        *Hint:* `np.arange(0, 0.151, 0.01)` includes 0.15; three nested `for` loops are fine (about 19 000 tries).
        ''', '''
        best_params = ...
        ...
        nugget_ratio = ...
        best_params, nugget_ratio
        '''),
        *question('q5', '''
        ### Q5. The Bassam model

        Write `aniso_h(dx, dy, azimuth, a_major, a_minor)` returning the rescaled distance $h'$. Then define
        `gamma_bassam(dx, dy)`: the model fitted on the directional variograms of week 4, which we keep for the rest
        of the semester:

        * nugget 0.06, one spherical structure with partial sill 0.20,
        * major direction N045 with range 300 m, minor direction N135 with range 150 m.

        Check it: plot the model along N045 and N135 on top of the directional variograms.
        ''', '''
        def aniso_h(dx, dy, azimuth, a_major, a_minor):
            ...

        def gamma_bassam(dx, dy):
            ...

        gamma_bassam(np.array([70.7, -70.7]), np.array([70.7, 70.7]))   # 100 m along N045 and along N135
        '''),
        *closing('''
        ### Going further (not checked)

        * Use `scipy.optimize.curve_fit` with `sigma=1/np.sqrt(n_exp)` to fit the spherical model. Same answer?
        * Fit an exponential model and compare its WSSE with the spherical one. Which one would you choose, and why?
        '''),
    ]
    save_notebook(NB, 'w5', cells)

def build():
    write_tests('w5', TESTS)
    notebook()
    return f'{NB} written'
