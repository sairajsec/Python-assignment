import numpy as np

print("Enter 8 elements for Matrix A:")
arr1 = np.array(list(map(int, input().split()))).reshape(2, 4)

print("Enter 8 elements for Matrix B:")
arr2 = np.array(list(map(int, input().split()))).reshape(2, 4)

arr3 = arr1 + arr2

print("Matrix A =", arr1)
print("Matrix B =", arr2)
print("Addition of two matrices =", arr3)


print("Enter 12 elements for Matrix C:")
arr4 = np.array(list(map(int, input().split()))).reshape(2, 2, 3)

print("Enter 12 elements for Matrix D:")
arr5 = np.array(list(map(int, input().split()))).reshape(2, 2, 3)

arr6 = arr4 + arr5

print("Matrix C =", arr4)
print("Matrix D =", arr5)
print("Addition of two matrices =", arr6)