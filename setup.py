from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt')) as f:
    reqs = f.read().split()

with open(path.join(here, 'README.md')) as f:
    readme = f.read()

with open(path.join(here, 'mastermind', 'version')) as f:
    version = f.read().strip()

setup(
    name='open_mastermind',
    version=version,
    description='A terminal-based code-breaking game Mastermind',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/philshem/open-mastermind',
    author='Philip Shemella',
    author_email='philshem@pm.me',
    classifiers=[
        'Environment :: Console :: Curses',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment :: Puzzle Games',
    ],
    packages=find_packages(),
    python_requires='>=2.7',
    install_requires=reqs,
    package_data={
        'open_mastermind': ['version']
    },
    entry_points={
        'console_scripts': [
            'mastermind=mastermind:main',
        ],
    },
    keywords='puz mastermind code-breaking puzzle game'
)
