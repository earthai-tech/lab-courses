OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> _v = stoiip_mmbbl(_np.array([1.0, 2.0]), _np.array([10.0, '
                                '10.0]), 0.2, _np.array([0.25, 0.5]), 1.2)\n'
                                '>>> bool(_np.allclose(_v, [7.86225, 10.483]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'stoiip_mmbbl must work on arrays too: only arithmetic, '
                                           'no if, no loop, no math module.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> bool(isinstance(u, _np.ndarray) and u.shape == (5,) and (u >= '
                                '0).all() and (u < 1).all())\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'u = rng.uniform(0, 1, 5) with rng = '
                                           'np.random.default_rng(13).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
