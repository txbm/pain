import argparse, string, os
from fabric import *
from cuisine import *

def make_project(name, *files, **kwargs):
	project_path = '%s/%s' % (os.getcwd(), name)
	with mode_local():
		dir_ensure(project_path)
	for f in files:
		f(project_path, **kwargs)

def make_file(path, text, **kwargs):
	text = text_template(text, kwargs)
	with mode_local():
		file_write(path, text)

def parse_command(command):
	if command.command == 'inflict': pass

def main():
	parser = argparse.ArgumentParser(description='The CLI interface for managing your pain.')
	subs = parser.add_subparsers(dest='command')
	inflict = subs.add_parser('inflict')
	inflict.add_argument('template')
	cli_input = parser.parse_args()
	parse_command(cli_input)