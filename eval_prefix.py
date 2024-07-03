
def parse(tokens):
    print(tokens)
    token=tokens.pop(0)
    print(token)
    if token=='+':
            print("add")
            print(tokens) 
            return parse(tokens)+parse(tokens)
    elif token=='-':
            return parse(tokens)-parse(tokens)
    elif token=='*':
            print("multiply")
            print(tokens) 
            return parse(tokens)*parse(tokens)
    elif token=='/':
            return parse(tokens)/parse(tokens)
    else:
            print("value returned")
            print(token)
            # must be just a number
            return int(token)


if __name__=='__main__':
        expression="+ * 4 5 10"
        #expression="* + 6 9 - 3 1"
        print(parse(expression.split()))
        print (expression.split())
