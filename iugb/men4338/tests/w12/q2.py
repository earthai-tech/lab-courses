OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np, pandas as _pd\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _x, _y, _v = "
                                "(_s[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n"
                                ">>> _i = (_v > 1.0).astype(float); _gm = (_s['campaign'] == "
                                "'grid').to_numpy()\n"
                                '>>> def _w(x, y, c):\n'
                                '...     k = _np.floor(x / c).astype(int) * 100000 + _np.floor(y / '
                                'c).astype(int)\n'
                                '...     _, inv, cnt = _np.unique(k, return_inverse=True, '
                                'return_counts=True); w = 1.0 / cnt[inv]\n'
                                '...     return w / w.sum()\n'
                                '>>> def _gi(dx, dy):\n'
                                '...     t = _np.radians(45); u = dx * _np.sin(t) + dy * '
                                '_np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n'
                                '...     h = _np.sqrt(u ** 2 + (w * 280 / 130) ** 2); r = '
                                '_np.minimum(h / 280, 1)\n'
                                '...     return _np.where(h > 0, 0.08 + 0.17 * (1.5 * r - 0.5 * r '
                                '** 3), 0.0)\n'
                                '>>> def _ik(x0, y0):\n'
                                '...     k = _np.argsort(_np.hypot(_x - x0, _y - y0))[:16]; xs, ys '
                                '= _x[k], _y[k]\n'
                                '...     A = _np.ones((17, 17)); A[16, 16] = 0; A[:16, :16] = '
                                '_gi(xs[:, None] - xs[None, :], ys[:, None] - ys[None, :])\n'
                                '...     b = _np.ones(17); b[:16] = _gi(xs - x0, ys - y0)\n'
                                '...     return float(_np.clip(_np.linalg.solve(A, b)[:16] @ '
                                '_i[k], 0, 1))\n'
                                '>>> _T = '
                                "_pd.read_csv('bassam_truth_grid.csv')['au_gpt'].to_numpy().reshape(100, "
                                '120)[1::2, 1::2]\n'
                                '>>> bool(_np.allclose(g_ind, exp_variogram(_x[_gm], _y[_gm], '
                                '_i[_gm], 50, 10)[1]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'g_ind: omnidirectional variogram of ind_1 on the grid '
                                           'holes, lag 50 m, 10 lags.'},
                       {'code': '>>> import numpy as _np, pandas as _pd\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _x, _y, _v = "
                                "(_s[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n"
                                ">>> _i = (_v > 1.0).astype(float); _gm = (_s['campaign'] == "
                                "'grid').to_numpy()\n"
                                '>>> def _w(x, y, c):\n'
                                '...     k = _np.floor(x / c).astype(int) * 100000 + _np.floor(y / '
                                'c).astype(int)\n'
                                '...     _, inv, cnt = _np.unique(k, return_inverse=True, '
                                'return_counts=True); w = 1.0 / cnt[inv]\n'
                                '...     return w / w.sum()\n'
                                '>>> def _gi(dx, dy):\n'
                                '...     t = _np.radians(45); u = dx * _np.sin(t) + dy * '
                                '_np.cos(t); w = dx * _np.cos(t) - dy * _np.sin(t)\n'
                                '...     h = _np.sqrt(u ** 2 + (w * 280 / 130) ** 2); r = '
                                '_np.minimum(h / 280, 1)\n'
                                '...     return _np.where(h > 0, 0.08 + 0.17 * (1.5 * r - 0.5 * r '
                                '** 3), 0.0)\n'
                                '>>> def _ik(x0, y0):\n'
                                '...     k = _np.argsort(_np.hypot(_x - x0, _y - y0))[:16]; xs, ys '
                                '= _x[k], _y[k]\n'
                                '...     A = _np.ones((17, 17)); A[16, 16] = 0; A[:16, :16] = '
                                '_gi(xs[:, None] - xs[None, :], ys[:, None] - ys[None, :])\n'
                                '...     b = _np.ones(17); b[:16] = _gi(xs - x0, ys - y0)\n'
                                '...     return float(_np.clip(_np.linalg.solve(A, b)[:16] @ '
                                '_i[k], 0, 1))\n'
                                '>>> _T = '
                                "_pd.read_csv('bassam_truth_grid.csv')['au_gpt'].to_numpy().reshape(100, "
                                '120)[1::2, 1::2]\n'
                                '>>> _p = _i[_gm].mean()\n'
                                '>>> bool(abs(ind_sill - _p * (1 - _p)) < 1e-12)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The variance of an indicator is p(1 - p), with p its '
                                           'mean on the grid holes.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
