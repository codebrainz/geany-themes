#
# Makefile for geany-themes 0.21 release
#

THEMES				= $(wildcard colorschemes/*.conf)
FILEDEFS			= $(wildcard filedefs/filetypes.*)
COLORSCHEME_DIR		= ${HOME}/.config/geany/colorschemes
FILEDEFS_DIR		= ${HOME}/.config/geany/filedefs
UNINSTALL_THEMES	= $(addprefix $(COLORSCHEME_DIR)/, $(notdir $(THEMES)))
UNINSTALL_FILEDEFS	= $(addprefix $(FILEDEFS_DIR)/, $(notdir $(FILEDEFS)))
GEANY_VERSION		= $(shell pkg-config --modversion geany 2>/dev/null)
THEMES_VERSION		= 0.21
MISMATCH_MESSAGE	= Warning: Possible wrong version of Geany installed
ARCHIVE_NAME		= geany-themes-$(THEMES_VERSION).tar.bz2
ARCHIVE_TEMP_DIR	= geany-themes-$(THEMES_VERSION)

# dummy rule to handle default case, doesn't do anything useful
all:
	@test "$(GEANY_VERSION)" = "$(THEMES_VERSION)" || echo "$(MISMATCH_MESSAGE)"
	@echo "Nothing to do, use \`make install' instead."

install:
	@test "$(GEANY_VERSION)" = "$(THEMES_VERSION)" || echo "$(MISMATCH_MESSAGE)"
	mkdir -p $(COLORSCHEME_DIR)
	mkdir -p $(FILEDEFS_DIR)
	install -m 0644 $(THEMES) "$(COLORSCHEME_DIR)"
	install -m 0644 $(FILEDEFS) "$(FILEDEFS_DIR)"

uninstall:
	@test "$(GEANY_VERSION)" = "$(THEMES_VERSION)" || echo "** $(MISMATCH_MESSAGE)"
	# NOTE: leave straggling directories ~/.config/geany/{colorschemes,filedefs}
	# this is for safety in case there's other stuff in there.
	rm -f $(UNINSTALL_THEMES) $(UNINSTALL_FILEDEFS)

ChangeLog:
	git --no-pager log --format="%ai %aN %n%n%x09* %s%d%n" > ChangeLog

dist: $(THEMES) $(FILDEFS) README Makefile ChangeLog
	mkdir -p geany-themes-$(THEMES_VERSION)/colorschemes/
	mkdir -p geany-themes-$(THEMES_VERSION)/filedefs/
	cp colorschemes/*.conf $(ARCHIVE_TEMP_DIR)/colorschemes/
	cp filedefs/filetypes.* $(ARCHIVE_TEMP_DIR)/filedefs/
	cp AUTHORS COPYING README ChangeLog $(ARCHIVE_TEMP_DIR)/
	tar -cjf $(ARCHIVE_NAME) $(ARCHIVE_TEMP_DIR)/
	rm -rf $(ARCHIVE_TEMP_DIR) ChangeLog

.PHONY: all install uninstall dist ChangeLog
