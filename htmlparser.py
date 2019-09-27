from htmlgrammar import *
from htmllexer import *

def closure(grammar,i,x,ab,cd):
    if cd == []:
        return []
    new_states = []
    for rule in grammar:
        if rule[0] == cd[0]:
            k=[cd[0]]
            
            new_states = new_states + [[(rule[0],[],rule[1],i),k]]
    return new_states

def shift(tokens,i,x,ab,cd,j,k):
    if cd!=[] and (tokens[i])[0]==cd[0]:
        k = [k[0],[tokens[i]]]
        return [(x,ab+[cd[0]],cd[1:],j),k]
    else:
        return None

def reductions(chart,i,x,ab,cd,j,k):
    new_states = []
    if cd != []:
        return []
    for jstate in chart[j]:
        if (jstate[0])[2] != [] and ((jstate[0])[2])[0] == x:   
            jstate[1] = jstate[1] + [k]
            new_states = new_states + [[((jstate[0])[0],(jstate[0])[1]+[x],((jstate[0])[2])[1:],(jstate[0])[3]),jstate[1]]]
    return new_states

def addtochart(chart,index,state):
    t=[m[0] for m in chart[index]]
    if not (state[0] in t):
        chart[index] = chart[index] + [state]
        return True
    return False

def parse(tokens,grammar):
    tokens = tokens + [("end","")]
    chart = {}
    ast =["S",]
    start_rule = grammar[0]
    for i in range(len(tokens)+2):
        chart[i]=[]
    start_state = [(start_rule[0],[],start_rule[1],0),ast]
    chart[0] = [start_state]
    for i in range(len(tokens)+1):
        print(i)
        while True:
            changes = False
            for state in chart[i]:
                x=(state[0])[0]
                ab=(state[0])[1]
                cd=(state[0])[2]
                j=(state[0])[3]
                k=state[1]
                next_states = closure(grammar,i,x,ab,cd)
                for next_state in next_states:
                    changes = addtochart(chart,i,next_state) or changes
                next_state = shift(tokens,i,x,ab,cd,j,k)
                if next_state != None:
                    any_changes = addtochart(chart,i+1,next_state) or any_changes
                next_states = reductions(chart,i,x,ab,cd,j,k)
                for next_state in next_states:
                    changes = addtochart(chart,i,next_state) or changes
            if not changes:
                break
    accepting_state = (start_rule[0],start_rule[1],[],0)
    final_states = [state[0] for state in chart[len(tokens)]]
    for states in chart[len(tokens)]:
        if states[0]==accepting_state:
            print(states[1])
    return accepting_state in final_states

tokk=[]
while True:
    tok = htmllexer.token()
    if not tok:
        break
    tokk=tokk+[(tok.type,tok.value)]
print(tokk)
result = parse(tokk,grammar)
print(result)
