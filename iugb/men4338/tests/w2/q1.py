OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _iv = _pd.read_csv('bassam_intervals.csv')\n"
                                ">>> _iv['_l'] = _iv['to_m'] - _iv['from_m']\n"
                                ">>> bool(_np.allclose(intervals['length_m'], _iv['_l']))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Add the column intervals['length_m'] = to_m - from_m."},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _iv = _pd.read_csv('bassam_intervals.csv')\n"
                                ">>> _iv['_l'] = _iv['to_m'] - _iv['from_m']\n"
                                ">>> bool(int(n_missing) == int(_iv['au_gpt'].isna().sum()))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'n_missing counts the empty au_gpt cells: '
                                           "intervals['au_gpt'].isna().sum()."},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _iv = _pd.read_csv('bassam_intervals.csv')\n"
                                ">>> _iv['_l'] = _iv['to_m'] - _iv['from_m']\n"
                                ">>> bool(abs(sampled_m - _iv.loc[_iv['au_gpt'].notna(), "
                                "'_l'].sum()) < 1e-6)\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'sampled_m is the total length of the intervals that '
                                           'have an assay (not the missing ones).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
