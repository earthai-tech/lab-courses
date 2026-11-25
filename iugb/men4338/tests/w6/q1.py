OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> bool(nearest_estimate(1.0, 1.0, _np.array([0., 5, 2]), '
                                '_np.array([0., 5, 2]), _np.array([10., 20, 30])) == 10.0)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Return the value of the closest sample (np.argmin of '
                                           'the distances).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _x, _y, _v = (_s[c].to_numpy() for c in ('x', 'y', "
                                "'au_gpt'))\n"
                                '>>> _d = _np.hypot(_x - 500, _y - 500)\n'
                                '>>> bool(abs(nn_500 - _v[_np.argmin(_d)]) < 1e-12)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'nn_500 = nearest_estimate(500, 500, x, y, au).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
