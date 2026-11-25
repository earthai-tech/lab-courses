OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> bool(_np.allclose(cell_sizes, _np.arange(25, 201, 25)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'cell_sizes = np.arange(25, 201, 25).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                '>>> def _w(x, y, c):\n'
                                '...     k = _np.floor(_np.asarray(x) / c).astype(int) * 100000 + '
                                '_np.floor(_np.asarray(y) / c).astype(int)\n'
                                '...     _, inv, cnt = _np.unique(k, return_inverse=True, '
                                'return_counts=True)\n'
                                '...     w = 1.0 / cnt[inv]\n'
                                '...     return w / w.sum()\n'
                                ">>> _m = [(_w(_s['x'], _s['y'], c) * _s['au_gpt']).sum() for c in "
                                'range(25, 201, 25)]\n'
                                '>>> bool(_np.allclose(declus_means, _m))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'declus_means[k] is the declustered mean with cell size '
                                           'cell_sizes[k].'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> bool(best_cell == cell_sizes[int(_np.argmin(declus_means))])\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'When the clusters are on high grades, choose the cell '
                                           'size giving the lowest declustered mean.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
