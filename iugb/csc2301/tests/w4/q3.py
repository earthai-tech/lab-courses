OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> def _hole(s):\n'
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
                                '>>> bool(n_samples == len(_rows))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Count only the sample lines: they start with 'S0' and "
                                           "have 5 fields separated by ';'."},
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
                                '>>> bool(n_missing == sum(1 for r in _rows if r[3] is None))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'n_missing counts the samples whose grade is None.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
