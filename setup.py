import setuptools


setuptools.setup(
     name='demo_package',
     version='0.1',
     description='A demo package',
     packages=setuptools.find_packages(exclude=('unwanted_dir',)),
     classifiers=[
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
     ],
)
