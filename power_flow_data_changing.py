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

psspy.throwPsseException = True
i_default = psspy.getdefaultint()  # in place of default integer values, the variable i is used
f_default = psspy.getdefaultreal()  # in place of default float values, the variable f is used.
s_default = psspy.getdefaultchar()  # in place of default char values, the variable f is used.


def load(bus_no,
         load_id=1,
         load_status=1,
         area_no=i_default,
         zone_no=i_default,
         owner_no=i_default,
         load_scaling_flag=1,
         interruptible_load_flag=0,
         load_distributed_gen_flag=0,
         p_const_power=f_default,
         q_const_power=f_default,
         p_const_current=f_default,
         q_const_current=f_default,
         p_const_admittance=f_default,
         q_const_admittance=f_default,
         p_distributed_gen=f_default,
         q_distributed_gen=f_default,
         ):
    i = bus_no
    if type(load_id) != str:
        load_id = str(load_id)

    intgar = [
        load_status,
        area_no,
        zone_no,
        owner_no,
        load_scaling_flag,
        interruptible_load_flag,
        # load_distributed_gen_flag
    ]
    realar = [
        p_const_power,
        q_const_power,
        p_const_current,
        q_const_current,
        p_const_admittance,
        q_const_admittance,
        # p_distributed_gen,
        # q_distributed_gen
    ]

    return psspy.load_data_4(i, load_id, intgar, realar)
