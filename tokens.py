TOKEN_TYPES = [
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
    ('MOD',          r'%'),
    
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
    ('WHITESPACE',   r'[ \t]+'),
]






