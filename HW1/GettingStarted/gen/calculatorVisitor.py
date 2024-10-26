# Generated from D:/Elmos/S4031/CompilerDesign/TA1/TA1/1-GettingStarted/1-GettingStarted/grammar/calculator.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .calculatorParser import calculatorParser
else:
    from calculatorParser import calculatorParser

# This class defines a complete generic visitor for a parse tree produced by calculatorParser.

class calculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calculatorParser#start.
    def visitStart(self, ctx:calculatorParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#expr.
    def visitExpr(self, ctx:calculatorParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#term.
    def visitTerm(self, ctx:calculatorParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#factor.
    def visitFactor(self, ctx:calculatorParser.FactorContext):
        return self.visitChildren(ctx)



del calculatorParser