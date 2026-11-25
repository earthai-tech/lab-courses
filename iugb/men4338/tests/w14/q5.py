OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> _o = (ks_blocks >= 0.8)\n'
                                ">>> bool(abs(resource['tonnes_mt'].sum() - _o.sum() * 54000 / "
                                '1e6) < 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'One block = 50 × 50 × 8 m × 2.7 t/m³ = 54 000 t; the '
                                           'categories together hold every block estimated >= 0.8 '
                                           'g/t.'},
                       {'code': '>>> import numpy as _np\n'
                                ">>> bool(list(resource['category']) == ['Measured', 'Indicated', "
                                "'Inferred'])\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'resource has one row per category, in the order '
                                           'Measured, Indicated, Inferred.'},
                       {'code': '>>> import numpy as _np\n'
                                ">>> _ok = resource['tonnes_mt'] > 0\n"
                                ">>> bool(_np.allclose(resource.loc[_ok, 'metal_koz'], "
                                "resource.loc[_ok, 'tonnes_mt'] * 1e6 * resource.loc[_ok, "
                                "'grade_gpt'] / 31.1035 / 1000))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'metal_koz = tonnes × grade / 31.1035 / 1000 for each '
                                           'category.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> _o = ks_blocks >= 0.8\n'
                                ">>> bool(abs(resource['metal_koz'].sum() - (ks_blocks[_o] * "
                                '54000).sum() / 31.1035 / 1000) < 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The total metal must equal the metal of all blocks >= '
                                           '0.8 g/t.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
