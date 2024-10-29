import sys
from sly import Lexer

class Scanner(Lexer):
    # Set of token names and literals
    tokens = {IF, DOT_ADD, DOT_SUB, DOT_MUL, DOT_DIV, ADD_ASSIGN, SUB_ASSIGN, MUL_ASSIGN,
              DIV_ASSIGN, SMALLER_OR_EQUAL, BIGGER_OR_EQUAL, NONEQUAL, EQUAL, ELSE, FOR, WHILE, BREAK,
              CONTINUE, RETURN, EYE, ZEROS, ONES, PRINT, ID, STRING, INTNUM, FLOATNUM}

    literals = {'+', '-', '*', '=', ',', '<', '>', '(', ')', '[', ']', '{', '}', ':', '\'', ',', ';', }

    # matrix operators
    DOT_ADD = r'\.\+'
    DOT_SUB = r'\.\-'
    DOT_MUL = r'\.\*'
    DOT_DIV = r'\.\/'

    # assign actions
    ADD_ASSIGN = r'\+\='
    SUB_ASSIGN = r'\-\='
    MUL_ASSIGN = r'\*\='
    DIV_ASSIGN = r'\/\='

    # comparators
    SMALLER_OR_EQUAL = r'\<\='
    BIGGER_OR_EQUAL = r'\>\='
    NONEQUAL = r'\!\='
    EQUAL = r'\=\='

    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_comment = r'\#.*'

    # Regular expression rules for tokens
    FLOATNUM = r'(\d+\.\d*|\.\d+)([eE][+-]?\d+)?' #uproscilem wyciagajac przed nawias zapis
    INTNUM = r'\d+'
    STRING = r'\".*?\"' #tutaj trzeba dodac po gwiazdce pytajnik, zeby zachlannie przerywalo po napotkaniu pierwszego znaku konca komentarza



    # id mialem zmineic na takie, bo wersja wczesniejsza bylla ze standardow ply, a nie sly
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['for'] = FOR
    ID['while'] = WHILE
    ID['break'] = BREAK
    ID['continue'] = CONTINUE
    ID['return'] = RETURN
    ID['zeros'] = ZEROS
    ID['ones'] = ONES
    ID['print'] = PRINT


    # ignore newline wrzucone tutaj po maupce zamiast oddzielnie u gory, a potem to tutaj
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1