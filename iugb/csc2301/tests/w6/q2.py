OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> [water_cut(90.0, 10.0), water_cut(50.0, 50.0), water_cut(0.0, '
                                '20.0)]\n'
                                '[0.1, 0.5, 1.0]',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Water cut = water / (oil + water).'},
                       {'code': '>>> try:\n'
                                '...     water_cut(0.0, 0.0)\n'
                                '... except ValueError:\n'
                                "...     print('ValueError')\n"
                                'ValueError',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'When oil + water is 0 the water cut is undefined: '
                                           'raise ValueError (not ZeroDivisionError).'},
                       {'code': '>>> try:\n'
                                '...     water_cut(-5.0, 10.0)\n'
                                '... except ValueError:\n'
                                "...     print('ValueError')\n"
                                'ValueError',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'A negative volume is impossible: raise ValueError.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
