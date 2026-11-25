OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                ">>> _t = _np.loadtxt('temperature_survey_gt1.csv', delimiter=',', "
                                'skiprows=1)\n'
                                '>>> _q = [0.0, 1234.0, 1800.0, 2250.0, 2999.0, 3000.0] + '
                                'list(_t[:, 0])\n'
                                '>>> bool(all(abs(temperature_at(x, list(_t[:, 0]), list(_t[:, '
                                '1])) - _np.interp(x, _t[:, 0], _t[:, 1])) < 1e-9 for x in _q))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Find the interval with depth_index, then interp '
                                           'between its two ends. A depth equal to a table depth '
                                           'gives that temperature.'},
                       {'code': '>>> import numpy as _np\n'
                                ">>> _t = _np.loadtxt('temperature_survey_gt1.csv', delimiter=',', "
                                'skiprows=1)\n'
                                '>>> bool(abs(t_2250 - _np.interp(2250, _t[:, 0], _t[:, 1])) < '
                                '1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 't_2250 = temperature_at(2250, depths, temps).'},
                       {'code': '>>> try:\n'
                                '...     temperature_at(3500.0, [0.0, 1000.0], [27.0, 58.0])\n'
                                '... except ValueError:\n'
                                "...     print('ValueError')\n"
                                'ValueError',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Outside the surveyed depths, do not guess: raise '
                                           'ValueError.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
