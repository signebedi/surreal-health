import os
from setuptools import setup, find_packages

def read_version():
    with open('surreal_health/__metadata__.py', 'r') as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]

    raise RuntimeError("Unable to find version string.")

version = read_version()

# Read README for long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements_file = os.getenv('REQUIREMENTS', 'requirements/base.txt')

# Read requirements/base.txt for install_requires
with open(requirements_file, encoding="utf-8") as f:
    install_requires = f.read().splitlines()
    
setup(
    name='surreal_health',
    version=version,
    url='https://github.com/signebedi/surreal-health',
    author='Sig Janoska-Bedi',
    author_email='signe@atreeus.com',
    description='SurrealDB health data modeling ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    # entry_points={
    #     'console_scripts': [
    #         'appctl=surreal_health.cli.__init__:cli',
    #     ],
    # },
)
