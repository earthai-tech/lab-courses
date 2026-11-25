OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np, pandas as _pd\n'
                                '>>> from scipy.stats import norm as _norm\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _v = "
                                "_s['au_gpt'].to_numpy()\n"
                                '>>> def _ns(v):\n'
                                '...     r = _np.argsort(_np.argsort(v)); return _norm.ppf((r + '
                                '0.5) / len(v))\n'
                                '>>> bool(_np.allclose(nscore(_np.array([3., 1, 2, 10])), '
                                '_norm.ppf([0.625, 0.125, 0.375, 0.875])))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Rank the values (0 = smallest), then y = '
                                           'norm.ppf((rank + 0.5) / n).'},
                       {'code': '>>> import numpy as _np, pandas as _pd\n'
                                '>>> from scipy.stats import norm as _norm\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _v = "
                                "_s['au_gpt'].to_numpy()\n"
                                '>>> def _ns(v):\n'
                                '...     r = _np.argsort(_np.argsort(v)); return _norm.ppf((r + '
                                '0.5) / len(v))\n'
                                '>>> bool(_np.allclose(y_ns, _ns(_v)) and abs(y_ns.mean()) < '
                                '1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'y_ns = nscore(au): mean 0 and variance close to 1.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
