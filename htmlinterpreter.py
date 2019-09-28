from htmlparser import *
from tagsandmeanings import switcher
#defining function to get the meaning of each tag
def tagmeaning(tag):
    return switcher.get(tag)

#defining interpreter to check meaning of the webpage
def interpreter(ast):
    global contentstack
    global tagstack
    if ast[0]=='html':
        for m in ast:
            interpreter(m)#interpreting all subtrees
    if ast[0] == 'elt' and (ast[1])[0] == 'WORD':
        contentstack = contentstack + [((ast[1])[1],tagstack[:])]
    #checking the tagelt and checking if same opening and closing tags are associated with each other
    if ast[0] == 'elt' and (ast[1])[0] == 'tagelt':
        z = ast[1]
        if (z[1])[2] != (z[3])[2]:
            raise Exception(str(((z[1])[2])[1]) + " tag mismatch "+str(((z[3])[2])[1]))
        elif (((z[1])[2])[1] not in taglist):
            raise Exception("Unknown tag: "+str(((z[1])[2])[1]))
        elif (((z[3])[2])[1] not in taglist):
            raise Exception("Unknown tag: "+str(((z[3])[2])[1]))
        else:
            tagstack = tagstack + [tagmeaning(((z[1])[2])[1])]
            interpreter(z[2])
            del tagstack[len(tagstack) -1]   
#stack for content
contentstack = []
#stack for tags geting applied
tagstack = []
#making a list of tags that are valid
taglist = [f for f in switcher.keys()]
try:
    interpreter(ast)
except:
    print("mismatch")
    raise #to stop the execution of code
print(contentstack)