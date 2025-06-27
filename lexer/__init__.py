import re

TOKEN_TYPES = [
    ('AT',        r'@'),
    ('ID',        r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('STRING',    r'"(?:\\.|[^\\"])*"'),
    ('FSTRING',   r'f"(?:\\.|[^\\"])*"'),
    ('NUMBER',    r'\d+'),
    ('FLOAT',     r'\d+\.\d+'),
    ('COLON',     r':'),
    ('EQUALS',    r'='),
    ('ARROW',     r'->'),
    ('COMMA',     r','),
    ('DOT',       r'\.'),
    
    # Brackets
    ('LPAREN',    r'$'),
    ('RPAREN',    r'$'),
    ('LBRACE',    r'\{'),
    ('RBRACE',    r'\}'),
    ('LSQUARE',   r'$'),
    ('RSQUARE',   r'$'),

    # Operators
    ('PLUS',      r'\+'),
    ('MINUS',     r'-'),
    ('TIMES',     r'\*'),
    ('DIVIDE',    r'/'),
    ('GT',        r'>'),
    ('LT',        r'<'),
    ('GE',        r'>='),
    ('LE',        r'<='),  
    ('EQ',        r'=='),  
    ('NEQ',       r'!='),  

    # Keywords
    ('FOR',       r'for'),
    ('IN',        r'in'),
    ('IF',        r'if'),
    ('ELSE',      r'else'),

    # Whitespace & comments
    ('WS',        r'[ \t\n\r]+'),
    ('COMMENT',   r'#.*'),
]