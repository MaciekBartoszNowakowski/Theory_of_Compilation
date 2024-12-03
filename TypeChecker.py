import AST
from SymbolTable import *


class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):  # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    # def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)


class TypeChecker(NodeVisitor):

    def __init__(self):
        self.symbolTable = SymbolTable(None, "global")

    def error(self, message, node):
        line = getattr(node, "line", "unknown")
        print(f"Error line {line}: {message}")

    def visit_BinExpr(self, node):
        # alternative usage,
        # requires definition of accept method in class Node
        type1 = self.visit(node.left)  # type1 = node.left.accept(self)
        type2 = self.visit(node.right)  # type2 = node.right.accept(self)
        op = node.op
        #

    def visit_UnaryExpr(self, node):
        self.visit(node.operand)

    # to-do: check whether value match the type ?
    def visit_Variable(self, node):
        if not self.symbolTable.get(node.name):
            self.error(f"Variable {node.name} was not defined", node)

    def visit_Program(self, node):
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_IfStatement(self, node):

        self.visit(node.condition)
        self.symbolTable.pushScope("if")
        self.visit(node.body)
        self.symbolTable.popScope()

    def visit_IfElseStatement(self, node):

        self.visit(node.condition)
        self.symbolTable.pushScope("if")
        self.visit(node.if_body)
        self.visit(node.else_body)
        self.symbolTable.popScope()

    # add checking if assignment to matrix/vector element is correct
    # add checking if type is correct (?)
    def visit_AssignmentOrCreation(self, node):

        if self.symbolTable.get(node.target.name):
            pass
        else:
            self.symbolTable.put(node.target.name, VariableSymbol(node.target.name, type(node.value)))

        self.visit(node.value)

    # add checking if assignment to matrix/vector element is correct
    def visit_Assignment(self, node):
        type = self.visit(node.value)

        if not self.symbolTable.get(node.target.name):
            self.error(f"variable {node.target.name} was not defined", node.target)

    def visit_MatrixFunction(self, node):

        if isinstance(node.argument, AST.UnaryExpr):
            if node.argument.op == "-":
                self.error(f"{node.function} argument cannot be less than 0", node)

        elif isinstance(node.argument, (AST.IntNum, AST.Number)):
            try:
                value = int(node.argument.value)

                if value < 0:
                    self.error(f"{node.function} argument cannot be less than 0", node)
            except ValueError:
                self.error(f"{node.function} argument must be an integer", node)

        elif not isinstance(node.argument, AST.Variable):
            self.error(f"{node.function} argument is not recognized", node)

    def visit_Number(self, node):
        pass

    def visit_IntNum(self, node):
        if not isinstance(node.value, int):
            self.error("Unrecogniezed type of IntNum" + type(node.value), node)  # I hope it would never trigger

    def visit_FloatNum(self, node):
        if not isinstance(node.value, float):
            self.error("Unrecognized type of FloatNum" + type(node.value), node)

    # to-do: check if variable creating matrix/vector is valid (has type matching other things there)
    def visit_ArrayCreation(self, node):  # creation of vector or matrix

        if node.elements is None:
            # empty init - like v = [] or m = [[]]
            pass

        matrix_size = None

        for element in node.elements:

            if isinstance(element, AST.ArrayCreation):
                curr_element_size = len(element.elements)

                if matrix_size is None:
                    matrix_size = curr_element_size
                elif matrix_size != curr_element_size:
                    self.error(f"Matrix size is invalid", element)

            elif isinstance(element, (AST.Number, AST.IntNum, AST.FloatNum)):
                curr_element_size = 1
                if matrix_size == None:
                    matrix_size = 1
                elif matrix_size != curr_element_size:
                    self.error(f"Matrix size is invalid", element)

            elif isinstance(element, AST.Variable):
                if not self.symbolTable.get(element.name):
                    self.error(f"Variable {element.name} was not defined", element)

    # to-do: check if variable do not get out of matrix size
    def visit_ArrayAccess(self, node):
        self.visit(node.array)
        self.visit(node.row)
        if node.col is not None:
            self.visit(node.col)

    def visit_ForLoop(self, node):
        self.visit(node.start)
        self.visit(node.end)

        if self.symbolTable.get(node.var.name):
            pass
        else:
            self.symbolTable.put(node.var.name, VariableSymbol(node.var.name, AST.ArrayCreation))

        self.symbolTable = self.symbolTable.pushScope("loop")
        self.visit(node.body)
        self.symbolTable = self.symbolTable.popScope()

    def visit_Block(self, node):
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_WhileLoop(self, node):
        self.visit(node.condition)

        self.symbolTable = self.symbolTable.pushScope("loop")
        self.visit(node.body)
        self.symbolTable = self.symbolTable.popScope()

    def visit_Print(self, node):
        for value in node.values:
            self.visit(value)

    def visit_Break(self, node):
        if "loop" not in self.symbolTable.all_names():
            self.error(f"Instruction break outside of loop", node)

    def visit_Continue(self, node):
        if "loop" not in self.symbolTable.all_names():
            self.error(f"Instruction continue outside of loop", node)

    def visit_Return(self, node):
        self.visit(node.value)

    def visit_String(self, node):
        pass
