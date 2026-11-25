OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np, pandas as _pd\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _x, _y, _v = "
                                "(_s[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n"
                                '>>> _T = '
                                "_pd.read_csv('bassam_truth_grid.csv')['au_gpt'].to_numpy().reshape(100, "
                                '120)\n'
                                '>>> _B = _T.reshape(20, 5, 24, 5).mean(axis=(1, 3))\n'
                                '>>> def _gb(dx, dy):\n'
                                '...     t = _np.radians(45); u = dx * _np.sin(t) + dy * '
                                '_np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n'
                                '...     h = _np.sqrt(u ** 2 + (2 * w) ** 2); r = _np.minimum(h / '
                                '300, 1)\n'
                                '...     return _np.where(h > 0, 0.06 + 0.20 * (1.5 * r - 0.5 * r '
                                '** 3), 0.0)\n'
                                '>>> def _disc(xc, yc, size, n):\n'
                                '...     o = (_np.arange(n) + 0.5) / n * size - size / 2; px, py = '
                                '_np.meshgrid(xc + o, yc + o)\n'
                                '...     return px.ravel(), py.ravel()\n'
                                '>>> def _gbar(size, n=5):\n'
                                '...     px, py = _disc(0, 0, size, n)\n'
                                '...     return float(_gb(px[:, None] - px[None, :], py[:, None] - '
                                'py[None, :]).mean())\n'
                                '>>> def _okb(xc, yc, size=50, nd=4, nmax=16):\n'
                                '...     k = _np.argsort(_np.hypot(_x - xc, _y - yc))[:nmax]; xs, '
                                'ys = _x[k], _y[k]; m = len(k)\n'
                                '...     px, py = _disc(xc, yc, size, nd)\n'
                                '...     A = _np.ones((m + 1, m + 1)); A[m, m] = 0; A[:m, :m] = '
                                '_gb(xs[:, None] - xs[None, :], ys[:, None] - ys[None, :])\n'
                                '...     b = _np.ones(m + 1); b[:m] = _gb(xs[:, None] - px[None, '
                                ':], ys[:, None] - py[None, :]).mean(axis=1)\n'
                                '...     s = _np.linalg.solve(A, b)\n'
                                '...     return float(s[:m] @ _v[k]), float(s[:m] @ b[:m] + s[m] - '
                                '_gbar(size, nd))\n'
                                '>>> bool(all(abs(ok_block(a, b, 50, x, y, au, gamma_bassam)[0] - '
                                '_okb(a, b)[0]) < 1e-6 and abs(ok_block(a, b, 50, x, y, au, '
                                'gamma_bassam)[1] - _okb(a, b)[1]) < 1e-6 for a, b in [(325., '
                                '475.), (625., 225.), (1175., 975.)]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Right-hand side = mean of γ between sample i and the 4 '
                                           '× 4 block points; block variance = Σλ b̄ + μ - '
                                           'γ̄(block).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
