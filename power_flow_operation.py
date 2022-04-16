# import os
# import sys
#
# psse_path=r'C:\Program Files (x86)\PTI\PSSE33\PSSBIN'
# sys.path.append(psse_path)
# os.environ['PATH'] += ';' + psse_path

import pssepath

pssepath.add_pssepath()
"""Importing from PSSE path"""
import psspy, redirect


def save_current_case():
    ierr = psspy.save('*')  # if want to save


def fnsl(tap_adjustment_flag=0,
         area_interchange_adjustment_flag=0,
         phase_shift_adjustment_flag=0,
         dc_tap_adjustment_flag=1,
         switched_shunt_adjustment_flag=1,
         flat_start_flag=1,
         var_limit_flag=99,
         non_divergent_solution_flag=0):
    """
    var_limit_flag = 99 -> var limit is applied after 99th iteration,
                   = 0 -> var limit is applied Immediately (from 0th Iteration)
                   = -1 -> var limit is Never Applied
    """
    return psspy.fnsl([
        tap_adjustment_flag,
        area_interchange_adjustment_flag,
        phase_shift_adjustment_flag,
        dc_tap_adjustment_flag,
        switched_shunt_adjustment_flag,
        flat_start_flag,
        var_limit_flag,
        non_divergent_solution_flag
    ])
