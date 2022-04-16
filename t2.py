import psse_utils
import pandas as pd
import numpy as np
import power_flow_operation, subsytem_data_retrieval

P = psse_utils.InitializePsspy()

import psspy  # Must be imported after Initializing PSSPY, may show false error

sav_path = r'D:\My Drive\my_works\PSSE\test_3_bus_line_close.sav'
psspy.case(sav_path)

i = power_flow_operation.fnsl()  # Perform fnsl
print('Iteration number:%s' % psspy.iterat())

bus_df = subsytem_data_retrieval.Bus().df
print bus_df.to_string()
a = 4

# open line with CB
ierr = psspy.branch_chng(201, 302, r"""@1""", [1, P.i, P.i, P.i, P.i, P.i],
                         [P.f, P.f, P.f, P.f, P.f, P.f, P.f, P.f, P.f, P.f, P.f, P.f, P.f,
                          P.f, P.f])
# ierr = psspy.save('*')  # if want to save
"""Next LF"""
# sav_path = r'G:\My Drive\my_works\PSSE\test_3_bus_line_close.sav'
# psspy.case(sav_path)
# psspy.fnsl([0, 0, 0, 1, 1, 0, 99, 0])
# psspy.lout(0,1)
i = power_flow_operation.fnsl()
print('Iteration number:%s' % psspy.iterat())
bus_df = subsytem_data_retrieval.Bus().df
branch = subsytem_data_retrieval.Branch()
print bus_df.to_string()
b = 4
