import re

def tokenize(data,token_types):
    complied_regex = [(name, re.compile(pattern)) for name, pattern in token_types if pattern]

    tokens = []

    for text in data:
        pos = 0

        while (pos < len(text)) and (text[pos] == " "):
            pos +=1
        
        for t in range(int((pos+1)//4)):
            tokens.append(("INDENT","INDENT"))

        while pos < len(text):
            match = None
            for name, regex in complied_regex:
                match = regex.match(text, pos)
                if match:
                    if name != 'WHITESPACE':
                        tokens.append((name, match.group(0)))
                    pos = match.end()
                    break
            if not match:
                raise SyntaxError(f'Unexpected character: {text[pos]} at position {pos}')

        tokens.append(("NEWLINE", "\n"))
    return tokens
