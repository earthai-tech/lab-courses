OK_FORMAT = True

test = {'name': 'q2',
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
                                '>>> _i, _j = _np.triu_indices(len(_x), 1); _d = '
                                '_np.full((len(_x), len(_x)), _np.inf)\n'
                                '>>> _d[_i, _j] = _d[_j, _i] = _np.hypot(_x[_j] - _x[_i], _y[_j] - '
                                '_y[_i])\n'
                                ">>> _m = ks.set_index('hole_id').loc[_co['hole_id']]\n"
                                ">>> bool(_np.array_equal(_np.asarray(_m['is_infill'], bool), "
                                '_d.min(axis=1) < 40))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "ks['is_infill'] is True for the holes whose nearest "
                                           'neighbour is closer than 40 m.'},
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
                                '>>> _k = _np.floor(_x / 50).astype(int) * 100000 + _np.floor(_y / '
                                '50).astype(int)\n'
                                '>>> _, _inv, _cnt = _np.unique(_k, return_inverse=True, '
                                'return_counts=True); _w = 1 / _cnt[_inv]; _w = _w / _w.sum()\n'
                                '>>> bool(abs(ks_naive_mean - _v.mean()) < 1e-9 and '
                                'abs(ks_declus_mean - (_w * _v).sum()) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'ks_naive_mean: plain mean; ks_declus_mean: declustered '
                                           'mean with 50 m cells.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
