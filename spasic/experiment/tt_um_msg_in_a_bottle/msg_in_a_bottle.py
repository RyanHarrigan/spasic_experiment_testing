'''
Created on May 26, 2025

@author: Ryan Harrigan, Rachel Moheban
@copyright: Copyright (C) 2025 Ryan Harrigan, https://changeprogramming.com
'''
import random
from spasic.experiment.experiment_result import ExpResult
from spasic.experiment.experiment_parameters import ExperimentParameters
from spasic.experiment.tt_um_msg_in_a_bottle.tt06_rng import generate_index

# family and friend aliases
messages = [
    "gauss",
    "picklejar",
    "apiaceae",
    "compost",
    "jp_67",
    "jamacosin",
    "ms_muffet",
    "QVXAGNDAUK",
    "2GradeFren",
    "Jyn&Maz"
]

def inspect_bottle(params:ExperimentParameters, response:ExpResult):
    # preload response
    write_response(response, uncork_message())

    try:
        idx_555 = generate_index(params)
        write_response(response, uncork_message(idx_555))
    finally:
        print("could not generate 555 index")

    return

def uncork_message(idx: int = random.randint(0, len(messages) - 1)):
    _idx = idx

    # prevent out-of-bounds
    if (idx < 0 or idx > len(messages)):
        _idx = random.randint(0, len(messages) - 1)

    return messages[idx]

def write_response(response:ExpResult, message:str = ""):
    # clamp to 10 characters
    shunted = message[:10]

    # rjust in uPython
    padded = "{:>10}".format(shunted)

    # tx payload
    response.result = bytes(padded, "utf8")

    return
