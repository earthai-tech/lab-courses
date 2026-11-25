OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(grades_by_hole, dict) and all(isinstance(v, '
                                'list) for v in grades_by_hole.values()))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'grades_by_hole maps each hole_id to a list.'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _a = list(_csv.DictReader(open('drillholes_assays.csv', "
                                "encoding='utf-8')))\n"
                                ">>> bool(all(grades_by_hole[h] == [int(r['au_ppb']) / 1000 for r "
                                "in _a if r['hole_id'] == h] for h in {r['hole_id'] for r in "
                                '_a}))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Each list holds the grades of that hole in g/t (au_ppb '
                                           '/ 1000), in file order.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
