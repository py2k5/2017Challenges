s=input()

def closer(s):
    stack = []
    for c in s:
        if c in [ '[','(','{' ]:
            stack.append(c)
        elif c in [ ']',')','}' ]:
            if any ( [(c == ']' and stack[-1] == '['), (c == '}' and stack[-1] == '{'), (c == ')' and stack[-1] == '(') ]) :
                stack.pop()
               
         

    #print(stack)
    if len(stack) > 0:
        return False
    else:
        return True


print(closer(s))
