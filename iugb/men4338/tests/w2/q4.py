OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> bool(abs(naive_mean - _s['au_gpt'].mean()) < 1e-9)\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'naive_mean is the plain mean of all samples.'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                '>>> def _w(x, y, c):\n'
                                '...     k = _np.floor(_np.asarray(x) / c).astype(int) * 100000 + '
                                '_np.floor(_np.asarray(y) / c).astype(int)\n'
                                '...     _, inv, cnt = _np.unique(k, return_inverse=True, '
                                'return_counts=True)\n'
                                '...     w = 1.0 / cnt[inv]\n'
                                '...     return w / w.sum()\n'
                                ">>> bool(abs(declus_mean - (_w(_s['x'], _s['y'], 50) * "
                                "_s['au_gpt']).sum()) < 1e-9)\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'declus_mean = sum(weights * au) with the 50 m cell '
                                           'weights.'},
                       {'code': '>>> bool(declus_mean < naive_mean)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The infill holes sit on rich ground: declustering '
                                           'should lower the mean.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
