#!/usr/bin/env python

import sys
import re

RE_COLOR = re.compile(r'(#|0[xX])([a-fA-F0-9]{6}|[a-fA-F0-9]{3})')

def iter_matched_colors(input_text, normalize=False, regexp=RE_COLOR):

    def normalize_hex_color(hex_color, condense=True):

        def is_condensable(hc):
            return len(hc) == 6 and \
                hc[0] == hc[1] and hc[2] == hc[3] and hc[4] == hc[5]

        def condense_hex_color(hc):
            if not is_condensable(hc): return hc
            else: return hc[0:1] + hc[2:3] + hc[4:5]

        hex_color = hex_color.lower()
        if condense:
            hex_color = condense_hex_color(hex_color)
        return hex_color

    for match in regexp.finditer(input_text):
        hex_color = match.group(2)
        if normalize:
            hex_color = normalize_hex_color(hex_color)
        pfx = match.group(1)
        yield pfx, hex_color, match.start(0), match.end(0)

def main(args):

    if len(args) < 2:
        sys.stderr.write("error: no input file specified\n")
        return 1

    for filename in args[1:]:
        input_text = open(filename).read()
        norm_color_matches = iter_matched_colors(input_text, normalize=True)
        output_text = ''
        last_end = 0
        n_matches = 0
        for pfx, hex_color, start, end in norm_color_matches:
            output_text += input_text[last_end:start] + '#' + hex_color
            last_end = end
            n_matches += 1
        if n_matches == 0: # hack to prevent blank files when no colors match
            output_text = input_text.rstrip() + '\n'
        else:
            output_text += input_text[last_end:]
            output_text = output_text.rstrip() + '\n'
        open(filename, 'w').write(output_text)

    return 0


if __name__ == "__main__": sys.exit(main(sys.argv))
