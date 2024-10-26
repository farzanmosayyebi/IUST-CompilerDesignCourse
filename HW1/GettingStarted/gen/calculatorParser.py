# Generated from D:/Elmos/S4031/CompilerDesign/TA1/TA1/1-GettingStarted/1-GettingStarted/grammar/calculator.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,38,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        5,1,15,8,1,10,1,12,1,18,9,1,1,2,1,2,1,2,5,2,23,8,2,10,2,12,2,26,
        9,2,1,3,3,3,29,8,3,1,3,1,3,1,3,1,3,1,3,3,3,36,8,3,1,3,0,0,4,0,2,
        4,6,0,2,1,0,1,2,1,0,3,4,37,0,8,1,0,0,0,2,11,1,0,0,0,4,19,1,0,0,0,
        6,35,1,0,0,0,8,9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,16,3,4,2,0,
        12,13,7,0,0,0,13,15,3,4,2,0,14,12,1,0,0,0,15,18,1,0,0,0,16,14,1,
        0,0,0,16,17,1,0,0,0,17,3,1,0,0,0,18,16,1,0,0,0,19,24,3,6,3,0,20,
        21,7,1,0,0,21,23,3,6,3,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,
        0,24,25,1,0,0,0,25,5,1,0,0,0,26,24,1,0,0,0,27,29,7,0,0,0,28,27,1,
        0,0,0,28,29,1,0,0,0,29,30,1,0,0,0,30,36,5,7,0,0,31,32,5,5,0,0,32,
        33,3,2,1,0,33,34,5,6,0,0,34,36,1,0,0,0,35,28,1,0,0,0,35,31,1,0,0,
        0,36,7,1,0,0,0,4,16,24,28,35
    ]

class calculatorParser ( Parser ):

    grammarFileName = "calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "ADD", "SUB", "MUL", "DIV", "LPAREN", 
                      "RPAREN", "NUMBER", "WS" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3

    ruleNames =  [ "start", "expr", "term", "factor" ]

    EOF = Token.EOF
    ADD=1
    SUB=2
    MUL=3
    DIV=4
    LPAREN=5
    RPAREN=6
    NUMBER=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(calculatorParser.ExprContext,0)


        def EOF(self):
            return self.getToken(calculatorParser.EOF, 0)

        def getRuleIndex(self):
            return calculatorParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = calculatorParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr()
            self.state = 9
            self.match(calculatorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculatorParser.TermContext)
            else:
                return self.getTypedRuleContext(calculatorParser.TermContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(calculatorParser.ADD)
            else:
                return self.getToken(calculatorParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(calculatorParser.SUB)
            else:
                return self.getToken(calculatorParser.SUB, i)

        def getRuleIndex(self):
            return calculatorParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = calculatorParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.term()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 12
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 13
                self.term()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculatorParser.FactorContext)
            else:
                return self.getTypedRuleContext(calculatorParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(calculatorParser.MUL)
            else:
                return self.getToken(calculatorParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(calculatorParser.DIV)
            else:
                return self.getToken(calculatorParser.DIV, i)

        def getRuleIndex(self):
            return calculatorParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = calculatorParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.factor()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 20
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 21
                self.factor()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(calculatorParser.NUMBER, 0)

        def ADD(self):
            return self.getToken(calculatorParser.ADD, 0)

        def SUB(self):
            return self.getToken(calculatorParser.SUB, 0)

        def LPAREN(self):
            return self.getToken(calculatorParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(calculatorParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(calculatorParser.RPAREN, 0)

        def getRuleIndex(self):
            return calculatorParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = calculatorParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1 or _la==2:
                    self.state = 27
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 30
                self.match(calculatorParser.NUMBER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(calculatorParser.LPAREN)
                self.state = 32
                self.expr()
                self.state = 33
                self.match(calculatorParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





