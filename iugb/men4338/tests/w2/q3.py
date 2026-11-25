OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> _w = cell_weights(_np.array([10., 20., 30., 160.]), '
                                '_np.array([10., 15., 20., 40.]), 100)\n'
                                '>>> bool(_np.allclose(_w, [1/6, 1/6, 1/6, 1/2]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Three samples share one 100 m cell (1/3 each), one is '
                                           'alone (weight 1); then divide by the sum so the '
                                           'weights add up to 1.'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                '>>> def _w(x, y, c):\n'
                                '...     k = _np.floor(_np.asarray(x) / c).astype(int) * 100000 + '
                                '_np.floor(_np.asarray(y) / c).astype(int)\n'
                                '...     _, inv, cnt = _np.unique(k, return_inverse=True, '
                                'return_counts=True)\n'
                                '...     w = 1.0 / cnt[inv]\n'
                                '...     return w / w.sum()\n'
                                ">>> bool(_np.allclose(cell_weights(_s['x'].to_numpy(), "
                                "_s['y'].to_numpy(), 50), _w(_s['x'], _s['y'], 50)))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Cells start at x = 0, y = 0: cell index = floor(x / '
                                           'cell_size), floor(y / cell_size).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
