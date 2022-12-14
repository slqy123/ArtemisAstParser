from ply.lex import lex
from ply.yacc import yacc

tokens = ('NUMBER', 'COMMA', 'LPAREN', 'RPAREN', 'NAME', 'EQUAL', 'STRING', 'LL', 'RL')

t_ignore = ' \t'
t_COMMA = r','
t_LPAREN = r'\{'
t_RPAREN = r'\}'
t_LL = r'\['
t_RL = r'\]'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'  # 在02_華乃10.ast出现了NAME=[50]的情况，仅此一例
t_EQUAL = r'='


def t_ignore_VER(t):
    r'astver[^\n]+\n'
    return


def t_STRING(t):
    r'"(\\"|[^"])*"'
    t.value = t.value[1:-1]
    return t


def t_NUMBER(t):
    r'-?\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

count = 0
def t_error(t):
    global count
    print(f'Illegal character {t.value[0]!r}', t.lexer.lineno)
    count += 1
    if count > 10:
        exit(0)
    t.lexer.skip(1)


def p_kwarg(p):
    """kwarg : name EQUAL STRING
    | name EQUAL NUMBER
    | name EQUAL block
    | name EQUAL arg"""
    p[0] = (p[1], p[3])


def p_arg(p):
    """arg : STRING 
    | block"""
    p[0] = p[1]

def p_list_name(p):
    """name : LL STRING RL
    | LL NUMBER RL"""
    p[0] = f'[{p[2]}]'
def p_name_NAME(p):
    """name : NAME"""
    p[0] = p[1]

def p_gen_block(p):
    """block : LPAREN params RPAREN"""
    b = {'args': []}
    for item in p[2]:
        if isinstance(item, tuple):
            b[item[0]] = item[1]
        else:
            b['args'].append(item)
    p[0] = b



def p_params(p):
    """params : arg
    | kwarg"""
    p[0] = [p[1]]


def p_params_merge(p):
    """params : params COMMA arg
    | params COMMA kwarg"""
    p[1].append(p[3])
    p[0] = p[1]


def p_params_end_comma(p):
    'params : params COMMA'
    p[0] = p[1]

def p_null_block(p):
    """block : LPAREN RPAREN"""
    p[0] = {'args': []}

def p_error(p):
    print(f'Syntax error at {p.value!r}')


class Ast:
    def __init__(self):
        self.lexer = lex()
        self.parser = yacc()

    def parse(self, txt: str, encoding: str = 'utf-8', save_path: str = './result.json') -> None:
        #
        # self.lexer.input(txt)
        # for l in self.lexer:
        #     print(l)

        result = self.parser.parse(txt)
        if isinstance(result, tuple):
            result = {result[0]: result[1]}

        import json
        with open(save_path, 'w', encoding=encoding) as f:
            json.dump(result, f, ensure_ascii=False)


if __name__ == '__main__':
    ast = Ast()
    ast.parse('astver = 2.0\nast = {"123",}')
