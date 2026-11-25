OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(len(fig_kw3.axes) == 3 and '
                                'fig_kw3.axes[0].yaxis_inverted())\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Three tracks sharing depth (plt.subplots(1, 3, '
                                           'sharey=True)), depth increasing downwards.'},
                       {'code': ">>> bool(fig_kw3.axes[2].get_xscale() == 'log')\nTrue",
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Resistivity is always shown on a logarithmic scale: '
                                           "ax.set_xscale('log')."},
                       {'code': '>>> bool(len(fig_kw3.axes[0].patches) >= len(zones))\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Shade each pay zone in the GR track with '
                                           'ax.axhspan(top, base, color=..., alpha=0.3).'},
                       {'code': '>>> import os\n'
                                ">>> bool(os.path.exists('kw3_logs.png') and "
                                "os.path.getsize('kw3_logs.png') > 20000)\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Save the figure as kw3_logs.png (dpi=150, '
                                           "bbox_inches='tight')."}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
