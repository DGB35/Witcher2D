from distutils.core import setup
import py2exe

setup(
    name='game',
    version='0.1.0',
    description='Simple python game',
    author='DGB',
    author_email='grobovoydgb@gmail.com',
    requirments=[
        'pygame==1.9.1release',
        'enum34',
        'py2exe',
    ],
    console=['main.py']
)
