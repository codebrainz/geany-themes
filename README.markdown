Geany Color Themes
==================

geany-themes is a set of filedefs and colorschemes containing some really nice
themes.  I have ported almost all of the existing Geany themes I could find to
use the new filedefs so that you can still use those if you like them.  Also
included is an `alt.conf` theme, ported from Geany to make sure you can still
use that as well, if you like it.

Some of the new themes were ported from the 
[gedit-themes](https://github.com/mig/gedit-themes/) and I plan to port the 
rest of them.  There is also a bunch of available themes for 
[vim](http://www.google.com/search?q=vim+color+themes) and 
[TextMate](http://wiki.macromates.com/Themes/UserSubmittedThemes) that would 
also be nice to port.

Your help creating new themes and checking the `mappings/*.conf` files would
be greatly appreciated.  You can use one of the existing themes as a starting
point and there is more information in the 
[Geany Manual](http://www.geany.org/manual/current/index.html#filetype-definition-files).
No programming skills are required at all to help out.


## Installation:

*NOTE: this will overwrite any of your customized filedefs/colorschemes in your home directory, you may want to back them up first, for example:*

<pre>
$ cd ~/.config/geany
$ tar cjf themes-orig.tar.bz2 colorschemes/ filedefs/
</pre>

Copy all the `filetypes.*` files from the `filedefs` dir into your Geany 
filedefs dir, for example `~/.config/geany/filedefs`.

<pre>
$ cp -v filedefs/filetypes.* ~/.config/geany/filedefs
</pre>

Copy all the `*.conf` files from the colorschemes dir into your Geany 
colorschemes dir, for example `~/.config/geany/colorschems`.

<pre>
$ cp -v colorschemes/*.conf ~/.config/geany/colorschemes
</pre>


## Simpler Installation:

There is a simple installation script that can copy the files for you, see
`./install --help` for usage.  It was not tested on Windows.


## Uninstallation:

Remove all the files copied in 'Installation' and put the backed up files
back (if any).


## Helping Out:

You can use the below steps to make it easier to contribute changes back or
if you want to easily keep up to date with geany-themes.  There is a README
file in the sub directories with some info that will be helpful if you want
to hack/contribute.

### Installing:

*NOTE: replace `~/src` with wherever you would like to keep the files.  These are example commands only, don't just copy and paste them into a terminal.*

<pre>
killall geany
cd ~/.config/geany
tar cjf themes-orig.tar.bz2 colorschemes/ filedefs/
rm -r colorschemes filedefs
mkdir -p ~/src
cd ~/src/
git clone git://github.com/codebrainz/geany-themes.git
ln -s ~/src/geany-themes/colorschemes ~/.config/geany/colorschemes
ln -s ~/src/geany-themes/filedefs ~/.config/geany/filedefs
geany -v
</pre>

### Keeping up to Date:

<pre>
cd ~/src/geany-themes
git stash
git pull
git stash pop
</pre>

*NOTE: You'll need to fix any conflicts if you've made local changes.*

### Submitting your changes:

<pre>
cd ~/src/geany-themes
git diff > ../the_patch_name.patch
</pre>

Send me your patch and I'll apply it here or send a 
[pull request](http://help.github.com/pull-requests/) on
[GitHub](https://github.com/) if you've forked the repository.
