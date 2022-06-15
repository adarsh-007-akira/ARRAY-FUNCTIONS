def rotateArray(a,d):
    n=len(a)
    a[:]=a[d:n]+a[0:d]
    return a

arr = [1, 2, 3, 4, 5, 6]

print("Rotated list is")
print(rotateArray(arr,4))