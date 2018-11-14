from setuptools import setup, find_packages

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='messanger',
	description='Free SMS API',
	version='1.0',
	install_requires=(
		'requests',
		'lxml',
	),
	author='Yash Pokar',
	author_email='hello@yashpokar.com',
	packages=find_packages(),
	long_description=long_description,
	long_description_content_type="text/markdown",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
)
