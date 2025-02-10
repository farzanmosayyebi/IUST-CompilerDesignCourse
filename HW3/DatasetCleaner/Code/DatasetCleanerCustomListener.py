from Repository.ast import AST
from Repository.make_ast_subtree import make_ast_subtree
from gen.DatasetCleanerListener import DatasetCleanerListener

class DatasetCleanerCustomListener(DatasetCleanerListener):
    def __init__(self, rule_names):
        self.overridden_rules = [
            "cleaning",
            "command",
            "column",
            "rmvDupCommand",
            "drpMissCommand",
            "fillMissCommand",
            "filterCommand",
            "renameCommand",
            "filePath",
        ]
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)

    def exitCleaning(self, ctx):
        file_path = ctx.file_path().getText()
        make_ast_subtree(self.ast, ctx, f"CLEAN {file_path}", keep_node=True)

    def exitFilePath(self, ctx):
        path = ctx.getText()
        make_ast_subtree(self.ast, ctx, f"FILE {path}", keep_node=True)

    def exitRmvDupCommand(self, ctx):
        make_ast_subtree(self.ast, ctx, "REMOVE DUPLICATES", keep_node=True)

    def exitDrpMissCommand(self, ctx):
        make_ast_subtree(self.ast, ctx, "DROP MISSING", keep_node=True)

    def exitFillMissCommand(self, ctx):
        column = ctx.column().getText()
        value = ctx.value().getText()
        make_ast_subtree(self.ast, ctx, f"FILL MISSING {column} WITH {value}", keep_node=True)

    def exitFilterCommand(self, ctx):
        column = ctx.column().getText()
        op = ctx.COMPARISON_OPERATOR().getText()
        value = ctx.value().getText()
        make_ast_subtree(self.ast, ctx, f"FILTER {column} {op} {value}", keep_node=True)

    def exitRenameCommand(self, ctx):
        old_column = ctx.column(0).getText()
        new_column = ctx.column(1).getText()
        make_ast_subtree(self.ast, ctx, f"RENAME {old_column} TO {new_column}", keep_node=True)

    def exitColumn(self, ctx):
        name = ctx.getText()
        make_ast_subtree(self.ast, ctx, name, keep_node=True)