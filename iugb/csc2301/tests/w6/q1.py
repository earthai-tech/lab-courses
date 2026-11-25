OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': ">>> [safe_float(s) for s in ('12.5', ' 3 ', '-4.0')]\n"
                                '[12.5, 3.0, -4.0]',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Return float(s) when the conversion works.'},
                       {'code': ">>> [safe_float(s) for s in ('N/A', '', '1,5', 'abc')]\n"
                                '[None, None, None, None]',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Catch the ValueError with try/except and return None. '
                                           'Do not use a bare except.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
