import psse_utils
import pandas as pd
import numpy as np
import power_flow_operation, subsytem_data_retrieval, power_flow_data_changing, sweep
import openpyxl
P = psse_utils.InitializePsspy()

import psspy  # Must be imported after Initializing PSSPY, may show false error

sav_path = r'G:\My Drive\my_works\PSSE\Coductor Loading Profile\case1.sav'
psspy.case(sav_path)

i = power_flow_operation.fnsl()  # Perform fnsl
print('Iteration number:%s' % psspy.iterat())

bus_df = subsytem_data_retrieval.Bus().df
print bus_df.to_string()
a = 4

ierr = power_flow_data_changing.load(bus_no=201, p_const_power=50, q_const_power=10)

# ierr = psspy.save('*')  # if want to save
"""Next LF"""
ierr = power_flow_operation.fnsl()
print('Iteration number:%s' % psspy.iterat())
bus_df = subsytem_data_retrieval.Bus().df
branch = subsytem_data_retrieval.Branch()
branch_df = branch.df
print bus_df.to_string()
print branch_df.to_string()
b = 4

df = sweep.load_sweep(load_bus_no=401, start_load_mva=1, end_load_mva=319, interval=1, pf=.9)
df.to_excel('op.xlsx')
print('saved in' + 'op.xlsx')
a = 7
