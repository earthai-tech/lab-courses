OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _a = _s['au_gpt'].to_numpy()\n"
                                '>>> _q = _np.percentile(_a, [10, 25, 50, 75, 90])\n'
                                '>>> bool(_np.allclose(quantiles, _q))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'quantiles = np.percentile(au, [10, 25, 50, 75, 90]).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _a = _s['au_gpt'].to_numpy()\n"
                                '>>> bool(abs(iqr_au - (_np.percentile(_a, 75) - '
                                '_np.percentile(_a, 25))) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'iqr_au is the 75th percentile minus the 25th '
                                           'percentile.'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _a = _s['au_gpt'].to_numpy()\n"
                                '>>> _l = _np.log(_a)\n'
                                '>>> bool(abs(log_mean - _l.mean()) < 1e-9 and abs(log_var - '
                                '_l.var(ddof=1)) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'log_mean and log_var are the mean and the sample '
                                           'variance (ddof=1) of np.log(au).'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> bool(abs(lognormal_mean - _np.exp(log_mean + log_var / 2)) < '
                                '1e-12)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Lognormal mean: exp(log_mean + log_var / 2).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
