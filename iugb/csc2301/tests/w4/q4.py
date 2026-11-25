OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(samples, list) and isinstance(samples[0], '
                                'dict))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'samples must be a list of dictionaries.'},
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
                                ">>> bool(sorted(samples[0]) == ['au_gpt', 'from_m', 'hole_id', "
                                "'to_m'])\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Each dictionary has exactly the keys hole_id, from_m, '
                                           'to_m, au_gpt.'},
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
                                ">>> bool([(s['hole_id'], s['from_m'], s['to_m'], s['au_gpt']) for "
                                's in samples] == _rows)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Same samples, in file order, with clean hole ids, '
                                           'depths as floats and grades from parse_grade.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
