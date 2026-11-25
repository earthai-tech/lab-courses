OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd\n'
                                ">>> _a = _pd.read_csv('drillholes_assays.csv')\n"
                                ">>> _a['length_m'] = _a['to_m'] - _a['from_m']; _a['au_gpt'] = "
                                "_a['au_ppb'] / 1000\n"
                                ">>> bool(len(high_grade) == int((_a['au_gpt'] >= 2).sum()) and "
                                "(high_grade['au_gpt'] >= 2).all())\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'high_grade: the rows with au_gpt >= 2, selected with a '
                                           "mask: assays[assays['au_gpt'] >= 2]."},
                       {'code': '>>> import pandas as _pd\n'
                                ">>> _a = _pd.read_csv('drillholes_assays.csv')\n"
                                ">>> _a['length_m'] = _a['to_m'] - _a['from_m']; _a['au_gpt'] = "
                                "_a['au_ppb'] / 1000\n"
                                ">>> bool(abs(granite_mean - _a.loc[_a['lithology'] == 'granite', "
                                "'au_gpt'].mean()) < 1e-9)\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'granite_mean: the (simple) mean au_gpt of the granite '
                                           'intervals.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
