OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                ">>> _x, _y, _v = (_g[c].to_numpy() for c in ('x', 'y', "
                                "'au_gpt'))\n"
                                '>>> _i, _j = _np.triu_indices(len(_x), 1)\n'
                                '>>> _d = _np.hypot(_x[_j] - _x[_i], _y[_j] - _y[_i]); _m = (_d >= '
                                '40) & (_d < 60)\n'
                                '>>> bool(n_pairs_50 == int(_m.sum()) and len(tail) == len(head) '
                                '== int(_m.sum()))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Keep the pairs with 40 <= d < 60 m; tail and head are '
                                           'the two grades of each kept pair.'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                ">>> _x, _y, _v = (_g[c].to_numpy() for c in ('x', 'y', "
                                "'au_gpt'))\n"
                                '>>> _i, _j = _np.triu_indices(len(_x), 1)\n'
                                '>>> _d = _np.hypot(_x[_j] - _x[_i], _y[_j] - _y[_i]); _m = (_d >= '
                                '40) & (_d < 60)\n'
                                '>>> bool(abs(gamma_50 - 0.5 * ((_v[_j][_m] - _v[_i][_m]) ** '
                                '2).mean()) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'gamma_50 = 0.5 * mean((head - tail)**2) over these '
                                           'pairs.'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                ">>> _x, _y, _v = (_g[c].to_numpy() for c in ('x', 'y', "
                                "'au_gpt'))\n"
                                '>>> _i, _j = _np.triu_indices(len(_x), 1)\n'
                                '>>> _d = _np.hypot(_x[_j] - _x[_i], _y[_j] - _y[_i]); _m = (_d >= '
                                '40) & (_d < 60)\n'
                                '>>> bool(abs(rho_50 - _np.corrcoef(_v[_i][_m], _v[_j][_m])[0, 1]) '
                                '< 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'rho_50 = np.corrcoef(tail, head)[0, 1].'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
