from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

package = Extension('parent_updates', ['parent_updates.pyx'], include_dirs=[numpy.get_include()])
setup(ext_modules=cythonize([package]))