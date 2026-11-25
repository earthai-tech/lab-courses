OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> _m = {a: _np.nanmean(dir_gammas[a][:4]) for a in dir_gammas}\n'
                                '>>> bool(major_az == min(_m, key=_m.get))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'major_az: the direction whose variogram rises the '
                                           'slowest, i.e. the smallest mean semivariance over the '
                                           'first 4 lags.'},
                       {'code': '>>> bool(minor_az == (major_az + 90) % 180)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'minor_az is perpendicular to major_az (add 90°, modulo '
                                           '180).'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> _m = {a: _np.nanmean(dir_gammas[a][:4]) for a in dir_gammas}\n'
                                '>>> bool(abs(continuity_ratio - _m[minor_az] / _m[major_az]) < '
                                '1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'continuity_ratio = mean of the first 4 lags in the '
                                           'minor direction / same in the major direction.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
