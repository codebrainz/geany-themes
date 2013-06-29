Geany Themes README
===================

Introduction
------------

Geany-themes is a collection of color schemes for the
[Geany IDE/editor][geany], either written originally by the Geany community
or ported from color schemes for other editors. These schemes are compatible
with Geany 1.22 and greater. Check out the [screenshots][scrn] to get an
idea for what each color scheme looks like.

If you're using an older version of Geany, see these links:

* 0.19 or earlier is not supported
* 0.20 [geany-themes-0.20.zip][020zip] or [geany-themes-0.20.tar.bz2][020tar]
* 0.21 [geany-themes-0.21.1.zip][021zip] or [geany-themes-0.21.1.tar.bz2][021tar]

**Note:** There are no plans to further update Geany Themes releases before
the one for Geany 1.22. If you send me an udpated and tested
`geany-themes-0.2x.x.zip` or `geany-themes-0.2x.x.tar.bz2` file (or both),
I will check them out and add them as updated download links here in the
[README.md][readme] and in the [Github downloads][ghdl].

Unix-like Installation
----------------------

Extract the tarball and copy all of the files in the `colorschemes` directory
to your `~/.config/geany/colorschemes/` directory. Create that directory if it
doesn't already exist.

Windows Installation
--------------------

Extract the tarball and copy all of the files in the `colorschemes` directory
to your `C:\Users\YourUserName\AppData\Roaming\geany\colorschemes` directory.
Create this directory if it doesn't already exist.

**Note:** The Windows directory paths above are for Windows 7, they might be
different for other Windows versions (see the Geany manual).

**Note:** Both of the above instructions will want to over-write your existing
colorschemes which you might have customized. Be sure to backup any files in
those directories that you do not want over-written.

Docs
----

If you want to add a theme, read the [ADDING-A-THEME.md][add-theme] file. If you
are a package maintainer, consult the [MAKING-A-RELEASE.md][make-release] file. For
all other cases, consult the official Geany documentation.

Known Bugs
----------

## Backwards-compatiblity

These color schemes are not compatible with older version of Geany, including
its old filetypes files, which you may have customized and are found in
your per-user configuration folder. All bets are off if you mix and match
old filetypes/color schemes and the color schemes here. The best way to
handle it is to simple move your old filetypes out of the way, copy the ones
you want to customize from Geany's system data folder and hand-copy over the
non-`[styling]` groups from the old filetypes file into the new one.

## Ubuntu Unity

There is a conflict in Geany's code when you are using Unity's DBUS menu (that
global menu at the top of the screen). The fix for this is available in the
1.22 release of Geany. To work around the problem in older versions, you can
ensure that the environment variable `UBUNTU_MENUPROXY` is set to `0` before
running Geany. This will disable Unity from stealing Geany's main menu and
will leave it within Geany's main window. You should be able to edit your
launchers for Geany to run like this `UBUNTU_MENUPROXY=0 geany`. You can even
make a Bash alias if you wish.

Geany Themes was created and is maintained by Matthew Brush <matt@geany.org>.

[geany]: http://www.geany.org
[readme]: https://github.com/codebrainz/geany-themes/blob/master/README.md
[ghdl]: https://github.com/codebrainz/geany-themes/downloads
[scrn]: https://github.com/codebrainz/geany-themes/tree/master/screenshots
[020zip]: https://github.com/downloads/codebrainz/geany-themes/geany-themes-0.20.zip
[020tar]: https://github.com/downloads/codebrainz/geany-themes/geany-themes-0.20.tar.bz2
[021zip]: https://github.com/downloads/codebrainz/geany-themes/geany-themes-0.21.1.zip
[021tar]: https://github.com/downloads/codebrainz/geany-themes/geany-themes-0.21.1.tar.bz2
[add-theme]: https://github.com/geany/geany-themes/blob/master/ADDING-A-THEME.md
[make-release]: https://github.com/geany/geany-themes/blob/master/MAKING-A-RELEASE.md
