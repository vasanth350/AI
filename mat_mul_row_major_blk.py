
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

def mat_mul(A,B,m,n,p,b_size,chunk_size):
    c=create_zero_mat(m,p)
    print("block size = ",b_size)
    #Outer loop to control block size
    for b in range(0,m,b_size):
        
        print("row block")
        #for final block when it is smaller than block size
        if (m-b) < b_size:
            limit=m
        else:
            limit=b+b_size
        
        #use B Matrix p value as column size here 
        for p_val in range (0,p,p_size):
            
            if (p-p_val) < p_size:
                p_limit=p
            else:
                p_limit=p_val+p_size

            # block of rows 
            # Rows of A, where b is the start of block and limit defines the available block size
            for i in range(b,limit):

                # block of rows 
                # Rows of B, where b is the start of block and limit defines the available block size (p_size)
                for j in range(p_val,p_limit): 
                    for k in range(n):
                        #for nxn matrix
                        # result[i*n+j] +=  A[i*n+k] * B[k*n+j]

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
m=7
n=5
p=41
b_size=3
p_size=5

A=create_mat(m,n)
B=create_mat(n,p)
R=mat_mul(A,B,m,n,p,b_size,p_size)

print('A', A)
print('B', B)
print('R', R)


A1 = np.array(A).reshape(m, n)
B1 = np.array(B).reshape(n, p)
C1 = np.matmul(A1, B1).flatten()
print('C',C1)
assert np.allclose(C1, R)
