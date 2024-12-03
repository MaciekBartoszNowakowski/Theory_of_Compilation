class Node(object):
    def __init__(self, value, line):
        self.value = value
        self.line = line


class Program(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class IntNum(Node):
    def __init__(self, value, line=None):
        self.value = value
        self.line = line


class FloatNum(Node):
    def __init__(self, value, line=None):
        self.value = value
        self.line = line


class String(Node):
    def __init__(self, value, line):
        self.name = value
        self.line = line


class Variable(Node):
    def __init__(self, name, line):
        self.name = name
        self.line = line


class If(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class IfElse(Node):
    def __init__(self, condition, if_body, else_body, line):
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body
        self.line = line


class For(Node):
    def __init__(self, var, start, end, body, line):
        self.var = var
        self.start = start
        self.end = end
        self.body = body
        self.line = line


class While(Node):
    def __init__(self, condition, body, line):
        self.condition = condition
        self.body = body
        self.line = line


class BinExpr(Node):
    def __init__(self, op, left, right, line):
        self.op = op
        self.left = left
        self.right = right
        self.line = line


class UnaryExpr(Node):
    def __init__(self, op, operand, line):
        self.op = op
        self.operand = operand
        self.line = line


class Assignment(Node):
    def __init__(self, op, target, value, line):
        self.op = op
        self.target = target
        self.value = value
        self.line = line


class AssignmentOrCreation(Node):
    def __init__(self, op, target, value, line):
        self.op = op
        self.target = target
        self.value = value
        self.line = line


class ArrayAccess(Node):
    def __init__(self, array, row, col, line):
        self.name = array
        self.array = array
        self.row = row
        self.col = col
        self.line = line


class ArrayCreation(Node):
    def __init__(self, elements, line):
        self.elements = elements
        self.line = line


class MatrixFunction(Node):
    def __init__(self, function, argument, line):
        self.function = function
        self.argument = argument
        self.line = line


class Block(Node):
    def __init__(self, instructions, line):
        self.instructions = instructions
        self.line = line


class Break(Node):
    def __init__(self, line):
        self.line = line


class Print(Node):
    def __init__(self, values, line):
        self.values = values
        self.line = line


class Continue(Node):
    def __init__(self, line):
        self.line = line


class Return(Node):
    def __init__(self, value, line):
        self.value = value
        self.line = line


class Error(Node):
    def __init__(self, line):
        self.line = line


class Number(Node):
    def __init__(self, value, line):
        self.value = value
        self.line = line
