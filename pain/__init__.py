import argparse, string, os
from fabric import *
from cuisine import *

from . import scaffolds

class File(object):

	def __init__(self, name):
		self.name = name
		self.content = ''

	def template(self, values):
		return text_template(self.content, values)

class Scaffold(object):

	def __init__(self, name, **config):
		self.config = config
		self.config.update(name=name)
		self.files = {}

	def add_file(self, path, f):
		if path not in self.files:
			self.files[path] = []
		self.files[path].append(f)

	def write(self, root_dir):
		for path, f in self.files.iteritems():
			write_path = os.path.join(root_dir, text_template(path, self.config))
			text = f.template(self.config)
			dir_ensure(os.path.dirname(write_path))
			file_write(write_path, text)

def parse_command(command):
	if command.command == 'new':
		root_path = os.getcwd()
		if command.template:
			scaffold = getattr(scaffolds, ucfirst(command.template))
			if not scaffold:
				raise RuntimeError('Specified scaffold not found.')
		else:
			scaffold = scaffolds.Default
		s = scaffold()
		s.write(root_path)

def main():
	parser = argparse.ArgumentParser(description='The CLI interface for managing your pain.')
	subs = parser.add_subparsers(dest='command')
	new = subs.add_parser('new')
	new.add_argument('name')
	new.add_argument('-t', '--template')
	new.add_argument('-c', '--config', help='Specify a config file to read in default information.')
	cli_input = parser.parse_args()
	return parse_command(cli_input)