import sys
from scanner_sly import Scanner
from parser_sly import MyParser
from TreePrinter import TreePrinter


# if __name__ == '__main__':
#
#     try:
#         filename = sys.argv[1] if len(sys.argv) > 1 else "lab4_examples/control_transfer.txt"
#         file = open(filename, "r")
#     except IOError:
#         print("Cannot open {0} file".format(filename))
#         sys.exit(0)
#
#     text = file.read()
#     lexer = Scanner()
#     parser = MyParser()
#
#     ast = parser.parse(lexer.tokenize(text))
#     ast.printTree()


# lab 4
import sys
from scanner_sly import Scanner
from parser_sly import MyParser
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "lab4_examples/control_transfer.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    lexer = Scanner()
    parser = MyParser()

    ast = parser.parse(lexer.tokenize(text))
    ast.printTree()

    typeChecker = TypeChecker()
    typeChecker.visit(ast)   # or alternatively ast.accept(typeChecker)
