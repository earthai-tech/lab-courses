OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> round(hydrostatic_mpa(1000), 4)\n10.1043',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'With the default density 1.03 g/cm³: P = depth × '
                                           'density × 9.81 ÷ 1000.'},
                       {'code': '>>> round(hydrostatic_mpa(2000, 1.20), 4)\n23.544',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The second parameter, density, must replace the '
                                           'default when it is given.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
