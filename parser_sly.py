from sly import Parser
from scanner_sly import Scanner


class MyParser(Parser):
    tokens = Scanner.tokens | Scanner.literals
    debugfile = 'parser.out'



    precedence = (
        ('nonassoc', "IFX"),
        ('nonassoc', "ELSE"),
        ("left", '<', '>', 'EQUAL', 'NONEQUAL', 'BIGGER_OR_EQUAL', 'SMALLER_OR_EQUAL'),
        ("left", '+', '-'),
        ("left", '*', '/'),
        ("left", 'DOT_ADD', 'DOT_SUB'),
        ("left", 'DOT_MUL', 'DOT_DIV'),
    )

    @_('instructions')
    def start(self, p):
        pass

    @_('instruction',
       'instruction instructions',
       '"{" instructions "}"'
       )
    def instructions(self, p):
        pass

    @_('instr_assign ";"',
       'instr_return ";"',
       'instr_loop',
       'instr_if',
       'instr_loop_flow ";"',
       'instr_print ";"'
       )
    def instruction(self, p):
        pass

    # if
    @_('IF "(" expr ")" statement ELSE statement',
       'IF "(" expr ")" statement %prec IFX')
    def instr_if(self, p):
        pass

    @_(' "{" instruction "}"',
       'instruction')
    def statement(self, p):
        pass

    # loop
    @_('WHILE "(" expr ")" "{" instructions "}"',
       'WHILE "(" expr ")" instruction',
       'FOR instr_assign statement')
    def instr_loop(self, p):
        pass

    @_('BREAK',
       'CONTINUE')
    def instr_loop_flow(self, p):
        pass

    # return
    @_('RETURN expr',
       'RETURN')
    def instr_return(self, p):
        pass

    @_('PRINT variables')
    def instr_print(self, p):
        pass



    @_('assignable "=" expr',
       'assignable ADD_ASSIGN expr',
       'assignable SUB_ASSIGN expr',
       'assignable MUL_ASSIGN expr',
       'assignable DIV_ASSIGN expr')
    def instr_assign(self, p):
        pass

    # math
    @_('expr SMALLER_OR_EQUAL expr',
       'expr BIGGER_OR_EQUAL expr',
       'expr NONEQUAL expr',
       'expr EQUAL expr',
       'expr ">" expr',
       'expr "<" expr',
       'expr DOT_ADD expr',
       'expr DOT_SUB expr',
       'expr DOT_MUL expr',
       'expr DOT_DIV expr',
       '"-" expr',
       'matrix',
       'vector',
       'matrix_create_expr',
       'expr "\'" ',
       'expr "+" expr',
       'expr "-" expr',
       'expr "*" expr',
       'expr "/" expr')
    def expr(self, p):
        pass

    # id
    @_("ID")
    def expr(self, p):
        pass

    # data types
    @_('FLOATNUM',
       'INTNUM')
    def expr(self, p):
        pass

    # assigns
    @_('ID',
       'matrix_ele',
       'vector_ele')
    def assignable(self, p):
        pass

    #     matrix
    @_('"[" vectors "]"')
    def matrix(self, p):
        pass

    #     creating matrix
    @_('ZEROS',
       'ONES',
       'EYE')
    def matrix_create_fun(self, p):
        pass

    @_('matrix_create_fun "(" expr ")"')
    def matrix_create_expr(self, p):
        pass

    @_('ID "[" INTNUM "," INTNUM "]"')
    def matrix_ele(self, p):
        pass

    # vector
    @_('"[" variables "]"',
       'variable ":" variable')
    def vector(self, p):
        pass

    @_('vector',
       'vector "," vectors')
    def vectors(self, p):
        pass

    @_('ID "[" INTNUM "]"')
    def vector_ele(self, p):
        pass

    # variable
    @_("INTNUM",
       "FLOATNUM",
       "STRING",
       'assignable')
    def variable(self, p):
        pass


    @_('variable "," variables',
       'variable')
    def variables(self, p):
        pass

    def error(self, p):
        if p:
            print(f"Syntax error at line {p.lineno}, character {p.index}: Unexpected token '{p.value}' ({p.type})")
        else:
            print("Unexpected end of input")
