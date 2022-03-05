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
        tokens.pop(0)  # pop off end )
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

if __name__ == '__main__':
    program = "(begin (define r 10) (* pi (* r r)))"
    print(parse(program))
