A = [4, -1, 7, 3, 9, 0, 11, 2, 14]

def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp

for i in range(len(A)):
  for j in range(len(A)):
    if (A[i] < A[j]):
      swap(A, i, j)

print(A)
