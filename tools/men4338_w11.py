# MEN 4338 week 11: trends, simple kriging and universal kriging of reservoir porosity.
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, toolbox_cell

NB = 'MEN4338_W11_trend_simple_universal_kriging.ipynb'
DATA = ['porosity_wells.csv']

BASE = (">>> import numpy as _np, pandas as _pd\n>>> _p = _pd.read_csv('porosity_wells.csv')\n"
        ">>> _x, _y = _p['x'].to_numpy(float), _p['y'].to_numpy(float); _v = 100 * _p['phi'].to_numpy()\n"
        ">>> _F = _np.c_[_np.ones(len(_x)), _x / 1000, _y / 1000]; _c = _np.linalg.lstsq(_F, _v, rcond=None)[0]; _r = _v - _F @ _c\n"
        ">>> def _g(dx, dy):\n...     h = _np.hypot(dx, dy); q = _np.minimum(h / 1000, 1)\n"
        "...     return _np.where(h > 0, 0.3 + 1.5 * (1.5 * q - 0.5 * q ** 3), 0.0)\n"
        ">>> def _sk(x0, y0):\n"
        "...     C = 1.8 - _g(_x[:, None] - _x[None, :], _y[:, None] - _y[None, :]); c0 = 1.8 - _g(_x - x0, _y - y0)\n"
        "...     lam = _np.linalg.solve(C, c0)\n"
        "...     return float(lam @ _r), float(1.8 - lam @ c0)\n"
        ">>> def _uk(x0, y0):\n"
        "...     n = len(_x); A = _np.zeros((n + 3, n + 3)); A[:n, :n] = _g(_x[:, None] - _x[None, :], _y[:, None] - _y[None, :])\n"
        "...     A[:n, n:] = _F; A[n:, :n] = _F.T\n"
        "...     b = _np.concatenate([_g(_x - x0, _y - y0), [1, x0 / 1000, y0 / 1000]]); s = _np.linalg.solve(A, b)\n"
        "...     return float(s[:n] @ _v), float(s @ b)\n")
TESTS = {
 "q1": [(BASE + ">>> bool(_np.allclose(trend_coef, _c))\nTrue",
         "Least squares on the design matrix [1, x/1000, y/1000] (coordinates in km): np.linalg.lstsq(F, phi_pct, rcond=None)[0]."),
        (BASE + ">>> bool(_np.allclose(resid, _r))\nTrue", "resid = phi_pct - F @ trend_coef."),
        (BASE + ">>> bool(abs(trend_at_center - (_c[0] + _c[1] * 2 + _c[2] * 1.5)) < 1e-9)\nTrue", "trend_at_center: the trend at x = 2000 m, y = 1500 m.")],
 "q2": [(BASE + ">>> bool(abs(raw_var - _v.var(ddof=1)) < 1e-9 and abs(resid_var - _r.var(ddof=1)) < 1e-9)\nTrue",
         "raw_var and resid_var: sample variances (ddof=1) of phi_pct and of resid."),
        (BASE + ">>> bool(_np.allclose(g_raw, exp_variogram(_x, _y, _v, 400, 8)[1]) and _np.allclose(g_res, exp_variogram(_x, _y, _r, 400, 8)[1]))\nTrue",
         "g_raw and g_res: semivariances with lag 400 m and 8 lags, of phi_pct and of resid.")],
 "q3": [(BASE + ">>> bool(all(abs(sk_residual(a, b, x, y, resid, gamma_res, 1.8)[0] - _sk(a, b)[0]) < 1e-6 and abs(sk_residual(a, b, x, y, resid, gamma_res, 1.8)[1] - _sk(a, b)[1]) < 1e-6 for a, b in [(2000., 1500.), (500., 2600.)]))\nTrue",
         "Simple kriging with mean 0: C λ = c0 with C = sill - γ; estimate = λ · resid; variance = sill - λ · c0. Use all wells."),
        (BASE + ">>> bool(abs(phi_sk_center - (_c[0] + _c[1] * 2 + _c[2] * 1.5 + _sk(2000., 1500.)[0])) < 1e-6)\nTrue",
         "phi_sk_center = trend at (2000, 1500) + simple-kriged residual there.")],
 "q4": [(BASE + ">>> bool(all(abs(uk_point(a, b, x, y, phi_pct, gamma_res)[0] - _uk(a, b)[0]) < 1e-6 and abs(uk_point(a, b, x, y, phi_pct, gamma_res)[1] - _uk(a, b)[1]) < 1e-6 for a, b in [(2000., 1500.), (500., 2600.)]))\nTrue",
         "UK system: [[Γ, F], [Fᵀ, 0]] [λ, μ] = [γ0, 1, x0/1000, y0/1000]; estimate = λ · phi_pct; variance = [λ, μ] · right-hand side."),
        (BASE + ">>> bool(abs(phi_uk_center - _uk(2000., 1500.)[0]) < 1e-6)\nTrue", "phi_uk_center = UK estimate at (2000, 1500).")],
 "q5": [(BASE + ">>> def _ok(x0, y0):\n...     n = len(_x); A = _np.ones((n + 1, n + 1)); A[n, n] = 0; A[:n, :n] = _g(_x[:, None] - _x[None, :], _y[:, None] - _y[None, :])\n"
         "...     b = _np.ones(n + 1); b[:n] = _g(_x - x0, _y - y0); s = _np.linalg.solve(A, b)\n...     return float(s[:n] @ _v)\n"
         ">>> bool(abs(phi_ok_corner - _ok(4400., 3300.)) < 1e-6 and abs(phi_uk_corner - _uk(4400., 3300.)[0]) < 1e-6)\nTrue",
         "At (4400, 3300), outside the wells: phi_ok_corner with ok_point(..., gamma_res, nmax=48), phi_uk_corner with uk_point."),
        (BASE + ">>> bool(uk_map.shape == (30, 40) and all(abs(uk_map[r, c] - _uk(50 + 100 * c, 50 + 100 * r)[0]) < 1e-6 for r, c in [(0, 0), (15, 20), (29, 39)]))\nTrue",
         "uk_map: UK estimate on the 100 m grid, node (r, c) at x = 50 + 100 c, y = 50 + 100 r (30 rows, 40 columns).")],
}

def notebook():
    cells = [
        header(11, 'Trends: simple and universal kriging of porosity', NB, '''
        Ordinary kriging assumes the mean is constant over the neighbourhood. Many variables have a **trend**:
        porosity decreases with burial depth, temperature increases towards a heat source, the thickness of a
        weathering profile follows the topography. This week, a petroleum case: porosity measured in 48 wells of a
        4 km × 3 km sandstone reservoir (synthetic), tighter towards the north-east where the reservoir is deeper.

        **What you will practise:** fitting a linear trend · residuals and their variogram · simple kriging (known
        mean) · universal kriging (kriging with a drift) · the risk of extrapolating a trend.
        '''),
        setup_cell('w11', DATA, TESTS),
        otter_cell(),
        toolbox_cell('variogram', 'models', 'kriging'),
        code('''
        import pandas as pd
        import matplotlib.pyplot as plt

        wells = pd.read_csv("porosity_wells.csv")
        x, y = wells["x"].to_numpy(float), wells["y"].to_numpy(float)
        phi_pct = 100 * wells["phi"].to_numpy()          # porosity in %
        sc = plt.scatter(x, y, c=phi_pct, cmap="viridis"); plt.colorbar(sc, label="porosity (%)")
        plt.gca().set_aspect("equal"); plt.xlabel("East (m)"); plt.ylabel("North (m)"); plt.show()
        '''),
        md('''
        ## 1. A variogram that never stops rising

        With a trend, pairs far apart differ systematically, so the variogram of the raw data keeps increasing,
        often faster than linearly. That is the signal to model the trend first:

        $$Z(\\mathbf{x}) = m(\\mathbf{x}) + R(\\mathbf{x}), \\qquad m(\\mathbf{x}) = a_0 + a_1 x + a_2 y$$

        The residuals $R$ have a mean of zero and a variogram with a sill. Here the residual variogram is modelled by
        `gamma_res`: nugget 0.3 + spherical 1.5, range 1000 m, isotropic (total sill 1.8 %²).
        '''),
        code('''
        def gamma_res(dx, dy):
            return spherical(np.hypot(dx, dy), 0.3, 1.5, 1000)
        '''),
        md('''
        ## 2. Three kinds of kriging

        | | mean | system | use |
        |---|---|---|---|
        | **simple** (SK) | known (here: 0 for the residuals) | $C\\lambda = c_0$, no constraint | residuals, normal scores, simulation |
        | **ordinary** (OK) | unknown, constant locally | $\\sum\\lambda = 1$ | most grade estimation |
        | **universal** (UK) | unknown, $a_0 + a_1x + a_2y$ | one constraint per drift term | trends |

        SK uses covariances $C(h) = C(0) - \\gamma(h)$; its variance is $C(0) - \\sum\\lambda_i c_{i0}$.
        For UK with a linear drift the system is

        $$
        \\begin{bmatrix} \\Gamma & F \\\\ F^T & 0 \\end{bmatrix}
        \\begin{bmatrix} \\lambda \\\\ \\mu \\end{bmatrix} =
        \\begin{bmatrix} \\gamma_0 \\\\ f_0 \\end{bmatrix}, \\qquad F = [1, x_i, y_i], \\; f_0 = [1, x_0, y_0]
        $$

        (coordinates in km to keep the numbers balanced), and $\\sigma^2_{UK} = [\\lambda, \\mu] \\cdot [\\gamma_0, f_0]$.

        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. The trend

        Build `F = np.c_[np.ones(n), x / 1000, y / 1000]` and fit the trend by least squares: store the 3 coefficients
        in `trend_coef`, the residuals in `resid`, and the trend value at the centre (2000, 1500) in `trend_at_center`.
        ''', '''
        F = ...
        trend_coef = ...
        resid = ...
        trend_at_center = ...
        trend_coef
        '''),
        *question('q2', '''
        ### Q2. Raw and residual variograms

        Store the variances `raw_var` and `resid_var`, and the semivariances `g_raw` and `g_res` (lag 400 m,
        8 lags). Plot both with the model `gamma_res`.
        ''', '''
        raw_var = ...
        resid_var = ...
        g_raw = ...
        g_res = ...
        '''),
        *question('q3', '''
        ### Q3. Simple kriging of the residuals

        Write `sk_residual(x0, y0, x, y, r, gamma, sill)` that krigs the residuals with a known mean of 0, using all
        wells, and returns `(estimate, variance)`. Store `phi_sk_center` = trend + kriged residual at (2000, 1500).
        ''', '''
        def sk_residual(x0, y0, x, y, r, gamma, sill):
            ...

        phi_sk_center = ...
        phi_sk_center
        '''),
        *question('q4', '''
        ### Q4. Universal kriging

        Write `uk_point(x0, y0, x, y, v, gamma)` with a linear drift (coordinates divided by 1000 in the drift),
        using all wells, returning `(estimate, variance)`. Store the estimate at (2000, 1500) in `phi_uk_center`.
        Compare with `phi_sk_center`.
        ''', '''
        def uk_point(x0, y0, x, y, v, gamma):
            ...

        phi_uk_center = ...
        phi_uk_center
        '''),
        *question('q5', '''
        ### Q5. Maps and extrapolation

        Make `uk_map` on a 100 m grid (30 rows × 40 columns, node `(r, c)` at `x = 50 + 100*c`, `y = 50 + 100*r`) and
        draw it. Then estimate the point (4400, 3300), **outside** the drilled area, with OK (`ok_point` with
        `gamma_res` and `nmax=48`: `phi_ok_corner`) and with UK (`phi_uk_corner`). Which one would you trust for a
        new well location there, and why is extrapolating the trend risky?
        ''', '''
        uk_map = ...
        phi_ok_corner = ...
        phi_uk_corner = ...
        phi_ok_corner, phi_uk_corner
        '''),
        *closing('''
        ### Going further (not checked)

        * Pore volume: with a net thickness of 20 m, sum `uk_map / 100 * 100 * 100 * 20` over the map (m³).
        * Fit a quadratic trend (add x², xy, y²). Do the residuals look better? Is the model still sensible at the edges?
        '''),
    ]
    save_notebook(NB, 'w11', cells)

def build():
    write_tests('w11', TESTS)
    notebook()
    return f'{NB} written'
