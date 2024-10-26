from gen.TypeCheckerListener import TypeCheckerListener
from gen.TypeCheckerParser import TypeCheckerParser


class CustomTypeCheckerListener(TypeCheckerListener):
    def __init__(self):
        pass

    def exitAssign(self, ctx:TypeCheckerParser.AssignContext):
        print(f'Datatype of {ctx.getChild(0).getText()} is: {ctx.getChild(2).datatype}')

    def exitFactInteger(self, ctx:TypeCheckerParser.FactIntegerContext):
        ctx.datatype = "INTEGER"

    def exitFactString(self, ctx:TypeCheckerParser.FactStringContext):
        ctx.datatype = "STRING"

    def exitExprTerm(self, ctx:TypeCheckerParser.ExprTermContext):
        ctx.datatype = ctx.getChild(0).datatype

    def exitExprPlus(self, ctx:TypeCheckerParser.ExprPlusContext):
        leftType = ctx.getChild(0).datatype
        rightType = ctx.getChild(2).datatype

        if leftType == rightType:
            ctx.datatype = leftType # or rightType
        elif leftType == "FLOAT" and rightType == "INTEGER":
            ctx.datatype = "FLOAT"
        elif leftType == "INTEGER" and rightType == "FLOAT":
            ctx.datatype = "FLOAT"
        elif leftType == "STRING" or rightType == "STRING":
            ctx.datatype = "STRING"
        else:
            raise TypeError('Datatype mismatch!')

    def exitTermFact(self, ctx:TypeCheckerParser.TermMulContext):
        ctx.datatype = ctx.getChild(0).datatype
