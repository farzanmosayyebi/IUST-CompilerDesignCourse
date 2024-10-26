# Generated from E:/IUST/TA/Compiler-14031/antlr_projects/2-TypeChecker/TypeChecker.g4 by ANTLR 4.13.2
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
        4,1,13,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,1,4,1,17,8,1,11,1,12,1,18,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,35,8,3,10,3,12,3,38,9,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,49,8,4,10,4,12,4,52,9,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,3,5,61,8,5,1,5,0,2,6,8,6,0,2,4,6,8,10,0,0,64,0,
        12,1,0,0,0,2,16,1,0,0,0,4,20,1,0,0,0,6,25,1,0,0,0,8,39,1,0,0,0,10,
        60,1,0,0,0,12,13,3,2,1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,17,3,4,2,
        0,16,15,1,0,0,0,17,18,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,3,1,
        0,0,0,20,21,5,12,0,0,21,22,5,6,0,0,22,23,3,6,3,0,23,24,5,1,0,0,24,
        5,1,0,0,0,25,26,6,3,-1,0,26,27,3,8,4,0,27,36,1,0,0,0,28,29,10,3,
        0,0,29,30,5,2,0,0,30,35,3,8,4,0,31,32,10,2,0,0,32,33,5,3,0,0,33,
        35,3,8,4,0,34,28,1,0,0,0,34,31,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,
        0,36,37,1,0,0,0,37,7,1,0,0,0,38,36,1,0,0,0,39,40,6,4,-1,0,40,41,
        3,10,5,0,41,50,1,0,0,0,42,43,10,3,0,0,43,44,5,4,0,0,44,49,3,10,5,
        0,45,46,10,2,0,0,46,47,5,5,0,0,47,49,3,10,5,0,48,42,1,0,0,0,48,45,
        1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,9,1,0,0,0,52,
        50,1,0,0,0,53,61,5,11,0,0,54,61,5,9,0,0,55,61,5,10,0,0,56,57,5,7,
        0,0,57,58,3,6,3,0,58,59,5,8,0,0,59,61,1,0,0,0,60,53,1,0,0,0,60,54,
        1,0,0,0,60,55,1,0,0,0,60,56,1,0,0,0,61,11,1,0,0,0,6,18,34,36,48,
        50,60
    ]

class TypeCheckerParser ( Parser ):

    grammarFileName = "TypeChecker.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'+'", "'-'", "'*'", "'/'", "'='", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "PLUS", "MINUS", "MUL", 
                      "DIV", "ASSIGN", "LPAREN", "RPAREN", "INTEGER", "FLOAT", 
                      "STRING", "ID", "WS" ]

    RULE_start = 0
    RULE_assigns = 1
    RULE_assign = 2
    RULE_expr = 3
    RULE_term = 4
    RULE_fact = 5

    ruleNames =  [ "start", "assigns", "assign", "expr", "term", "fact" ]

    EOF = Token.EOF
    T__0=1
    PLUS=2
    MINUS=3
    MUL=4
    DIV=5
    ASSIGN=6
    LPAREN=7
    RPAREN=8
    INTEGER=9
    FLOAT=10
    STRING=11
    ID=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assigns(self):
            return self.getTypedRuleContext(TypeCheckerParser.AssignsContext,0)


        def EOF(self):
            return self.getToken(TypeCheckerParser.EOF, 0)

        def getRuleIndex(self):
            return TypeCheckerParser.RULE_start

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

        localctx = TypeCheckerParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.assigns()
            self.state = 13
            self.match(TypeCheckerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.AssignContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.AssignContext,i)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_assigns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigns" ):
                listener.enterAssigns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigns" ):
                listener.exitAssigns(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigns" ):
                return visitor.visitAssigns(self)
            else:
                return visitor.visitChildren(self)




    def assigns(self):

        localctx = TypeCheckerParser.AssignsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assigns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 15
                self.assign()
                self.state = 18 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==12):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = str()

        def ID(self):
            return self.getToken(TypeCheckerParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(TypeCheckerParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExprContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = TypeCheckerParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(TypeCheckerParser.ID)
            self.state = 21
            self.match(TypeCheckerParser.ASSIGN)
            self.state = 22
            self.expr(0)
            self.state = 23
            self.match(TypeCheckerParser.T__0)
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
            self.datatype = str()


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.datatype = ctx.datatype


    class ExprPlusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExprContext,0)

        def PLUS(self):
            return self.getToken(TypeCheckerParser.PLUS, 0)
        def term(self):
            return self.getTypedRuleContext(TypeCheckerParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPlus" ):
                listener.enterExprPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPlus" ):
                listener.exitExprPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPlus" ):
                return visitor.visitExprPlus(self)
            else:
                return visitor.visitChildren(self)


    class ExprMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExprContext,0)

        def MINUS(self):
            return self.getToken(TypeCheckerParser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(TypeCheckerParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMinus" ):
                listener.enterExprMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMinus" ):
                listener.exitExprMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMinus" ):
                return visitor.visitExprMinus(self)
            else:
                return visitor.visitChildren(self)


    class ExprTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(TypeCheckerParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprTerm" ):
                listener.enterExprTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprTerm" ):
                listener.exitExprTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprTerm" ):
                return visitor.visitExprTerm(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TypeCheckerParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = TypeCheckerParser.ExprTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 26
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = TypeCheckerParser.ExprPlusContext(self, TypeCheckerParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 29
                        self.match(TypeCheckerParser.PLUS)
                        self.state = 30
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = TypeCheckerParser.ExprMinusContext(self, TypeCheckerParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 32
                        self.match(TypeCheckerParser.MINUS)
                        self.state = 33
                        self.term(0)
                        pass

             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.datatype = str()


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.datatype = ctx.datatype


    class TermDivContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(TypeCheckerParser.TermContext,0)

        def DIV(self):
            return self.getToken(TypeCheckerParser.DIV, 0)
        def fact(self):
            return self.getTypedRuleContext(TypeCheckerParser.FactContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermDiv" ):
                listener.enterTermDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermDiv" ):
                listener.exitTermDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermDiv" ):
                return visitor.visitTermDiv(self)
            else:
                return visitor.visitChildren(self)


    class TermMulContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(TypeCheckerParser.TermContext,0)

        def MUL(self):
            return self.getToken(TypeCheckerParser.MUL, 0)
        def fact(self):
            return self.getTypedRuleContext(TypeCheckerParser.FactContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermMul" ):
                listener.enterTermMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermMul" ):
                listener.exitTermMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermMul" ):
                return visitor.visitTermMul(self)
            else:
                return visitor.visitChildren(self)


    class TermFactContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fact(self):
            return self.getTypedRuleContext(TypeCheckerParser.FactContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermFact" ):
                listener.enterTermFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermFact" ):
                listener.exitTermFact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermFact" ):
                return visitor.visitTermFact(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TypeCheckerParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = TypeCheckerParser.TermFactContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 40
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = TypeCheckerParser.TermMulContext(self, TypeCheckerParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 42
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 43
                        self.match(TypeCheckerParser.MUL)
                        self.state = 44
                        self.fact()
                        pass

                    elif la_ == 2:
                        localctx = TypeCheckerParser.TermDivContext(self, TypeCheckerParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 45
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 46
                        self.match(TypeCheckerParser.DIV)
                        self.state = 47
                        self.fact()
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.datatype = str()


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_fact

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.datatype = ctx.datatype



    class FactIntegerContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(TypeCheckerParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactInteger" ):
                listener.enterFactInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactInteger" ):
                listener.exitFactInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactInteger" ):
                return visitor.visitFactInteger(self)
            else:
                return visitor.visitChildren(self)


    class FactExprContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(TypeCheckerParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(TypeCheckerParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactExpr" ):
                listener.enterFactExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactExpr" ):
                listener.exitFactExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactExpr" ):
                return visitor.visitFactExpr(self)
            else:
                return visitor.visitChildren(self)


    class FactFloatContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(TypeCheckerParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactFloat" ):
                listener.enterFactFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactFloat" ):
                listener.exitFactFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactFloat" ):
                return visitor.visitFactFloat(self)
            else:
                return visitor.visitChildren(self)


    class FactStringContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(TypeCheckerParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactString" ):
                listener.enterFactString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactString" ):
                listener.exitFactString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactString" ):
                return visitor.visitFactString(self)
            else:
                return visitor.visitChildren(self)



    def fact(self):

        localctx = TypeCheckerParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fact)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = TypeCheckerParser.FactStringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(TypeCheckerParser.STRING)
                pass
            elif token in [9]:
                localctx = TypeCheckerParser.FactIntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(TypeCheckerParser.INTEGER)
                pass
            elif token in [10]:
                localctx = TypeCheckerParser.FactFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.match(TypeCheckerParser.FLOAT)
                pass
            elif token in [7]:
                localctx = TypeCheckerParser.FactExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.match(TypeCheckerParser.LPAREN)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(TypeCheckerParser.RPAREN)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        self._predicates[4] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




