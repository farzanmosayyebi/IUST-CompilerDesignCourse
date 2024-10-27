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

        # I modified this line
        elif leftType == "STRING" and (rightType == "INTEGER" or rightType == "FLOAT"):
            ctx.datatype = "STRING"
        else:
            raise TypeError('Datatype mismatch!')

    def exitTermFact(self, ctx:TypeCheckerParser.TermMulContext):
        ctx.datatype = ctx.getChild(0).datatype

    ############## I added the following methods ################

    def exitTermMul(self, ctx:TypeCheckerParser.TermMulContext):
        left_type = ctx.getChild(0).datatype
        right_type = ctx.getChild(2).datatype

        if left_type == "STRING" or right_type == "STRING":
            raise TypeError("Invalid operation!")

        if left_type == right_type:
            result_type = left_type

        elif (left_type == "INTEGER" and right_type == "FLOAT") \
            or (left_type == "FLOAT" and right_type == "INTEGER"):
            result_type = "FLOAT"

        else:
            raise TypeError('Datatype mismatch!')

        ctx.datatype = result_type

    # I added this
    def exitTermDiv(self, ctx:TypeCheckerParser.TermDivContext):
        left_type = ctx.getChild(0).datatype
        right_type = ctx.getChild(2).datatype

        if left_type == "STRING" or right_type == "STRING":
            raise TypeError('Invalid operation!')
        else:
            result_type = "FLOAT"

        ctx.datatype = result_type

    # I added this
    def exitExprMinus(self, ctx:TypeCheckerParser.ExprMinusContext):
        left_type = ctx.getChild(0).datatype
        right_type = ctx.getChild(2).datatype

        if left_type == "STRING" or right_type == "STRING":
            raise TypeError("Invalid operation!")

        if left_type == right_type:
            result_type = left_type

        elif (left_type == "INTEGER" and right_type == "FLOAT") \
                or (left_type == "FLOAT" and right_type == "INTEGER"):
            result_type = "FLOAT"

        else:
            raise TypeError('Datatype mismatch!')

        ctx.datatype = result_type

    # I added this
    def exitFactFloat(self, ctx:TypeCheckerParser.FactFloatContext):
        ctx.datatype = "FLOAT"