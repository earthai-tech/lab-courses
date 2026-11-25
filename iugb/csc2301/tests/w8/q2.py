OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                ">>> _a = _np.loadtxt('well_log_kw2.csv', delimiter=',', "
                                'skiprows=1)\n'
                                '>>> _d, _g, _r, _t = _a[:, 0], _a[:, 1], _a[:, 2], _a[:, 3]\n'
                                '>>> _phi = (2.65 - _r) / (2.65 - 1.0)\n'
                                '>>> bool(phi_d.shape == _r.shape and _np.allclose(phi_d, _phi))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Density porosity: (2.65 - rhob) / (2.65 - 1.0), '
                                           'computed on the whole array at once, no loop.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
