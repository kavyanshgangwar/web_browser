tokens = (
    'LANGLESLASH', # </
    'LANGLE', # <
    'RANGLE', # >
    'WORD', # WORD
    'EQUAL', # =
    'STRING', # quoted words eg: "hello", "www.google.com"
)

t_ignore = ' ' #shortcut for ignoring whitespace

def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'\"[^\"]*\"'
    token.value=token.value[1:-1]
    return token

def t_WORD(token):
    r'[^ <>]+'
    return token

