OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': ">>> _src = open('report.py', encoding='utf-8').read()\n"
                                ">>> bool('geotools' in _src and '__main__' in _src)\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'report.py must import geotools and call main() under '
                                           'if __name__ == "__main__":'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _b = list(_csv.DictReader(open('block_model_pit1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _t = [float(r['dx_m']) * float(r['dy_m']) * float(r['dz_m']) "
                                "* float(r['density_t_m3']) for r in _b]\n"
                                ">>> _g = [float(r['au_gpt']) for r in _b]\n"
                                '>>> _oz = sum(t * g / 31.1035 for t, g in zip(_t, _g))\n'
                                ">>> bool(open('pit1_report.txt', encoding='utf-8').read().strip() "
                                "== f'Pit 1: {len(_b)} blocks, {sum(_t):.0f} t, {_oz:.1f} oz')\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Run the script with %run report.py; it writes one '
                                           'line: Pit 1: 120 blocks, <tonnes, 0 decimals> t, '
                                           '<ounces, 1 decimal> oz'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
