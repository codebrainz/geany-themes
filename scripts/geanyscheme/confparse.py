#!/usr/bin/env python

"""
Replacement for the built-in ``configparser`` module.

See the ``confparse.test`` file for tests and examples.
"""

class ConfParse(object):
  """
  This is a less efficent (probably) and less robust ``ConfigParser`` which
  only exists because that module/class destroys whitespace and comments.
  This one is only meant to handle one file at a time and to preserve the
  original input as much as possible (ie. to make clean diffs).
  """
  def __init__(self, filename):
    self.filename = filename
    text = open(self.filename, 'r').read()
    self.lines = [l.strip() for l in text.split('\n')]

  @staticmethod
  def is_comment(line):
    line = line.strip()
    return line.startswith('#') or line.startswith(';')

  @staticmethod
  def is_group(line):
    line = line.strip()
    return line.startswith('[') and line.endswith(']')

  @staticmethod
  def is_key_value(line):
    fields = line.split('=')
    if len(fields) == 1 or not fields[0].strip() or \
      any(ch in fields[0].strip() for ch in [' ','\t']):
      return False
    return True

  def sections(self):
    sections = []
    for line in self.lines:
      if line.startswith('[') and line.endswith(']'):
        sections.append(line[1:-1])
    return sections

  def has_section(self, section):
    return section in self.sections()

  def options(self, section):
    in_section = False
    options = []
    for line in self.lines:
      if ConfParse.is_comment(line):
        continue
      if ConfParse.is_group(line):
        sect = line[1:-1]
        in_section = True if sect == section else False
        continue
      if in_section and '=' in line:
        key = line.split('=')[0].strip()
        options.append(key)
    return options

  def has_option(self, section, option):
    return option in self.options(section)

  def get(self, section, option):
    in_section = False
    for line in self.lines:
      if ConfParse.is_comment(line):
        continue
      if ConfParse.is_group(line):
        sect = line[1:-1]
        in_section = True if sect == section else False
        continue
      if in_section and '=' in line:
        parts = line.split('=')
        key = parts[0].strip()
        if key == option:
          return '='.join(parts[1:]).strip() if len(parts) > 1 else ''
    return None

  def set(self, section, option, new_value):
    self.add_section(section)
    self.add_option(section, option)
    in_section = False
    new_lines = self.lines[:]
    for i, line in enumerate(self.lines):
      if ConfParse.is_comment(line):
        continue
      if ConfParse.is_group(line):
        sect = line[1:-1]
        in_section = True if sect == section else False
        continue
      if in_section and '=' in line:
        parts = line.split('=')
        key = parts[0]
        value = '='.join(parts[1:])
        if key == option:
          new_lines[i] = '%s=%s' % (key, new_value.strip())
          self.lines = new_lines

  def add_section(self, section):
    if not self.has_section(section):
      self.lines.append('[%s]' % section)

  def add_option(self, section, option):
    self.add_section(section)
    if not self.has_option(section, option):
      for i, line in enumerate(self.lines):
        if ConfParse.is_group(line):
          group = line[1:-1]
          if group == section:
            self.lines.insert(i+1, '%s=' % option)
            break

  def to_dict(self):
    out_dict = {}
    current_group = None
    for line in self.lines:
      if ConfParse.is_comment(line):
        continue
      if ConfParse.is_group(line):
        current_group = line[1:-1]
        out_dict[current_group] = {}
        continue
      if current_group is not None and ConfParse.is_key_value(line):
        fields = line.split('=')
        if len(fields) > 0:
          key = fields[0]
          if len(fields) > 1:
            value = '='.join(fields[1:])
          else:
            value = ''
          out_dict[current_group][key] = value
    return out_dict

  def save(self):
    self.save_as(self.filename)

  def save_as(self, filename):
    open(filename, 'w').write(str(self))

  def __str__(self):
    return '\n'.join(self.lines).rstrip('\n') + '\n'

if __name__ == "__main__":
  import doctest
  doctest.testfile('confparse.test')
