import pandas as pd

import power_flow_data_changing
import power_flow_operation
import subsytem_data_retrieval
import pssepath

pssepath.add_pssepath()
"""Importing from PSSE path"""
import psspy


def load_sweep(load_bus_no, start_load_mva, end_load_mva, interval=1, pf=.9):
    """Varying Branch Load"""
    output_df = pd.DataFrame(columns=['p_loss'])

    for load_mva in range(start_load_mva, end_load_mva, interval):
        p = load_mva * pf
        q = (load_mva**2 - p**2)**0.5 if load_mva else 0.00000000001
        ierr = power_flow_data_changing.load(bus_no=load_bus_no, p_const_power=p, q_const_power=q)

        """Run load flow"""
        i = power_flow_operation.fnsl()  # Perform fnsl
        print('Iteration number:%s' % psspy.iterat())
        # bus_df = subsytem_data_retrieval.Bus().df
        if not i:
            branch_df = subsytem_data_retrieval.Branch().df
            branch_loss = branch_df[branch_df['FROM_BUS_No'] == load_bus_no].loc[:, 'P_Loss']
            output_df.loc[load_mva, 'p_loss'] = float(branch_loss.values[0])
            a = 0
    return output_df


a = 9