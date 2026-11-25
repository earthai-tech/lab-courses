OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                ">>> bool({'c0', 'c', 'azimuth', 'a_major', 'a_minor'} <= "
                                'set(ks_model) and float(gamma_ks(0.0, 0.0)) == 0.0)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'ks_model is a dictionary with c0, c, azimuth, a_major, '
                                           'a_minor, and gamma_ks(dx, dy) is your model (γ(0) = '
                                           '0).'},
                       {'code': '>>> import numpy as _np\n'
                                ">>> bool(abs(float(gamma_ks(1e5, 0.0)) - (ks_model['c0'] + "
                                "ks_model['c'])) < 1e-6 and ks_model['a_major'] >= "
                                "ks_model['a_minor'] > 0)\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Far away gamma_ks must equal the total sill c0 + c; '
                                           'a_major >= a_minor.'},
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
                                '>>> _e = []\n'
                                '>>> for _i in range(len(_v)):\n'
                                '...     _k = _np.argsort(_np.hypot(_x - _x[_i], _y - '
                                '_y[_i]))[1:17]; _xs, _ys = _x[_k], _y[_k]\n'
                                '...     _A = _np.ones((17, 17)); _A[16, 16] = 0; _A[:16, :16] = '
                                'gamma_ks(_xs[:, None] - _xs[None, :], _ys[:, None] - _ys[None, '
                                ':])\n'
                                '...     _b = _np.ones(17); _b[:16] = gamma_ks(_xs - _x[_i], _ys - '
                                '_y[_i]); _s = _np.linalg.solve(_A, _b)\n'
                                '...     _e.append(((_s[:16] @ _v[_k]) - _v[_i]) ** 2 / (_s[:16] @ '
                                '_b[:16] + _s[16]))\n'
                                '>>> bool(0.7 < _np.mean(_e) < 1.4)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Leave-one-out kriging with your model gives a mean '
                                           'standardised squared error outside 0.7–1.4: revise the '
                                           'nugget, sill or ranges.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
