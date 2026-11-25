OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(ks_blocks.shape == (16, 20) and ks_block_var.shape == '
                                '(16, 20))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': '50 m blocks over 1000 m × 800 m: 16 rows (north) × 20 '
                                           'columns (east).'},
                       {'code': '>>> import pandas as _pd, numpy as _np\n'
                                '>>> _iv = '
                                "_pd.read_csv('kossou_intervals.csv').dropna(subset=['au_gpt'])\n"
                                ">>> _iv['_l'] = _iv['to_m'] - _iv['from_m']; _iv['_gl'] = "
                                "_iv['au_gpt'] * _iv['_l']\n"
                                ">>> _t = _iv.groupby('hole_id')[['_gl', '_l']].sum(); _c = "
                                "(_t['_gl'] / _t['_l']).rename('_au')\n"
                                ">>> _co = _pd.read_csv('kossou_collars.csv').merge(_c, "
                                "left_on='hole_id', right_index=True)\n"
                                ">>> _x, _y, _v = (_co[c].to_numpy() for c in ('x', 'y', '_au'))\n"
                                '>>> bool(all(abs(ks_blocks[r, c] - ok_block(25 + 50 * c, 25 + 50 '
                                '* r, 50, _x, _y, _v, gamma_ks)[0]) < 1e-6 for r, c in [(0, 0), '
                                '(8, 10), (15, 19)]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Block (r, c) centred on (25 + 50 c, 25 + 50 r): '
                                           'ok_block(..., 50, x, y, au, gamma_ks) with the default '
                                           'nd=4, nmax=16.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
