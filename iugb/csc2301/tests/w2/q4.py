OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(net_pay_m, float))\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'net_pay_m must be a thickness in metres (a float).'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _r = list(_csv.DictReader(open('well_log_kw1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _d = [float(x['depth_m']) for x in _r]; _g = "
                                "[float(x['gr_api']) for x in _r]; _p = [float(x['phi']) for x in "
                                '_r]\n'
                                '>>> _v = lambda g: min(1.0, max(0.0, (g - 30) / (120 - 30)))\n'
                                '>>> bool(abs(net_pay_m - 0.5 * sum(1 for g, p in zip(_g, _p) if '
                                '_v(g) < 0.4 and p >= 0.12)) < 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'A sample is pay if vshale(GR) < 0.4 AND porosity >= '
                                           '0.12. Each sample stands for 0.5 m.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
