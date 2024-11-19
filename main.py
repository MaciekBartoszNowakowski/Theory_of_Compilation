import sys
from scanner_sly import Scanner
from parser_sly import MyParser


# if __name__ == '__main__':
#
#     try:
#         filename = sys.argv[1] if len(sys.argv) > 1 else "lab2_examples/ex3.txt"
#         file = open(filename, "r")
#     except IOError:
#         print("Cannot open {0} file".format(filename))
#         sys.exit(0)
#
#     text = file.read()
#     lexer = Scanner()
#     parser = MyParser()
#
#
#     parser.parse(lexer.tokenize(text))



# import sys
# from scanner_sly import Scanner
# from parser_sly import Mparser
# from TreePrinter import TreePrinter
#
#
# if __name__ == '__main__':
#
#     try:
#         filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
#         file = open(filename, "r")
#     except IOError:
#         print("Cannot open {0} file".format(filename))
#         sys.exit(0)
#
#     text = file.read()
#     lexer = Scanner()
#     parser = Mparser()
#
#     ast = parser.parse(lexer.tokenize(text))
#     ast.printTree()

import sys
from scanner_sly import Scanner
from parser_sly import MyParser
from TreePrinter import TreePrinter


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "lab3_examples/ex1.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    lexer = Scanner()
    parser = MyParser()

    ast = parser.parse(lexer.tokenize(text))
    ast.printTree()