OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(abs(stoiip_mmbbl(1.0, 10.0, 0.2, 0.25, 1.2) - 7.86225) < '
                                '1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'STOIIP (MMbbl) = A(km²) × 10⁶ × h × φ × (1 − Sw) / Bo '
                                           '× 6.2898 / 10⁶.'},
                       {'code': '>>> bool(abs(base_case - stoiip_mmbbl(12, 25, 0.22, 0.30, 1.25)) '
                                '< 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'base_case uses the most likely values of the table.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
