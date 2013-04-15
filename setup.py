from setuptools import setup, find_packages

setup(name='pain',
      version='0.1',
      description='A scaffolding tool to mitigate the pain of setting up a new project.',
      classifiers=[
      'Development Status :: 1 - Alpha',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Programming Language :: Python'
      ],
      keywords='scaffolding scaffold python setup project new',
      author='Peter M. Elias',
      author_email='petermelias@gmail.com',
      url='http://github.com/petermelias/pain',
      license='FreeBSD',
      packages=find_packages(),
      include_package_data=True,
      test_suite = "nose.collector",
      zip_safe=False,
      entry_points = {
        'console_scripts': [ 'pain = pain:main' ]
      }
)