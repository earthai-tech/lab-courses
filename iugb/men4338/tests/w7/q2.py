OK_FORMAT = True

test = {'name': 'q2',
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
                                '>>> bool(abs(naive_cu - _v.mean()) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'naive_cu = plain mean of the composites.'},
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
                                '>>> def _w(x, y, c):\n'
                                '...     k = _np.floor(x / c).astype(int) * 100000 + _np.floor(y / '
                                'c).astype(int)\n'
                                '...     _, inv, cnt = _np.unique(k, return_inverse=True, '
                                'return_counts=True); w = 1.0 / cnt[inv]\n'
                                '...     return w / w.sum()\n'
                                '>>> bool(abs(declus_cu - (_w(_x, _y, 60) * _v).sum()) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'declus_cu: declustered mean with 60 m cells (the '
                                           'drilling grid).'},
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
                                '>>> def _w(x, y, c):\n'
                                '...     k = _np.floor(x / c).astype(int) * 100000 + _np.floor(y / '
                                'c).astype(int)\n'
                                '...     _, inv, cnt = _np.unique(k, return_inverse=True, '
                                'return_counts=True); w = 1.0 / cnt[inv]\n'
                                '...     return w / w.sum()\n'
                                '>>> bool(abs(prop_above_05 - (_w(_x, _y, 60) * (_v > 0.5)).sum()) '
                                '< 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'prop_above_05: declustered proportion of composites '
                                           'above 0.5 % Cu = sum of the weights of those '
                                           'samples.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
