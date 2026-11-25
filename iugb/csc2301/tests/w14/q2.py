OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _t = _pd.DataFrame({'gr_api': [10.0, 80.0, 30.0, _np.nan], "
                                "'rhob_g_cc': [2.30, 2.40, 2.00, 2.30], 'rt_ohmm': [40.0, 40.0, "
                                '5.0, 40.0]})\n'
                                '>>> _e = evaluate(_t)\n'
                                ">>> [round(float(x), 3) for x in _e['vsh'].fillna(-1)], "
                                "[round(float(x), 3) for x in _e['phi']], [bool(x) for x in "
                                "_e['pay']]\n"
                                '([0.0, 0.5, 0.083, -1.0], [0.212, 0.152, 0.394, 0.212], [True, '
                                'False, False, False])',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'vsh = (GR − 20) / (140 − 20) clipped 0–1; phi = (2.65 '
                                           '− RHOB) / 1.65 clipped 0–0.40; pay = vsh < 0.35 & phi '
                                           '≥ 0.12 & RT ≥ 15. A missing value is never pay.'},
                       {'code': '>>> import pandas as _pd\n'
                                ">>> _t = _pd.DataFrame({'gr_api': [10.0], 'rhob_g_cc': [2.3], "
                                "'rt_ohmm': [40.0]})\n"
                                '>>> _e = evaluate(_t)\n'
                                '>>> list(_t.columns)\n'
                                "['gr_api', 'rhob_g_cc', 'rt_ohmm']",
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'evaluate must return a NEW table (work on df.copy()) '
                                           'and leave its input unchanged.'},
                       {'code': '>>> import numpy as _np, pandas as _pd\n'
                                ">>> _L = _pd.read_csv('well_log_kw3.csv').replace(-999.25, "
                                '_np.nan)\n'
                                ">>> _L['vsh'] = ((_L['gr_api'] - 20) / (140 - 20)).clip(0, 1)\n"
                                ">>> _L['phi'] = ((2.65 - _L['rhob_g_cc']) / (2.65 - 1.0)).clip(0, "
                                '0.40)\n'
                                ">>> _L['pay'] = (_L['vsh'] < 0.35) & (_L['phi'] >= 0.12) & "
                                "(_L['rt_ohmm'] >= 15)\n"
                                '>>> def _zones(d, p, min_m=1.0):\n'
                                '...     out, top, last = [], None, None\n'
                                '...     for x, q in list(zip(d, p)) + [(None, False)]:\n'
                                '...         if q and top is None:\n'
                                '...             top = x\n'
                                '...         if not q and top is not None:\n'
                                '...             if last + 0.5 - top >= min_m:\n'
                                '...                 out.append((top, last + 0.5))\n'
                                '...             top = None\n'
                                '...         last = x\n'
                                '...     return out\n'
                                ">>> _Z = _zones(list(_L['depth_m']), list(_L['pay']))\n"
                                '>>> _net = sum(b - t for t, b in _Z)\n'
                                ">>> _phi_pay = _L.loc[_L['pay'], 'phi'].mean()\n"
                                ">>> bool(_np.array_equal(kw3['pay'].values, _L['pay'].values) and "
                                "_np.allclose(kw3['phi'], _L['phi'], equal_nan=True))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'kw3 = evaluate(log): the whole well, including the '
                                           'depths with missing values.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
