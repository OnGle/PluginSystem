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
    
  Pros:
    - Incredibly simple to setup
    - Little to no restriction on plugin structure
    - Maintains menu order

  Cons:
    - Rather linear, scripts executed in sequence don't offer a whole lot
      of fancy menu interaction.
    - No callbacks (or communication other than exitcode)


- Structured python scripts, ran using execfile with a controlled
  environment. Each python script contains objects that are relevant to
  whatever it is the plugin is attempting to do. Some suggestions of
  objects in plugins is as follows:

    - menu_entry (a dictionary containing a name and arbitrarily deep
      values that represent `trees` of menu entries. In practice you would
      probably only create one or two menu entries. If any value in this
      menu_entry is not a dictionary it must be a callback function.)

      e.g.
      
      ```
      menu_entry = {
      'advanced_menu': {
            'networking': {
                'test': some_function
            }
         }
      }
      ```

      would mean when you clicked "Advanced Menu->Networking->Test" it would
      execute "some_function".

    - onExit (skipped if not defined, if defined handles any cleanup that
      would otherwise not be correctly closed by python. A database connection
      for example.)

  Alterations:

    It would also be possible to maintain menu entry order by using lists
    instead of dictionaries (or perhaps a psuedo dictionary class) that
    resembles the following:

    ```
    menu_entry = [
        [
            'advanced_menu',
            [
                'networking',
                [
                    'test',
                    some_function
                ]
            ]
        ]
    ]
    ```
    or even something which inferes location by string

    ```
    menu_entry = {'advanced_menu/networking/test': some_function}
    ```

  Pros:
    - Allows complex interaction between master program and plugins
    - Could maintain menu order
    - Pretty dynamic apart from certain restrictions

  Cons:
    - Maintaining menu order could introduce extra complexity

