from distutils.core import setup
setup(
  name = 'clockpy',
  packages = ['clockpy'],
  version = '0.3',
  license='MIT',
  description = 'A library that enables you an easy way to verify your code time consumption',
  author = 'Altieres Schincariol Netto',
  author_email = 'altnetto@gmail.com',
  url = 'https://github.com/altnetto/clockpy',
  download_url = 'https://github.com/altnetto/clockpy/archive/refs/tags/0.3.tar.gz',
  keywords = ['PYTHON', 'TIME', 'CALCULATION', 'PERFORMANCE'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
