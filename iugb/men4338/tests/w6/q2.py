OK_FORMAT = True

test = {'name': 'q2',
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
                                '>>> bool(all(abs(idw_estimate(a, b, _x, _y, _v) - _idw(a, b, _x, '
                                '_y, _v)) < 1e-9 for a, b in [(500, 500), (33, 870), (1190, '
                                '10)]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Default power 2 and the 12 nearest samples: w_i = 1 / '
                                           'd_i**power, estimate = sum(w v) / sum(w).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
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
                                '>>> bool(abs(idw_estimate(500, 500, _x, _y, _v, power=1, nmax=30) '
                                '- _idw(500, 500, _x, _y, _v, 1, 30)) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Use the power and nmax arguments.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> bool(idw_estimate(5.0, 5.0, _np.array([5., 0]), '
                                '_np.array([5., 0]), _np.array([3., 9])) == 3.0)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "At a sample location (distance 0) return that sample's "
                                           'value instead of dividing by zero.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
