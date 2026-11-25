OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import csv as _csv\n'
                                '>>> def _f(s):\n'
                                '...     try:\n'
                                '...         return float(s)\n'
                                '...     except ValueError:\n'
                                '...         return None\n'
                                ">>> _rows = list(_csv.DictReader(open('production_daily_kw1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _ok = [(r['date'], _f(r['oil_bbl']), _f(r['water_bbl'])) for "
                                'r in _rows]\n'
                                '>>> _ok = [(d, o, w) for d, o, w in _ok if o is not None and w is '
                                'not None and o >= 0 and w >= 0]\n'
                                '>>> bool(n_days == len(_rows))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'n_days counts every data line of the file.'},
                       {'code': '>>> import csv as _csv\n'
                                '>>> def _f(s):\n'
                                '...     try:\n'
                                '...         return float(s)\n'
                                '...     except ValueError:\n'
                                '...         return None\n'
                                ">>> _rows = list(_csv.DictReader(open('production_daily_kw1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _ok = [(r['date'], _f(r['oil_bbl']), _f(r['water_bbl'])) for "
                                'r in _rows]\n'
                                '>>> _ok = [(d, o, w) for d, o, w in _ok if o is not None and w is '
                                'not None and o >= 0 and w >= 0]\n'
                                '>>> bool(n_bad == len(_rows) - len(_ok))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'A day is bad when oil or water cannot be read as a '
                                           'number (safe_float gives None) or is negative.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
