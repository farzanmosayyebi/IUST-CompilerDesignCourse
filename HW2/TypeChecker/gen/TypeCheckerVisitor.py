# Generated from E:/IUST/TA/Compiler-14031/antlr_projects/2-TypeChecker/TypeChecker.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TypeCheckerParser import TypeCheckerParser
else:
    from TypeCheckerParser import TypeCheckerParser

# This class defines a complete generic visitor for a parse tree produced by TypeCheckerParser.

class TypeCheckerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TypeCheckerParser#start.
    def visitStart(self, ctx:TypeCheckerParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#assigns.
    def visitAssigns(self, ctx:TypeCheckerParser.AssignsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#assign.
    def visitAssign(self, ctx:TypeCheckerParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#exprPlus.
    def visitExprPlus(self, ctx:TypeCheckerParser.ExprPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#exprMinus.
    def visitExprMinus(self, ctx:TypeCheckerParser.ExprMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#exprTerm.
    def visitExprTerm(self, ctx:TypeCheckerParser.ExprTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#termDiv.
    def visitTermDiv(self, ctx:TypeCheckerParser.TermDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#termMul.
    def visitTermMul(self, ctx:TypeCheckerParser.TermMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#termFact.
    def visitTermFact(self, ctx:TypeCheckerParser.TermFactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#factString.
    def visitFactString(self, ctx:TypeCheckerParser.FactStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#factInteger.
    def visitFactInteger(self, ctx:TypeCheckerParser.FactIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#factFloat.
    def visitFactFloat(self, ctx:TypeCheckerParser.FactFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#factExpr.
    def visitFactExpr(self, ctx:TypeCheckerParser.FactExprContext):
        return self.visitChildren(ctx)



del TypeCheckerParser