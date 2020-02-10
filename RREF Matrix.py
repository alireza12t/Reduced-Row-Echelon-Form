

import numpy


r = int(input("Enter nummber of rows: "))
c = int(input("Enter nummber of Coloumns: "))
a = []

print("Enter your Matrix like this sample")
print("4 7 3 8")
print("8 3 8 7")
print("2 9 5 3")

for i in range(r):
    a.append(list(map(int, input().split(" "))))
A = numpy.array(a)


def row_reduced_echelon(A):
    r, c = A.shape
    if r == 0 or c == 0:
        return A
    for i in range(r):
        if A[i,0] != 0:
            break
    else:
        B = row_reduced_echelon(A[:,1:])
        return numpy.hstack([A[:,:1], B])

    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row

    A[0] = A[0] / A[0,0]
    A[1:] -= A[0] * A[1:,0:1]

    B = row_reduced_echelon(A[1:,1:])

    return numpy.vstack([A[:1], numpy.hstack([A[1:,:1], B]) ])


print(row_reduced_echelon(A))
