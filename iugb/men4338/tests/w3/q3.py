OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> _h, _gm, _n = exp_variogram(_np.array([0., 10, 20, 30]), '
                                '_np.zeros(4), _np.array([1., 2, 4, 7]), 10, 3)\n'
                                '>>> bool(_np.allclose(_n, [3, 2, 1]) and _np.allclose(_gm, [7 / '
                                '3, 8.5, 18]) and _np.allclose(_h, [10, 20, 30]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Class k (1..nlags) holds the pairs with |d - k*lag| < '
                                           'lag/2; return (mean distance, semivariance, number of '
                                           'pairs) as arrays.'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                '>>> def _vg(x, y, v, lag, nlags):\n'
                                '...     x, y, v = (_np.asarray(a, float) for a in (x, y, v))\n'
                                '...     i, j = _np.triu_indices(len(v), 1)\n'
                                '...     d = _np.hypot(x[j] - x[i], y[j] - y[i]); sq = 0.5 * (v[j] '
                                '- v[i]) ** 2\n'
                                '...     out = []\n'
                                '...     for k in range(1, nlags + 1):\n'
                                '...         m = _np.abs(d - k * lag) < lag / 2\n'
                                '...         out.append((d[m].mean() if m.any() else _np.nan, '
                                'sq[m].mean() if m.any() else _np.nan, int(m.sum())))\n'
                                '...     return [_np.array(c) for c in zip(*out)]\n'
                                ">>> _r = _vg(_g['x'], _g['y'], _g['au_gpt'], 50, 12)\n"
                                ">>> _o = exp_variogram(_g['x'].to_numpy(), _g['y'].to_numpy(), "
                                "_g['au_gpt'].to_numpy(), 50, 12)\n"
                                '>>> bool(all(_np.allclose(a, b, equal_nan=True) for a, b in '
                                'zip(_o, _r)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Your function gives different values on the grid '
                                           'holes: check the class rule and the 0.5 factor.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
