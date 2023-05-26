from distutils.util import convert_path
from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

main_ns = {}
ver_path = convert_path('bpython/__init__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)


setup(
  name="dspython",
  version=main_ns['__version__'],
  packages=find_packages(),
  description = 'Python library with tools for the book.',
  author = 'Miquel Perello Nieto',
  long_description=long_description,
  long_description_content_type='text/markdown'
)
