OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> pay_zones([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0], [True, True, '
                                'True, False, True, False, True])\n'
                                '[(1.0, 2.5)]',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'A zone is a run of consecutive pay samples: top = '
                                           'first depth, base = last depth + 0.5 m. Zones thinner '
                                           'than min_m (1.0 m) are dropped.'},
                       {'code': '>>> pay_zones([1.0, 1.5, 2.0, 2.5], [True, True, False, False], '
                                'min_m=0.5)\n'
                                '[(1.0, 2.0)]',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'min_m is a parameter with default 1.0.'},
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
                                '>>> bool([(float(a), float(b)) for a, b in zones] == [(float(a), '
                                'float(b)) for a, b in _Z] and abs(net_pay_m - _net) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "zones = pay_zones(kw3['depth_m'], kw3['pay']); "
                                           'net_pay_m = sum of (base − top) over the zones.'},
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
                                '>>> bool(abs(phi_pay - _phi_pay) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'phi_pay: mean porosity of the pay samples: '
                                           "kw3.loc[kw3['pay'], 'phi'].mean()."}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
