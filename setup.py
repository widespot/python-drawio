from distutils.core import setup

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='python-drawio',
      version='0.1.1',
      description='Draw.io, with Python',
      long_description="long_description",
      author='Raphaël JOIE',
      author_email='info@widespot.be',
      url='https://github.com/widespot/python-drawio/',
      packages=['python_drawio'],
      package_dir={'python_drawio': 'src/python_drawio'},
      )
