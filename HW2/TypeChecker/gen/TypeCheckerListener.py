# Generated from D:/Elmos/S4031/CompilerDesign/IUST-CompilerDesignCourse/HW2/TypeChecker/TypeChecker.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TypeCheckerParser import TypeCheckerParser
else:
    from TypeCheckerParser import TypeCheckerParser

# This class defines a complete listener for a parse tree produced by TypeCheckerParser.
class TypeCheckerListener(ParseTreeListener):

    # Enter a parse tree produced by TypeCheckerParser#start.
    def enterStart(self, ctx:TypeCheckerParser.StartContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#start.
    def exitStart(self, ctx:TypeCheckerParser.StartContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#assigns.
    def enterAssigns(self, ctx:TypeCheckerParser.AssignsContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#assigns.
    def exitAssigns(self, ctx:TypeCheckerParser.AssignsContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#assign.
    def enterAssign(self, ctx:TypeCheckerParser.AssignContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#assign.
    def exitAssign(self, ctx:TypeCheckerParser.AssignContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#exprPlus.
    def enterExprPlus(self, ctx:TypeCheckerParser.ExprPlusContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#exprPlus.
    def exitExprPlus(self, ctx:TypeCheckerParser.ExprPlusContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#exprMinus.
    def enterExprMinus(self, ctx:TypeCheckerParser.ExprMinusContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#exprMinus.
    def exitExprMinus(self, ctx:TypeCheckerParser.ExprMinusContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#exprTerm.
    def enterExprTerm(self, ctx:TypeCheckerParser.ExprTermContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#exprTerm.
    def exitExprTerm(self, ctx:TypeCheckerParser.ExprTermContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#termDiv.
    def enterTermDiv(self, ctx:TypeCheckerParser.TermDivContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#termDiv.
    def exitTermDiv(self, ctx:TypeCheckerParser.TermDivContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#termMul.
    def enterTermMul(self, ctx:TypeCheckerParser.TermMulContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#termMul.
    def exitTermMul(self, ctx:TypeCheckerParser.TermMulContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#termFact.
    def enterTermFact(self, ctx:TypeCheckerParser.TermFactContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#termFact.
    def exitTermFact(self, ctx:TypeCheckerParser.TermFactContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#factString.
    def enterFactString(self, ctx:TypeCheckerParser.FactStringContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#factString.
    def exitFactString(self, ctx:TypeCheckerParser.FactStringContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#factInteger.
    def enterFactInteger(self, ctx:TypeCheckerParser.FactIntegerContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#factInteger.
    def exitFactInteger(self, ctx:TypeCheckerParser.FactIntegerContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#factFloat.
    def enterFactFloat(self, ctx:TypeCheckerParser.FactFloatContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#factFloat.
    def exitFactFloat(self, ctx:TypeCheckerParser.FactFloatContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#factExpr.
    def enterFactExpr(self, ctx:TypeCheckerParser.FactExprContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#factExpr.
    def exitFactExpr(self, ctx:TypeCheckerParser.FactExprContext):
        pass



del TypeCheckerParser