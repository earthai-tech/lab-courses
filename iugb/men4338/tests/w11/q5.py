OK_FORMAT = True

test = {'name': 'q5',
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
                                '>>> def _ok(x0, y0):\n'
                                '...     n = len(_x); A = _np.ones((n + 1, n + 1)); A[n, n] = 0; '
                                'A[:n, :n] = _g(_x[:, None] - _x[None, :], _y[:, None] - _y[None, '
                                ':])\n'
                                '...     b = _np.ones(n + 1); b[:n] = _g(_x - x0, _y - y0); s = '
                                '_np.linalg.solve(A, b)\n'
                                '...     return float(s[:n] @ _v)\n'
                                '>>> bool(abs(phi_ok_corner - _ok(4400., 3300.)) < 1e-6 and '
                                'abs(phi_uk_corner - _uk(4400., 3300.)[0]) < 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'At (4400, 3300), outside the wells: phi_ok_corner with '
                                           'ok_point(..., gamma_res, nmax=48), phi_uk_corner with '
                                           'uk_point.'},
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
                                '>>> bool(uk_map.shape == (30, 40) and all(abs(uk_map[r, c] - '
                                '_uk(50 + 100 * c, 50 + 100 * r)[0]) < 1e-6 for r, c in [(0, 0), '
                                '(15, 20), (29, 39)]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'uk_map: UK estimate on the 100 m grid, node (r, c) at '
                                           'x = 50 + 100 c, y = 50 + 100 r (30 rows, 40 '
                                           'columns).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
