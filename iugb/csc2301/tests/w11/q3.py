OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import csv as _csv\n'
                                ">>> _b = list(_csv.DictReader(open('block_model_pit1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _t = [float(r['dx_m']) * float(r['dy_m']) * float(r['dz_m']) "
                                "* float(r['density_t_m3']) for r in _b]\n"
                                ">>> _g = [float(r['au_gpt']) for r in _b]\n"
                                '>>> bool(abs(total_t - sum(_t)) < 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'total_t: the tonnes of all 120 blocks, using '
                                           'geotools.block_tonnes (values from the file are '
                                           'text).'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _b = list(_csv.DictReader(open('block_model_pit1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _t = [float(r['dx_m']) * float(r['dy_m']) * float(r['dz_m']) "
                                "* float(r['density_t_m3']) for r in _b]\n"
                                ">>> _g = [float(r['au_gpt']) for r in _b]\n"
                                '>>> bool(abs(total_oz - sum(t * g / 31.1035 for t, g in zip(_t, '
                                '_g))) < 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'total_oz: the ounces of all blocks, using '
                                           'geotools.gold_ounces on each block.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
