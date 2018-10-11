from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name = 'emailpy',
    version = '1.0.0',
    description = 'Send emails from the command line',
    long_description = long_description,
    author = 'Deepak Nautiyal',
    url = 'https://github.com/nautiyaldeepak/emailpy',
    author_email = 'deepaknautiyal07@outlook.com',
    install_requires = [
        'requests',
    ],
    scripts=['emailpy'],
)