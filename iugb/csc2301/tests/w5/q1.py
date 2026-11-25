OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(collars, dict) and len(collars) == 6)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'collars must be a dictionary with one entry per hole '
                                           '(6 holes).'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _c = list(_csv.DictReader(open('collars.csv', "
                                "encoding='utf-8')))\n"
                                ">>> bool(all(collars[r['hole_id']] == (float(r['easting_m']), "
                                "float(r['northing_m']), float(r['elevation_m'])) for r in _c))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Each value is a tuple of three floats: (easting, '
                                           'northing, elevation).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
