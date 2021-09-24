from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

package = Extension('continuous_time_helpers', ['continuous_time_helpers.pyx'], include_dirs=[numpy.get_include()])
setup(ext_modules=cythonize([package]))