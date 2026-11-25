OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(all(len(x) == 100_000 for x in (area, h, phi, sw)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Draw N = 100_000 values for each parameter (size=N).'},
                       {'code': '>>> bool(area.min() >= 8 and area.max() <= 18 and abs(area.mean() '
                                '- 38 / 3) < 0.05)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'area: rng.triangular(8, 12, 18, N), in km².'},
                       {'code': '>>> bool(h.min() >= 5 and abs(h.mean() - 25) < 0.1 and 3.8 < '
                                'h.std() < 4.2)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'h: rng.normal(25, 4, N), then np.clip(h, 5, None) so '
                                           'that no thickness is below 5 m.'},
                       {'code': '>>> bool(phi.min() >= 0.18 and phi.max() <= 0.26 and sw.min() >= '
                                '0.20 and sw.max() <= 0.40 and abs(phi.mean() - 0.22) < 0.002 and '
                                'abs(sw.mean() - 0.30) < 0.002)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'phi: rng.uniform(0.18, 0.26, N); sw: rng.uniform(0.20, '
                                           '0.40, N).'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> _r = _np.random.default_rng(999)\n'
                                '>>> _n = 400_000\n'
                                '>>> _A = _r.triangular(8, 12, 18, _n); _h = '
                                '_np.clip(_r.normal(25, 4, _n), 5, None)\n'
                                '>>> _p = _r.uniform(0.18, 0.26, _n); _s = _r.uniform(0.20, 0.40, '
                                '_n)\n'
                                '>>> _S = _A * 1e6 * _h * _p * (1 - _s) / 1.25 * 6.2898 / 1e6\n'
                                '>>> bool(len(stoiip) == 100_000 and abs(stoiip.mean() / _S.mean() '
                                '- 1) < 0.01)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'stoiip = stoiip_mmbbl(area, h, phi, sw, 1.25): one '
                                           'STOIIP per draw.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
