OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                '>>> _n = len(_g)\n'
                                '>>> bool(n_pairs == _n * (_n - 1) // 2)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'With n grid holes there are n(n-1)/2 distinct pairs.'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                ">>> _x, _y = _g['x'].to_numpy(), _g['y'].to_numpy()\n"
                                '>>> _i, _j = _np.triu_indices(len(_x), 1)\n'
                                '>>> _d = _np.hypot(_x[_j] - _x[_i], _y[_j] - _y[_i])\n'
                                '>>> bool(len(dist) == len(_d) and _np.allclose(_np.sort(dist), '
                                '_np.sort(_d)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'dist holds the distance of every pair of grid holes '
                                           '(use np.triu_indices(n, 1) and np.hypot).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                ">>> _x, _y = _g['x'].to_numpy(), _g['y'].to_numpy()\n"
                                '>>> _i, _j = _np.triu_indices(len(_x), 1)\n'
                                '>>> bool(abs(max_dist - _np.hypot(_x[_j] - _x[_i], _y[_j] - '
                                '_y[_i]).max()) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'max_dist is the largest pair distance.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
