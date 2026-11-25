OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np, pandas as _pd\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _x, _y, _v = "
                                "(_s[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n"
                                '>>> _T = '
                                "_pd.read_csv('bassam_truth_grid.csv')['au_gpt'].to_numpy().reshape(100, "
                                '120)[1::2, 1::2]\n'
                                '>>> def _gb(dx, dy):\n'
                                '...     t = _np.radians(45); u = dx * _np.sin(t) + dy * '
                                '_np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n'
                                '...     h = _np.sqrt(u ** 2 + (2 * w) ** 2); r = _np.minimum(h / '
                                '300, 1)\n'
                                '...     return _np.where(h > 0, 0.06 + 0.20 * (1.5 * r - 0.5 * r '
                                '** 3), 0.0)\n'
                                '>>> def _ok(x0, y0, x, y, v, n=16):\n'
                                '...     k = _np.argsort(_np.hypot(x - x0, y - y0))[:n]; xs, ys = '
                                'x[k], y[k]; m = len(k)\n'
                                '...     A = _np.ones((m + 1, m + 1)); A[m, m] = 0; A[:m, :m] = '
                                '_gb(xs[:, None] - xs[None, :], ys[:, None] - ys[None, :])\n'
                                '...     b = _np.ones(m + 1); b[:m] = _gb(xs - x0, ys - y0); s = '
                                '_np.linalg.solve(A, b)\n'
                                '...     return float(s[:m] @ v[k]), float(s[:m] @ b[:m] + s[m])\n'
                                '>>> _e = []; _z = []\n'
                                '>>> for i in range(len(_v)):\n'
                                '...     m = _np.arange(len(_v)) != i\n'
                                '...     est, var = _ok(_x[i], _y[i], _x[m], _y[m], _v[m])\n'
                                '...     _e.append(est - _v[i]); _z.append((est - _v[i]) ** 2 / '
                                'var)\n'
                                '>>> bool(_np.allclose(ok_cv_err, _e) and abs(ok_cv_mse - '
                                '_np.mean(_np.square(_e))) < 1e-9 and abs(ok_cv_msse - '
                                '_np.mean(_z)) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Leave-one-out OK (16 neighbours): ok_cv_err = estimate '
                                           '- true; ok_cv_mse = mean squared error; ok_cv_msse = '
                                           'mean of err² / kriging variance.'},
                       {'code': '>>> bool(0.5 < ok_cv_msse < 2)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The mean standardised squared error should be close to '
                                           '1 if the variogram model is right.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
