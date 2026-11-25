OK_FORMAT = True

test = {'name': 'q3',
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
                                '>>> _xs = _np.array([100., 150, 120, 200]); _ys = '
                                '_np.array([100., 120, 170, 160]); _vs = _np.array([1.2, 0.8, 1.5, '
                                '2.1])\n'
                                '>>> _A, _b = _sys(_xs, _ys, 140., 140., _gb); _s = '
                                '_np.linalg.solve(_A, _b)\n'
                                '>>> bool(abs(ok_est - _s[:4] @ _vs) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'ok_est = sum(weights * values).'},
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
                                '>>> _xs = _np.array([100., 150, 120, 200]); _ys = '
                                '_np.array([100., 120, 170, 160]); _vs = _np.array([1.2, 0.8, 1.5, '
                                '2.1])\n'
                                '>>> _A, _b = _sys(_xs, _ys, 140., 140., _gb); _s = '
                                '_np.linalg.solve(_A, _b)\n'
                                '>>> bool(abs(ok_var - (_s[:4] @ _b[:4] + _s[4])) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Kriging variance: σ²_OK = Σ λ_i γ(x_i - x0) + μ.'},
                       {'code': '>>> bool(0 < ok_var < 0.26 * 2)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The kriging variance is positive and of the order of '
                                           'the sill.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
