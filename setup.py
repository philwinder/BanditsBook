from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='banditsbook',  # Required
    version='0.1.0',  # Required
    description='Python code from the book Bandit Algorithms for Website Optimization',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/philwinder/BanditsBook',  # Optional
    author='Phil Winder',  # Optional
    author_email='phil@WinderResearch.com',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='rl bandits abtesting',  # Optional
    packages=find_packages(where="python", exclude=["Package.egg_info", ]),
    package_dir={'': 'python'},
    python_requires='>=3.5',
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/philwinder/BanditsBook/issues',
        'Source': 'https://github.com/philwinder/BanditsBook/',
    },
)
