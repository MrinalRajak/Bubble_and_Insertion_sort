# sorting a list using insertion sort

n=int(input("Enter the number of inputs: "))
a=[input() for i in range(n)]
for i in range(n):
    position=i
    while position>0 and a[position]>a[position-1]:
        a[position],a[position-1]=a[position-1],a[position]
        position=position-1
    print(a)
