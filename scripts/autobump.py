#!/usr/bin/env python

"""
Automatically updates a color scheme's version number when the file
is modified. Run this before committing the change(s) to the repo.
"""

import os
import sys
import hashlib

def gen_sum(fn):
  return hashlib.md5(open(fn).read()).hexdigest()

def read_log(log_file):
  entries = []
  try:
    contents = open(log_file, 'r').read()
  except IOError:
    contents = ''
  for line in [l.strip() for l in contents.split('\n') if l.strip()]:
    m,n = line.split('\t')
    entries.append((n,m))
  return entries

def write_log(log_file, entries):
  new_lines = []
  for ent in entries:
    new_lines.append('\t'.join((ent[1], ent[0])))
  open(log_file, 'w').write('\n'.join(new_lines) + '\n')

def bump_version(fn):
  contents = open(fn).read()
  lines = contents.split('\n')
  new_lines = []
  for line in lines:
    line = line.rstrip()
    if line.strip().startswith('version'):
      k,v = line.split('=')
      v = int(v.strip())
      v += 1
      new_lines.append('version=%d' % v)
      print("Bumped version of '%s' from %d to %d" % (os.path.basename(fn), v-1, v))
    else:
      new_lines.append(line)
  open(fn, 'w').write('\n'.join(new_lines))

def check_scheme(entries, scheme_fn):
  for i, ent in enumerate(entries):
    n,m = ent
    if n == os.path.basename(scheme_fn):
      msum = gen_sum(scheme_fn)
      if m != msum:
        bump_version(scheme_fn)
        entries[i] = (n, gen_sum(scheme_fn))
      break
  else:
    entries.append((os.path.basename(scheme_fn), gen_sum(scheme_fn)))
  return entries

def main(args):
  cur_dir = os.path.abspath(os.path.dirname(__file__))
  root_dir = os.path.abspath(os.path.dirname(cur_dir))
  scheme_dir = os.path.join(root_dir, 'colorschemes')
  log_file = os.path.join(cur_dir, 'versions.log')
  entries = read_log(log_file)
  for fname in os.listdir(scheme_dir):
    if not fname.endswith(".conf"): continue
    path = os.path.join(scheme_dir, fname)
    entries = check_scheme(entries, path)
  write_log(log_file, entries)
  return 0

if __name__ == "__main__": sys.exit(main(sys.argv))
