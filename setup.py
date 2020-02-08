# Copyright 2020 Dominik Michael Rauh. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup, find_packages

from assessment import __version__ as version

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
              'console_scripts': ['assessment = assessment:main']
          })

