OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> bool(_np.allclose([p90, p50, p10], _np.percentile(stoiip, '
                                '[10, 50, 90])))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Industry convention: P90 is the value exceeded 90 % of '
                                           'the time, i.e. the 10th percentile: '
                                           'np.percentile(stoiip, [10, 50, 90]).'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> _r = _np.random.default_rng(999)\n'
                                '>>> _n = 400_000\n'
                                '>>> _A = _r.triangular(8, 12, 18, _n); _h = '
                                '_np.clip(_r.normal(25, 4, _n), 5, None)\n'
                                '>>> _p = _r.uniform(0.18, 0.26, _n); _s = _r.uniform(0.20, 0.40, '
                                '_n)\n'
                                '>>> _S = _A * 1e6 * _h * _p * (1 - _s) / 1.25 * 6.2898 / 1e6\n'
                                '>>> bool(p90 < p50 < p10 and abs(p50 / _np.percentile(_S, 50) - '
                                '1) < 0.015)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'p90 < p50 < p10.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
