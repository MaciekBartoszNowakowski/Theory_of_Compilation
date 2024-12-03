from sly import Parser
from scanner_sly import Scanner
from AST import *


class MyParser(Parser):
    tokens = Scanner.tokens | Scanner.literals
    debugfile = 'parser.out'

    precedence = (
        ('nonassoc', "IFX"),
        ('nonassoc', "ELSE"),
        ("nonassoc", '<', '>', 'EQUAL', 'NONEQUAL', 'BIGGER_OR_EQUAL', 'SMALLER_OR_EQUAL'),
        ("left", '+', '-'),
        ("left", 'DOT_ADD', 'DOT_SUB'),
        ("left", '*', '/'),
        ("left", 'DOT_MUL', 'DOT_DIV'),
        ("right", "UMINUS"),
        ("left", "'")
    )

    @_('instructions')
    def start(self, p):
        return Program(p[0])

    @_('instruction')
    def instructions(self, p):
        return [p.instruction]

    @_('instruction instructions')
    def instructions(self, p):
        return [p.instruction] + p.instructions

    @_('"{" instructions "}"')
    def instructions(self, p):
        return p.instructions

    @_('assignable "=" expr ";"')
    def instruction(self, p):
        return AssignmentOrCreation(p[1], p.assignable, p.expr, p.lineno)

    @_('assignable ADD_ASSIGN expr ";"',
       'assignable SUB_ASSIGN expr ";"',
       'assignable MUL_ASSIGN expr ";"',
       'assignable DIV_ASSIGN expr ";"')
    def instruction(self, p):
        return Assignment(p[1], p.assignable, p.expr, p.lineno)

    @_('ID "[" expr "," expr "]"')
    def assignable(self, p):
        return ArrayAccess(Variable(p.ID), p[2], p[4], p.lineno)

    @_('ID "[" expr "]"')
    def assignable(self, p):
        return ArrayAccess(Variable(p.ID, p.lineno), p[2], None, p.lineno)

    @_("ID")
    def assignable(self, p):
        return Variable(p.ID, p.lineno)

    @_('IF "(" condition ")" block ELSE block')
    def instruction(self, p):
        return IfElse(p.condition, p.block0, p.block1, p.lineno)

    @_('IF "(" condition ")" block %prec IFX')
    def instruction(self, p):
        return If(p.condition, p.block, p.lineno)

    @_('expr "<" expr',
       'expr ">" expr',
       'expr SMALLER_OR_EQUAL expr',
       'expr BIGGER_OR_EQUAL expr',
       'expr NONEQUAL expr',
       'expr EQUAL expr', )
    def condition(self, p):
        return BinExpr(p[1], p.expr0, p.expr1, p.lineno)

    @_('FOR ID "=" expr ":" expr block')
    def instruction(self, p):
        return For(Variable(p.ID, p.lineno), p.expr0, p.expr1, p.block, p.lineno)

    @_('WHILE "(" condition ")" block')
    def instruction(self, p):
        return While(p.condition, p.block, p.lineno)

    @_('BREAK ";"')
    def instruction(self, p):
        return Break(p.lineno)

    @_('CONTINUE ";"')
    def instruction(self, p):
        return Continue(p.lineno)

    @_('"{" instructions "}"')
    def block(self, p):
        return Block(p.instructions,p.lineno)

    @_('instruction')
    def block(self, p):
        return Block([p.instruction], p.lineno)

    @_('RETURN expr ";"')
    def instruction(self, p):
        return Return(p.expr, p.lineno)

    @_('PRINT sequence_element ";"')
    def instruction(self, p):
        return Print(p.sequence_element, p.lineno)


    @_('ID "," sequence_element')
    def sequence_element(self, p):
        return [Variable(p.ID)] + p.sequence_element

    @_('ID')
    def sequence_element(self, p):
        return [Variable(p.ID, p.lineno)]

    @_('STRING')
    def sequence_element(self, p):
        return [String(p[0], p.lineno)]

    @_('expr "+" expr',
       'expr "-" expr',
       'expr "*" expr',
       'expr "/" expr',
       'expr DOT_ADD expr',
       'expr DOT_SUB expr',
       'expr DOT_MUL expr',
       'expr DOT_DIV expr',
       )
    def expr(self, p):
        return BinExpr(p[1], p[0], p[2], p.lineno)

    # minus unarny
    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return UnaryExpr(p[0], p.expr, p.lineno)

    @_('expr "\'"')
    def expr(self, p):
        return UnaryExpr('transpose', p.expr, p.lineno)

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('FLOATNUM')
    def expr(self, p):
        return Number(p[0], p.lineno)

    @_('INTNUM')
    def expr(self, p):
        return Number(p[0], p.lineno)

    @_("STRING")
    def expr(self, p):
        return String(p.STRING, p.lineno)

    @_('ID')
    def expr(self, p):
        return Variable(p.ID, p.lineno)

    @_('ZEROS "(" expr ")"',
       'ONES "(" expr ")"',
       'EYE "(" expr ")"')
    def expr(self, p):
        return MatrixFunction(p[0], p.expr, p.lineno)

    @_('"[" array_element "]"')
    def expr(self, p):
        return ArrayCreation(p.array_element, p.lineno)

    @_('expr "," array_element')
    def array_element(self, p):
        return [p.expr] + p.array_element

    @_('expr')
    def array_element(self, p):
        return [p.expr]

    def error(self, p):
        if p:
            print(f"Syntax error at line {p.lineno}, character {p.index}: Unexpected token '{p.value}' ({p.type})")
        else:
            print("Unexpected end of input")
