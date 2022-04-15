import os
import sys


class InitializePsspy:
    def __init__(self, psse_path=r'C:\Program Files (x86)\PTI\PSSE33\PSSBIN'):
        # psse_path = r'C:\Program Files (x86)\PTI\PSSE33\PSSBIN'
        sys.path.append(psse_path)
        os.environ['PATH'] += ';' + psse_path

        """Importing from PSSE path"""
        import psspy, redirect
        psspy.throwPsseException = True
        self._i = psspy.getdefaultint()  # in place of default integer values, the variable _i is used
        self._f = psspy.getdefaultreal()  # in place of default float values, the variable _f is used.
        self._s = psspy.getdefaultchar()  # in place of default string values (not filenames) the variable _s is used.

        redirect.psse2py()
        psspy.psseinit(10000)  # starting bus size of 100

    @property
    def i(self):
        return self._i
