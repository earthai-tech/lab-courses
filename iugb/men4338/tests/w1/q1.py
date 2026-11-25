OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _a = _s['au_gpt'].to_numpy()\n"
                                '>>> bool(n_samples == len(_s))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'n_samples is the number of rows (holes) in the file: '
                                           'len(df).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _a = _s['au_gpt'].to_numpy()\n"
                                '>>> bool(abs(mean_au - _a.mean()) < 1e-9 and abs(median_au - '
                                '_np.median(_a)) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "mean_au = df['au_gpt'].mean(), median_au = "
                                           "df['au_gpt'].median()."},
                       {'code': '>>> bool(mean_au > median_au)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'For a positively skewed variable the mean is above the '
                                           'median: check your two values.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
