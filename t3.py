import psse_utils
import pandas as pd
import numpy as np
import power_flow_operation, subsytem_data_retrieval, power_flow_data_changing

P = psse_utils.InitializePsspy()

import psspy  # Must be imported after Initializing PSSPY, may show false error

sav_path = r'D:\My Drive\my_works\PSSE\Coductor Loading Profile\case1.sav'
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
print bus_df.to_string()
b = 4
