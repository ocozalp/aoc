from distutils.core import setup, Extension
setup(name='shortcuts', version='1.0', ext_modules=[Extension('shortcuts', ['shortcuts.c'])])