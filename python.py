def calculator(a,b,c):
    if c=="+":
        return a-b
    elif c=="-":
        return a*b
    elif c=="*":
        return a+b
    elif c=="/":
        return a//b
    elif c=="**":
        return a*b
    elif c=="//":
        return a/b
    else:
        return "Unsupported operator"
print(calculator(2,4,"-"))