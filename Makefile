#
# Makefile for geany-themes development
#

THEMES           = $(wildcard colorschemes/*.conf)
COLORSCHEME_DIR  = ${HOME}/.config/geany/colorschemes
UNINSTALL_THEMES = $(addprefix $(COLORSCHEME_DIR)/, $(notdir $(THEMES)))
THEMES_VERSION   = 1.24
MISMATCH_MESSAGE = Warning: Possible wrong version of Geany installed
ARCHIVE_NAME     = geany-themes-$(THEMES_VERSION).tar.bz2
ARCHIVE_TEMP_DIR = geany-themes-$(THEMES_VERSION)

all: autobump index

install:
	mkdir -p $(COLORSCHEME_DIR)
	install -m 0644 $(THEMES) "$(COLORSCHEME_DIR)"

uninstall:
	# NOTE: leave straggling directory ~/.config/geany/colorschemes this is for
	# safety in case there's other stuff in there.
	rm -f $(UNINSTALL_THEMES)

index: scripts/versions.log
	make -C index

autobump: $(THEMES)
	python scripts/autobump.py

clean:
	make -C index clean

colorsnormal:
	python scripts/colornorm.py $(THEMES)

usedefaults:
	python scripts/defaultify.py $(THEMES)

ChangeLog:
	git --no-pager log --format="%ai %aN %n%n%x09* %s%n" > ChangeLog

dist: $(THEMES) README.md Makefile ChangeLog AUTHORS COPYING
	mkdir -p geany-themes-$(THEMES_VERSION)/colorschemes/
	cp colorschemes/*.conf $(ARCHIVE_TEMP_DIR)/colorschemes/
	cp AUTHORS COPYING README.md ChangeLog $(ARCHIVE_TEMP_DIR)/
	tar -cjf $(ARCHIVE_NAME) $(ARCHIVE_TEMP_DIR)/
	rm -rf $(ARCHIVE_TEMP_DIR) ChangeLog

help:
	@echo "Geany-Themes Makefile Help"
	@echo "=========================="
	@echo ""
	@echo "  This is a little helper Makefile for managing the Geany-Themes "
	@echo "  source tree. Most users will at most want to use the "
	@echo "  \`make install' command or simply copy the files into the "
	@echo "  \`$(HOME)/.config/geany/colorschemes' directory."
	@echo ""
	@echo "Makefile Commands:"
	@echo "------------------"
	@echo "  make install - Installs all color scheme .conf files"
	@echo "  make uninstall - Uninstall tracked color scheme files"
	@echo "  make index - Regenerate the index/index.json file"
	@echo "  make autobump - Update scheme versions on change"
	@echo "  make dist - Create a .tar.bz2 package for release"
	@echo "  make ChangeLog - Update the ChangeLog file from Git log"
	@echo ""
	@echo "Experimental commands:"
	@echo "----------------------"
	@echo "  make colorsnormal - Normalize colour notation in schemes"
	@echo "  make defaultify - Add default values in the schemes"
	@echo ""
	@echo "For more up to date information, visit:"
	@echo "  https://github.com/geany/geany-themes"

.PHONY: all install uninstall dist ChangeLog index autobump clean help
