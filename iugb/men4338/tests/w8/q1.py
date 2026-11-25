OK_FORMAT = True

test = {'name': 'q1',
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
                                '>>> _A, _b = _sys(_xs, _ys, 140., 140., _gb)\n'
                                '>>> A, b = ok_matrices(_xs, _ys, 140., 140., gamma_bassam)\n'
                                '>>> bool(A.shape == (5, 5) and b.shape == (5,) and '
                                '_np.allclose(A, _A) and _np.allclose(b, _b))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'A = [[Γ, 1], [1ᵀ, 0]] with Γ[i, j] = γ(x_i - x_j, y_i '
                                           '- y_j); b = [γ(x_i - x0, y_i - y0)..., 1].'},
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
                                '>>> A, b = ok_matrices(_xs, _ys, 140., 140., gamma_bassam)\n'
                                '>>> bool(_np.allclose(_np.diag(A)[:4], 0) and A[4, 4] == 0 and '
                                '_np.allclose(A, A.T))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The diagonal of Γ is γ(0) = 0, the corner is 0 and A '
                                           'is symmetric.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
