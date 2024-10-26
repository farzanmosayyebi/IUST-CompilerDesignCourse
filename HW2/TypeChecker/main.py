from antlr4 import *
from gen.TypeCheckerLexer import TypeCheckerLexer
from gen.TypeCheckerParser import TypeCheckerParser
from Code.CustomTypeCheckerListener import CustomTypeCheckerListener


def run():
    input_expression = ''
    while True:
        line = input(">_")
        if line:
            input_expression += line
        else:
            break

    # Create a stream for input
    input_stream = InputStream(input_expression)

    # Create a lexer that feeds off the input stream
    lexer = TypeCheckerLexer(input_stream)

    # Create a stream of tokens using the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser that feeds off the token stream
    parser = TypeCheckerParser(token_stream)
    # Obtain the parse tree by invoking the parser's entry point
    parse_tree = parser.start()

    # Create a custom Code object
    listener = CustomTypeCheckerListener()

    # Walk the parse tree with the custom Code
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)

# Call the main function
if __name__ == '__main__':
    run()
