from distutils.core import setup, Extension

module1 = Extension('apng2gif',

					libraries = ['stdc++', 'm', 'png', 'z'],
                    sources = ['APNGLib.cpp'])

setup (name = 'APNG2gif',
       version = '1.0',
       description = 'APNGLib a few tools for working with APNG files',
       ext_modules = [module1])