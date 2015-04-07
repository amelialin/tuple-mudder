try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'PROJECT NAME',
    'author': 'Amelia Lin',
    'url': 'URL TO GET IT AT'
    'download_url': 'WHERE TO DOWNLOAD',
    'author_email': 'amelia.lin0@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': ['bin/SCRIPTNAME'],
    'name': 'projectname'
}

setup(**config) # uses the config dict that we just defined above