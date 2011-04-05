# Geany Color Themes #

_UPDATE: if you aren't using the development version of Geany from Git
or Subversion, you need to use the [deprecated branch][depr_branch]
instead.  The current master branch is using a new feature since the
last Geany release and so is not compatible._

geany-themes is a set of filedefs and colorschemes containing some really nice
themes.  I have ported almost all of the existing Geany themes I could find to
use the new filedefs so that you can still use those if you like them.  Also
included is an `alt.conf` theme, ported from Geany to make sure you can still
use that as well, if you like it.

Some of the new themes were ported from the [gedit-themes][gedit_themes] and I
plan to port the rest of them.  There is also a bunch of available themes for
[vim][vim_themes] and [TextMate][textmate_themes] that would also be nice to
port.

Your help creating new themes and checking the `filedefs/filetype.*` files would
be greatly appreciated.  You can use one of the existing themes as a starting
point and there is more information in the [Geany Manual][geany_manual].  No
programming skills are required at all to help out.

_UPDATE: Since Geany r5596, the substitution and mappings hackery is no longer
needed.  Geany now supports copying the styling of one filetype to another.
I've removed those parts from geany-themes, simplifying the entire project._
**Sweet!**


## Installation: ##

_NOTE: this will overwrite any of your customized filedefs/colorschemes in
your home directory, you may want to back them up first, for example:_

	$ cd ~/.config/geany
	$ tar cjf themes-orig.tar.bz2 colorschemes/ filedefs/

Copy all the `filetypes.*` files from the `filedefs` dir into your Geany
filedefs dir, for example `~/.config/geany/filedefs`.

	$ cp -v filedefs/filetypes.* ~/.config/geany/filedefs

Copy all the `*.conf` files from the colorschemes dir into your Geany
colorschemes dir, for example `~/.config/geany/colorschemes`.

	$ cp -v colorschemes/*.conf ~/.config/geany/colorschemes


## Easier Installation: ##

There is a simple installation script that can copy the files for you, see
`./install --help` for usage.  It was not tested on Windows or much at all.


## Uninstallation: ##

Remove all the files copied in the 'Installation' section and put the backed up
files back (if any).


## Helping Out: ##

You can use the below steps to make it easier to contribute changes back or
if you want to easily keep up to date with geany-themes.  There is a README
file in the sub directories with some info that will be helpful if you want
to hack/contribute.

### Installing: ###

_NOTE: replace `~/src` with wherever you would like to keep the files.  These
are example commands only, don't just copy and paste them into a terminal._

	$ killall geany
	$ cd ~/.config/geany
	$ tar cjf themes-orig.tar.bz2 colorschemes/ filedefs/
	$ rm -r colorschemes filedefs
	$ mkdir -p ~/src
	$ cd ~/src/
	$ git clone git://github.com/codebrainz/geany-themes.git
	$ ln -s ~/src/geany-themes/colorschemes ~/.config/geany/colorschemes
	$ ln -s ~/src/geany-themes/filedefs ~/.config/geany/filedefs
	$ geany -v

### Keeping up to Date: ###

	$ cd ~/src/geany-themes
	$ git stash
	$ git pull
	$ git stash pop

_NOTE: You'll need to fix any conflicts if you've made local changes._

### Making Changes: ###

Edit any of the `colorschemes/*.conf` files or `filedefs/filetypes.*` files or
create a new colorscheme `.conf` file in the `colorschemes` directory.  Using an
existing theme (ex. `gedit.conf`) and modifying will be easier than from
scratch.  When I get a chance I'll add a `README` in the `colorschemes`
directory explaining in detail what all the named styles should be used for,
but for the most part, the name says it all.

_NOTE: Geany doesn't update all of the styles when you select them through the
`View->Editor->Color Schemes` menu, so you might have to restart Geany to see
all of your changes take effect.  One of the styles that does not get applied
without restarting Geany is the 'selection' named style, I haven't noticed any
others yet._

Once you've made your changes, you can update your Geany by using the simple
Python scripts included with geany-themes.  The installation script just copies
all of the required files (ie. contents of `filedefs` and `colorschemes`
directories) to your personal Geany config directory, assuming as a default
that `~/.config/geany` is where your Geany configuration files are.  The
installation utility has a `--help` option that shows usage.  See the note
above about restarting Geany.

When creating a new theme, a command line session might look like this:

	$ cd ~/src/geany-themes
	$ cp -v colorschemes/{gedit.conf,yournewtheme.conf}
	$ geany colorschemes/yournewtheme.conf &
	... edit the theme .conf file and save ...
	$ ./install
	$ killall geany
	$ geany -v
	... debug output, possibly containing any problems with the theme ...

When editing a filetypes.* file, for example the Haskell lexer mappings, a
command line session might look like this:

	$ cd ~/src/geany-themes
	$ cp -v filedefs/filetypes.haskell{,.backup} # if you want
	$ geany filedefs/filetypes.haskell &
	... edit the haskell.conf file and save ...
	$ ./install
	$ killall geany
	$ geany -v
	... debug output, possibly containing any problems with the mappings ...

When you are done making changes, follow the 'Submitting your changes' section.
Don't forget to delete the `*.backup` file if you made one, before making a
patch.


### Submitting your changes: ###

	$ cd ~/src/geany-themes
	$ git diff > ../the_patch_name.patch

Send me your patch and I'll apply it after a quick review or send a
[pull request][pull_requests] on [GitHub][github] if you've forked the
repository.

[gedit_themes]:		https://github.com/mig/gedit-themes
[vim_themes]:		http://www.google.com/search?q=vim+color+themes
[textmate_themes]:	http://wiki.macromates.com/Themes/UserSubmittedThemes
[geany_manual]:		http://www.geany.org/manual/current/index.html#filetype-definition-files
[pull_requests]:	http://help.github.com/pull-requests
[github]:			https://github.com
[depr_branch]:		https://github.com/codebrainz/geany-themes/tree/deprecated
