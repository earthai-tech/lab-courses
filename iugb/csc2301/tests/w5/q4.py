OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(holes_with_vein, list))\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'holes_with_vein must be a list.'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _a = list(_csv.DictReader(open('drillholes_assays.csv', "
                                "encoding='utf-8')))\n"
                                ">>> bool(holes_with_vein == sorted({r['hole_id'] for r in _a if "
                                "r['lithology'] == 'quartz vein'}))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "The holes that cut at least one 'quartz vein', each "
                                           'listed once and sorted. A set removes repeats.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
