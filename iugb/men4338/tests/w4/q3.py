OK_FORMAT = True

test = {'name': 'q3',
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
                                '>>> bool(sorted(dir_gammas) == [0, 45, 90, 135] and '
                                'all(_np.allclose(dir_gammas[a], _dv(_x, _y, _v, 50, 10, a, 22.5), '
                                'equal_nan=True) for a in (0, 45, 90, 135)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'dir_gammas maps each azimuth (0, 45, 90, 135) to its '
                                           'semivariance array: lag 50 m, 10 lags, tolerance '
                                           '22.5°.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
