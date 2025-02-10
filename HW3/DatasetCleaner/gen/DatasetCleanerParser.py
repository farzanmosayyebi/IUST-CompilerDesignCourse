# Generated from D:/Elmos/S4031/CompilerDesign/TA1/TA1/HW3/Grammar/DatasetCleaner.g4 by ANTLR 4.13.1
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
        4,1,18,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,1,0,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,58,
        8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,0,66,0,12,1,
        0,0,0,2,25,1,0,0,0,4,47,1,0,0,0,6,49,1,0,0,0,8,57,1,0,0,0,10,59,
        1,0,0,0,12,13,5,3,0,0,13,14,3,10,5,0,14,15,3,2,1,0,15,16,5,0,0,1,
        16,1,1,0,0,0,17,22,3,4,2,0,18,19,5,1,0,0,19,21,3,4,2,0,20,18,1,0,
        0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,26,1,0,0,0,24,22,
        1,0,0,0,25,17,1,0,0,0,25,26,1,0,0,0,26,3,1,0,0,0,27,28,5,4,0,0,28,
        48,5,5,0,0,29,30,5,6,0,0,30,48,5,7,0,0,31,32,5,8,0,0,32,33,5,7,0,
        0,33,34,3,6,3,0,34,35,5,9,0,0,35,36,3,8,4,0,36,48,1,0,0,0,37,38,
        5,10,0,0,38,39,3,6,3,0,39,40,5,13,0,0,40,41,3,8,4,0,41,48,1,0,0,
        0,42,43,5,11,0,0,43,44,3,6,3,0,44,45,5,12,0,0,45,46,3,6,3,0,46,48,
        1,0,0,0,47,27,1,0,0,0,47,29,1,0,0,0,47,31,1,0,0,0,47,37,1,0,0,0,
        47,42,1,0,0,0,48,5,1,0,0,0,49,50,5,16,0,0,50,51,5,15,0,0,51,52,5,
        16,0,0,52,7,1,0,0,0,53,58,5,14,0,0,54,55,5,16,0,0,55,56,5,15,0,0,
        56,58,5,16,0,0,57,53,1,0,0,0,57,54,1,0,0,0,58,9,1,0,0,0,59,60,5,
        16,0,0,60,61,5,15,0,0,61,62,5,2,0,0,62,63,5,15,0,0,63,64,5,16,0,
        0,64,11,1,0,0,0,4,22,25,47,57
    ]

class DatasetCleanerParser ( Parser ):

    grammarFileName = "DatasetCleaner.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'.'", "'CLEAN'", "'REMOVE'", "'DUPLICATES'", 
                     "'DROP'", "'MISSING'", "'FILL'", "'WITH'", "'FILTER'", 
                     "'RENAME'", "'TO'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "CLEAN", "REMOVE", 
                      "DUPLICATES", "DROP", "MISSING", "FILL", "WITH", "FILTER", 
                      "RENAME", "TO", "COMPARISON_OPERATOR", "NUMBER", "STRING", 
                      "QUOTE", "WS", "NEWLINE" ]

    RULE_cleaning = 0
    RULE_commandList = 1
    RULE_command = 2
    RULE_column = 3
    RULE_value = 4
    RULE_file_path = 5

    ruleNames =  [ "cleaning", "commandList", "command", "column", "value", 
                   "file_path" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    CLEAN=3
    REMOVE=4
    DUPLICATES=5
    DROP=6
    MISSING=7
    FILL=8
    WITH=9
    FILTER=10
    RENAME=11
    TO=12
    COMPARISON_OPERATOR=13
    NUMBER=14
    STRING=15
    QUOTE=16
    WS=17
    NEWLINE=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CleaningContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.datatype = str()

        def CLEAN(self):
            return self.getToken(DatasetCleanerParser.CLEAN, 0)

        def file_path(self):
            return self.getTypedRuleContext(DatasetCleanerParser.File_pathContext,0)


        def commandList(self):
            return self.getTypedRuleContext(DatasetCleanerParser.CommandListContext,0)


        def EOF(self):
            return self.getToken(DatasetCleanerParser.EOF, 0)

        def getRuleIndex(self):
            return DatasetCleanerParser.RULE_cleaning

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCleaning" ):
                listener.enterCleaning(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCleaning" ):
                listener.exitCleaning(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCleaning" ):
                return visitor.visitCleaning(self)
            else:
                return visitor.visitChildren(self)




    def cleaning(self):

        localctx = DatasetCleanerParser.CleaningContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_cleaning)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(DatasetCleanerParser.CLEAN)
            self.state = 13
            self.file_path()
            self.state = 14
            self.commandList()
            self.state = 15
            self.match(DatasetCleanerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.datatype = str()

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DatasetCleanerParser.CommandContext)
            else:
                return self.getTypedRuleContext(DatasetCleanerParser.CommandContext,i)


        def getRuleIndex(self):
            return DatasetCleanerParser.RULE_commandList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandList" ):
                listener.enterCommandList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandList" ):
                listener.exitCommandList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandList" ):
                return visitor.visitCommandList(self)
            else:
                return visitor.visitChildren(self)




    def commandList(self):

        localctx = DatasetCleanerParser.CommandListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commandList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3408) != 0):
                self.state = 17
                self.command()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 18
                    self.match(DatasetCleanerParser.T__0)
                    self.state = 19
                    self.command()
                    self.state = 24
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.datatype = str()


        def getRuleIndex(self):
            return DatasetCleanerParser.RULE_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.datatype = ctx.datatype



    class FillMissCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatasetCleanerParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FILL(self):
            return self.getToken(DatasetCleanerParser.FILL, 0)
        def MISSING(self):
            return self.getToken(DatasetCleanerParser.MISSING, 0)
        def column(self):
            return self.getTypedRuleContext(DatasetCleanerParser.ColumnContext,0)

        def WITH(self):
            return self.getToken(DatasetCleanerParser.WITH, 0)
        def value(self):
            return self.getTypedRuleContext(DatasetCleanerParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFillMissCommand" ):
                listener.enterFillMissCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFillMissCommand" ):
                listener.exitFillMissCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFillMissCommand" ):
                return visitor.visitFillMissCommand(self)
            else:
                return visitor.visitChildren(self)


    class RmvDupCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatasetCleanerParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REMOVE(self):
            return self.getToken(DatasetCleanerParser.REMOVE, 0)
        def DUPLICATES(self):
            return self.getToken(DatasetCleanerParser.DUPLICATES, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRmvDupCommand" ):
                listener.enterRmvDupCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRmvDupCommand" ):
                listener.exitRmvDupCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRmvDupCommand" ):
                return visitor.visitRmvDupCommand(self)
            else:
                return visitor.visitChildren(self)


    class FilterCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatasetCleanerParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FILTER(self):
            return self.getToken(DatasetCleanerParser.FILTER, 0)
        def column(self):
            return self.getTypedRuleContext(DatasetCleanerParser.ColumnContext,0)

        def COMPARISON_OPERATOR(self):
            return self.getToken(DatasetCleanerParser.COMPARISON_OPERATOR, 0)
        def value(self):
            return self.getTypedRuleContext(DatasetCleanerParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterCommand" ):
                listener.enterFilterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterCommand" ):
                listener.exitFilterCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterCommand" ):
                return visitor.visitFilterCommand(self)
            else:
                return visitor.visitChildren(self)


    class DrpMissCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatasetCleanerParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DROP(self):
            return self.getToken(DatasetCleanerParser.DROP, 0)
        def MISSING(self):
            return self.getToken(DatasetCleanerParser.MISSING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrpMissCommand" ):
                listener.enterDrpMissCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrpMissCommand" ):
                listener.exitDrpMissCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrpMissCommand" ):
                return visitor.visitDrpMissCommand(self)
            else:
                return visitor.visitChildren(self)


    class RenameCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatasetCleanerParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RENAME(self):
            return self.getToken(DatasetCleanerParser.RENAME, 0)
        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DatasetCleanerParser.ColumnContext)
            else:
                return self.getTypedRuleContext(DatasetCleanerParser.ColumnContext,i)

        def TO(self):
            return self.getToken(DatasetCleanerParser.TO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRenameCommand" ):
                listener.enterRenameCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRenameCommand" ):
                listener.exitRenameCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRenameCommand" ):
                return visitor.visitRenameCommand(self)
            else:
                return visitor.visitChildren(self)



    def command(self):

        localctx = DatasetCleanerParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = DatasetCleanerParser.RmvDupCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(DatasetCleanerParser.REMOVE)
                self.state = 28
                self.match(DatasetCleanerParser.DUPLICATES)
                pass
            elif token in [6]:
                localctx = DatasetCleanerParser.DrpMissCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(DatasetCleanerParser.DROP)
                self.state = 30
                self.match(DatasetCleanerParser.MISSING)
                pass
            elif token in [8]:
                localctx = DatasetCleanerParser.FillMissCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(DatasetCleanerParser.FILL)
                self.state = 32
                self.match(DatasetCleanerParser.MISSING)
                self.state = 33
                self.column()
                self.state = 34
                self.match(DatasetCleanerParser.WITH)
                self.state = 35
                self.value()
                pass
            elif token in [10]:
                localctx = DatasetCleanerParser.FilterCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.match(DatasetCleanerParser.FILTER)
                self.state = 38
                self.column()
                self.state = 39
                self.match(DatasetCleanerParser.COMPARISON_OPERATOR)
                self.state = 40
                self.value()
                pass
            elif token in [11]:
                localctx = DatasetCleanerParser.RenameCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.match(DatasetCleanerParser.RENAME)
                self.state = 43
                self.column()
                self.state = 44
                self.match(DatasetCleanerParser.TO)
                self.state = 45
                self.column()
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


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.datatype = str()

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(DatasetCleanerParser.QUOTE)
            else:
                return self.getToken(DatasetCleanerParser.QUOTE, i)

        def STRING(self):
            return self.getToken(DatasetCleanerParser.STRING, 0)

        def getRuleIndex(self):
            return DatasetCleanerParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn" ):
                return visitor.visitColumn(self)
            else:
                return visitor.visitChildren(self)




    def column(self):

        localctx = DatasetCleanerParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(DatasetCleanerParser.QUOTE)
            self.state = 50
            self.match(DatasetCleanerParser.STRING)
            self.state = 51
            self.match(DatasetCleanerParser.QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.datatype = str()

        def NUMBER(self):
            return self.getToken(DatasetCleanerParser.NUMBER, 0)

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(DatasetCleanerParser.QUOTE)
            else:
                return self.getToken(DatasetCleanerParser.QUOTE, i)

        def STRING(self):
            return self.getToken(DatasetCleanerParser.STRING, 0)

        def getRuleIndex(self):
            return DatasetCleanerParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = DatasetCleanerParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(DatasetCleanerParser.NUMBER)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(DatasetCleanerParser.QUOTE)
                self.state = 55
                self.match(DatasetCleanerParser.STRING)
                self.state = 56
                self.match(DatasetCleanerParser.QUOTE)
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


    class File_pathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.datatype = str()


        def getRuleIndex(self):
            return DatasetCleanerParser.RULE_file_path

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.datatype = ctx.datatype



    class FilePathContext(File_pathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatasetCleanerParser.File_pathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(DatasetCleanerParser.QUOTE)
            else:
                return self.getToken(DatasetCleanerParser.QUOTE, i)
        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(DatasetCleanerParser.STRING)
            else:
                return self.getToken(DatasetCleanerParser.STRING, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilePath" ):
                listener.enterFilePath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilePath" ):
                listener.exitFilePath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilePath" ):
                return visitor.visitFilePath(self)
            else:
                return visitor.visitChildren(self)



    def file_path(self):

        localctx = DatasetCleanerParser.File_pathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_file_path)
        try:
            localctx = DatasetCleanerParser.FilePathContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(DatasetCleanerParser.QUOTE)
            self.state = 60
            self.match(DatasetCleanerParser.STRING)
            self.state = 61
            self.match(DatasetCleanerParser.T__1)
            self.state = 62
            self.match(DatasetCleanerParser.STRING)
            self.state = 63
            self.match(DatasetCleanerParser.QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





