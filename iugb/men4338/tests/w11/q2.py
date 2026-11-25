OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np, pandas as _pd\n'
                                ">>> _p = _pd.read_csv('porosity_wells.csv')\n"
                                ">>> _x, _y = _p['x'].to_numpy(float), _p['y'].to_numpy(float); _v "
                                "= 100 * _p['phi'].to_numpy()\n"
                                '>>> _F = _np.c_[_np.ones(len(_x)), _x / 1000, _y / 1000]; _c = '
                                '_np.linalg.lstsq(_F, _v, rcond=None)[0]; _r = _v - _F @ _c\n'
                                '>>> def _g(dx, dy):\n'
                                '...     h = _np.hypot(dx, dy); q = _np.minimum(h / 1000, 1)\n'
                                '...     return _np.where(h > 0, 0.3 + 1.5 * (1.5 * q - 0.5 * q ** '
                                '3), 0.0)\n'
                                '>>> def _sk(x0, y0):\n'
                                '...     C = 1.8 - _g(_x[:, None] - _x[None, :], _y[:, None] - '
                                '_y[None, :]); c0 = 1.8 - _g(_x - x0, _y - y0)\n'
                                '...     lam = _np.linalg.solve(C, c0)\n'
                                '...     return float(lam @ _r), float(1.8 - lam @ c0)\n'
                                '>>> def _uk(x0, y0):\n'
                                '...     n = len(_x); A = _np.zeros((n + 3, n + 3)); A[:n, :n] = '
                                '_g(_x[:, None] - _x[None, :], _y[:, None] - _y[None, :])\n'
                                '...     A[:n, n:] = _F; A[n:, :n] = _F.T\n'
                                '...     b = _np.concatenate([_g(_x - x0, _y - y0), [1, x0 / 1000, '
                                'y0 / 1000]]); s = _np.linalg.solve(A, b)\n'
                                '...     return float(s[:n] @ _v), float(s @ b)\n'
                                '>>> bool(abs(raw_var - _v.var(ddof=1)) < 1e-9 and abs(resid_var - '
                                '_r.var(ddof=1)) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'raw_var and resid_var: sample variances (ddof=1) of '
                                           'phi_pct and of resid.'},
                       {'code': '>>> import numpy as _np, pandas as _pd\n'
                                ">>> _p = _pd.read_csv('porosity_wells.csv')\n"
                                ">>> _x, _y = _p['x'].to_numpy(float), _p['y'].to_numpy(float); _v "
                                "= 100 * _p['phi'].to_numpy()\n"
                                '>>> _F = _np.c_[_np.ones(len(_x)), _x / 1000, _y / 1000]; _c = '
                                '_np.linalg.lstsq(_F, _v, rcond=None)[0]; _r = _v - _F @ _c\n'
                                '>>> def _g(dx, dy):\n'
                                '...     h = _np.hypot(dx, dy); q = _np.minimum(h / 1000, 1)\n'
                                '...     return _np.where(h > 0, 0.3 + 1.5 * (1.5 * q - 0.5 * q ** '
                                '3), 0.0)\n'
                                '>>> def _sk(x0, y0):\n'
                                '...     C = 1.8 - _g(_x[:, None] - _x[None, :], _y[:, None] - '
                                '_y[None, :]); c0 = 1.8 - _g(_x - x0, _y - y0)\n'
                                '...     lam = _np.linalg.solve(C, c0)\n'
                                '...     return float(lam @ _r), float(1.8 - lam @ c0)\n'
                                '>>> def _uk(x0, y0):\n'
                                '...     n = len(_x); A = _np.zeros((n + 3, n + 3)); A[:n, :n] = '
                                '_g(_x[:, None] - _x[None, :], _y[:, None] - _y[None, :])\n'
                                '...     A[:n, n:] = _F; A[n:, :n] = _F.T\n'
                                '...     b = _np.concatenate([_g(_x - x0, _y - y0), [1, x0 / 1000, '
                                'y0 / 1000]]); s = _np.linalg.solve(A, b)\n'
                                '...     return float(s[:n] @ _v), float(s @ b)\n'
                                '>>> bool(_np.allclose(g_raw, exp_variogram(_x, _y, _v, 400, '
                                '8)[1]) and _np.allclose(g_res, exp_variogram(_x, _y, _r, 400, '
                                '8)[1]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'g_raw and g_res: semivariances with lag 400 m and 8 '
                                           'lags, of phi_pct and of resid.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
