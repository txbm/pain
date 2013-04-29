from . import Scaffold
from .files import *

class Default(Scaffold):

	def __init__(self):
		super(Default, self).__init__('default')

		self.files = {
			'/': [SetupPy(), SetupCfg(), Requirements(), TODO(), README(), MANIFEST(), TravisYaml(), GitIgnore(), Env()],
			'/$name': [Init()],
			'/$name/tests': [Init()]
		}