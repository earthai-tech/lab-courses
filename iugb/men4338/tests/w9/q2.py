OK_FORMAT = True

test = {'name': 'q2',
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
                                '>>> bool(ok_map.shape == (50, 60) and ok_varmap.shape == (50, '
                                '60))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'ok_map and ok_varmap have the shape of gx.'},
                       {'code': '>>> import numpy as _np, pandas as _pd\n'
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
                                '>>> bool(all(abs(ok_map[r, c] - _ok(15 + 20 * c, 15 + 20 * r, _x, '
                                '_y, _v)[0]) < 1e-6 and abs(ok_varmap[r, c] - _ok(15 + 20 * c, 15 '
                                '+ 20 * r, _x, _y, _v)[1]) < 1e-6 for r, c in [(0, 0), (10, 17), '
                                '(25, 40), (33, 5), (49, 59)]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Each node: ok_point(gx[r, c], gy[r, c], x, y, au, '
                                           'gamma_bassam, nmax=16).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
