grammar = [
    ("S",["html"]),
    ("html",["elt","html"]),
    ("html",["end"]),
    ("elt",["WORD"]),
    ("elt",["opentag","html","closetag"]),
    ("opentag",["LANGLE","WORD","RANGLE"]),
    ("closetag",["LANGLESLASH","WORD","RANGLE"]),
]

    