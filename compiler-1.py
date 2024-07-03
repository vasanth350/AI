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
       

def evaluate(expression, env):

    if isinstance(expression, list):
        operator=expression[0]
        if operator=='+':
                return evaluate(expression[1],env)+evaluate(expression[2],env)
        elif operator=='-':
                return evaluate(expression[1],env)-evaluate(expression[2],env)
        elif operator=='*':
                return evaluate(expression[1],env)*evaluate(expression[2],env)
        elif operator=='/':
                return evaluate(expression[1],env)/evaluate(expression[2],env)
        elif operator == "let":
            for k,v in expression[1]:  
                env[k]= evaluate(v, env)     
            return evaluate(expression[2], env)
        elif operator == "lambda":
            return expression
        elif operator in env:
            lamb=env[operator]
            args=lamb[1]
            out_expression=lamb[2]
            for i in range(len(args)):
                env[args[i]]=evaluate(expression[i+1], env)
            return evaluate(out_expression,env)
        else:
            raise Exception("wrong", expression)
        
    elif isinstance(expression, int):
        return expression
    elif isinstance(expression, float):
        return expression
    elif isinstance(expression, str):
        if expression in env:
            return env[expression]
        else:    
            raise Exception('Variable not defined')




        

f = open("y.sexp", "r")
str1=f.readline()

tokens=tokenize(str1)
print(tokens)
expression=convert_tokens(tokenize(str1))
print(expression)

env = {"a": 20,"b":5}
print(evaluate(expression, env))

f.close()
