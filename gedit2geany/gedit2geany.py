#!/usr/bin/env python

import os
import sys
from lxml import etree

GEDIT_INPUT = "github.xml"
GEANY_TEMPLATE = "template.conf"

# maps style names from Gedit to Geany names
_MAPPING = {
	# Editor styles
	"text": "default",
	"selection": "selection",
	"cursor": "caret",
	"current-line": "current_line",
	"line-numbers": "margin_line_number",
	"bracket-match": "brace_good",
	"bracket-mismatch": "brace_bad",
	"def:error": "error",
	
	# Programming styles
	"def:comment": "comment",
	"def:number": "number",
	"def:string": "string",
	"def:type": "type",
	"def:function": "function",
	"def:keyword": "keyword",
	"def:builtin": "keyword_2",
	"def:identifier": "label", #?
	"def:preprocessor": "preprocessor",
	"def:complex": "regex",
	"def:operator": "operator",
	"def:statement": "decorator", #?
	"def:constant": "other", #?
	
	# Markup-type languages
	"xml:tag": "tag",
	"xml:attribute-name": "attribute",
	
	# Diff
	"diff:added-line": "line_added",
	"diff:changed-line": "line_changed",
	"diff:removed-line": "line_removed",
}

COLORS = {}
STYLES = {}

tree = etree.parse(open(GEDIT_INPUT, "r"))

root = tree.getroot()

def hex_to_int(hexstr):
	if len(hexstr.strip()) == 0:
		return ""
	if hexstr.startswith("#"):
		hexstr = hexstr[1:]
	if hexstr.startswith("0x"):
		hexstr = hexstr[2:]
	if len(hexstr) == 3:
		hexstr = "%c%c%c%c%c%c" % (hexstr[0], hexstr[0],
									hexstr[1], hexstr[1],
									hexstr[2], hexstr[2])
	if len(hexstr) > 6:
		sys.stderr.write("Truncated 0x%s to 0x%s\n" % (hexstr, hexstr[:6]))
		hexstr = hexstr[:6]
	return "0x%s" % hexstr

INFO = {}
if root.get("_name", False):
	INFO["name"] = root.get("_name")

# Read Gedit theme into dict
for child in root:
	if child.tag == "color":
		if child.get("name", False):
			COLORS[child.get("name")] = child.get("value", "")
	elif child.tag == "style" and child.get("name", "") in _MAPPING:
		if child.get("name", False) and child.get("name")  in _MAPPING:
			fg = child.get("foreground", "")
			bg = child.get("background", "")
			if fg in COLORS: fg = COLORS[fg]
			if bg in COLORS: bg = COLORS[bg]
			if not fg.startswith("#"): fg = ""
			if not bg.startswith("#"): bg = ""
			bold = child.get("bold", "")
			italic = child.get("italic", "")
			style = "%s;%s;%s;%s" % (hex_to_int(fg), hex_to_int(bg), bold, italic)
			STYLES[_MAPPING[child.get("name")]] = style
	elif child.tag == "author":
		INFO["author"] = child.text
	elif child.tag == "description":
		INFO["description"] = child.text

op_file = "%s.conf" % os.path.splitext(os.path.basename(GEDIT_INPUT))[0]
with open(op_file, "w") as op:
	
	op.write("[theme_info]\n")
	for key, value in sorted(INFO.items()):
		op.write("%s=%s\n" % (key, value))
	op.write("\n[named_styles]\n")
	for key, value in sorted(STYLES.items()):
		op.write("%s=%s\n" % (key, value))
	op.write("\n")
	
	op.write("margin_folding=margin_margin_line_number\n")
	op.write("fold_symbol_highlight=%s\n" % STYLES["margin_line_number"].split(";")[1])
	
	# make indent guide and white space bg color but bit lighter
	bg_color = int(STYLES.get("default", "0x000000").split(";")[1], base=16)
	bg_blue = bg_color & 255
	bg_green = (bg_color >> 8) & 255
	bg_red = (bg_color >> 16) & 255
	#bg_inc = 0xff - 0xc0 # tweak me
	bg_inc = 10
	
	bg_lighter = "0x%02X%02X%02X" % (int(bg_red + bg_inc), 
										int(bg_green + bg_inc), 
										int(bg_blue + bg_inc))
										
	bg_even_lighter = "0x%02x%02x%02x" % (bg_red + (bg_inc*2),
										bg_green + (bg_inc*2),
										bg_blue + (bg_inc*2))
	bg_lighter_still = "0x%02x%02x%02x" % (bg_red + (bg_inc*3),
										bg_green + (bg_inc*3),
										bg_blue + (bg_inc*3))
	
	op.write("indent_guide=%s;%s\n" % (bg_lighter, 
					STYLES["default"].split(";")[1]))
	op.write("white_space=indent_guide\n")
	
	op.write("comment_doc=comment\n")
	op.write("comment_line=comment\n")
	op.write("comment_line_doc=comment_doc\n")
	op.write("comment_doc_keyword=comment_doc,bold\n")
	op.write("comment_doc_keyword_error=comment_doc,italic\n")
	
	op.write("number_1=number\n")
	op.write("number_2=number_1\n")
	
	op.write("class=type\n")
	
	op.write("parameter=function\n")
	
	op.write("keyword_1=keyword\n")
	op.write("keyword_2=keyword_1\n")
	op.write("keyword_3=keyword_1\n")
	op.write("keyword_4=keyword_1\n")
	
	
	
	op.write("\n")





























