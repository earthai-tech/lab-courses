OK_FORMAT = True

test = {'name': 'q1',
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
                                ">>> _m = cs.set_index('hole_id')\n"
                                '>>> bool(len(cs) == len(_co) and '
                                "_np.allclose(_m.loc[_co['hole_id'], 'cu_pct'].to_numpy(), _v))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'cs: one row per hole with hole_id, x, y and its '
                                           'length-weighted composite cu_pct (missing assays '
                                           'ignored).'},
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
                                ">>> bool(_np.allclose(cs.set_index('hole_id').loc[_co['hole_id'], "
                                "['x', 'y']].to_numpy(), _co[['x', 'y']].to_numpy()))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Merge the composites with copper_south_collars.csv to '
                                           'get x and y.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
