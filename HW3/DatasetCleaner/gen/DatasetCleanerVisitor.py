# Generated from D:/Elmos/S4031/CompilerDesign/TA1/TA1/HW3/Grammar/DatasetCleaner.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DatasetCleanerParser import DatasetCleanerParser
else:
    from DatasetCleanerParser import DatasetCleanerParser

# This class defines a complete generic visitor for a parse tree produced by DatasetCleanerParser.

class DatasetCleanerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DatasetCleanerParser#cleaning.
    def visitCleaning(self, ctx:DatasetCleanerParser.CleaningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatasetCleanerParser#commandList.
    def visitCommandList(self, ctx:DatasetCleanerParser.CommandListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatasetCleanerParser#rmvDupCommand.
    def visitRmvDupCommand(self, ctx:DatasetCleanerParser.RmvDupCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatasetCleanerParser#drpMissCommand.
    def visitDrpMissCommand(self, ctx:DatasetCleanerParser.DrpMissCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatasetCleanerParser#fillMissCommand.
    def visitFillMissCommand(self, ctx:DatasetCleanerParser.FillMissCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatasetCleanerParser#filterCommand.
    def visitFilterCommand(self, ctx:DatasetCleanerParser.FilterCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatasetCleanerParser#renameCommand.
    def visitRenameCommand(self, ctx:DatasetCleanerParser.RenameCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatasetCleanerParser#column.
    def visitColumn(self, ctx:DatasetCleanerParser.ColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatasetCleanerParser#value.
    def visitValue(self, ctx:DatasetCleanerParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatasetCleanerParser#filePath.
    def visitFilePath(self, ctx:DatasetCleanerParser.FilePathContext):
        return self.visitChildren(ctx)



del DatasetCleanerParser