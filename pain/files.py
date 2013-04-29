import string
''' Abstract File Class '''

class File(object):

	def __init__(self, name):
		self.name = name
		self.content = ''

	def template(self, values):
		return string.Template(self.content).safe_substitute(**values)

class SetupPy(File):

	def __init__(self):
		super(SetupPy, self).__init__('setup.py')
		self.content = '''
			from setuptools import setup, find_packages
			
			setup(
				name='$name',
				version='0.1',
				description='$description',
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
class SetupCfg(File):

	def __init__(self):
		super(SetupCfg, self).__init__('setup.cfg')
		self.content = ''

class Requirements(File):

	def __init__(self):
		super(Requirements, self).__init__('requirements.txt')
		self.content = ''

class TODO(File):

	def __init__(self):
		super(TODO, self).__init__('TODO.md')
		self.content = ''

class README(File):

	def __init__(self):
		super(README, self).__init__('README.md')
		self.content = ''

class MANIFEST(File):

	def __init__(self):
		super(MANIFEST, self).__init__('MANIFEST.in')
		self.content = ''

class TravisYaml(File):

	def __init__(self):
		super(TravisYaml, self).__init__('.travis-yml')
		self.content = ''

class GitIgnore(File):

	def __init__(self):
		super(GitIgnore, self).__init__('.gitignore')
		self.content = '''
			*.py[cod]
			.env
			# C extensions
			*.so

			# Packages
			*.egg
			*.egg-info
			dist
			build
			eggs
			parts
			bin
			var
			sdist
			develop-eggs
			.installed.cfg
			lib
			lib64

			# Installer logs
			pip-log.txt

			# Unit test / coverage reports
			.coverage
			.tox
			nosetests.xml

			# Translations
			*.mo

			# Mr Developer
			.mr.developer.cfg
			.project
			.pydevproject
		'''
class Env(File):

	def __init__(self):
		super(Env, self).__init__('.env')
		self.content = '''
			use_env $name
		'''

class Init(File):

	def __init__(self):
		super(Init, self).__init__('__init__.py')
		self.content = ''