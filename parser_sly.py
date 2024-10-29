from sly import Parser
from scanner_sly import Scanner



# class Mparser(Parser):
#
#     tokens = Scanner.tokens
#
#     debugfile = 'parser.out'
#
#
#     precedence = (
#     # to fill ...
#         ()
#         ("right", 'ADD_ASSIGN', 'SUB_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN'),
#         ("left", 'DOT_ADD', 'DOT_SUB'),
#         ("left", '+', '-'),
#         ("left", '*', '/')
#     # to fill ...
#     )
#
#
#     @_('instructions_opt')
#     def p_program(self, p):
#         return ('program', p.instructions_opt)
#
#
#     @_('instructions')
#     def p_instructions_opt(self, p):
#         return p.p_instructions
#
#     @_('')
#     def p_instructions_opt(self, p):
#         return []
#
#     @_('instructions instruction')
#     def p_instructions(self, p):
#         return p.instructions + [p.instruction]
#
#     @_('instruction')
#     def p_instructions(self, p):
#         return [p.instruction]
#
#     # to finish the grammar
#     # ....

class MyParser(Parser):
    tokens = Scanner.tokens | Scanner.literals
    debugfile = 'parser.out'


    precedence = (
        ('nonassoc', 'IF'),
        ('nonassoc', 'ELSE'),
        ('nonassoc', '=', 'SUB_ASSIGN', 'ADD_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN'),
        ('left', 'DOT_ADD', 'DOT_SUB'),
        ('left', 'DOT_MUL', 'DOT_DIV'),
        ('left', '<', '>', 'SMALLER_OR_EQUAL', 'BIGGER_OR_EQUAL', 'EQUAL', 'NONEQUAL'),
        ('left', '+', '-'),
        ('left', '*'),
        ('left', 'PRINT'),
        ('right', ':', 'RETURN'),
        ('left', 'ID', 'STRING', 'INTNUM', 'FLOATNUM'),
    )

    @_('instructions_opt')
    def program(self, p):
        return p.instructions_opt

    @_('instructions')
    def instructions_opt(self, p):
        return p.instructions

    @_('')
    def instructions_opt(self, p):
        return []

    @_('instructions instruction')
    def instructions(self, p):
        return p.instructions + [p.instruction]

    @_('instruction')
    def instructions(self, p):
        return [p.instruction]

    @_('statement')
    def instruction(self, p):
        return p.statement


    # lista rzeczy do zdefiniowania
    # ('nonassoc', 'IF'),
    # ('nonassoc', 'ELSE'),
    # ('nonassoc', '=', 'SUB_ASSIGN', 'ADD_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN'),
    # ('left', 'DOT_ADD', 'DOT_SUB'),
    # ('left', 'DOT_MUL', 'DOT_DIV'),
    # ('left', '<', '>', 'SMALLER_OR_EQUAL', 'BIGGER_OR_EQUAL', 'EQUAL', 'NONEQUAL'),
    # ('left', '+', '-'),
    # ('left', '*'),
    # ('left', 'PRINT'),
    # ('right', ':', 'RETURN'),
    # ('left', 'ID', 'STRING', 'INTNUM', 'FLOATNUM'),


    # to finish the grammar
    # ....

    # mathematical operators

    @_('expression "+" expression')
