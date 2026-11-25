OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _x, _y, _v = (_s[c].to_numpy() for c in ('x', 'y', "
                                "'au_gpt'))\n"
                                '>>> def _idw(x0, y0, x, y, v, p=2, nmax=12):\n'
                                '...     d = _np.hypot(x - x0, y - y0); k = _np.argsort(d)[:nmax]\n'
                                '...     if d[k[0]] < 1e-9: return float(v[k[0]])\n'
                                '...     w = 1 / d[k] ** p\n'
                                '...     return float((w * v[k]).sum() / w.sum())\n'
                                '>>> def _cv(p):\n'
                                '...     e = []\n'
                                '...     for i in range(len(_v)):\n'
                                '...         m = _np.arange(len(_v)) != i\n'
                                '...         e.append(_idw(_x[i], _y[i], _x[m], _y[m], _v[m], p, '
                                '12) - _v[i])\n'
                                '...     return _np.array(e)\n'
                                '>>> _t = [(312.0, 457.0), (641.0, 213.0), (906.0, 782.0), (152.0, '
                                '933.0), (1083.0, 97.0)]\n'
                                '>>> bool(_np.allclose(idw_at_targets, [_idw(a, b, _x, _y, _v) for '
                                'a, b in _t]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'idw_at_targets: idw_estimate (power 2, 12 samples) at '
                                           'each of the 5 targets, in order.'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _tg = _pd.read_csv('bassam_truth_grid.csv')\n"
                                '>>> _t = [(312.0, 457.0), (641.0, 213.0), (906.0, 782.0), (152.0, '
                                '933.0), (1083.0, 97.0)]\n'
                                ">>> _tv = [_tg['au_gpt'].to_numpy()[_np.argmin(_np.hypot(_tg['x'] "
                                "- a, _tg['y'] - b))] for a, b in _t]\n"
                                '>>> bool(_np.allclose(true_at_targets, _tv))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'true_at_targets: the au_gpt of the truth-grid cell '
                                           'centre closest to each target.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> bool(abs(mae_targets - '
                                '_np.mean(_np.abs(_np.array(idw_at_targets) - '
                                '_np.array(true_at_targets)))) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'mae_targets = mean absolute error of the 5 '
                                           'estimates.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
