OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': ">>> [parse_grade(s) for s in ('1.25', '1,25', ' 0,80 g/t ')]\n"
                                '[1.25, 1.25, 0.8]',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Remove spaces and the unit 'g/t', replace the decimal "
                                           'comma by a point, then convert with float().'},
                       {'code': ">>> parse_grade('<0.01')\n0.005",
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Below detection limit '<0.01' counts as half the "
                                           'limit: 0.005.'},
                       {'code': ">>> [parse_grade(s) for s in ('n.d.', '')]\n[None, None]",
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Not determined ('n.d.') or empty: return None, not "
                                           '0.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
