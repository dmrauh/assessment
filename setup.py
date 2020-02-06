from setuptools import setup

import assessment

setup(name='assessment',
      version=assessment.__version__,
      description='The Bewertungsbogen assessment tool.',
      url='https://git.rz.uni-augsburg.de/oc-m/assessment',
      author='Dominik Rauh',
      author_email='dominik.rauh@informatik.uni-augsburg.de',
      license='Apache License, Version 2.0',
      packages=['assessment'],
      classifiers=['Environment :: Console'],
      entry_points={'console_scripts': ['assessment = assessment:main']})
