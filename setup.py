# setup.py

from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[],  # List your package dependencies here
    url='https://github.com/abhineshkr/mylibrary',
    author='Your Name',
    author_email='yourname@example.com',
    description='A simple example library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT'
)
