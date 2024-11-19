import AST


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


class TreePrinter:
    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Program)
    def printTree(self, indent=0):
        for instr in self.instructions:
            instr.printTree(indent)

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        print("| " * indent + str(self.value))

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        print("| " * indent + str(self.value))

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print("| " * indent + self.name)

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print("| " * indent + str(self.name))

    @addToClass(AST.If)
    def printTree(self, indent=0):
        print("| " * indent + "IF")
        self.condition.printTree(indent + 1)
        print("| " * indent + "THEN")
        self.body.printTree(indent + 1)

    @addToClass(AST.IfElse)
    def printTree(self, indent=0):
        print("| " * indent + "IF")
        self.condition.printTree(indent + 1)
        print("| " * indent + "THEN")
        self.if_body.printTree(indent + 1)
        print("| " * indent + "ELSE")
        self.else_body.printTree(indent + 1)

    @addToClass(AST.For)
    def printTree(self, indent=0):
        print("| " * indent + "FOR")
        indent += 1
        self.var.printTree(indent)
        print("| " * indent + "RANGE")
        self.start.printTree(indent + 1)
        self.end.printTree(indent + 1)
        self.body.printTree(indent)

    @addToClass(AST.While)
    def printTree(self, indent=0):
        print("| " * indent + "WHILE")
        indent += 1
        self.condition.printTree(indent)
        self.body.printTree(indent)

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        print("| " * indent + str(self.op))
        indent += 1
        self.left.printTree(indent)
        self.right.printTree(indent)

    @addToClass(AST.UnaryExpr)
    def printTree(self, indent=0):
        print("| " * indent + str(self.op))
        self.operand.printTree(indent + 1)

    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        print("| " * indent + str(self.op))
        self.target.printTree(indent + 1)
        self.value.printTree(indent + 1)

    @addToClass(AST.ArrayAccess)
    def printTree(self, indent=0):
        print("| " * indent + "REF")
        indent += 1
        self.array.printTree(indent)
        self.row.printTree(indent)
        self.col.printTree(indent)

    @addToClass(AST.FunctionOnMatrix)
    def printTree(self, indent=0):
        print("| " * indent + self.function)
        self.argument.printTree(indent + 1)

    @addToClass(AST.MakeArray)
    def printTree(self, indent=0):
        print("| " * indent + "Vector")
        for element in self.elements:
            element.printTree(indent + 1)

    @addToClass(AST.Block)
    def printTree(self, indent=0):
        for instr in self.instructions:
            instr.printTree(indent)

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        print("| " * indent + "PRINT")
        for v in self.values:
            v.printTree(indent + 1)

    @addToClass(AST.Break)
    def printTree(self, indent=0):
        print("| " * indent + "BREAK")

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        print("| " * indent + "CONTINUE")

    @addToClass(AST.Return)
    def printTree(self, indent=0):
        print("| " * indent + "RETURN")
        self.value.printTree(indent + 1)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
