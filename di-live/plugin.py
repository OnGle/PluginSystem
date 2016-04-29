#!/usr/bin/python
import re
import os
from os.path import basename, dirname, isdir, join

class PluginError(Exception):
    pass

class Plugin(object):
    ''' Object that holds various information about a `plugin` '''

    def __init__(self, path):
        
        self.path = path
        self.name = re.sub('^[\d]*', '', basename(path))
        self.exitcode = None

    def execute(self):
        error = os.system(self.path)
        if error:
            self.exitcode = os.WEXITSTATUS(error)
            return False
        self.exitcode = 0
        return True

class Plugins(object):
    def __init__(self, path):
        self.plugins = []

        if not isdir(path):
            raise PluginError('Plugin directory "{}" does not exist!'.format(dirname(path)))

        for file_name in os.listdir(path):
            file_path = join(path, file_name)

            if not os.stat(file_path).st_mode & 0111 == 0:
                self.plugins.append(Plugin(file_path))

    def __iter__(self):
        for plugin in self.plugins:
            yield plugin

if __name__ == '__main__':
    print 'This plugin implementation uses os.system to run executable scripts as `plugins` so restrictions on program structure are minimal however effeciently sharing data could be hard, complex models would most likely want to be defined in some common file such as common.py like in di-live.\n'

    plugins = Plugins('plugins.d')
    for plugin in plugins:
        plugin.execute()
