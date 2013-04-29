import argparse, os
from . import scaffolds

def parse_command(command):
	if command.command == 'new':
		root_path = os.path.abspath(os.getcwd())
		if command.template:
			scaffold = getattr(scaffolds, ucfirst(command.template))
			if not scaffold:
				raise RuntimeError('Specified scaffold not found.')
		else:
			scaffold = scaffolds.Default
		s = scaffold(command.name)
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