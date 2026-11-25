OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                ">>> _a = _np.loadtxt('well_log_kw2.csv', delimiter=',', "
                                'skiprows=1)\n'
                                '>>> _d, _g, _r, _t = _a[:, 0], _a[:, 1], _a[:, 2], _a[:, 3]\n'
                                '>>> _phi = (2.65 - _r) / (2.65 - 1.0)\n'
                                '>>> bool(sand.dtype == bool and _np.array_equal(sand, _g < 60))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'sand is a Boolean array: gr < 60.'},
                       {'code': '>>> import numpy as _np\n'
                                ">>> _a = _np.loadtxt('well_log_kw2.csv', delimiter=',', "
                                'skiprows=1)\n'
                                '>>> _d, _g, _r, _t = _a[:, 0], _a[:, 1], _a[:, 2], _a[:, 3]\n'
                                '>>> _phi = (2.65 - _r) / (2.65 - 1.0)\n'
                                '>>> bool(n_sand == int((_g < 60).sum()) and abs(sand_phi_mean - '
                                '_phi[_g < 60].mean()) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Count with .sum() on the mask; average the porosity of '
                                           'the sand samples only: phi_d[sand].mean().'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
