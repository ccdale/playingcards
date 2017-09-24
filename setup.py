try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Set of classes to represent playing cards in python games',
    'author': 'Chris Allison',
    'url': 'https://github.com/ccdale/playingcards',
    'download_url': 'https://github.com/ccdale/playingcards',
    'author_email': 'chris.charles.allison+playingcards@gmail.com',
    'version': '1.0.2',
    'install_requires': [],
    'packages': ['playingcards'],
    'package_dir': {'playingcards':''},
    'package_data': {'':'img/*.png'},
    'scripts': [],
    'name': 'playingcards'
}
setup(**config)
