OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np, pandas as _pd\n'
                                '>>> from scipy.stats import norm as _norm\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _v = "
                                "_s['au_gpt'].to_numpy()\n"
                                '>>> def _ns(v):\n'
                                '...     r = _np.argsort(_np.argsort(v)); return _norm.ppf((r + '
                                '0.5) / len(v))\n'
                                '>>> bool(_np.allclose(back_transform(_ns(_v), _v), _v))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'back_transform(y, v) = np.interp(y, '
                                           'np.sort(nscore(v)), np.sort(v)): it must give the data '
                                           'back exactly.'},
                       {'code': '>>> import numpy as _np, pandas as _pd\n'
                                '>>> from scipy.stats import norm as _norm\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _v = "
                                "_s['au_gpt'].to_numpy()\n"
                                '>>> def _ns(v):\n'
                                '...     r = _np.argsort(_np.argsort(v)); return _norm.ppf((r + '
                                '0.5) / len(v))\n'
                                '>>> bool(_np.allclose(back_transform(_np.array([-9., 9.]), _v), '
                                '[_v.min(), _v.max()]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Beyond the extreme normal scores, np.interp keeps the '
                                           'minimum and maximum grade.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
