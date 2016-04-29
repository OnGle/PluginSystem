#!/usr/bin/python
import os
from os.path import basename, dirname, isdir, join
from json import dumps

def dict_merge(x, y, path = []):
    for k in y:
        if k in x:
            if isinstance(x[k], dict) and isinstance(y[k], dict):
                dict_merge(x[k], y[k], path + [k])
            else:
                # NOTE THIS LINE COULD CAUSE ISSUES
                x[k] = y[k]
        else:
            x[k] = y[k]
    return x

class PluginError(Exception):
    pass

class Plugin(object):
    ''' Object that holds various information about a `plugin` '''

    def __init__(self, path):

        self.path = path
        self.name = basename(path)
        self._globals = {'__builtins__': __builtins__}
        self._locals = {}

        execfile(self.path, self._globals, self._locals)
        
        if self._globals.has_key('menu_entry'):
            self.menu_entry = self._globals['menu_entry']
        else:
            self.menu_entry = {}

        if self._globals.has_key('onExit'):
            self.onExit = self._globals['onExit']
        else:
            self.onExit = lambda:None

class Plugins(object):
    def __init__(self, path):
        self.plugins = []

        if not isdir(path):
            raise PluginError('Plugin directory "{}" does not exist!'.format(dirname(path)))

        for file_name in os.listdir(path):
            file_path = join(path, file_name)
            
            if not os.stat(file_path).st_mode & 0111 == 0:
                self.plugins.append(Plugin(file_path))

    def build_menu_entry(self):
        menu = {}
        for plugin in self.plugins:
            if plugin.menu_entry:
                menu = dict_merge(menu, plugin.menu_entry)
    
        return menu    

if __name__ == '__main__':
    print 'This plugin implementation uses execfile and controlled environments to load plugin data into the main program\n'

    plugins = Plugins('plugins.d')
    print dumps(plugins.build_menu_entry(), indent=4, default=str)
