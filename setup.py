from setuptools import setup

setup(
        name='assessment',
        version='1.0.0'.
        py_modules=['assessment'],
        install_requires=[
            'click',
            'pprint'
        ],
        entry_points'''
            [console_scripts]
            assessment=assessment:main
        ''',
        )
