#!/usr/bin/env python

from setuptools import setup

setup(
    name='PynPoint',
    version='0.5.3',
    description='Pipeline for processing and analysis of high-contrast imaging data',
    long_description=open('README.rst').read(),
    author='Tomas Stolker, Markus Bonse, Sascha Quanz, and Adam Amara',
    author_email='tomas.stolker@phys.ethz.ch',
    url='http://pynpoint.ethz.ch',
    packages=['PynPoint',
              'PynPoint.Core',
              'PynPoint.IOmodules',
              'PynPoint.ProcessingModules',
              'PynPoint.Util'],
    package_dir={'PynPoint': 'PynPoint'},
    include_package_data=True,
    install_requires=['configparser==3.5.0',
                      'h5py==2.6.0',
                      'numpy==1.15.4',
                      'numba==0.40.1',
                      'scipy==1.1.0',
                      'astropy==2.0.9',
                      'photutils==0.4.1',
                      'scikit-image==0.14.1',
                      'scikit-learn==0.20.0',
                      'opencv-python==3.4.3.18',
                      'statsmodels==0.9.0',
                      'PyWavelets==1.0.1',
                      'matplotlib==2.2.3',
                      'emcee==2.2.1',
                      'ephem==3.7.6.0'],
    license='GPLv3',
    zip_safe=False,
    keywords='PynPoint',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    tests_require=['pytest'],
)
