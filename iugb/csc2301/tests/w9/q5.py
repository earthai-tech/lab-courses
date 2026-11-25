OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import os\n'
                                ">>> bool(os.path.exists('well_kw2.png') and "
                                "os.path.getsize('well_kw2.png') > 20000)\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Save the log figure: fig_log.savefig('well_kw2.png', "
                                           "dpi=150, bbox_inches='tight')."}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
