OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                ">>> _x, _y, _v = (_g[c].to_numpy() for c in ('x', 'y', "
                                "'au_gpt'))\n"
                                '>>> def _dv(x, y, v, lag, nlags, az, atol):\n'
                                '...     i, j = _np.triu_indices(len(v), 1)\n'
                                '...     dx, dy = x[j] - x[i], y[j] - y[i]; d = _np.hypot(dx, dy)\n'
                                '...     a = _np.degrees(_np.arctan2(dx, dy)) % 180; df = '
                                '_np.abs(a - az % 180)\n'
                                '...     keep = _np.minimum(df, 180 - df) <= atol; sq = 0.5 * '
                                '(v[j] - v[i]) ** 2\n'
                                '...     g = []\n'
                                '...     for k in range(1, nlags + 1):\n'
                                '...         m = keep & (_np.abs(d - k * lag) < lag / 2)\n'
                                '...         g.append(sq[m].mean() if m.any() else _np.nan)\n'
                                '...     return _np.array(g)\n'
                                '>>> bool(_np.allclose(dir_variogram(_x, _y, _v, 50, 10, 60, '
                                '22.5)[1], _dv(_x, _y, _v, 50, 10, 60, 22.5), equal_nan=True))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'dir_variogram must keep only the pairs whose azimuth '
                                           'is within atol of the direction (remember 175° and 5° '
                                           'are only 10° apart).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                ">>> _x, _y, _v = (_g[c].to_numpy() for c in ('x', 'y', "
                                "'au_gpt'))\n"
                                '>>> def _dv(x, y, v, lag, nlags, az, atol):\n'
                                '...     i, j = _np.triu_indices(len(v), 1)\n'
                                '...     dx, dy = x[j] - x[i], y[j] - y[i]; d = _np.hypot(dx, dy)\n'
                                '...     a = _np.degrees(_np.arctan2(dx, dy)) % 180; df = '
                                '_np.abs(a - az % 180)\n'
                                '...     keep = _np.minimum(df, 180 - df) <= atol; sq = 0.5 * '
                                '(v[j] - v[i]) ** 2\n'
                                '...     g = []\n'
                                '...     for k in range(1, nlags + 1):\n'
                                '...         m = keep & (_np.abs(d - k * lag) < lag / 2)\n'
                                '...         g.append(sq[m].mean() if m.any() else _np.nan)\n'
                                '...     return _np.array(g)\n'
                                '>>> bool(_np.allclose(dir_variogram(_x, _y, _v, 50, 10, 170, '
                                '15)[1], _dv(_x, _y, _v, 50, 10, 170, 15), equal_nan=True))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Check the angular difference near 0/180°: use '
                                           'min(diff, 180 - diff).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                ">>> _x, _y, _v = (_g[c].to_numpy() for c in ('x', 'y', "
                                "'au_gpt'))\n"
                                '>>> _o = dir_variogram(_x, _y, _v, 50, 10, 0, 90)\n'
                                '>>> _i, _j = _np.triu_indices(len(_v), 1); _d = _np.hypot(_x[_j] '
                                '- _x[_i], _y[_j] - _y[_i])\n'
                                '>>> bool(int(_o[2][0]) == int((_np.abs(_d - 50) < 25).sum()))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'With atol = 90 every pair is kept: the result must '
                                           'equal the omnidirectional variogram.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
