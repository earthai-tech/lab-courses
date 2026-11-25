OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd\n'
                                ">>> _a = _pd.read_csv('drillholes_assays.csv')\n"
                                ">>> _a['length_m'] = _a['to_m'] - _a['from_m']; _a['au_gpt'] = "
                                "_a['au_ppb'] / 1000\n"
                                ">>> bool(__import__('numpy').allclose(assays['length_m'], "
                                "_a['length_m']) and "
                                "__import__('numpy').allclose(assays['au_gpt'], _a['au_gpt']))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "New columns: assays['length_m'] = to_m - from_m; "
                                           "assays['au_gpt'] = au_ppb / 1000."}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
