a = [2,4,10,16]
def multiply(a,b):
    for i in range(0,len(a)):
        a[i] = a[i] * b
    return a

c = multiply(a,5)
print c

