from setuptools import setup

setup(
    name = 'emailpy',
    version = '1.0.0',
    description = 'Send emails from the command line',
    author = 'Deepak Nautiyal',
    url = 'https://github.com/nautiyaldeepak/emailpy',
    author_email = 'deepaknautiyal07@outlook.com',
    install_requires = [
        'requests',
    ],
    scripts=['emailpy'],
)