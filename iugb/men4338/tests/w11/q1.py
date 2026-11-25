OK_FORMAT = True

test = {'name': 'q1',
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
                                '>>> bool(_np.allclose(trend_coef, _c))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Least squares on the design matrix [1, x/1000, y/1000] '
                                           '(coordinates in km): np.linalg.lstsq(F, phi_pct, '
                                           'rcond=None)[0].'},
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
                                '>>> bool(_np.allclose(resid, _r))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'resid = phi_pct - F @ trend_coef.'},
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
                                '>>> bool(abs(trend_at_center - (_c[0] + _c[1] * 2 + _c[2] * 1.5)) '
                                '< 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'trend_at_center: the trend at x = 2000 m, y = 1500 '
                                           'm.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
