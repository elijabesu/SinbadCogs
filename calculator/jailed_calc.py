import asteval
import sys
import numpy


def run_in_jail(expr):
    sym_table = asteval.make_symbol_table(
        pi=numpy.pi, e=numpy.e, gamma=numpy.euler_gamma
    )
    evaler = asteval.Interpreter(symtable=sym_table)
    evaler.eval(expr, show_errors=False)


if __name__ == '__main__':
    run_in_jail(' '.join(sys.argv[1:]))
    sys.exit(0)
