OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> def _gb(dx, dy):\n'
                                '...     t = _np.radians(45); u = dx * _np.sin(t) + dy * '
                                '_np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n'
                                '...     h = _np.sqrt(u ** 2 + (2 * w) ** 2); r = _np.minimum(h / '
                                '300, 1)\n'
                                '...     return _np.where(h > 0, 0.06 + 0.20 * (1.5 * r - 0.5 * r '
                                '** 3), 0.0)\n'
                                '>>> def _sys(xs, ys, x0, y0, g):\n'
                                '...     n = len(xs); A = _np.ones((n + 1, n + 1)); A[n, n] = 0\n'
                                '...     A[:n, :n] = g(xs[:, None] - xs[None, :], ys[:, None] - '
                                'ys[None, :])\n'
                                '...     b = _np.ones(n + 1); b[:n] = g(xs - x0, ys - y0)\n'
                                '...     return A, b\n'
                                '>>> import pandas as _pd\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _x, _y, _v = "
                                "(_s[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n"
                                '>>> def _okp(x0, y0):\n'
                                '...     k = _np.argsort(_np.hypot(_x - x0, _y - y0))[:16]\n'
                                '...     A, b = _sys(_x[k], _y[k], x0, y0, _gb); s = '
                                '_np.linalg.solve(A, b)\n'
                                '...     return float(s[:16] @ _v[k]), float(s[:16] @ b[:16] + '
                                's[16])\n'
                                '>>> _t = [(312., 457.), (641., 213.), (906., 782.)]\n'
                                '>>> bool(all(abs(a - _okp(*t)[0]) < 1e-6 and abs(b - _okp(*t)[1]) '
                                '< 1e-6 for (a, b), t in zip(ok_targets, _t)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'ok_targets: list of (estimate, variance) from '
                                           'ok_point(x0, y0, x, y, au, gamma_bassam, nmax=16) at '
                                           'the 3 targets.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> def _gb(dx, dy):\n'
                                '...     t = _np.radians(45); u = dx * _np.sin(t) + dy * '
                                '_np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n'
                                '...     h = _np.sqrt(u ** 2 + (2 * w) ** 2); r = _np.minimum(h / '
                                '300, 1)\n'
                                '...     return _np.where(h > 0, 0.06 + 0.20 * (1.5 * r - 0.5 * r '
                                '** 3), 0.0)\n'
                                '>>> def _sys(xs, ys, x0, y0, g):\n'
                                '...     n = len(xs); A = _np.ones((n + 1, n + 1)); A[n, n] = 0\n'
                                '...     A[:n, :n] = g(xs[:, None] - xs[None, :], ys[:, None] - '
                                'ys[None, :])\n'
                                '...     b = _np.ones(n + 1); b[:n] = g(xs - x0, ys - y0)\n'
                                '...     return A, b\n'
                                '>>> import pandas as _pd\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _x, _y, _v = "
                                "(_s[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n"
                                '>>> def _okp(x0, y0):\n'
                                '...     k = _np.argsort(_np.hypot(_x - x0, _y - y0))[:16]\n'
                                '...     A, b = _sys(_x[k], _y[k], x0, y0, _gb); s = '
                                '_np.linalg.solve(A, b)\n'
                                '...     return float(s[:16] @ _v[k]), float(s[:16] @ b[:16] + '
                                's[16])\n'
                                '>>> bool(abs(var_far - _okp(1190., 990.)[1]) < 1e-6 and var_far > '
                                'max(v for _, v in ok_targets))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'var_far: kriging variance at the corner (1190, 990), '
                                           'far from the infill: it should be larger.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
