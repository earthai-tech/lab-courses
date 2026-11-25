OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(abs(prob_200 - float((stoiip >= 200).mean())) < 1e-12)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The probability is the share of draws with stoiip >= '
                                           '200: (stoiip >= 200).mean().'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> _r = _np.random.default_rng(999)\n'
                                '>>> _n = 400_000\n'
                                '>>> _A = _r.triangular(8, 12, 18, _n); _h = '
                                '_np.clip(_r.normal(25, 4, _n), 5, None)\n'
                                '>>> _p = _r.uniform(0.18, 0.26, _n); _s = _r.uniform(0.20, 0.40, '
                                '_n)\n'
                                '>>> _S = _A * 1e6 * _h * _p * (1 - _s) / 1.25 * 6.2898 / 1e6\n'
                                '>>> bool(abs(prob_200 - (_S >= 200).mean()) < 0.01)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'prob_200 is a fraction between 0 and 1, not a '
                                           'percentage.'},
                       {'code': '>>> bool(len(ax_mc.patches) >= 10 and len(ax_mc.lines) >= 3 and '
                                "'MMbbl' in ax_mc.get_xlabel())\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Histogram of stoiip in ax_mc, three vertical lines '
                                           '(ax_mc.axvline) at P90, P50, P10, x label with the '
                                           'unit MMbbl.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
