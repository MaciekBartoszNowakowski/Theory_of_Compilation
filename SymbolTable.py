#!/usr/bin/python


from time import sleep
from symtable import Symbol


class VariableSymbol(Symbol):

    def __init__(self, name, type):
        self.name = name
        self.type = type


class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.symbols = {}
    #

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        if name in self.symbols:
            print(f"Variable {name} already defined")
        self.symbols[name] = symbol
    #

    def get(self, name): # get variable symbol or fundef from <name> entry
        searched_table = self
        while searched_table is not None:
            if name in searched_table.symbols.keys():
                return searched_table.symbols[name]
            else:
                searched_table = searched_table.getParentScope()
        return
    #

    def getParentScope(self):
        return self.parent
    #

    def all_names(self):
        names = [self.name]
        curr_table = self.getParentScope()
        while curr_table is not None:
            names.append(curr_table.name)
            curr_table = curr_table.getParentScope()

        return names

    def pushScope(self, name):
        return SymbolTable(self, name)
    #

    def popScope(self):
        self.name = None
        return self.parent
    #
