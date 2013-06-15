Making a Geany-Themes Release
=============================

This guide is meant for distribution/OS packagers to give some hints
and ideas for making Geany-Themes available to end-users.

Short and Sweet
---------------

The Geany-Themes files are just `.conf` files that get put into a
directory where Geany is looking for them. Assuming prefix `$PREFIX`,
which is where Geany is itself installed, the files should be installed
to `$PREFIX/share/geany/colorschemes`. Inside the repository, the
colorschemes are inside the `colorschemes` directory.

For example, a common installation location in Linux would be:

    /usr/share/geany/colorschemes

Or if you're packaging for Windows, the directory will likely be something
like this (I didn't boot Windows to verify):

    C:\Program Files\Geany\shared\geany\colorschemes

You'll probably also want/need to add some other files as described
below, but since the attributions/copyrights/credits are inside each
their own `.conf` file, you could safely just ship the `.conf` files.

A Note About Licensing
----------------------

Many of the colour schemes have different license. The canonical
reference to the licenses used is found at the beginning of each
`.conf` file in the `colorschemes` directory. All of the licenses are
free-software friendly but it is up to you to determine if the licenses
are compatible with your distribution method/rules. Feel free to drop
any colour schemes that do not suit your packaging/licensing needs by
just excluding that particular scheme. The default/recommended license
is GPL v2.

The Makefile
------------

I created a GNU Make file that has most of the stuff needed to create
a package. You can run it like this:

    $ make dist

You can use this created archive as the template for your package. It
contains all of the files you should distribute and none of the meta
stuff you don't need. See the Makefile itself for more ideas.

Since you know more than me about your distribution's requirements,
I'll not go into any more detail than this.
