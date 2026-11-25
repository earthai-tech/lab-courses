OK_FORMAT = True

test = {'name': 'q4',
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
                                '>>> _e = _cv(2)\n'
                                '>>> bool(len(cv_err) == len(_v) and _np.allclose(cv_err, _e))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Leave-one-out: for each sample i, estimate it from all '
                                           'the OTHER samples (power 2, 12 nearest), error = '
                                           'estimate - true value.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> bool(abs(cv_me - _np.mean(cv_err)) < 1e-12 and abs(cv_mse - '
                                '_np.mean(_np.asarray(cv_err) ** 2)) < 1e-12)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'cv_me = mean error (bias), cv_mse = mean squared '
                                           'error.'},
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
                                '>>> _e = _cv(2)\n'
                                '>>> bool(abs(cv_rho - _np.corrcoef(_v + _e, _v)[0, 1]) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'cv_rho = correlation between the cross-validation '
                                           'estimates and the true values.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
