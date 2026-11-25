OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                '>>> def _vg(x, y, v, lag, nlags):\n'
                                '...     x, y, v = (_np.asarray(a, float) for a in (x, y, v))\n'
                                '...     i, j = _np.triu_indices(len(v), 1)\n'
                                '...     d = _np.hypot(x[j] - x[i], y[j] - y[i]); sq = 0.5 * (v[j] '
                                '- v[i]) ** 2\n'
                                '...     out = []\n'
                                '...     for k in range(1, nlags + 1):\n'
                                '...         m = _np.abs(d - k * lag) < lag / 2\n'
                                '...         out.append((d[m].mean() if m.any() else _np.nan, '
                                'sq[m].mean() if m.any() else _np.nan, int(m.sum())))\n'
                                '...     return [_np.array(c) for c in zip(*out)]\n'
                                ">>> _r = _vg(_g['x'], _g['y'], _g['au_gpt'], 50, 12)\n"
                                '>>> bool(_np.allclose(g_grid, _r[1]) and _np.allclose(h_grid, '
                                '_r[0]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'h_grid, g_grid, n_grid = exp_variogram(...) on the '
                                           'grid holes only, lag 50 m, 12 lags.'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                '>>> def _vg(x, y, v, lag, nlags):\n'
                                '...     x, y, v = (_np.asarray(a, float) for a in (x, y, v))\n'
                                '...     i, j = _np.triu_indices(len(v), 1)\n'
                                '...     d = _np.hypot(x[j] - x[i], y[j] - y[i]); sq = 0.5 * (v[j] '
                                '- v[i]) ** 2\n'
                                '...     out = []\n'
                                '...     for k in range(1, nlags + 1):\n'
                                '...         m = _np.abs(d - k * lag) < lag / 2\n'
                                '...         out.append((d[m].mean() if m.any() else _np.nan, '
                                'sq[m].mean() if m.any() else _np.nan, int(m.sum())))\n'
                                '...     return [_np.array(c) for c in zip(*out)]\n'
                                ">>> _r = _vg(_s['x'], _s['y'], _s['au_gpt'], 50, 12)\n"
                                '>>> bool(_np.allclose(g_all, _r[1]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'h_all, g_all, n_all = exp_variogram(...) on all '
                                           'samples (grid + infill), lag 50 m, 12 lags.'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                ">>> bool(abs(var_grid - _g['au_gpt'].var()) < 1e-9 and "
                                "abs(var_all - _s['au_gpt'].var()) < 1e-9)\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'var_grid and var_all: sample variances (pandas .var()) '
                                           'of the grid holes and of all samples.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
