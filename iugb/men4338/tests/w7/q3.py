OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                '>>> _iv = '
                                "_pd.read_csv('copper_south_intervals.csv').dropna(subset=['cu_pct'])\n"
                                ">>> _iv['_l'] = _iv['to_m'] - _iv['from_m']; _iv['_gl'] = "
                                "_iv['cu_pct'] * _iv['_l']\n"
                                ">>> _t = _iv.groupby('hole_id')[['_gl', '_l']].sum(); _c = "
                                "(_t['_gl'] / _t['_l']).rename('_cu')\n"
                                ">>> _co = _pd.read_csv('copper_south_collars.csv').merge(_c, "
                                "left_on='hole_id', right_index=True)\n"
                                ">>> _x, _y, _v = (_co[c].to_numpy() for c in ('x', 'y', '_cu'))\n"
                                '>>> _h, _g, _n = exp_variogram(_x, _y, _v, 60, 10)\n'
                                '>>> bool(_np.allclose(g_cu, _g) and _np.allclose(n_cu, _n) and '
                                '_np.allclose(h_cu, _h))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'h_cu, g_cu, n_cu = exp_variogram(x, y, cu, 60, 10) on '
                                           'all the composites.'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                '>>> _iv = '
                                "_pd.read_csv('copper_south_intervals.csv').dropna(subset=['cu_pct'])\n"
                                ">>> _iv['_l'] = _iv['to_m'] - _iv['from_m']; _iv['_gl'] = "
                                "_iv['cu_pct'] * _iv['_l']\n"
                                ">>> _t = _iv.groupby('hole_id')[['_gl', '_l']].sum(); _c = "
                                "(_t['_gl'] / _t['_l']).rename('_cu')\n"
                                ">>> _co = _pd.read_csv('copper_south_collars.csv').merge(_c, "
                                "left_on='hole_id', right_index=True)\n"
                                ">>> _x, _y, _v = (_co[c].to_numpy() for c in ('x', 'y', '_cu'))\n"
                                '>>> bool(abs(var_cu - _v.var(ddof=1)) < 1e-12)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'var_cu: sample variance of the composites (ddof=1).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
