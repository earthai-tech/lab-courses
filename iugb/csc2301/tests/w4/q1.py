OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': ">>> [clean_hole_id(s) for s in ('DH-03', 'dh-03', ' DH03', 'dh 03 "
                                "')]\n"
                                "['DH-03', 'DH-03', 'DH-03', 'DH-03']",
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Keep only the digits, then rebuild the name as 'DH-' + "
                                           'two digits.'},
                       {'code': ">>> clean_hole_id('DH-7')\n'DH-07'",
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Pad the number to two digits: str.zfill(2) or '
                                           "f'{int(n):02d}'."}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
