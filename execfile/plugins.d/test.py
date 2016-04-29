#!/usr/bin/python
global menu_entry, onExit


def some_new_option():
    print 'Hi I\'m a new option'

def onExit():
    pass


menu_entry = {
    'advanced_menu': {
        'network': {
            'some_new_option': some_new_option
        }
    }
}
