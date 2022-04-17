import numpy as np
import pandas as pd
import pssepath

pssepath.add_pssepath()
import psspy, redirect


class Bus:
    def __init__(self):
        ierr, bus_no_list = psspy.abusint(string='NUMBER')
        ierr, bus_name_list = psspy.abuschar(string='NAME')
        ierr, bus_area_list = psspy.abusint(string='AREA')
        ierr, volt_pu_mag_list = psspy.abusreal(-1, string='PU')
        ierr, volt_complex_list = psspy.abuscplx(-1, string='VOLTAGE')

        self.df = pd.DataFrame.from_records({
            'NUMBER': bus_no_list[0],
            'NAME': bus_name_list[0],
            'AREA': bus_area_list[0],
            'Voltage Magnitude': volt_pu_mag_list[0],
            'Voltage Phasor': volt_complex_list[0]
        })
        self.df.loc[:, 'Angle(degree)'] = [np.angle(z, deg=True) for z in self.df.loc[:, 'Voltage Phasor']]


class Branch:
    def __init__(self):
        # ierr, number_of_branches = psspy.aflowcount()
        ierr, from_bus_no_list = psspy.aflowint(string='FROMNUMBER')
        ierr, from_bus_name_list = psspy.aflowchar(string='FROMNAME')
        ierr, to_bus_no_list = psspy.aflowint(string='TONUMBER')
        ierr, to_bus_name_list = psspy.aflowchar(string='TONAME')
        ierr, branch_id = psspy.aflowchar(string='ID')

        ierr, amps = psspy.aflowreal(string='AMPS')
        ierr, amps_pu = psspy.aflowreal(string='PUCUR')
        # ierr, loading_amp = psspy.aflowreal(string='PCTRATE')
        # ierr, loading_amp_a = psspy.aflowreal(string='PCTRATEA')
        # ierr, loading_mva = psspy.aflowreal(string='PCTMVARATE')
        ierr, loading_mva_a = psspy.aflowreal(string='PCTMVARATEA')

        # ierr, s = psspy.aflowcplx(string='PQ')
        # ierr, s_loss = psspy.aflowcplx(string='PQ')
        ierr, p = psspy.aflowreal(string='P')
        ierr, q = psspy.aflowreal(string='Q')
        ierr, mva = psspy.aflowreal(string='MVA')
        ierr, p_loss = psspy.aflowreal(string='PLOSS')
        ierr, q_loss = psspy.aflowreal(string='QLOSS')

        b = 3

        self.df = pd.DataFrame.from_records({
            'FROM_BUS_No': from_bus_no_list[0],
            'FROM_BUS_Name': from_bus_name_list[0],
            'TO_BUS_No': to_bus_no_list[0],
            'TO_BUS_Name': to_bus_name_list[0],
            'ID': branch_id[0],
            'AMPS': amps[0],
            'AMPS_PU': amps_pu[0],
            'Loading': loading_mva_a[0],
            'P': p[0],
            'Q': q[0],
            'MVA': mva[0],
            'P_Loss': p_loss[0],
            'Q_Loss': q_loss[0],
        })
        # self.df.loc[:, 'Angle(degree)'] = [np.angle(z, deg=True) for z in self.df.loc[:, 'Voltage Phasor']]