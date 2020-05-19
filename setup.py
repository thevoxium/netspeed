from setuptools import setup

setup(
    name='netspeed',
    version='0.1',
    py_modules=['netspeed'],
    install_requires=[
        'Click',
        'pyspeedtest'
    ],
    entry_points='''
        [console_scripts]
        netspeed=netspeed:cli
    ''',
)
