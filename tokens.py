from test import *
import re
PP_TOKEN_TYPES = [
    ('ID',           r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('COLON',        r':'),
    ('LPAREN',       r'\('),
    ('RPAREN',       r'\)'),
    ('LBRACE',       r'\{'),
    ('RBRACE',       r'\}'),
    ('STRING',       r'"[^"]*"'),
    ('NUMBER',       r'\d+(\.\d+)?'),
    ('COMMA',        r','),
    ('INDENT',       r'^[ \t]+'),
    ('DEDENT',       r''),
    ('NEWLINE',      r'\n'),
    ('BODY_LINE',    r'.+'),
    ('WHITESPACE',   r'[ \t]+'),
]

# Example template for your structure
template = [
    'NAME(PLACEHOLDER):',
    '    {"key": PLACEHOLDER}',
    '',
    'tem(data):',
    '    "test":data',
    ')'
]


token_regexes = [(name, re.compile(pattern)) for name, pattern in PP_TOKEN_TYPES if pattern]
# print(token_regexes)

for line in template:
    # print(f"Line: {line}")
    tokens = []
    pos = 0
    while pos < len(line):
        match = None
        for name, regex in token_regexes:
            match = regex.match(line, pos)
            if match:
                if name != 'WHITESPACE':  # skip whitespace tokens
                    tokens.append((name, match.group()))
                pos = match.end()
                break
        if not match:
            pos += 1  # skip unrecognized character
    print("Tokens:", tokens)

