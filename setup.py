
from os.path import join, dirname
from setuptools import setup


setup(
    name='bibjeeves',
    version='0.0.0',

    description='a research paper reference tree manager',
    long_description=open(join(dirname(__file__), 'README.md')).read(),

    packages=[
        'bibjeeves',
    ],

    entry_points={
        'console_scripts': [
            'bibjeeves = bibjeeves.__main__:main'
        ]
    },

    install_requires=[
        'sqlalchemy',
        'requests',
    ],

    test_suite='tests',
    tests_require=[
        'pytest',
    ],

    setup_requires=['pytest_runner'],
)
