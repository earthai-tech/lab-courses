OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                '>>> _iv = '
                                "_pd.read_csv('kossou_intervals.csv').dropna(subset=['au_gpt'])\n"
                                ">>> _iv['_l'] = _iv['to_m'] - _iv['from_m']; _iv['_gl'] = "
                                "_iv['au_gpt'] * _iv['_l']\n"
                                ">>> _t = _iv.groupby('hole_id')[['_gl', '_l']].sum(); _c = "
                                "(_t['_gl'] / _t['_l']).rename('_au')\n"
                                ">>> _co = _pd.read_csv('kossou_collars.csv').merge(_c, "
                                "left_on='hole_id', right_index=True)\n"
                                ">>> _x, _y, _v = (_co[c].to_numpy() for c in ('x', 'y', '_au'))\n"
                                ">>> _m = ks.set_index('hole_id')\n"
                                '>>> bool(len(ks) == len(_co) and '
                                "_np.allclose(_m.loc[_co['hole_id'], 'au_gpt'].to_numpy(), _v) and "
                                "_np.allclose(_m.loc[_co['hole_id'], 'x'].to_numpy(), _x))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'ks: one row per hole with hole_id, x, y and the 8 m '
                                           'bench composite au_gpt (length-weighted, missing '
                                           'assays ignored).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                '>>> _iv = '
                                "_pd.read_csv('kossou_intervals.csv').dropna(subset=['au_gpt'])\n"
                                ">>> _iv['_l'] = _iv['to_m'] - _iv['from_m']; _iv['_gl'] = "
                                "_iv['au_gpt'] * _iv['_l']\n"
                                ">>> _t = _iv.groupby('hole_id')[['_gl', '_l']].sum(); _c = "
                                "(_t['_gl'] / _t['_l']).rename('_au')\n"
                                ">>> _co = _pd.read_csv('kossou_collars.csv').merge(_c, "
                                "left_on='hole_id', right_index=True)\n"
                                ">>> _x, _y, _v = (_co[c].to_numpy() for c in ('x', 'y', '_au'))\n"
                                ">>> bool(n_holes == len(_co) and abs(sampled_m - _iv['_l'].sum()) "
                                '< 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'n_holes = number of holes; sampled_m = total length of '
                                           'assayed intervals.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
