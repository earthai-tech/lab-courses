OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _iv = _pd.read_csv('bassam_intervals.csv')\n"
                                ">>> _iv['_l'] = _iv['to_m'] - _iv['from_m']\n"
                                ">>> _ok = _iv.dropna(subset=['au_gpt'])\n"
                                ">>> _c = (_ok['au_gpt'] * "
                                "_ok['_l']).groupby(_ok['hole_id']).sum() / "
                                "_ok['_l'].groupby(_ok['hole_id']).sum()\n"
                                '>>> bool(len(composites) == len(_c) and '
                                '_np.allclose(composites.sort_index().to_numpy(), '
                                '_c.sort_index().to_numpy()))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'composites: one length-weighted grade per hole, '
                                           'ignoring the missing intervals (weights = length_m of '
                                           'the assayed intervals).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                '>>> bool(abs(max_diff - '
                                "(composites.reindex(_s['hole_id']).to_numpy() - "
                                "_s['au_gpt'].to_numpy()).__abs__().max()) < 1e-9)\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'max_diff = largest absolute difference between your '
                                           'composites and the au_gpt column of bassam_samples.csv '
                                           '(match them by hole_id).'},
                       {'code': '>>> bool(max_diff < 0.002)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Your composites should match bassam_samples.csv to the '
                                           'third decimal.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
