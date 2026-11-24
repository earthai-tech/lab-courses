OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(n_sand, int))\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'n_sand must be a whole number (an int).'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _r = list(_csv.DictReader(open('well_log_kw1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _d = [float(x['depth_m']) for x in _r]; _g = "
                                "[float(x['gr_api']) for x in _r]; _p = [float(x['phi']) for x in "
                                '_r]\n'
                                '>>> bool(n_sand == sum(1 for g in _g if g < 60))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Count the samples whose GR is strictly below 60 API.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
