OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(callable(ppb_to_gpt))\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Define a function called ppb_to_gpt.'},
                       {'code': '>>> bool(abs(ppb_to_gpt(1000) - 1.0) < 1e-9 and '
                                'abs(ppb_to_gpt(250) - 0.25) < 1e-9)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': '1 g/t is 1000 ppb: divide by 1000.'},
                       {'code': '>>> bool(ppb_to_gpt(0) == 0)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': '0 ppb should give 0 g/t.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
