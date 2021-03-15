from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
   name='Spurwing',
   version='1.0.0',
   author='Ilya Nevolin',
   author_email='ilya@spurwing.io',
   packages=['spurwing', 'spurwing.tests'],
   url='',
   license='MIT License (MIT)',
   description='Python Library for Spurwing API',
   long_description=long_description,
   long_description_content_type="text/markdown",
   install_requires=[
       "requests",
   ],
)