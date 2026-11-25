OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> bool(_np.allclose(azimuth_of(_np.array([0., 1, 1, -1, 0, '
                                '-1]), _np.array([1., 1, 0, 1, -1, -1])), [0, 45, 90, 135, 0, '
                                '45]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Azimuth = degrees clockwise from north of the vector '
                                           '(dx, dy): np.degrees(np.arctan2(dx, dy)), folded into '
                                           '[0, 180) with % 180.'},
                       {'code': '>>> bool(abs(float(azimuth_of(-1.0, 0.0)) - 90) < 1e-9)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'A pair is the same in both directions: west (270°) '
                                           'folds back to 90°.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
