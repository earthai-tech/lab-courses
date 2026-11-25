OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> average_positive([2.0, -1.0, 4.0, 0.0])\n3.0',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Average only the values that are > 0: (2 + 4) / 2 = '
                                           '3.'},
                       {'code': '>>> average_positive([5.0])\n5.0',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'One value: the average is that value.'},
                       {'code': '>>> print(average_positive([-1.0, 0.0]))\nNone',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'No positive value: return None instead of dividing by '
                                           'zero.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
