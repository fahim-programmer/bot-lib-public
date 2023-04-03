from setuptools import setup

# python setup.py bdist_wheel

setup(
    name='bot_lib_public',
    version='1.0.1',
    packages=['package'],
    url='https://github.com/fahim-programmer/bot-lib-public/',
    license='Apache-2.0 license',
    author='Fahim Chohan',
    description='Wrapper for Selenium and contains supporting classes',
    install_requires=[
        'selenium>=4.8.0',
        'requests>=2.27.0'
    ],
)