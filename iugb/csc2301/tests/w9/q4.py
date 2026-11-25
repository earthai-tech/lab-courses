OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(len(ax_map.collections) >= 1 and '
                                'len(ax_map.collections[0].get_offsets()) == 6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Draw the 6 collars with ax_map.scatter(easting, '
                                           'northing).'},
                       {'code': '>>> bool(len(ax_map.texts) == 6)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Write each hole name next to its point with '
                                           'ax_map.annotate (or ax_map.text).'},
                       {'code': ">>> bool(ax_map.get_aspect() in (1.0, 'equal'))\nTrue",
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'A map must not stretch distances: '
                                           "ax_map.set_aspect('equal')."}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
