import psse_utils
import pandas as pd
import numpy as np

P = psse_utils.InitializePsspy()

import psspy  # Must be imported after Initializing PSSPY, may show false error

sav_path = r'D:\My Drive\my_works\PSSE\test_3_bus_line_close.sav'
psspy.case(sav_path)
psspy.fnsl([
    0,  # tap adjustment flag
    0,  # area interchange adjustment flag
    0,  # phase shift adjustment flag
    1,  # dc tap adjustment flag
    1,  # switched shunt adjustment flag
    1,  # flat start flag
    99,  # var limit flag
    0,  # non-divergent solution flag
])
print('Iteration number:%s' % psspy.iterat())
# psspy.read(0, r"""C:\Users\hE\Downloads\IEEE 14 bus.raw""")
# psspy.fnsl([0, 0, 0, 1, 1, 1, 99, 0])
a = 5
ierr, bus_no_list = psspy.abusint(string='NUMBER')
ierr, bus_name_list = psspy.abuschar(string='NAME')
ierr, bus_area_list = psspy.abusint(string='AREA')
b = 4
ierr, volt_pu_mag_list = psspy.abusreal(-1, string='PU')
ierr, volt_complex_list = psspy.abuscplx(-1, string='VOLTAGE')
c = 5
df = pd.DataFrame.from_records({
    'NUMBER': bus_no_list[0],
    'NAME': bus_name_list[0],
    'AREA': bus_area_list[0],
    'Voltage Magnitude': volt_pu_mag_list[0],
    'Voltage Phasor': volt_complex_list[0]
})
# h = help(psspy)
# h1 = str(h)
# with open('PSSPY Reference.txt', 'w') as txt_file:
#     txt_file.write(h1)
df.loc[:, 'Angle(degree)'] = [np.angle(z, deg=True) for z in df.loc[:, 'Voltage Phasor']]
print df.to_string()
a = 4

# open line with CB
ierr = psspy.branch_chng(201, 302, r"""@1""", [1, P._i, P._i, P._i, P._i, P._i],
                         [P._f, P._f, P._f, P._f, P._f, P._f, P._f, P._f, P._f, P._f, P._f, P._f, P._f,
                          P._f, P._f])
# ierr = psspy.save('*')  # if want to save
"""Next LF"""
# psspy.fnsl([
#     0,  # tap adjustment flag
#     0,  # area interchange adjustment flag
#     0,  # phase shift adjustment flag
#     1,  # dc tap adjustment flag
#     1,  # switched shunt adjustment flag
#     1,  # flat start flag
#     99,  # var limit flag
#     0,  # non-divergent solution flag
# ])
# psspy.psseinit(1000)
# sav_path = r'G:\My Drive\my_works\PSSE\test_3_bus_line_close.sav'
# psspy.case(sav_path)
psspy.fnsl([0, 0, 0, 1, 1, 0, 99, 0])
# psspy.lout(0,1)
print('Iteration number:%s' % psspy.iterat())
# psspy.read(0, r"""C:\Users\hE\Downloads\IEEE 14 bus.raw""")
# psspy.fnsl([0, 0, 0, 1, 1, 1, 99, 0])
a = 5
ierr, bus_no_list = psspy.abusint(string='NUMBER')
ierr, bus_name_list = psspy.abuschar(string='NAME')
ierr, bus_area_list = psspy.abusint(string='AREA')
b = 4
ierr, volt_pu_mag_list = psspy.abusreal(-1, string='PU')
ierr, volt_complex_list = psspy.abuscplx(-1, string='VOLTAGE')
c = 5
df1 = pd.DataFrame.from_records({
    'NUMBER': bus_no_list[0],
    'NAME': bus_name_list[0],
    'AREA': bus_area_list[0],
    'Voltage Magnitude': volt_pu_mag_list[0],
    'Voltage Phasor': volt_complex_list[0]
})
# h = help(psspy)
# h1 = str(h)
# with open('PSSPY Reference.txt', 'w') as txt_file:
#     txt_file.write(h1)
df1.loc[:, 'Angle(degree)'] = [np.angle(z, deg=True) for z in df1.loc[:, 'Voltage Phasor']]
print df1.to_string()
b = 4