import json
import sys


# def compile(exp):
"""     if isinstance(exp,list):
        if exp[0] == "s-kaleidoscope":
            exp[0] = "brilisp"
        operator=exp[1][0]
        #print (operator)
        if operator == "define":
            header = exp[1][1] # (fn_name n) -> ((fn_name int) (n int))
            f=header[0]
            n=header[1]
            header[0]=[f,"int"]
            #print(header)
            header[1]=[n,"int"]
            #print(header)
            return exp
        else:
            raise Exception ("Error",exp) """


def random_num():
    import random
    return random.randint(0, 200)

def gen_body(bvalue):
    out=[]
    def gen_expr(bvalue, out_var):
        if isinstance(bvalue, list):
            operator = bvalue[0]
            
            tmp_num = random_num()
            operand1 = gen_expr(bvalue[1], out_var=f'temp_{tmp_num}')

            tmp_num = random_num()
            operand2 = gen_expr(bvalue[2], out_var=f'temp_{tmp_num}')
            
            if operator == "*":
                out.append(["set", [out_var, "int"], ["mul", operand1, operand2]])
            elif operator == "/":
                out.append(["set", [out_var, "int"], ["div", operand1, operand2]])
            elif operator == "+":
                out.append(["set", [out_var, "int"], ["add", operand1, operand2]])
            elif operator == "-":
                out.append(["set", [out_var, "int"], ["sub", operand1, operand2]])
            else:
                raise Exception("unknown op")
        else:
            out.append(["set", [out_var, "int"], ["id", bvalue]])
        
        return out_var

    gen_expr(bvalue, out_var="temp_final")
    out.append(["ret", "temp_final"])
    return out
        


def gen_header(f_header):
    out=[]
    for arg in f_header:
        out.append([arg,"int"])
    #print(out)
    return out
    

def gen_fn(fn):
   assert fn[0]=="define"
   out=[]
   out.append("define")
   header=fn[1]
   # fn -> (define ...)
   # fn[1] -> (name arg1 arg2)
   # fn[2] -> body
   out.append(gen_header(fn[1]))
   
   body = fn[2]
   #print(body)
   assert body[0] == "ret"
   value=body[1]
   out.extend(gen_body(value))
   #print(fn[2])
   #out.append(fn[2])

   return out



def compile(inp):
    assert inp[0]=="s-kaleidoscope"
    out=[]
    out.append("brilisp")
    #print(out)
    fns=inp[1:]
    for fn in fns:
     #fn = inp[1]
        out.append(gen_fn(fn))
    return out
        


inp = json.load(sys.stdin)

print(json.dumps(compile(inp)))


