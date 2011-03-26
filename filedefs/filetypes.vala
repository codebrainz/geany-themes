# For complete documentation of this file, please see Geany's main documentation
[styling]
# Edit these in the colorscheme .conf file intead
default=default
comment=comment
commentline=comment
commentdoc=comment_doc
number=number_1
word=keyword_1
word2=keyword_2
string=string_1
character=string_1
uuid=other
preprocessor=preprocessor
operator=operator
identifier=identifier_1
stringeol=string_eol
verbatim=string_2
regex=regex
commentlinedoc=comment_doc
commentdockeyword=comment_doc_keyword
commentdockeyworderror=comment_doc_keyword_error
globalclass=class


[keywords]
# all items must be in one line
primary=else if switch case default break continue return for foreach in do while is try catch finally throw namespace interface class struct enum signal errordomain construct callback get set base const static var weak virtual abstract override inline extern public protected private delegate out ref lock using true false null generic new delete base this value typeof sizeof throws requires ensures void bool char uchar int uint short ushort long ulong size_t ssize_t int8 uint8 int16 uint16 int32 uint32 int64 uint64 float double unichar string constpointer time_t
#secondary=
# these are some doxygen keywords (incomplete)
docComment=attention author brief bug class code date def enum example exception file fn namespace note param remarks return see since struct throw todo typedef var version warning union

[lexer_properties]
styling.within.preprocessor=1
lexer.cpp.track.preprocessor=0
preprocessor.symbol.$(file.patterns.cpp)=#
preprocessor.start.$(file.patterns.cpp)=if
preprocessor.middle.$(file.patterns.cpp)=else elif
preprocessor.end.$(file.patterns.cpp)=endif

[settings]
lexer_filetype=C

# default extension used when saving files
extension=vala

# the following characters are these which a "word" can contains, see documentation
#wordchars=_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

# single comments, like # in this file
comment_single=//
# multiline comments
comment_open=/*
comment_close=*/

# set to false if a comment character/string should start at column 0 of a line, true uses any
# indentation of the line, e.g. setting to true causes the following on pressing CTRL+d
	#command_example();
# setting to false would generate this
#	command_example();
# This setting works only for single line comments
#comment_use_indent=true

# context action command (please see Geany's main documentation for details)
#context_action_cmd=

[build_settings]
# %f will be replaced by the complete filename
# %e will be replaced by the filename without extension
# (use only one of it at one time)
compiler=valac -c "%f"
linker=valac "%f"
run_cmd=./"%e"
