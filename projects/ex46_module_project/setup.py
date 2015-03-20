try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Package written for Ex 46 in LPTHW.',
    'author': 'Amelia Lin',
    'url': 'No URL',
    'download_url': 'No URL',
    'author_email': 'amelia.lin0@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex46_module'],
    'scripts': ['bin/counttoten'],
    'name': 'ex46_module_project'
}

setup(**config) # uses the config dict that we just defined above