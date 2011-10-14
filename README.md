Color Schemes for Geany
=======================

These are some color schemes for the [Geany IDE](http://geany.org) converted from other editors' color 
schemes and some created by the Geany community.  

__Note:__ Please don't report any bugs on the Geany tracker for issues with these color schemes.  Instead use the 
[Issues Tracker](https://github.com/codebrainz/colorschemes/issues) for the 
[colorschemes](https://github.com/codebrainz/colorschemes) repository.

Installation Instructions:
--------------------------

```
$ cd ~/.config/geany/
$ mv colorschemes{,-backup}
$ git clone git://github.com/codebrainz/colorschemes.git
```

Now restart Geany and you should see the color schemes under the View->Editor->Color Schemes menu.

Keeping up to Date:
-------------------

```
$ cd ~/.config/geany/colorschemes
$ git pull master
```

Now restart Geany and you should see the updated color schemes.

Hacking:
--------

Feel free to send any Pull Requests on Github if you fix or improve existing schemes or create a new one.

Try to make sure you test your scheme running `geany -v` and make sure there's no related warning.