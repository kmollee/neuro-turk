from setuptools import setup

setup(name='NeuroTurk', version='0.1',
      description='Neuroscience experiments for Amazon Mechanical Turk',
      author='Alejandro Pulver', author_email='alepulver@gmail.com',
      url='https://github.com/alepulver/neuro-turk',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['WebOb',
                        'Django>=1.5',
                        #  'mysql-connector-python',
                        #  'pymongo',
                        #  'psycopg2',
      ],
     )
