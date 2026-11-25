OK_FORMAT = True

test = {'name': 'q5',
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
                                '>>> _m = {p: float(_np.mean(_cv(p) ** 2)) for p in (1, 2, 3)}\n'
                                '>>> bool(sorted(cv_mse_by_power) == [1, 2, 3] and '
                                'all(abs(cv_mse_by_power[p] - _m[p]) < 1e-9 for p in _m))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'cv_mse_by_power maps 1, 2, 3 to the leave-one-out MSE '
                                           '(12 nearest samples).'},
                       {'code': '>>> bool(best_power == min(cv_mse_by_power, '
                                'key=cv_mse_by_power.get))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'best_power: the power with the smallest MSE.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
