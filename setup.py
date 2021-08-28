from setuptools import setup
  
  
# specify requirements of your package here
REQUIREMENTS = ['pandas','numpy','matplotlib']
  
# some more details
CLASSIFIERS = [
    'Development Status :: Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    ]
  
# calling the setup function 
setup(name='Financial Graph Lib',
      version='1.0.0',
      description='Financial graph lib for different stock market graph',
      url='',
      author='Homofabers Stock Devs',
      author_email='kdivyanshu3@gmail.com',
      license='MIT',
      packages=['lib'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='finance graph stocks analysis line area baseline candle hollow hollowcandle renko'
      +' pnf point and figure'
      )