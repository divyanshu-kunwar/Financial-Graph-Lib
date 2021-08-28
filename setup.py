import setuptools
from setuptools import setup
from setuptools import find_packages

pkg_location = 'src'
pkg_name     = 'lib'
  
# specify requirements of your package here
REQUIREMENTS = ['pandas','numpy','matplotlib']
  
# calling the setup function 
setup(name='Financial Graph Lib',
      version='1.0.4',
      description='Financial graph lib for different stock market graph',
      url='https://github.com/kUNWAR-DIVYANSHU/Financial-Graph-Lib',
      author='Homofabers Stock Devs',
      author_email='kdivyanshu3@gmail.com',
      license='MIT',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      install_requires=REQUIREMENTS,
      py_modules=["fglib"],
      keywords='finance graph stocks analysis line area baseline candle hollow hollowcandle renko'
      +' pnf point and figure',
      package_dir={"": "src"},
      packages=find_packages(where="src"),
      python_requires=">=3.6",
      )