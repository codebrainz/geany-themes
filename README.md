Color Schemes for Geany
=======================

__IMPORTANT:__ These themes are **only** for Geany's `master` development branch!  If you are using Geany 0.20, use
the geany-themes `0.20` branch, if you are using Geany 0.21, use the geany-themes `0.21` branch.

These are some color schemes for the [Geany IDE](http://geany.org) converted from other editors' color
schemes and some created by the Geany community.

__Note:__ Please don't report any bugs on the Geany tracker for issues with these color schemes.  Instead use the
[Issues Tracker](https://github.com/codebrainz/geany-themes/issues) for the
[geany-themes](https://github.com/codebrainz/geany-themes) repository.

Installation Instructions:
--------------------------

```
$ cd /home/you/some/place
$ git clone git://github.com/codebrainz/geany-themes.git
$ mv /home/you/.config/geany/colorschemes{,-backup}
$ ln -s /home/you/some/place/geany-themes /home/you/.config/geany/colorschemes 
```

Now restart Geany and you should see the color schemes under the View->Editor->Color Schemes menu.

Keeping up to Date:
-------------------

```
$ cd ~/.config/geany/colorschemes
$ git pull origin master
```

Now restart Geany and you should see the updated color schemes.

Hacking:
--------

Feel free to send any Pull Requests on Github if you fix or improve existing schemes or create a new one.

Try to make sure you test your scheme running `geany -v` and make sure there's no related warning.
