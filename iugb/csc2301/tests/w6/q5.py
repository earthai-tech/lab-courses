OK_FORMAT = True

test = {'name': 'q5',
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
                                '>>> bool(abs(cum_oil_bbl - sum(o for d, o, w in _ok)) < 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Add the oil of the valid days only.'},
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
                                '>>> _wc = [(w / (o + w), d) for d, o, w in _ok if o + w > 0]\n'
                                '>>> bool(worst_day == max(_wc)[1])\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'worst_day is the date (text) with the highest water '
                                           'cut among valid days with oil + water > 0.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
