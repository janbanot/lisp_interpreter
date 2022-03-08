import operator as op

# Lisp type definitons
Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)
Env = dict


def tokenize(chars: str) -> list:
    """
    Converts a string of characters into a list of tokens
    :param chars: an input program string
    :return: a list of tokens
    """
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()


def read_from_tokens(tokens: list) -> Exp:
    """
    Assembles nested list of prefix expressions from tokenized program intput string.
    :param tokens: list of tokens
    :return: nested list of expressions or a symbol
    """
    if not tokens:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        form = []
        while tokens[0] != ')':
            form.append(read_from_tokens(tokens))
        tokens.pop(0)  # pop off ending )
        return form
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)


def atom(token: str) -> Atom:
    """
    Distinguishes number tokens from symbol tokens by converting token to an integer or floating point number
    :param token: single token
    :return: token in correct type
    """
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)


def parse(input_program: str) -> Exp:
    """
    Reads a scheme expression from an input program string
    :param input_program: input program string
    :return: nested list of expressions
    """
    return read_from_tokens(tokenize(input_program))


def standard_env() -> Env:
    """
    An environment maps includes neccessary lisp standard function to their python implementation
    :return: dictionary with mapping from lisp primitives to python implementation
    """
    env = Env()
    env.update({
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
        'eq': op.eq,
        'begin': lambda *x: x[-1],
        'cons': lambda x, y: [x] + y,
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'atom': lambda x: isinstance(x, Atom)
    })
    return env

global_env = standard_env()


def lisp_eval(x: Exp, env=global_env) -> Exp:
    """
    Evaluation of lisp expressions consist of 5 scenarios:
    - a symbol interpreted as a variable name
    - a number that evaluates to itself
    - a conditional if statement
    - a new variable definition
    - a procedure call
    :param x: parsed expression
    :param env: environment dictionary
    :return: evaluation result
    """
    if isinstance(x, Symbol):
        return env[x]
    elif isinstance(x, Number):
        return x
    elif x[0] == 'if':
        (_, condition, consequent, alternative) = x
        exp = (consequent if lisp_eval(condition, env) else alternative)
        return lisp_eval(exp, env)
    elif x[0] == 'define':
        (_, symbol, exp) = x
        env[symbol] = lisp_eval(exp, env)
    else:
        proc = lisp_eval(x[0], env)
        args = [lisp_eval(arg, env) for arg in x[1:]]
        return proc(*args)


def repl(prompt='>> '):
    """
    REPL - a read-eval-print loop
    :param prompt: prompt strin
    """

    while True:
        try:
            val = lisp_eval(parse(input(prompt)))
            if val is not None:
                print(scheme_str(val))
        except SyntaxError as e:
            print(f"Syntax error: {e}")
        except ZeroDivisionError:
            print("Zero Division Error")
        except KeyError as e:
            print(f"Lisp syntax error: {e}")
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break


def scheme_str(exp):
    """
    Converts a Python object back into scheme-readable string
    :param exp: nested expression
    :return: scheme-readable string
    """
    if isinstance(exp, List):
        return '(' + ' '.join(map(schemestr, exp)) + ')'
    else:
        return str(exp)