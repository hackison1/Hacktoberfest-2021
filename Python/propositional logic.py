#logic

x, transcript, variables = input(), [], []
for c in x:
    if c.isalpha() and c!="v":
        transcript.append(c)
        variables.append(c)
    elif (c == "(") or (c == ")") or (c == " "):
        transcript.append(c)
    elif c == "^":
        transcript.append("and")
    elif c == "v":
        transcript.append("or")
    elif c == "=":
        transcript.append("==")
    elif c == "~":
        transcript.append("not")

transcript, variables = "".join(transcript), list(set(variables))

f = open("operation1.py", "w")
for n in range(len(variables)):
    f.write("\t"*n + "for {} in [True, False]:\n".format(variables[n]))
f.write("\t"*len(variables) + "print({})".format(transcript))