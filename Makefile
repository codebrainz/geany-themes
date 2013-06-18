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

# dummy rule to handle default case, doesn't do anything useful
all:
	@echo "Nothing to do, use \`make install' instead."

install:
	mkdir -p $(COLORSCHEME_DIR)
	install -m 0644 $(THEMES) "$(COLORSCHEME_DIR)"

uninstall:
	# NOTE: leave straggling directory ~/.config/geany/colorschemes this is for
	# safety in case there's other stuff in there.
	rm -f $(UNINSTALL_THEMES)

index:
	make -C index

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

.PHONY: all install uninstall dist ChangeLog index clean
