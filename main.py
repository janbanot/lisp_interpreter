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
    if not tokens:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        form = []
        while tokens[0] != ')':
            form.append(read_from_tokens(tokens))
        tokens.pop(0)  # pop off end )
        return form
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)


def atom(token: str) -> Atom:
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)


def parse(input_program: str) -> Exp:
    return read_from_tokens(tokenize(input_program))

if __name__ == '__main__':
    program = "(begin (define r 10) (* pi (* r r)))"
    print(parse(program))
