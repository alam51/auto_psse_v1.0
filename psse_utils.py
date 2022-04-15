import os
import sys
import pssepath


# class InitializePsspy:
#     def __init__(self, psse_path=r'C:\Program Files (x86)\PTI\PSSE33\PSSBIN'):
#         # psse_path = r'C:\Program Files (x86)\PTI\PSSE33\PSSBIN'
#         sys.path.append(psse_path)
#         os.environ['PATH'] += ';' + psse_path
#
#         """Importing from PSSE path"""
#         import psspy, redirect
#         psspy.throwPsseException = True
#         self.i = psspy.getdefaultint()  # in place of default integer values, the variable i is used
#         self.f = psspy.getdefaultreal()  # in place of default float values, the variable f is used.
#         self.s = psspy.getdefaultchar()  # in place of default string values (not filenames) the variable s is used.
#
#         redirect.psse2py()
#         psspy.psseinit(10000)  # starting bus size of 100


class InitializePsspy:
    def __init__(self):
        # psse_path = r'C:\Program Files (x86)\PTI\PSSE33\PSSBIN'
        pssepath.add_pssepath()

        """Importing from PSSE path"""
        import psspy, redirect
        psspy.throwPsseException = True
        self.i = psspy.getdefaultint()  # in place of default integer values, the variable i is used
        self.f = psspy.getdefaultreal()  # in place of default float values, the variable f is used.
        self.s = psspy.getdefaultchar()  # in place of default string values (not filenames) the variable s is used.

        redirect.psse2py()
        psspy.psseinit(10000)  # starting bus size of 100
