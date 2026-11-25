OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> bool(_np.allclose(cutoffs, _np.arange(0, 2.01, 0.25)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'cutoffs = np.arange(0, 2.01, 0.25).'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> _t = _np.array([(bk_map >= c).sum() * 67500 / 1e6 for c in '
                                'cutoffs])\n'
                                '>>> _g = _np.array([bk_map[bk_map >= c].mean() if (bk_map >= '
                                'c).any() else _np.nan for c in cutoffs])\n'
                                '>>> bool(_np.allclose(tonnes_mt, _t) and '
                                '_np.allclose(grade_above, _g, equal_nan=True))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'One block = 50 × 50 × 10 m × 2.7 t/m³ = 67 500 t. '
                                           'tonnes_mt: tonnage of blocks with estimate >= cutoff '
                                           '(Mt); grade_above: their mean grade.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> _t = _np.array([(blocks_true >= c).sum() * 67500 / 1e6 for c '
                                'in cutoffs])\n'
                                '>>> bool(_np.allclose(tonnes_true_mt, _t))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'tonnes_true_mt: the same tonnage curve for '
                                           'blocks_true.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> bool(abs(metal_koz - (bk_map[bk_map >= 1.0] * 67500).sum() / '
                                '31.1035 / 1000) < 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'metal_koz: gold contained in the blocks estimated >= '
                                           '1.0 g/t, in thousands of troy ounces (1 oz = 31.1035 '
                                           'g).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
