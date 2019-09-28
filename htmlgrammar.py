grammar = [
    ("html",["elt","html"]),
    ("html",[]),
    ("elt",["WORD"]),
    ("elt",["tagelt"]),
    ("tagelt",["opentag","html","closetag"]),
    ("opentag",["LANGLE","WORD","RANGLE"]),
    ("closetag",["LANGLESLASH","WORD","RANGLE"]),
]

    