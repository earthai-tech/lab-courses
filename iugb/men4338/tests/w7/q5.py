OK_FORMAT = True

test = {'name': 'q5',
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
                                '>>> def _idw(x0, y0, x, y, v):\n'
                                '...     d = _np.hypot(x - x0, y - y0); k = _np.argsort(d)[:8]; w '
                                '= 1 / d[k] ** 2\n'
                                '...     return (w * v[k]).sum() / w.sum()\n'
                                '>>> _e = _np.array([_idw(_x[i], _y[i], _np.delete(_x, i), '
                                '_np.delete(_y, i), _np.delete(_v, i)) - _v[i] for i in '
                                'range(len(_v))])\n'
                                '>>> bool(abs(cu_cv_me - _e.mean()) < 1e-9 and abs(cu_cv_mse - (_e '
                                '** 2).mean()) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Leave-one-out IDW (power 2, 8 nearest): cu_cv_me = '
                                           'mean error, cu_cv_mse = mean squared error.'},
                       {'code': ">>> bool(isinstance(summary, dict) and {'declustered_mean', "
                                "'nugget', 'sill', 'range_m', 'cv_mse'} <= set(summary))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'summary is a dictionary with the keys '
                                           'declustered_mean, nugget, sill, range_m, cv_mse.'},
                       {'code': ">>> bool(abs(summary['sill'] - (cu_params[0] + cu_params[1])) < "
                                "1e-9 and summary['range_m'] == cu_params[2] and summary['cv_mse'] "
                                '== cu_cv_mse)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'sill = c0 + c (the total sill), range_m = a, cv_mse = '
                                           'cu_cv_mse.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
