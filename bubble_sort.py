# sorting a list using bubble sort

n=int(input("Enter the numbers of inputs: "))
a=[]
for i in range(n):
    a.append(input("Enter the numbers: "))
print("sorting list using bubble sort")
for i in range(n):
    for j in range(n-i-1):
        if(a[j]>a[j+1]):
            a[j+1],a[j]=a[j],a[j+1]
print(a)

