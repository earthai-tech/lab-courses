OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np, pandas as _pd\n'
                                '>>> from scipy.stats import norm as _norm\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _v = "
                                "_s['au_gpt'].to_numpy()\n"
                                '>>> def _ns(v):\n'
                                '...     r = _np.argsort(_np.argsort(v)); return _norm.ppf((r + '
                                '0.5) / len(v))\n'
                                '>>> def _gn(dx, dy):\n'
                                '...     t = _np.radians(45); u = dx * _np.sin(t) + dy * '
                                '_np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n'
                                '...     h = _np.sqrt(u ** 2 + (2 * w) ** 2); r = _np.minimum(h / '
                                '300, 1)\n'
                                '...     return _np.where(h > 0, 0.15 + 0.85 * (1.5 * r - 0.5 * r '
                                '** 3), 0.0)\n'
                                '>>> def _sk(x0, y0, xs, ys, vs):\n'
                                '...     C = 1 - _gn(xs[:, None] - xs[None, :], ys[:, None] - '
                                'ys[None, :]); c0 = 1 - _gn(xs - x0, ys - y0)\n'
                                '...     lam = _np.linalg.solve(C, c0); return float(lam @ vs), '
                                'float(1 - lam @ c0)\n'
                                '>>> _xs = _np.array([0., 60, 0, 100]); _ys = _np.array([0., 0, '
                                '50, 100]); _vs = _np.array([0.5, -0.2, 1.1, 0.3])\n'
                                '>>> _o = sk_normal(30., 20., _xs, _ys, _vs, gamma_ns)\n'
                                '>>> bool(abs(_o[0] - _sk(30., 20., _xs, _ys, _vs)[0]) < 1e-9 and '
                                'abs(_o[1] - _sk(30., 20., _xs, _ys, _vs)[1]) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Simple kriging with mean 0 and sill 1: C = 1 - γ; λ = '
                                           'solve(C, c0); mean = λ · values; variance = 1 - λ · '
                                           'c0.'},
                       {'code': '>>> import numpy as _np, pandas as _pd\n'
                                '>>> from scipy.stats import norm as _norm\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _v = "
                                "_s['au_gpt'].to_numpy()\n"
                                '>>> def _ns(v):\n'
                                '...     r = _np.argsort(_np.argsort(v)); return _norm.ppf((r + '
                                '0.5) / len(v))\n'
                                '>>> def _gn(dx, dy):\n'
                                '...     t = _np.radians(45); u = dx * _np.sin(t) + dy * '
                                '_np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n'
                                '...     h = _np.sqrt(u ** 2 + (2 * w) ** 2); r = _np.minimum(h / '
                                '300, 1)\n'
                                '...     return _np.where(h > 0, 0.15 + 0.85 * (1.5 * r - 0.5 * r '
                                '** 3), 0.0)\n'
                                '>>> def _sk(x0, y0, xs, ys, vs):\n'
                                '...     C = 1 - _gn(xs[:, None] - xs[None, :], ys[:, None] - '
                                'ys[None, :]); c0 = 1 - _gn(xs - x0, ys - y0)\n'
                                '...     lam = _np.linalg.solve(C, c0); return float(lam @ vs), '
                                'float(1 - lam @ c0)\n'
                                '>>> _xs = _np.array([0., 60]); _ys = _np.array([0., 0]); _vs = '
                                '_np.array([0.5, -0.2])\n'
                                '>>> bool(abs(sk_normal(5000., 5000., _xs, _ys, _vs, gamma_ns)[0]) '
                                '< 1e-9 and abs(sk_normal(5000., 5000., _xs, _ys, _vs, '
                                'gamma_ns)[1] - 1) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Far from all data, SK returns the mean (0) and the '
                                           'full variance (1).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
