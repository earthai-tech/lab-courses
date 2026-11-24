OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(first_shale_depth, float))\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'first_shale_depth must be a depth in metres (a '
                                           'float).'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _r = list(_csv.DictReader(open('well_log_kw1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _d = [float(x['depth_m']) for x in _r]; _g = "
                                "[float(x['gr_api']) for x in _r]; _p = [float(x['phi']) for x in "
                                '_r]\n'
                                '>>> bool(first_shale_depth == next(d for d, g in zip(_d, _g) if d '
                                '> 1540 and g >= 100))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Go down the log from the top, skip depths down to 1540 '
                                           'm, and stop (break) at the first GR of 100 API or '
                                           'more.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
