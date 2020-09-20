
M, N = map(int, input("\nEnter dimensions of Matrix A: ").split('x'))

P, Q = map(int, input("Enter dimensions of Matrix B: ").split('x'))

if(N != P):
    print("Matrix Multiplication not possible")
    exit()

print("Enter Matrix A")

A = list()

for i in range(M):
    A.append(list(map(int, input().split(' '))))
        
print("Enter Matrix B")

B = list()

for i in range(P):
    B.append(list(map(int, input().split(' '))))

result = list()

for i in range(M):
    result.append([0]*Q)
    

for i in range(len(A)): 
    for j in range(len(B[0])): 
        for k in range(len(B)): 
            result[i][j] += A[i][k] * B[k][j] 

print("Matrix after multiplication: \n")
    
for r in result: 
    print(r)
