Plugin System
=============

A `plugin system` for lack of a better term to be used as a basis for confconsole's
new modular advanced menu.

The `plugin system` is a more generic version of what's used in di-live.



Methods
-------

- Di-live method, the di-live method is pretty much as follows.
    1. Get a directory and find all the executable files inside it.
    2. Execute each file in order.

  It's pretty simple and effective but since it does not import or
  execute the file using exec or execfile, it has no control over the
  plugins environment and therefor using complex models in between
  plugins could be difficult.

  A possible solution to this issue to some extent is to pass data
  through commandline or into config files each plugin could load.

  The other problem is there's no way to do a callback without perhaps
  making the plugin directory a subdirectory of the plugin framework
  and make all directories in between python packages (adding a __init__.py)
  then using relative imports to access the original file. This however
  would be cause circular references and break pythons garbage collection
  unless it was implemented in a clever fashion.

  All of these `problems` could be more inconveniences than real issues,
  depending on the extent of functionality intended for confconsole's new
  modular system.
    

