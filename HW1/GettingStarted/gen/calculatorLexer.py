# Generated from D:/Elmos/S4031/CompilerDesign/TA1/TA1/1-GettingStarted/1-GettingStarted/grammar/calculator.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,58,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,
        6,5,6,31,8,6,10,6,12,6,34,9,6,1,6,1,6,4,6,38,8,6,11,6,12,6,39,1,
        6,4,6,43,8,6,11,6,12,6,44,1,6,3,6,48,8,6,3,6,50,8,6,1,7,4,7,53,8,
        7,11,7,12,7,54,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,
        1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,63,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,1,17,1,0,0,0,3,19,1,0,0,0,5,21,1,0,0,0,7,23,1,0,0,0,9,
        25,1,0,0,0,11,27,1,0,0,0,13,49,1,0,0,0,15,52,1,0,0,0,17,18,5,43,
        0,0,18,2,1,0,0,0,19,20,5,45,0,0,20,4,1,0,0,0,21,22,5,42,0,0,22,6,
        1,0,0,0,23,24,5,47,0,0,24,8,1,0,0,0,25,26,5,40,0,0,26,10,1,0,0,0,
        27,28,5,41,0,0,28,12,1,0,0,0,29,31,7,0,0,0,30,29,1,0,0,0,31,34,1,
        0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,32,1,0,0,0,35,
        37,5,46,0,0,36,38,7,0,0,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,
        0,0,39,40,1,0,0,0,40,50,1,0,0,0,41,43,7,0,0,0,42,41,1,0,0,0,43,44,
        1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,48,5,46,0,0,
        47,46,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,32,1,0,0,0,49,42,1,
        0,0,0,50,14,1,0,0,0,51,53,7,1,0,0,52,51,1,0,0,0,53,54,1,0,0,0,54,
        52,1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,57,6,7,0,0,57,16,1,0,0,
        0,7,0,32,39,44,47,49,54,1,6,0,0
    ]

class calculatorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    LPAREN = 5
    RPAREN = 6
    NUMBER = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUB", "MUL", "DIV", "LPAREN", "RPAREN", "NUMBER", "WS" ]

    ruleNames = [ "ADD", "SUB", "MUL", "DIV", "LPAREN", "RPAREN", "NUMBER", 
                  "WS" ]

    grammarFileName = "calculator.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


