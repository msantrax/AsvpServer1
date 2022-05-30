import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()

setup(
    name='asvp',
    version='0.6',
    license='MIT license',
    url='https://anfitria.dev:8443/asvp',

    packages=find_packages('asvp'),
    package_dir={'': 'asvp'},
    py_modules=[splitext(basename(path))[0] for path in glob('asvp/*.py')],
    include_package_data=True,
    zip_safe=False,

    author='Opus Equipamentos Ltda.',
    author_email='msantrax@gmail.com',
    description='Servidor de calculo asvp',

    keywords=[
        'adsorption', 'science', 'porous materials'
    ],
    setup_requires=[

    ],
    install_requires=[
        'numpy >= 1.13',
        'scipy >= 1.0.0',
        'pandas >= 0.21.1',
        'matplotlib >= 2.1',
        'xlrd >= 1.1',
        'xlwt >= 1.3',
        'coolprop >= 6.0',
    ],
    tests_require=[

    ],
    extras_require={
        'reST': [
            'docutils>=0.11'
            'doc9',
            'pandoc',
            'restructuredtext-lint',
        ],
    },


)
