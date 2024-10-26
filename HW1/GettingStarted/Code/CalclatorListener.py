from gen.calculatorListener import calculatorListener
from gen.calculatorParser import calculatorParser


class CustomCalculatorListener(calculatorListener):
    def __init__(self):
        self.result = 0

    # Expression:
    def exitExpr(self, ctx:calculatorParser.ExprContext):
        if ctx.getChildCount() == 1:
            self.result = ctx.getChild(0).value
            ctx.value = self.result
        else:
            result = ctx.getChild(0).value
            length = ctx.getChildCount()-1
            for i in range(1,length,2):
                op = ctx.getChild(i).getText()
                if op == '+':
                    value = ctx.getChild(i+1).value
                    result = result + value
                elif op == '-':
                    value = ctx.getChild(i+1).value
                    result = result - value
            self.result = result
            ctx.value = result

    # Term:
    def exitTerm(self, ctx:calculatorParser.TermContext):
        if ctx.getChildCount() == 1:
            ctx.value = ctx.getChild(0).value
        else:
            result = ctx.getChild(0).value
            length = ctx.getChildCount() - 1
            for i in range(1, length, 2):
                op = ctx.getChild(i).getText()
                if op == '*':
                    value = ctx.getChild(i + 1).value
                    result = result * value
                elif op == '/':
                    value = ctx.getChild(i + 1).value
                    result = result / value
            self.result = result
            ctx.value = self.result

    def exitFactor(self, ctx:calculatorParser.FactorContext):
        print(ctx.getChildCount())
        if ctx.getChildCount() == 2:
            sign = 1
            if ctx.getChild(0).getText() == '-':
                sign = -1
                number_text = ctx.getChild(1).getText()
            elif ctx.getChild(0).getText() == '+':
                number_text = ctx.getChild(1).getText()
            else:
                number_text = ctx.getChild(0).getText()

            ctx.value = sign * float(number_text)

        else:
            ctx.value = float(ctx.NUMBER().getText())
