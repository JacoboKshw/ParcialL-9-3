from antlr4 import *
from FibonacciLexer import FibonacciLexer
from FibonacciParser import FibonacciParser

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

class FibonacciListener(ParseTreeListener):
    def enterExpresion(self, ctx):
        n = int(ctx.NUMERO().getText())
        resultado = [fibonacci(i) for i in range(n)]
        print(f"FIBO({n}) = {', '.join(map(str, resultado))}")

def main():
    entrada = input("Ingrese la expresion")
    stream    = InputStream(entrada)
    lexer     = FibonacciLexer(stream)
    tokens    = CommonTokenStream(lexer)
    parser    = FibonacciParser(tokens)
    tree      = parser.programa()

    walker    = ParseTreeWalker()
    listener  = FibonacciListener()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
