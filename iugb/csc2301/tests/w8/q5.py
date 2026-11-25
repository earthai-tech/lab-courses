OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                ">>> _a = _np.loadtxt('well_log_kw2.csv', delimiter=',', "
                                'skiprows=1)\n'
                                '>>> _d, _g, _r, _t = _a[:, 0], _a[:, 1], _a[:, 2], _a[:, 3]\n'
                                '>>> _phi = (2.65 - _r) / (2.65 - 1.0)\n'
                                '>>> _v = _np.clip((_g - 25) / (130 - 25), 0, 1)\n'
                                '>>> _pay = (_v < 0.35) & (_phi >= 0.10) & (_t >= 10)\n'
                                '>>> bool(abs(net_pay_m - 0.5 * _pay.sum()) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Pay: vsh < 0.35 AND phi_d ≥ 0.10 AND rt ≥ 10 ohm·m. '
                                           'Combine masks with & and brackets; each sample is 0.5 '
                                           'm.'},
                       {'code': '>>> import numpy as _np\n'
                                ">>> _a = _np.loadtxt('well_log_kw2.csv', delimiter=',', "
                                'skiprows=1)\n'
                                '>>> _d, _g, _r, _t = _a[:, 0], _a[:, 1], _a[:, 2], _a[:, 3]\n'
                                '>>> _phi = (2.65 - _r) / (2.65 - 1.0)\n'
                                '>>> _v = _np.clip((_g - 25) / (130 - 25), 0, 1)\n'
                                '>>> _pay = (_v < 0.35) & (_phi >= 0.10) & (_t >= 10)\n'
                                '>>> bool(abs(top_pay_m - _d[_pay][0]) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'top_pay_m is the depth of the shallowest pay sample: '
                                           'depth[pay][0].'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
