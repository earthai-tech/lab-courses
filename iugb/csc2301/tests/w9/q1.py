OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(len(fig_log.axes) == 2)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'fig_log needs two panels side by side: plt.subplots(1, '
                                           '2, sharey=True).'},
                       {'code': '>>> import numpy as _np\n'
                                ">>> _a = _np.loadtxt('well_log_kw2.csv', delimiter=',', "
                                'skiprows=1)\n'
                                '>>> bool(len(ax_gr.lines) >= 1 and '
                                '_np.allclose(ax_gr.lines[0].get_xdata(), _a[:, 1]) and '
                                '_np.allclose(ax_gr.lines[0].get_ydata(), _a[:, 0]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'In a log display the value is on x and the depth on y: '
                                           'ax_gr.plot(gr, depth).'},
                       {'code': '>>> bool(len(ax_rhob.lines) >= 1)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Plot rhob against depth in ax_rhob.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
