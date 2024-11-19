class Node(object):
    pass


class Program(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class IntNum(Node):
    def __init__(self, value):
        self.value = value


class FloatNum(Node):
    def __init__(self, value):
        self.value = value


class String(Node):
    def __init__(self, text):
        self.text = text


class Variable(Node):
    def __init__(self, name):
        self.name = name


class If(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class IfElse(Node):
    def __init__(self, condition, if_body, else_body):
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body


class For(Node):
    def __init__(self, var, start, end, body):
        self.var = var
        self.start = start
        self.end = end
        self.body = body


class While(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class UnaryExpr(Node):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand


class Assignment(Node):
    def __init__(self, op, target, value):
        self.op = op
        self.target = target
        self.value = value


class ArrayAccess(Node):
    def __init__(self, array, row, col):
        self.array = array
        self.row = row
        self.col = col


class FunctionOnMatrix(Node):
    def __init__(self, function, argument):
        self.function = function
        self.argument = argument


class MakeArray(Node):
    def __init__(self, elements):
        self.elements = elements


class Block(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class Break(Node):
    def __init__(self):
        pass


class Print(Node):
    def __init__(self, values):
        self.values = values


class Continue(Node):
    def __init__(self):
        pass


class Return(Node):
    def __init__(self, value):
        self.value = value


class Error(Node):
    def __init__(self):
        pass
