import setuptools
from setuptools import setup
from setuptools import find_packages

pkg_location = 'src'
pkg_name     = 'lib'
  
# specify requirements of your package here
REQUIREMENTS = ['pandas','numpy','matplotlib']
  
# some more details
CLASSIFIERS=['Development Status :: 3 - Alpha',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Framework :: Matplotlib',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Education',
                   'Intended Audience :: Financial and Insurance Industry',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: BSD License',
                   'Topic :: Office/Business :: Financial',
                   'Topic :: Office/Business :: Financial :: Investment',
                   'Topic :: Scientific/Engineering :: Visualization',
                   'Topic :: Scientific/Engineering :: Information Analysis',
                   ],
  
# calling the setup function 
setup(name='Financial Graph Lib',
      version='1.0.1',
      description='Financial graph lib for different stock market graph',
      url='https://github.com/kUNWAR-DIVYANSHU/Financial-Graph-Lib',
      author='Homofabers Stock Devs',
      author_email='kdivyanshu3@gmail.com',
      license='MIT',
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      py_modules=["fglib"],
      keywords='finance graph stocks analysis line area baseline candle hollow hollowcandle renko'
      +' pnf point and figure',
      package_dir={"": "src"},
      packages=find_packages(where="src"),
      python_requires=">=3.6",
      )