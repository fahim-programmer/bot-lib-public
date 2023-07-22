from setuptools import setup

# Build a Wheel Using this python setup.py bdist_wheel

LONG_DESCRIPTION = 'bot-lib-public is a Python library aimed at simplifying the creation of web bots for data extraction from dynamic HTML websites. Leveraging the power of Selenium, the library enables developers to swiftly and accurately interact with dynamic content, facilitating efficient data retrieval.'

setup(
    name='bot_lib_public',
    version='2.0.0',
    packages=['bot_lib'],
    url='https://github.com/fahim-programmer/bot-lib-public/',
    license='Apache-2.0 license',
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    author='Fahim Chohan',
    platforms=['Windows', 'MacOS', 'Linux'],
    description='Wrapper for Selenium and contains supporting classes for browser automation',
    install_requires=[
        'selenium==4.8.0',
        'requests==2.27.0',
        'Pillow==10.0.0',
        'PySocks==1.7.1',
        'numpy==1.25.1'
    ],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)