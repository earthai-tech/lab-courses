OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(reals.shape == (20, 33, 40))\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'reals: 20 realisations on 33 rows × 40 columns (30 m '
                                           'nodes).'},
                       {'code': '>>> import numpy as _np, pandas as _pd\n'
                                '>>> from scipy.stats import norm as _norm\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _v = "
                                "_s['au_gpt'].to_numpy()\n"
                                '>>> def _ns(v):\n'
                                '...     r = _np.argsort(_np.argsort(v)); return _norm.ppf((r + '
                                '0.5) / len(v))\n'
                                '>>> bool(reals.min() >= _v.min() - 1e-9 and reals.max() <= '
                                '_v.max() + 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Back-transform each realisation to grades: values stay '
                                           'within the data range.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> bool(0.85 < reals.mean() < 1.25 and _np.mean([r.var() for r '
                                'in reals]) > 0.12)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Each realisation should have a mean near 1 g/t and a '
                                           'variance close to that of the data (no smoothing).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
