OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd\n'
                                '>>> bool(isinstance(log, _pd.DataFrame) and len(log) == '
                                "len(_pd.read_csv('well_log_kw3.csv')))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'log: the whole file read with pd.read_csv, one row per '
                                           'depth (do not drop rows in log).'},
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
                                ">>> bool(not (log[['gr_api', 'rhob_g_cc', 'rt_ohmm']] == "
                                "-999.25).any().any() and int(log[['gr_api', 'rhob_g_cc', "
                                "'rt_ohmm']].isna().sum().sum()) == int(_L[['gr_api', 'rhob_g_cc', "
                                "'rt_ohmm']].isna().sum().sum()))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Replace the null code -999.25 by NaN: log = '
                                           'log.replace(-999.25, np.nan).'},
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
                                ">>> bool(n_bad == int(_L[['gr_api', 'rhob_g_cc', "
                                "'rt_ohmm']].isna().any(axis=1).sum()))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'n_bad: the number of DEPTHS (rows) with at least one '
                                           'missing value: log.isna().any(axis=1).sum().'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
