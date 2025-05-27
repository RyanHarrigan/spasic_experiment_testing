'''
Created on May 26, 2025

@author: Ryan Harrigan, Rachel Moheban
@copyright: Copyright (C) 2025 Ryan Harrigan, https://changeprogramming.com
'''
import random
from spasic.experiment.experiment_parameters import ExperimentParameters

import gc
gc.threshold(10000)

def generate_index(params:ExperimentParameters):
    # get the TT DemoBoard object from params passed in
    tt = params.tt

    # tt06 experiments: rng
    tt.shuttle.tt_um_rng.enable()

    # Likely you want to clock it yourself, stop any auto-clocking
    tt.clock_project_stop()

    # setup seed input
    tt.ui_in[0:4] = [random.choice([0,1]) for _ in range(4)]

    # random mode input
    tt.ui_in[5:6] = [random.choice([0,1]) for _ in range(2)]

    # reset project
    tt.reset_project(True)

    # idk how many ticks
    tt.clock_project_once()  # tick

    # release from reset
    tt.reset_project(False)

    # inside tightest loop, keep checking if
    # termination has been requested
    if not params.keep_running:
        return

    tt.uo_out.value

    raise('index generation error')