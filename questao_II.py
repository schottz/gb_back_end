val = [ "{[()]}", "{[(])}", "{{[[(())]]}}"]

def check_balance(string):
    balance = []
    for s in string:
        if s == '(' or s == '[' or s == '{':
            balance.append(s)
        else:
            if not balance:
                return "Não"
            else:
                top = balance[-1]
                if s == ')' and top == '(' or s == ']' and top == '[' or s == '}' and top == '{':
                    balance.pop()
    if not balance:
        return "Sim"
    else:
        return "Não"


for v in val:
    print(check_balance(v))