from setuptools import setup

# python setup.py bdist_wheel

setup(
    name='bot_lib_public',
    version='2.0.0',
    packages=['package'],
    url='https://github.com/fahim-programmer/bot-lib-public/',
    license='Apache-2.0 license',
    author='Fahim Chohan',
    description='Wrapper for Selenium and contains supporting classes for browser automation',
    install_requires=[
        'selenium>=4.8.0',
        'requests>=2.27.0'
    ],
    classifiers=[
        'License :: Apache-2.0 license',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Release 22-July-2023'
    ]
)