OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': ">>> bool(isinstance(block_summary({'dx_m': '10', 'dy_m': '10', "
                                "'dz_m': '5', 'density_t_m3': '2.70', 'au_gpt': '2.00'}), tuple))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'block_summary must return a tuple: return tonnes, '
                                           'ounces'},
                       {'code': ">>> [round(v, 3) for v in block_summary({'dx_m': '10', 'dy_m': "
                                "'10', 'dz_m': '5', 'density_t_m3': '2.70', 'au_gpt': '2.00'})]\n"
                                '[1350.0, 86.807]',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Read the values from the row (they are text: convert '
                                           'with float), then reuse block_tonnes and '
                                           'gold_ounces.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
