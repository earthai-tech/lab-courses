OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> round(distance_m((0.0, 0.0, 0.0), (3.0, 4.0, 12.0)), 6)\n5.0',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Horizontal distance only: use easting and northing, '
                                           'ignore elevation.'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _c = list(_csv.DictReader(open('collars.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _p = {r['hole_id']: (float(r['easting_m']), "
                                "float(r['northing_m'])) for r in _c}\n"
                                '>>> _d = lambda a, b: ((_p[a][0] - _p[b][0]) ** 2 + (_p[a][1] - '
                                '_p[b][1]) ** 2) ** 0.5\n'
                                ">>> bool(nearest_to_dh01 == min((h for h in _p if h != 'DH-01'), "
                                "key=lambda h: _d('DH-01', h)))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'nearest_to_dh01 is the hole_id closest to DH-01 (not '
                                           'DH-01 itself).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
