import psse_utils
import pandas as pd
import numpy as np
import power_flow_operation, subsytem_data_retrieval, power_flow_data_changing

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

"""Varying Branch Load"""
start_load_mva = 5
end_load_mva = 143
interval = 1
pf = .9
load_bus_no = 201

output_df = pd.DataFrame(columns=['branch_loss'])

for load_mva in range(start_load_mva, end_load_mva, interval):
    p = load_mva * pf
    q = (load_mva**2 - p**2)**0.5 if load_mva else 0
    ierr = power_flow_data_changing.load(bus_no=load_bus_no, p_const_power=p, q_const_power=q)

    """Run load flow"""
    i = power_flow_operation.fnsl()  # Perform fnsl
    print('Iteration number:%s' % psspy.iterat())
    bus_df = subsytem_data_retrieval.Bus().df
    branch_df = subsytem_data_retrieval.Branch().df

    branch_loss = branch_df[branch_df['FROM_BUS_No'] == load_bus_no].loc[:, 'P_Loss']
    output_df.loc[load_mva, 'branch_loss'] = branch_loss.values[0]
    b = 5
a = 9
output_df.to_excel()