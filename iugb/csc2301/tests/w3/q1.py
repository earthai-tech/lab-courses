OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(callable(block_tonnes))\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Define a function called block_tonnes.'},
                       {'code': '>>> round(block_tonnes(10, 10, 5, 2.7), 6)\n1350.0',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Tonnes = length × width × height × density (10 × 10 × '
                                           '5 × 2.7 = 1350).'},
                       {'code': '>>> round(block_tonnes(2, 3, 4, 1.0), 6)\n24.0',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Use all four parameters in the order (length, width, '
                                           'height, density).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
