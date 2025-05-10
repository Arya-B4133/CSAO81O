def two_d_matrix(m, n):
    Outp = []
    for i in range(m):
        row = []  
        for j in range(n):
            num = int(input(f"Enter the matrix [{i}][{j}]: "))  
            row.append(num) 
        Outp.append(row)   
    return Outp

def diff(A, B):   
    output = []   
    for i in range(len(A)): 
        row = []  
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])   
        output.append(row)  
    return output     

def sum(A, B):   
    output = []   
    for i in range(len(A)): 
        row = []  
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])   
        output.append(row)  
    return output     

def transpose(matrix):
    output = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        output.append(row)
    return output

def multiply(A, B):
    result = []
    if len(A[0]) != len(B):
        return []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result

m = int(input("Enter the number of rows:"))
n = int(input("Enter the number of coloumns:"))
print("\n------------- FIRST MATRIX -----------------\n")
A = two_d_matrix(m, n)
print("\n------------- SECOND MATRIX -----------------\n")
B = two_d_matrix(m, n)
s = sum(A, B)
for row in s:
    print(row)
d = diff(A, B)
for row in d:
    print(row)
tA = transpose(A)
for row in tA:
    print(row)
C = two_d_matrix(A, B)
product = multiply(A, C)
for row in product:
    print(row)
