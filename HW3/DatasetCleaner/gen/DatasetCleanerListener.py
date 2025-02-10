# Generated from D:/Elmos/S4031/CompilerDesign/TA1/TA1/HW3/Grammar/DatasetCleaner.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DatasetCleanerParser import DatasetCleanerParser
else:
    from DatasetCleanerParser import DatasetCleanerParser

# This class defines a complete listener for a parse tree produced by DatasetCleanerParser.
class DatasetCleanerListener(ParseTreeListener):

    # Enter a parse tree produced by DatasetCleanerParser#cleaning.
    def enterCleaning(self, ctx:DatasetCleanerParser.CleaningContext):
        pass

    # Exit a parse tree produced by DatasetCleanerParser#cleaning.
    def exitCleaning(self, ctx:DatasetCleanerParser.CleaningContext):
        pass


    # Enter a parse tree produced by DatasetCleanerParser#commandList.
    def enterCommandList(self, ctx:DatasetCleanerParser.CommandListContext):
        pass

    # Exit a parse tree produced by DatasetCleanerParser#commandList.
    def exitCommandList(self, ctx:DatasetCleanerParser.CommandListContext):
        pass


    # Enter a parse tree produced by DatasetCleanerParser#rmvDupCommand.
    def enterRmvDupCommand(self, ctx:DatasetCleanerParser.RmvDupCommandContext):
        pass

    # Exit a parse tree produced by DatasetCleanerParser#rmvDupCommand.
    def exitRmvDupCommand(self, ctx:DatasetCleanerParser.RmvDupCommandContext):
        pass


    # Enter a parse tree produced by DatasetCleanerParser#drpMissCommand.
    def enterDrpMissCommand(self, ctx:DatasetCleanerParser.DrpMissCommandContext):
        pass

    # Exit a parse tree produced by DatasetCleanerParser#drpMissCommand.
    def exitDrpMissCommand(self, ctx:DatasetCleanerParser.DrpMissCommandContext):
        pass


    # Enter a parse tree produced by DatasetCleanerParser#fillMissCommand.
    def enterFillMissCommand(self, ctx:DatasetCleanerParser.FillMissCommandContext):
        pass

    # Exit a parse tree produced by DatasetCleanerParser#fillMissCommand.
    def exitFillMissCommand(self, ctx:DatasetCleanerParser.FillMissCommandContext):
        pass


    # Enter a parse tree produced by DatasetCleanerParser#filterCommand.
    def enterFilterCommand(self, ctx:DatasetCleanerParser.FilterCommandContext):
        pass

    # Exit a parse tree produced by DatasetCleanerParser#filterCommand.
    def exitFilterCommand(self, ctx:DatasetCleanerParser.FilterCommandContext):
        pass


    # Enter a parse tree produced by DatasetCleanerParser#renameCommand.
    def enterRenameCommand(self, ctx:DatasetCleanerParser.RenameCommandContext):
        pass

    # Exit a parse tree produced by DatasetCleanerParser#renameCommand.
    def exitRenameCommand(self, ctx:DatasetCleanerParser.RenameCommandContext):
        pass


    # Enter a parse tree produced by DatasetCleanerParser#column.
    def enterColumn(self, ctx:DatasetCleanerParser.ColumnContext):
        pass

    # Exit a parse tree produced by DatasetCleanerParser#column.
    def exitColumn(self, ctx:DatasetCleanerParser.ColumnContext):
        pass


    # Enter a parse tree produced by DatasetCleanerParser#value.
    def enterValue(self, ctx:DatasetCleanerParser.ValueContext):
        pass

    # Exit a parse tree produced by DatasetCleanerParser#value.
    def exitValue(self, ctx:DatasetCleanerParser.ValueContext):
        pass


    # Enter a parse tree produced by DatasetCleanerParser#filePath.
    def enterFilePath(self, ctx:DatasetCleanerParser.FilePathContext):
        pass

    # Exit a parse tree produced by DatasetCleanerParser#filePath.
    def exitFilePath(self, ctx:DatasetCleanerParser.FilePathContext):
        pass



del DatasetCleanerParser