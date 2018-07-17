Geany Themes README
===================

Introduction
------------

Geany-themes is a collection of color schemes for the
[Geany IDE/editor][geany], either written originally by the Geany community
or ported from color schemes for other editors. These schemes are compatible
with Geany 1.22 and greater. Check out the [screenshots][scrn] to get an
idea for what each color scheme looks like.

Installation
------------

**Note:** the following instructions will overwrite any themes with
the same filename you have already installed, so if you have customized
any of them, you will lose your customizations if you don't back them
up first.

### Unix-like Systems

Extract the zip file, tarball or checkout with Git to a local 
directory. In this directory you will find a sub-directory named 
`colorschemes` which contains all of the color scheme files. Copy all of 
these `*.conf` files into the directory named 
`~/.config/geany/colorschemes/`, where `~` means your personal home 
directory. Create the `~/.config/geany/colorschemes/` directory if it
does not already exist.

After copying the files you can choose a new theme by selecting
`Change Color Scheme...` from Geany's `View` menu.

### Windows

Installing the themes on Windows is the same as with Unix-like systems 
with the exception that the target directory will be different. With 
Windows 7, the directory should be named
`C:\Users\YourUserName\AppData\Roaming\geany\colorschemes`, but the 
exact path may vary depending on your Windows configuration and/or 
version. Refer to [the Geany Manual][man-paths] for more information on 
configuration file paths.

Documentation
-------------

If you want to add a theme, read the [ADDING-A-THEME.md][add-theme] file. If you
are a package maintainer, consult the [MAKING-A-RELEASE.md][make-release] file. For
all other cases, consult the official Geany documentation.

Other Themes
------------

You can also also sometimes find bleeding edge themes which have yet to 
be fully integrated into the repository by looking at the
[Issues on Github][issues] labelled with the [`new-theme`][new-themes] label.
There may also be some unofficial themes on [the wiki][wiki-themes].

Be wary of old-style themes you may find in random places on the 
Internet as they may only be compatible with old Geany versions before 
1.22 and will likely result in grief. If the file doesn't contain a 
section called `[theme_info]` it almost sure to be an incompatible 
older theme. See below for more details.

Compatibility
-------------

These color schemes are not compatible with older version of Geany 
prior to 1.22, including its old filetypes files, which you may have 
customized and are found in your per-user configuration folder. All 
bets are off if you mix and match old filetypes/color schemes and the 
color schemes here. The best way to handle it is to simple move your 
old filetypes out of the way, copy the ones you want to customize from 
Geany's system data folder and hand-copy over the non-`[styling]` 
groups from the old filetypes file into the new one.

[geany]: http://www.geany.org
[scrn]: https://github.com/geany/geany-themes/tree/master/screenshots
[issues]: https://github.com/geany/geany-themes/issues?q=is%3Aopen
[new-themes]: https://github.com/geany/geany-themes/labels/new-theme
[wiki-themes]: https://wiki.geany.org/themes/start
[man-paths]: https://www.geany.org/manual/current/index.html#configuration-file-paths
[add-theme]: https://github.com/geany/geany-themes/blob/master/ADDING-A-THEME.md
[make-release]: https://github.com/geany/geany-themes/blob/master/MAKING-A-RELEASE.md
