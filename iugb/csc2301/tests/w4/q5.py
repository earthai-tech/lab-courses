OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import csv as _c\n'
                                ">>> _w = list(_c.DictReader(open('lab_report_clean.csv', "
                                "encoding='utf-8')))\n"
                                ">>> bool(list(_w[0]) == ['hole_id', 'from_m', 'to_m', 'au_gpt'])\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Write lab_report_clean.csv with the header '
                                           'hole_id,from_m,to_m,au_gpt.'},
                       {'code': '>>> def _hole(s):\n'
                                "...     d = ''.join(c for c in s if c.isdigit())\n"
                                "...     return 'DH-' + d.zfill(2)\n"
                                '>>> def _grade(s):\n'
                                "...     s = s.strip().lower().replace('g/t', "
                                "'').strip().replace(',', '.')\n"
                                "...     if s in ('', 'n.d.'):\n"
                                '...         return None\n'
                                "...     if s.startswith('<'):\n"
                                '...         return float(s[1:]) / 2\n'
                                '...     return float(s)\n'
                                '>>> _rows = []\n'
                                ">>> for _l in open('lab_report_raw.txt', encoding='utf-8'):\n"
                                "...     _p = [x.strip() for x in _l.split(';')]\n"
                                "...     if len(_p) == 5 and _p[0].startswith('S0'):\n"
                                "...         _a, _b = _p[2].split('-')\n"
                                '...         _rows.append((_hole(_p[1]), float(_a), float(_b), '
                                '_grade(_p[3])))\n'
                                '>>> import csv as _c\n'
                                ">>> _w = list(_c.DictReader(open('lab_report_clean.csv', "
                                "encoding='utf-8')))\n"
                                '>>> bool(len(_w) == sum(1 for r in _rows if r[3] is not None))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Write only the samples that have a grade (leave out '
                                           'the None ones).'},
                       {'code': ">>> summary_line('DH-03', 12, 1.2345)\n"
                                "'DH-03: 12 samples, mean 1.23 g/t'",
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Use an f-string with :.2f for the mean.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
