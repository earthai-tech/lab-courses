OK_FORMAT = True

test = {'name': 'q4',
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
                                '>>> def _sph(h, c0, c, a):\n'
                                '...     r = _np.minimum(_np.asarray(h, float) / a, 1)\n'
                                '...     return _np.where(_np.asarray(h) > 0, c0 + c * (1.5 * r - '
                                '0.5 * r ** 3), 0.0)\n'
                                '>>> _h, _g, _n = exp_variogram(_x, _y, _v, 60, 10)\n'
                                '>>> _b = min(_np.sum(_n * (_g - _sph(_h, c0, c, a)) ** 2) for c0 '
                                'in _np.arange(0, 0.0601, 0.005) for c in _np.arange(0.05, 0.2501, '
                                '0.01) for a in range(60, 601, 20))\n'
                                '>>> bool(_np.sum(_n * (_g - _sph(_h, *cu_params)) ** 2) <= _b * '
                                '(1 + 1e-9))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Grid search c0 0..0.06 (step 0.005), c 0.05..0.25 '
                                           '(step 0.01), a 60..600 m (step 20) minimising the '
                                           'weighted SSE.'},
                       {'code': '>>> bool(len(cu_params) == 3)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'cu_params = (c0, c, a).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
