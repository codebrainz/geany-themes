#!/usr/bin/env python

"""
Generates the screenshots/README.md file.
"""

import os
import sys
from geanyscheme.confparse import ConfParse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THEME_DIR = os.path.join(BASE_DIR, "colorschemes")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
RAW_URL = 'https://raw.githubusercontent.com/geany/geany-themes/master/colorschemes/'

class ColorScheme:
  def __init__(self, name, theme, screenshot):
    self.name = name
    self.theme = theme
    self.screenshot = screenshot

  @property
  def title(self):
    return "The %s Theme" % self.name

  @property
  def theme_url(self):
    return RAW_URL + os.path.basename(self.theme)

  @property
  def markdown(self):
    code  = '### [%s](%s)\n' % (self.title, self.theme)
    code += '\n'
    code += '[![%s](%s)](%s "%s")\n' % (
      self.screenshot, self.screenshot, self.screenshot, self.title)
    code += '\n'
    code += '[%s Direct Download](%s)\n' % (self.title, self.theme_url)
    code += '\n\n'
    return code

def list_colorschemes():
  schemes = []
  for fn in os.listdir(THEME_DIR):
    path = os.path.join(THEME_DIR, fn)
    conf = ConfParse(path)
    scheme = ColorScheme(
      conf.get("theme_info", "name"),
      os.path.join("..", "colorschemes", fn),
      os.path.splitext(fn)[0] + ".png")
    schemes.append(scheme)
  return schemes

def main(args):
  for scheme in list_colorschemes():
    sys.stdout.write(scheme.markdown)
  return 0

if __name__ == "__main__":
  sys.exit(main(sys.argv))
