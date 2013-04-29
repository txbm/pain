import os, string
from .files import *

''' Abstract scaffold class '''

class Scaffold(object):

	def __init__(self, name, **config):
		self.config = config
		self.config.update(name=name)
		self.config.update(is_package=True)
		self.files = {}

	def add_file(self, path, f):
		if path not in self.files:
			self.files[path] = []
		self.files[path].append(f)

	def write(self, root_dir):
		if self.config.get('is_package'):
			root_dir = os.path.join(root_dir, self.config.get('name'))
		for path, files in self.files.iteritems():
				for f in files:
					write_path = '%s%s' % (root_dir, os.path.join(string.Template(path).safe_substitute(**self.config), f.name))
					if not os.path.exists(os.path.dirname(write_path)):
						os.makedirs(os.path.dirname(write_path))
					text = f.template(self.config)
					with open(write_path, 'w+') as f:
						f.write(text)

class Default(Scaffold):

	def __init__(self, name, **config):
		super(Default, self).__init__(name, **config)

		self.files = {
			'/': [SetupPy(), SetupCfg(), Requirements(), TODO(), README(), MANIFEST(), TravisYaml(), GitIgnore(), Env()],
			'/$name': [Init()],
			'/$name/tests': [Init()]
		}