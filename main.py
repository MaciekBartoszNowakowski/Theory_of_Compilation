import sys
from scanner_sly import Scanner
from parser_sly import Mparser


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "lab2_examples/ex1.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    lexer = Scanner()
    parser = Mparser()

    parser.parse(lexer.tokenize(text))


# class Scanner(Lexer):
#     # Set of token names and literals
#     tokens = {IF, DOT_ADD, DOT_SUB, DOT_MUL, DOT_DIV, ADD_ASSIGN, SUB_ASSIGN, MUL_ASSIGN,
#               DIV_ASSIGN, SMALLER_OR_EQUAL, BIGGER_OR_EQUAL, NONEQUAL, EQUAL, ELSE, FOR, WHILE, BREAK,
#               CONTINUE, RETURN, EYE, ZEROS, ONES, PRINT, ID, STRING, INTNUM, FLOATNUM}
#
#     literals = {'+', '-', '*', '=', ',', '<', '>', '(', ')', '[', ']', '{', '}', ':', '\'', ',', ';', }
#
#     # matrix operators
#     DOT_ADD = r'\.\+'
#     DOT_SUB = r'\.\-'
#     DOT_MUL = r'\.\*'
#     DOT_DIV = r'\.\/'
#
#     # assign actions
#     ADD_ASSIGN = r'\+\='
#     SUB_ASSIGN = r'\-\='
#     MUL_ASSIGN = r'\*\='
#     DIV_ASSIGN = r'\/\='
#
#     # comparators
#     SMALLER_OR_EQUAL = r'\<\='
#     BIGGER_OR_EQUAL = r'\>\='
#     NONEQUAL = r'\!\='
#     EQUAL = r'\=\='
#
#     # String containing ignored characters between tokens
#     ignore = ' \t'
#     ignore_comment = r'\#.*'
#
#     # Regular expression rules for tokens
#     FLOATNUM = r'(\d+\.\d*|\.\d+)([eE][+-]?\d+)?'
#     INTNUM = r'\d+'
#     STRING = r'\".*?\"'
#
#     ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
#     ID['if'] = IF
#     ID['else'] = ELSE
#     ID['for'] = FOR
#     ID['while'] = WHILE
#     ID['break'] = BREAK
#     ID['continue'] = CONTINUE
#     ID['return'] = RETURN
#     ID['zeros'] = ZEROS
#     ID['ones'] = ONES
#     ID['print'] = PRINT
#
#     @_(r'\n+')
#     def ignore_newline(self, t):
#         self.lineno += t.value.count('\n')
#
#     def error(self, t):
#         print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
#         self.index += 1
#
#
# if __name__ == '__main__':
#
#     try:
#         filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
#         file = open(filename, "r")
#     except IOError:
#         print("Cannot open {0} file".format(filename))
#         sys.exit(0)
#
#     text = file.read()
#     lexer = Scanner()
#
#     for tok in lexer.tokenize(text):
#         print('Line number = %r, token type = %r, token value = %r' % (tok.lineno, tok.type, tok.value))
