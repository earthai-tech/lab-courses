OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> _h = _np.array([0., 30, 100, 300])\n'
                                '>>> bool(_np.allclose(exponential(_h, 0.1, 0.5, 100), '
                                '_np.where(_h > 0, 0.1 + 0.5 * (1 - _np.exp(-3 * _h / 100)), 0)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'exponential with practical range a: c0 + c (1 - '
                                           'exp(-3h/a)), and 0 at h = 0.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> _h = _np.array([0., 30, 100, 300])\n'
                                '>>> bool(_np.allclose(gaussian(_h, 0.1, 0.5, 100), _np.where(_h > '
                                '0, 0.1 + 0.5 * (1 - _np.exp(-3 * (_h / 100) ** 2)), 0)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'gaussian with practical range a: c0 + c (1 - exp(-3 '
                                           '(h/a)^2)), and 0 at h = 0.'},
                       {'code': '>>> bool(abs(float(exponential(100.0, 0, 1, 100)) - 0.95) < '
                                '0.001)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'At the practical range the model reaches 95 % of the '
                                           'sill: 1 - exp(-3) ≈ 0.95.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
