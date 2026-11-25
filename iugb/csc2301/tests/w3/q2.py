OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> round(gold_ounces(1000, 31.1035), 6)\n1000.0',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Grams of gold = tonnes × grade (g/t); one troy ounce '
                                           'is 31.1035 g.'},
                       {'code': '>>> round(gold_ounces(1350, 2.0), 3)\n86.807',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Divide the grams by 31.1035, do not round inside the '
                                           'function.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
