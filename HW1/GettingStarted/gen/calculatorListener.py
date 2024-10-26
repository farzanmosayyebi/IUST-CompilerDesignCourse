# Generated from D:/Elmos/S4031/CompilerDesign/TA1/TA1/1-GettingStarted/1-GettingStarted/grammar/calculator.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .calculatorParser import calculatorParser
else:
    from calculatorParser import calculatorParser

# This class defines a complete listener for a parse tree produced by calculatorParser.
class calculatorListener(ParseTreeListener):

    # Enter a parse tree produced by calculatorParser#start.
    def enterStart(self, ctx:calculatorParser.StartContext):
        pass

    # Exit a parse tree produced by calculatorParser#start.
    def exitStart(self, ctx:calculatorParser.StartContext):
        pass


    # Enter a parse tree produced by calculatorParser#expr.
    def enterExpr(self, ctx:calculatorParser.ExprContext):
        pass

    # Exit a parse tree produced by calculatorParser#expr.
    def exitExpr(self, ctx:calculatorParser.ExprContext):
        pass


    # Enter a parse tree produced by calculatorParser#term.
    def enterTerm(self, ctx:calculatorParser.TermContext):
        pass

    # Exit a parse tree produced by calculatorParser#term.
    def exitTerm(self, ctx:calculatorParser.TermContext):
        pass


    # Enter a parse tree produced by calculatorParser#factor.
    def enterFactor(self, ctx:calculatorParser.FactorContext):
        pass

    # Exit a parse tree produced by calculatorParser#factor.
    def exitFactor(self, ctx:calculatorParser.FactorContext):
        pass



del calculatorParser