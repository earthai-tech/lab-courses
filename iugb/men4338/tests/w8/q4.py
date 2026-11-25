OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> bool(_np.allclose(weights_nugget, 0.25))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'With a pure nugget model every sample is equally '
                                           '(un)informative: each weight is 1/n.'},
                       {'code': '>>> bool(abs(ok_var_nugget - 1.25) < 1e-9)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Pure nugget of sill 1: σ²_OK = 1 + 1/n.'},
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
                                '>>> _xs = _np.array([140., 160, 165]); _ys = _np.array([140., '
                                '160, 165])\n'
                                '>>> _A, _b = _sys(_xs, _ys, 140., 140., _gb)\n'
                                '>>> bool(_np.allclose(weights_screen, _np.linalg.solve(_A, '
                                '_b)[:3]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'weights_screen: OK weights with gamma_bassam for '
                                           'samples at (140,140), (160,160), (165,165) and target '
                                           '(140,140).'},
                       {'code': '>>> bool(abs(weights_screen[0] - 1) < 1e-9)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'A sample exactly at the target gets weight 1: kriging '
                                           'is an exact interpolator.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
