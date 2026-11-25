OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _a = _s['au_gpt'].to_numpy()\n"
                                '>>> bool(abs(prop_above_1 - (_a > 1.0).mean()) < 1e-12)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'prop_above_1 is the share of samples with au_gpt > '
                                           '1.0: (au > 1.0).mean().'},
                       {'code': '>>> bool(len(ax_map.collections) >= 1 and ax_map.get_aspect() in '
                                "(1.0, 'equal'))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Draw the samples with ax_map.scatter(x, y, c=au, ...) '
                                           "and use ax_map.set_aspect('equal')."},
                       {'code': ">>> bool('m' in ax_map.get_xlabel() and 'm' in "
                                'ax_map.get_ylabel())\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Label both axes with their unit, e.g. 'East (m)' and "
                                           "'North (m)'."}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
