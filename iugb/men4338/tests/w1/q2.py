OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _a = _s['au_gpt'].to_numpy()\n"
                                '>>> bool(abs(var_au - _a.var(ddof=1)) < 1e-9 and abs(std_au - '
                                '_a.std(ddof=1)) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Use the sample variance and standard deviation (pandas '
                                           '.var() and .std(), i.e. ddof=1).'},
                       {'code': '>>> bool(abs(cv_au - std_au / mean_au) < 1e-12)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'cv_au = std_au / mean_au (no unit, not a '
                                           'percentage).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
