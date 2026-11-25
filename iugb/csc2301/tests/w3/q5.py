OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(ore_tonnes, float) and isinstance(ore_ounces, '
                                'float))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'ore_tonnes and ore_ounces must be floats.'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _b = list(_csv.DictReader(open('block_model_pit1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _t = lambda r: float(r['dx_m']) * float(r['dy_m']) * "
                                "float(r['dz_m']) * float(r['density_t_m3'])\n"
                                ">>> _o = [r for r in _b if float(r['au_gpt']) >= 0.5]\n"
                                '>>> bool(abs(ore_tonnes - sum(_t(r) for r in _o)) < 1e-3)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Add the tonnes of the blocks whose grade is at least '
                                           'the 0.5 g/t cut-off.'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _b = list(_csv.DictReader(open('block_model_pit1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _t = lambda r: float(r['dx_m']) * float(r['dy_m']) * "
                                "float(r['dz_m']) * float(r['density_t_m3'])\n"
                                ">>> _o = [r for r in _b if float(r['au_gpt']) >= 0.5]\n"
                                ">>> bool(abs(ore_ounces - sum(_t(r) * float(r['au_gpt']) / "
                                '31.1035 for r in _o)) < 1e-3)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Add the ounces of the same ore blocks (grade ≥ 0.5 '
                                           'g/t).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
