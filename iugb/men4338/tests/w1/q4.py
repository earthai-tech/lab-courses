OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _a = _s['au_gpt'].to_numpy()\n"
                                '>>> bool(abs(cap_value - _np.percentile(_a, 99)) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'cap_value = np.percentile(au, 99).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _a = _s['au_gpt'].to_numpy()\n"
                                '>>> bool(_np.allclose(au_capped, _np.minimum(_a, '
                                '_np.percentile(_a, 99))))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'au_capped keeps every value but replaces those above '
                                           'cap_value by cap_value: np.minimum(au, cap_value).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _a = _s['au_gpt'].to_numpy()\n"
                                '>>> _c = _np.minimum(_a, _np.percentile(_a, 99))\n'
                                '>>> bool(abs(metal_removed - (1 - _c.sum() / _a.sum())) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'metal_removed = 1 - sum(capped) / sum(original): a '
                                           'fraction, not a percentage.'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _a = _s['au_gpt'].to_numpy()\n"
                                '>>> bool(n_capped == int((_a > _np.percentile(_a, 99)).sum()))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'n_capped counts the values strictly above cap_value.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
