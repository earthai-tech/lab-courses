OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> def _sph(h, c0, c, a):\n'
                                '...     h = _np.asarray(h, float); r = _np.minimum(h / a, 1)\n'
                                '...     return _np.where(h > 0, c0 + c * (1.5 * r - 0.5 * r ** '
                                '3), 0.0)\n'
                                '>>> import pandas as _pd\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _g = "
                                "_s[_s['campaign'] == 'grid']\n"
                                ">>> _h, _gm, _n = exp_variogram(_g['x'], _g['y'], _g['au_gpt'], "
                                '50, 12)\n'
                                '>>> bool(_np.allclose(h_exp, _h) and _np.allclose(g_exp, _gm) and '
                                '_np.allclose(n_exp, _n))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'h_exp, g_exp, n_exp = exp_variogram(x, y, au, 50, 12) '
                                           'on the grid holes.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> def _sph(h, c0, c, a):\n'
                                '...     h = _np.asarray(h, float); r = _np.minimum(h / a, 1)\n'
                                '...     return _np.where(h > 0, c0 + c * (1.5 * r - 0.5 * r ** '
                                '3), 0.0)\n'
                                '>>> import pandas as _pd\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv'); _g = "
                                "_s[_s['campaign'] == 'grid']\n"
                                ">>> _h, _gm, _n = exp_variogram(_g['x'], _g['y'], _g['au_gpt'], "
                                '50, 12)\n'
                                '>>> bool(abs(wsse((0.05, 0.2, 250), _h, _gm, _n) - _np.sum(_n * '
                                '(_gm - _sph(_h, 0.05, 0.2, 250)) ** 2)) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'wsse(params, h, g, n) = sum of n * (g - spherical(h, '
                                           'c0, c, a))**2 with params = (c0, c, a).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
