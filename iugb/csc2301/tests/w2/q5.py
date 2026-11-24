OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(n_sand_beds, int))\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'n_sand_beds must be a whole number (an int).'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _r = list(_csv.DictReader(open('well_log_kw1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _d = [float(x['depth_m']) for x in _r]; _g = "
                                "[float(x['gr_api']) for x in _r]; _p = [float(x['phi']) for x in "
                                '_r]\n'
                                '>>> _n = 0; _prev = False\n'
                                '>>> for g in _g:\n'
                                '...     s = g < 60\n'
                                '...     if s and not _prev:\n'
                                '...         _n += 1\n'
                                '...     _prev = s\n'
                                '>>> bool(n_sand_beds == _n)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Count how many times the log enters sand (GR < 60) '
                                           'after a non-sand sample, plus 1 if the log starts in '
                                           'sand.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
