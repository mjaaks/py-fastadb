from setuptools import setup, find_packages

setup(
    name='py-fastadb',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Mjaaks',
    description='Python wrapper for adb & fastboot',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mjaaks/py-fastadb',
)