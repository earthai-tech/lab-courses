OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> _t = _np.array([(r >= 1.0).sum() * 24300 / 1e6 for r in '
                                'reals])\n'
                                '>>> bool(_np.allclose(tonnage_mt, _t))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'One 30 m node = 30 × 30 × 10 m × 2.7 t/m³ = 24 300 t. '
                                           'tonnage_mt[k]: tonnage of nodes >= 1.0 g/t in '
                                           'realisation k (Mt).'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> bool(_np.allclose([t_p90, t_p50, t_p10], '
                                '_np.percentile(tonnage_mt, [10, 50, 90])))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'P90 = 10th percentile (the value exceeded in 90 % of '
                                           'the realisations), P50 = median, P10 = 90th '
                                           'percentile.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> bool(prob_ore.shape == (33, 40) and _np.allclose(prob_ore, '
                                '(reals >= 1.0).mean(axis=0)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'prob_ore: share of the realisations above 1.0 g/t at '
                                           'each node.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
