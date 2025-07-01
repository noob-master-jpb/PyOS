import re

PP_TOKEN_TYPES = [
    ('ID',           r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('COLON',        r':'),
    ('SEMICOLON',    r';'),
    ('LPAREN',       r'\('),
    ('RPAREN',       r'\)'),
    ('LBRACE',       r'\{'),
    ('RBRACE',       r'\}'),
    ('LBRACKET',     r'\['),
    ('RBRACKET',     r'\]'),
    ('STRING',       r'"[^"]*"'),
    ('FLOAT',        r'\d+\.\d+'),  # Floating-point numbers
    ('INT',          r'\d+'), 
    ('COMMA',        r','),
    ('DOT',          r'\.'),
    ('PLUS',         r'\+'),
    ('MINUS',        r'-'),
    ('STAR',         r'\*'),
    ('SLASH',        r'/'),
    ('EQUAL',        r'='),
    ('EQEQ',         r'=='),
    ('NOTEQ',        r'!='),
    ('LT',           r'<'),
    ('GT',           r'>'),
    ('LE',           r'<='),
    ('GE',           r'>='),
    ('AND',          r'\band\b'),
    ('OR',           r'\bor\b'),
    ('NOT',          r'\bnot\b'),
    ('NEWLINE',      r'\n'),
    ('BODY_LINE',    r'.+'),
    ('WHITESPACE',   r'[ \t]+'),

]

# Example template for your structure
template = [
    'NAME(PLACEHOLDER):',
    '    {"key": PLACEHOLDER}',
    'tem(data):',
    '    "test":data',
    ')'
]

complied_regex = [(name, re.compile(pattern)) for name, pattern in PP_TOKEN_TYPES if pattern]





        




