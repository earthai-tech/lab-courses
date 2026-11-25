OK_FORMAT = True

test = {'name': 'q4',
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
                                '>>> bool(all(abs(uk_point(a, b, x, y, phi_pct, gamma_res)[0] - '
                                '_uk(a, b)[0]) < 1e-6 and abs(uk_point(a, b, x, y, phi_pct, '
                                'gamma_res)[1] - _uk(a, b)[1]) < 1e-6 for a, b in [(2000., 1500.), '
                                '(500., 2600.)]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'UK system: [[Γ, F], [Fᵀ, 0]] [λ, μ] = [γ0, 1, x0/1000, '
                                           'y0/1000]; estimate = λ · phi_pct; variance = [λ, μ] · '
                                           'right-hand side.'},
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
                                '>>> bool(abs(phi_uk_center - _uk(2000., 1500.)[0]) < 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'phi_uk_center = UK estimate at (2000, 1500).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
