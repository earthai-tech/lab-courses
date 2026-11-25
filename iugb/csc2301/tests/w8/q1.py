OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> bool(isinstance(gr, _np.ndarray) and isinstance(rhob, '
                                '_np.ndarray))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'gr and rhob must be NumPy arrays (not lists).'},
                       {'code': '>>> import numpy as _np\n'
                                ">>> _a = _np.loadtxt('well_log_kw2.csv', delimiter=',', "
                                'skiprows=1)\n'
                                '>>> _d, _g, _r, _t = _a[:, 0], _a[:, 1], _a[:, 2], _a[:, 3]\n'
                                '>>> _phi = (2.65 - _r) / (2.65 - 1.0)\n'
                                '>>> bool(abs(mean_gr - _g.mean()) < 1e-9 and abs(max_rhob - '
                                '_r.max()) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Use the array methods .mean() and .max() (or np.mean, '
                                           'np.max).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
