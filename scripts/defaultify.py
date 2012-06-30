#!/usr/bin/env python

import sys
from geanyscheme.confparse import ConfParse

def seq_get(seq, idx, default=None):
  try:
    return seq[idx]
  except IndexError:
    return default

def expand_style(style_str, defaults=('#000', '#fff', 'false', 'false')):
  fields = style_str.split(';')
  fg = seq_get(fields, 0, defaults[0])
  bg = seq_get(fields, 1, defaults[1])
  bold = seq_get(fields, 2, defaults[2])
  italic = seq_get(fields, 3, defaults[3])
  return (fg, bg, bold, italic)

def remove_redundant(style_fields, default_fields):
  new_style = []
  for i, field in enumerate(style_fields):
    if field == default_fields[i]:
      new_style.append('')
    else:
      new_style.append(field)
  return tuple(new_style)

def defaultify_named_styles(conf, defaults):
  for option in conf.options('named_styles'):
    if option == 'default':
      continue
    style = expand_style(conf.get('named_styles', option), defaults)
    style = remove_redundant(style, defaults)
    new_line = ';'.join(style).rstrip(';')
    conf.set('named_styles', option, new_line)

def main(args):
  if len(args) < 2:
    sys.stderr.write("error: no input file(s) specified\n")
    return 1
  for filename in args[1:]:
    conf = ConfParse(filename)
    if conf.has_option('named_styles', 'default'):
      def_line = conf.get('named_styles', 'default')
    else:
      def_line = '#000;#fff;false;false'
    def_fields = expand_style(def_line)
    defaultify_named_styles(conf, def_fields)
    #print(str(conf))
    conf.save()

  return 0

if __name__ == "__main__": sys.exit(main(sys.argv))
