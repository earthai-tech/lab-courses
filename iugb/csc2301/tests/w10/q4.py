OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd\n'
                                ">>> _a = _pd.read_csv('drillholes_assays.csv')\n"
                                ">>> _a['length_m'] = _a['to_m'] - _a['from_m']; _a['au_gpt'] = "
                                "_a['au_ppb'] / 1000\n"
                                ">>> _a['metal'] = _a['au_gpt'] * _a['length_m']\n"
                                ">>> _s = _a.groupby('hole_id')[['metal', 'length_m']].sum()\n"
                                ">>> _w = _s['metal'] / _s['length_m']\n"
                                '>>> '
                                "bool(__import__('numpy').allclose(weighted_by_hole.sort_index().values, "
                                '_w.sort_index().values))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Per hole: sum of (au_gpt × length_m) divided by sum of '
                                           "length_m. groupby('hole_id') then .sum()."}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
