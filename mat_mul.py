
import random
import matplotlib.pyplot as plt
import time
import numpy as np


def create_zero_mat(m,n):
    A=[]
    for i in range(m):
        K=[]
        for j in range(n):
            K.append(0)
        A.append(K)
    return A


def create_mat(m,n):
    A=[]
    for i in range(m):
        K=[]
        for j in range(n):
            K.append(random.uniform(0,1))
        A.append(K)
    
    return A

def mat_mul(A,B,n):
    result=create_zero_mat(n,n)
    for i in range(len(A)):
        for j in range (len(B[0])): 
            for k in range (len(B)):
                result[i][j] = result[i][j]+ A[i][k] * B[k][j]
    return result

# Placing the plots in the plane 
plot1 = plt.subplot2grid((1, 2), (0, 0)) 
plot2 = plt.subplot2grid((1, 2), (0, 1)) 

size=[]
etime=[]
flops=[]
for n in range(2,400,50):

    A=create_mat(n,n)
    B=create_mat(n,n)
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
