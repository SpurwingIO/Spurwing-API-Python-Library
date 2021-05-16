from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as build_py_orig

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


class build_py(build_py_orig):
  def find_package_modules(self, package, package_dir):
    modules = super().find_package_modules(package, package_dir)
    included = []
    for (pkg, filename, filepath) in modules:
      if filename in ['config']:
        continue
      included.append((pkg, filename, filepath))
    return included

setup(
   name='Spurwing',
   version='1.0.6',
   author='Ilya Nevolin',
   author_email='ilya@spurwing.io',
   packages=find_packages(),
   cmdclass={'build_py': build_py},
   url='https://github.com/Spurwing/Spurwing-API-Python-Library/',
   license='MIT License (MIT)',
   description='Python Library for Spurwing API',
   long_description=long_description,
   long_description_content_type="text/markdown",
   install_requires=[
       "requests",
   ],
)