OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd\n'
                                '>>> bool(isinstance(assays, _pd.DataFrame) and '
                                'isinstance(collars, _pd.DataFrame))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Read both files with pd.read_csv.'},
                       {'code': '>>> import pandas as _pd\n'
                                ">>> _a = _pd.read_csv('drillholes_assays.csv')\n"
                                ">>> _a['length_m'] = _a['to_m'] - _a['from_m']; _a['au_gpt'] = "
                                "_a['au_ppb'] / 1000\n"
                                '>>> bool(n_rows == len(_a) and n_holes == '
                                "_a['hole_id'].nunique())\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'n_rows = len(assays); n_holes = number of different '
                                           'hole_id values (.nunique()).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
