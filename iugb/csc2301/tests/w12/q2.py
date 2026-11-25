OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import bisect as _bi, random as _r\n'
                                '>>> _d = [2100 + 0.5 * k for k in range(601)]\n'
                                '>>> _q = [2099.0, 2100.0, 2400.0, 2401.0] + [_r.uniform(2090, '
                                '2410) for _ in range(300)]\n'
                                '>>> bool(all(depth_index(_d, x) == _bi.bisect_left(_d, x) for x '
                                'in _q))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'depth_index(depths, d): index of the first depth >= d '
                                           '(0 if d is above the first, len(depths) if below the '
                                           'last). Compare with bisect.bisect_left.'},
                       {'code': '>>> import inspect as _in\n'
                                ">>> bool('while' in _in.getsource(depth_index) and 'bisect' not "
                                'in _in.getsource(depth_index))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Write the binary search yourself with lo, hi and a '
                                           'while loop; do not call bisect inside the function.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
