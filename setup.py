# flake8: noqa
import os
from setuptools import setup, Extension, find_packages


here = os.path.abspath(os.path.dirname(__file__))
# Get the long description from the README file
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()


if os.name == 'nt':
    extra_compile_args = ["-Ox"]
else:
    extra_compile_args = ['-std=c++0x', '-pthread', '-O3']

original_ext = Extension('topn.topn',
                         sources=[
                                    './topn/topn.pyx',
                                    './topn/topn_source.cpp'
                                ],
                         extra_compile_args=extra_compile_args,
                         language='c++')

threaded_ext = Extension('topn.topn_threaded',
                         sources=[
                             './topn/topn_threaded.pyx',
                             './topn/topn_parallel.cpp'],
                         extra_compile_args=extra_compile_args,
                         language='c++')


setup(
    name='topn',
    version='0.0.8',
    description='This package boosts a group-wise nlargest sort',
    keywords='nlargest hstack csr csc scipy cython',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ParticularMiner/topn',
    download_url='https://github.com/ParticularMiner/topn/archive/refs/tags/v0.0.7.tar.gz',
    author='Particular Miner', 
    author_email='particularminer@fake.com',
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    ext_modules=[original_ext, threaded_ext],
    package_data = {
        'topn': ['./topn/*.pxd']
    },
    include_package_data=True,    
)
