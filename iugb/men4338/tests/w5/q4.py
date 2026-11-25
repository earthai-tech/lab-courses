OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> def _sph(h, c0, c, a):\n'
                                '...     h = _np.asarray(h, float); r = _np.minimum(h / a, 1)\n'
                                '...     return _np.where(h > 0, c0 + c * (1.5 * r - 0.5 * r ** '
                                '3), 0.0)\n'
                                '>>> import pandas as _pd\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _g = "
                                "_s[_s['campaign'] == 'grid']\n"
                                ">>> _h, _gm, _n = exp_variogram(_g['x'], _g['y'], _g['au_gpt'], "
                                '50, 12)\n'
                                '>>> _best = min(_np.sum(_n * (_gm - _sph(_h, c0, c, a)) ** 2) for '
                                'c0 in _np.arange(0, 0.151, 0.01) for c in _np.arange(0.05, 0.301, '
                                '0.01) for a in range(50, 501, 10))\n'
                                '>>> bool(wsse(best_params, _h, _gm, _n) <= _best * (1 + 1e-9))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Search c0 in 0..0.15 (step 0.01), c in 0.05..0.30 '
                                           '(step 0.01), a in 50..500 m (step 10) and keep the '
                                           'triple with the smallest wsse.'},
                       {'code': '>>> bool(len(best_params) == 3 and all(p >= 0 for p in '
                                'best_params))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'best_params = (c0, c, a), all non-negative.'},
                       {'code': '>>> bool(abs(nugget_ratio - best_params[0] / (best_params[0] + '
                                'best_params[1])) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'nugget_ratio = c0 / (c0 + c): the share of the '
                                           'variance that is not spatially structured.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
