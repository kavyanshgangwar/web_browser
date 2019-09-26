from htmltokens import *
import ply.lex as lex
import webpage

states = (
    ('htmlcomment','exclusive'),
)

def t_htmlcomment(token):
    r'<!--'
    token.lexer.begin('htmlcomment')

def t_htmlcomment_end(token):
    r'-->'
    token.lexer.begin('INITIAL')

def t_htmlcomment_error(token):
    token.lexer.skip(1)
    if token.value[0:1]=='\n':
        token.lexer.lineno +=1

def t_newline(token):
    r'\n'
    token.lexer.lineno += 1
    pass


htmllexer = lex.lex()
htmllexer.input(webpage.webpage)

