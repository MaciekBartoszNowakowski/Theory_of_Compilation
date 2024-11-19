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

    @addToClass(AST.Number)
    def printTree(self, indent=0):
        print("| " * indent + str(self.value))

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass

    @addToClass(AST.Program)
    def printTree(self, indent=0):
        for instr in self.instructions:
            instr.printTree(indent)

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print("| " * indent + self.name)

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print("| " * indent + str(self.name))

    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        print("| " * indent + str(self.op))
        self.target.printTree(indent + 1)
        self.value.printTree(indent + 1)

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        print("| " * indent + str(self.op))
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.UnaryExpr)
    def printTree(self, indent=0):
        print("| " * indent + str(self.op))
        self.operand.printTree(indent + 1)

    @addToClass(AST.MatrixFunction)
    def printTree(self, indent=0):
        print("| " * indent + self.function)
        self.argument.printTree(indent + 1)

    @addToClass(AST.ArrayCreation)
    def printTree(self, indent=0):
        print("| " * indent + "Vector")
        for element in self.elements:
            element.printTree(indent + 1)

    @addToClass(AST.ArrayAccess)
    def printTree(self, indent=0):
        print("| " * indent + "REF")
        self.array.printTree(indent + 1)
        self.row.printTree(indent + 1)
        self.col.printTree(indent + 1)

    @addToClass(AST.ForLoop)
    def printTree(self, indent=0):
        print("| " * indent + "FOR")
        indent += 1
        self.var.printTree(indent)
        print("| " * indent + "RANGE")
        self.start.printTree(indent+1)
        self.end.printTree(indent+1)
        self.body.printTree(indent)


    @addToClass(AST.WhileLoop)
    def printTree(self, indent=0):












