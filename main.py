from interpreter import repl

if __name__ == '__main__':
    program = "(begin (define r 10) (* 3.14 (* r r)))"
    program2 = "(if (> 10 20) 1 2)"
    repl()
