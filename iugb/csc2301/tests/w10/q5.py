OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd\n'
                                ">>> _a = _pd.read_csv('drillholes_assays.csv')\n"
                                ">>> _a['length_m'] = _a['to_m'] - _a['from_m']; _a['au_gpt'] = "
                                "_a['au_ppb'] / 1000\n"
                                ">>> _c = _pd.read_csv('collars.csv')\n"
                                ">>> _m = _a.merge(_c, on='hole_id')\n"
                                ">>> bool(len(summary) == 6 and {'easting_m', 'northing_m', "
                                "'mean_gpt'} <= set(summary.columns))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'summary: one row per hole with hole_id, easting_m, '
                                           'northing_m and mean_gpt (the weighted mean).'},
                       {'code': ">>> bool(summary['mean_gpt'].is_monotonic_decreasing)\nTrue",
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Sort summary from the richest hole to the poorest: '
                                           "sort_values('mean_gpt', ascending=False)."},
                       {'code': ">>> import os\n>>> bool(os.path.exists('hole_summary.csv'))\nTrue",
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Save it with summary.to_csv('hole_summary.csv', "
                                           'index=False).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
