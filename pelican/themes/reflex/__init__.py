'''
Reflex theme for Pelican static site generator
'''

from importlib.resources import files


def path():
    '''
    Return path to theme templates and assets.
    Use this as value for THEME in Pelican settings.
    '''
    return str(files(__name__))
