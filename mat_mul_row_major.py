
import random
import matplotlib.pyplot as plt
import time
import numpy as np
import sys


def create_zero_mat(m,n):
    A=[]
    for i in range(m*n):
            A.append(0)
    return A


def create_mat(m,n):
    A=[]
    for i in range(m*n):
        #A.append(random.uniform(0,1))    
        A.append(random.choice([1,2,3,4,5]))
    return A

def mat_mul(A,B,m,n,p):
    c=create_zero_mat(m,p)
    
    for i in range(m):
        for j in range(p): 
            for k in range(n):
                #result[i*n+j] +=  A[i*n+k] * B[k*n+j]
            
                c[i*p+j] += A[i*n+k] * B[k*p+j] 
                #print(result)
                print(c)
            
    return c

# Placing the plots in the plane 
plot1 = plt.subplot2grid((1, 2), (0, 0)) 
plot2 = plt.subplot2grid((1, 2), (0, 1)) 

size=[]
etime=[]
flops=[]
m=2
n=2
p=2

A=create_mat(m,n)
B=create_mat(n,p)

print(A)
print(B)

R=mat_mul(A,B,m,n,p)
print(R)
sys.exit()


start = time.time()
R=mat_mul(A,B,n)
end = time.time()
exec_time= (end-start)
print (f"N value: {n}\tTime taken: {exec_time}ms")
size.append(n)
etime.append(exec_time)
flops_value= 2 * n**3 / exec_time 
print(flops_value)
flops.append(flops_value)

plot1.plot(size,etime)
plot2.plot(size,flops)
plt.show()




""" print(A)
print(B)
print("result")
print(R)

import numpy as np
print(np.matmul(A, B))
assert np.allclose(np.matmul(A, B), R) """




#print(R)
