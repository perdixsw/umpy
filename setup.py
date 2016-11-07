#! /usr/bin/env python
from setuptools import setup

setup(
	name='umpy',
	packages=['umpy',],
	version='0.1.0',
	url='https://www.github.com/perdixsw/umpy',
	download_url='https://www.github.com/perdixsw/umpy/tarball/0.1.0',
	author='Perdix Software',
	author_email='ssmith@perdixsw.com',
	description=('Simple unit of measure conversion for python, optimized for manufacturing contexts.'),
	license='MIT',
	include_package_data=True,
	zip_safe=False,
	install_requires=[],
	keywords=['units', 'measure', 'measurement', 'conversion', 'converter',],
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: Office/Business :: Financial',
		'Topic :: Scientific/Engineering :: Mathematics',
	],
)
