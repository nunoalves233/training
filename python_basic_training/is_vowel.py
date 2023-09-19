def iscons(x):
    logic = ""
    if x.lower() in ('a', 'e', 'i', 'o', 'u'):
        logic = "True"
    elif x.upper() in ('A', 'E', 'I', 'O', 'U'):
        logic = "True"
    else: logic = "False"
    return logic


