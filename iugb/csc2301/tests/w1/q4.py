OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': ">>> [classify(g) for g in (0.1, 0.49)]\n['waste', 'waste']",
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Below 0.5 g/t the rock is 'waste'."},
                       {'code': '>>> [classify(g) for g in (0.5, 1.2, 1.99)]\n'
                                "['low grade', 'low grade', 'low grade']",
                        'hidden': False,
                        'locked': False,
                        'failure_message': "From 0.5 up to (not including) 2.0 g/t it is 'low "
                                           "grade'. Check the boundary at 0.5."},
                       {'code': '>>> [classify(g) for g in (2.0, 7.5)]\n'
                                "['high grade', 'high grade']",
                        'hidden': False,
                        'locked': False,
                        'failure_message': "2.0 g/t and above is 'high grade'. Check the boundary "
                                           'at 2.0.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
