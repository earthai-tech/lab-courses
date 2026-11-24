OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> [round(vshale(g), 3) for g in (30, 75, 120)]\n[0.0, 0.5, 1.0]',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Use (gr - 30) / (120 - 30): 30 API gives 0, 120 API '
                                           'gives 1.'},
                       {'code': '>>> [vshale(g) for g in (10, 150)]\n[0.0, 1.0]',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Clip the result: below 0 return 0, above 1 return 1.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
