#include<stdlib.h>
#include<stdio.h>

int *gen_mat(int m, int n)
{
 int length=m*n;
 static int A[length];
 for(int i=0;i<length;i++)
 { A[i]=rand() % 5;}
 return A;
}

void print_arr(int A[], int m, int n)
{
    for (int i=0; i<m*n; i++)
    printf("Array %d",A[i]);

}

int main()
{
int m=2;
int n=2;
int p=2;
int *A;
int *B;
A=gen_mat(m,n);
B=gen_mat(n,p);

print_arr(A,m,n);
print_arr(B,n,p);

for (int i=0;i<)


}