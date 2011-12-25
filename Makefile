ifndef PREFIX
PREFIX = ~/.config
endif

INSTALL_DIR = $(PREFIX)/geany/colorschemes/

COLOR_SCHEMES = $(wildcard *.conf)
COLOR_SCHEMES_INSTALLED = $(addprefix $(INSTALL_DIR), $(COLOR_SCHEMES))

all:
	@echo "Nothing to be done, use \`make install' to install."

install:
	install -m 0644 $(COLOR_SCHEMES) $(INSTALL_DIR)

uninstall:
	rm -f $(COLOR_SCHEMES_INSTALLED)
