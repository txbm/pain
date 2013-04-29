from . import make_file

def setup_py(root_dir, path='/', name='setup.py', **kwargs):
	string = '''
		from setuptools import setup, find_packages

		setup(
			name='$name',
			version='0.1',
			description=$description,
			classifiers=[],
			keywords='',
			author='$author',
			author_email='$author_email',
			url='$url',
			license='$license',
			packages=find_packages(),
			include_package_data=True,
			test_suite='nose.collector',
			zip_safe=False,
		)
	'''

	make_file('%s/%s/%s' % (root_dir, path, name), string, **kwargs)

def setup_cfg(root_dir, path='/', name='setup.cfg', **kwargs):
	string = ''
	make_file('%s')