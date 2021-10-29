#! /usr/bin/env python
from setuptools import setup

setup(
	name='umpy',
	packages=['umpy',],
	version='0.9.9',
	url='https://www.github.com/perdixsw/umpy',
	download_url='https://www.github.com/perdixsw/umpy/tarball/master',
	author='Perdix Software',
	author_email='ssmith@perdixsw.com',
	description=('Simple unit of measure conversion for python, optimized for manufacturing contexts.'),
	license='MIT',
	include_package_data=True,
	zip_safe=False,
	install_requires=[],
	keywords=['units', 'measure', 'measurement', 'conversion', 'converter', 'manufacturing',],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Office/Business :: Financial',
		'Topic :: Scientific/Engineering :: Mathematics',
		'Topic :: Manufacturing',
	],
)
