OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(ax_gr.yaxis_inverted())\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Depth increases downwards: ax_gr.invert_yaxis() '
                                           '(shared y: once is enough).'},
                       {'code': ">>> bool('API' in ax_gr.get_xlabel() and 'g/cm' in "
                                "ax_rhob.get_xlabel() and 'epth' in ax_gr.get_ylabel())\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Label every axis with its unit: GR (API), RHOB '
                                           '(g/cm³), Depth (m).'},
                       {'code': '>>> bool(fig_log.texts or fig_log._suptitle is not None or '
                                "ax_gr.get_title() != '')\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Give the figure a title, e.g. fig_log.suptitle('Well "
                                           "KW-2')."}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
