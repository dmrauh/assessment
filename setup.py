from setuptools import setup, find_packages

from assessment.main import __version__ as version

with open('README.md', 'r', encoding='utf_8') as fd:
    setup(name='assessment',
          version=version,
          description='The Bewertungsbogen assessment tool.',
          long_description=fd.read(),
          long_description_content_type="text/markdown",
          url='https://git.rz.uni-augsburg.de/oc-m/assessment',
          author='Dominik Rauh',
          author_email='dominik.rauh@informatik.uni-augsburg.de',
          license='Apache License, Version 2.0',
          packages=find_packages(),
          classifiers=[
              'Environment :: Console', 'Operating System :: OS Independent',
              'License :: OSI Approved :: Apache Software License',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.6'
          ],
          python_requires=">=3.6",
          install_requires=['click>=7'],
          entry_points={
              'console_scripts': ['assessment = assessment.main:main']
          })

