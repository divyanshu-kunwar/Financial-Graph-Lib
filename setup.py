import setuptools
  
  
# specify requirements of your package here
REQUIREMENTS = ['pandas','numpy','matplotlib']
  
# some more details
CLASSIFIERS = [
    'Development Status :: Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    ]
  
# calling the setup function 
setuptools.setup(name='Financial Graph Lib',
      version='1.0.0',
      description='Financial graph lib for different stock market graph',
      url='https://github.com/kUNWAR-DIVYANSHU/Financial-Graph-Lib',
      author='Homofabers Stock Devs',
      author_email='kdivyanshu3@gmail.com',
      license='MIT',
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='finance graph stocks analysis line area baseline candle hollow hollowcandle renko'
      +' pnf point and figure',
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      python_requires=">=3.6",
      )