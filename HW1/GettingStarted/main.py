from antlr4 import *
from gen.calculatorLexer import calculatorLexer
from gen.calculatorParser import calculatorParser
from Code.CalclatorListener import CustomCalculatorListener


def run():
    # Example input: "3 + 4"
    input_expression = input("Enter an arithmetic expression: ")

    # Create a stream for input
    input_stream = InputStream(input_expression)

    # Create a lexer that feeds off the input stream
    lexer = calculatorLexer(input_stream)

    # Create a stream of tokens using the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser that feeds off the token stream
    parser = calculatorParser(token_stream)
    # Obtain the parse tree by invoking the parser's entry point
    parse_tree = parser.start()

    # Create a custom Code object
    listener = CustomCalculatorListener()

    # Walk the parse tree with the custom Code
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)

    # Get the result from the Listener
    result = listener.result

    # Output the result
    print("Result:", result)

# Call the main function
if __name__ == '__main__':
    run()
