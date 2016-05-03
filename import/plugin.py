#!/usr/bin/python
import re
import os
from os.path import basename, dirname, isdir, join, isfile

class PluginError(Exception):
    pass

class Plugin(object):
    ''' Object that holds various information about a `plugin` '''

    def __init__(self, name):
        self.module = getattr(__import__(name), name.split('.')[-1])
        self.description = self.module.__doc__
        self.weight = self.module.WEIGHT
        
    def execute(self):
        self.module.run()

class Plugins(object):
    
    def __init__(self, path):
        self.plugins = []
        
        if not isdir(path):
            raise PluginError('Plugin directory "{}" does not exist!'.format(path))

        for file_name in os.listdir(path):
            file_path = join(path, file_name)
            module_name = '{}.{}'.format(path, file_name)
            if isdir(file_path) and isfile(join(file_path,'__init__.py')):
                self.plugins.append(Plugin(module_name))

        self.plugins = sorted(self.plugins, key = lambda x:x.weight)
            
    def __iter__(self):
        for plugin in self.plugins:
            yield plugin
        

if __name__ == '__main__':
    print 'This plugin implementation uses python modules as plugins.\n'
    for plugin in Plugins('modules'):
        plugin.execute()
