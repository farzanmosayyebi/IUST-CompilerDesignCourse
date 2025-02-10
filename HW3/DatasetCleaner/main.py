from antlr4 import *
import argparse
from Code.DatasetCleanerCustomListener import DatasetCleanerCustomListener
from Repository.ast_to_networkx_graph import show_ast
from gen.DatasetCleanerLexer import DatasetCleanerLexer
from gen.DatasetCleanerParser import DatasetCleanerParser
from Repository.post_order_ast_traverser import PostOrderASTTraverser
from Code.DatasetCleanerCodeGenerator import DatasetCleanerCodeGenerator


def main(arguments):
	stream = FileStream(arguments.input, encoding='utf8')
	lexer = DatasetCleanerLexer(stream)
	token_stream = CommonTokenStream(lexer)
	parser = DatasetCleanerParser(token_stream)
	parse_tree = parser.cleaning()
	ast_builder_listener = DatasetCleanerCustomListener(parser.ruleNames)
	walker = ParseTreeWalker()
	walker.walk(t=parse_tree, listener=ast_builder_listener)
	ast = ast_builder_listener.ast
	print(ast.root)
	show_ast(ast.root)
	post_order_ast_traverser = PostOrderASTTraverser()
	post_order_ast_traverser.node_attributes = ["label", "text", "number"]
	traversal = post_order_ast_traverser.traverse_ast(ast.root)
	print(traversal)
	code_generator = DatasetCleanerCodeGenerator()
	generated_code = code_generator.generate_code(traversal)
	with open(arguments.output, 'w') as output_file:
		output_file.write(generated_code)


if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-i', '--input', help='Input source', default=r'input.dc')
	argparser.add_argument('-o', '--output', help='Output path', default=r'test_output.py')
	args = argparser.parse_args()
	main(args)
