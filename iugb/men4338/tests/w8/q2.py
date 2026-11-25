OK_FORMAT = True

test = {'name': 'q2',
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
                                '>>> bool(_np.allclose(weights, _s[:4]) and abs(mu - _s[4]) < '
                                '1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Solve A [λ, μ] = b with np.linalg.solve: weights = '
                                           'first 4 values, mu = the last one.'},
                       {'code': '>>> bool(abs(sum(weights) - 1) < 1e-9)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The ordinary kriging weights add up to 1 '
                                           '(unbiasedness).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
