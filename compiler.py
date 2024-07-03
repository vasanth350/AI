import sys
def tokenize(string):
    string = string.replace("("," ( ")
    string = string.replace(")"," ) ")
    string = string.replace("  ", " ")
    li = list(string.split())
    return li

def symbol(token: str):
    "Numbers become numbers; every other token is a symbol."
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return str(token)

def convert_tokens(tokens: list):
    
    if len(tokens)==0:
     print("empty list")
    
    token=tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(convert_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return symbol(token)
       


f = open("x.sexp", "r")
str1=f.readline()
if (str1.count('(')!=str1.count(')')):
    sys.exit("braces too many/too less")
tokens=tokenize(str1)
print(tokens)
expression=convert_tokens(tokenize(str1))
print(expression)


f.close()
