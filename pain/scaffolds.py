import os
from cuisine import text_template, dir_ensure, file_write, mode_local
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
		with mode_local():
			if self.config.get('is_package'):
				root_dir = root_dir + '/' + self.config.get('name')
			for path, files in self.files.iteritems():
				for f in files:
					write_path = '%s%s' % (root_dir, os.path.join(text_template(path, self.config), f.name))
					dir_ensure(os.path.dirname(write_path), recursive=True)
					text = f.template(self.config)
					file_write(write_path, text)

class Default(Scaffold):

	def __init__(self, name, **config):
		super(Default, self).__init__(name, **config)

		self.files = {
			'/': [SetupPy(), SetupCfg(), Requirements(), TODO(), README(), MANIFEST(), TravisYaml(), GitIgnore(), Env()],
			'/$name': [Init()],
			'/$name/tests': [Init()]
		}