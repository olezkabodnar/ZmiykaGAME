def max(a):
    b = a[0]
    for k in a:
        if k > b:
            b = k
    return b
def min(a):
    b = a[0]
    for k in a:
        if k < b:
            b = k
    return b
def sort(a):
    for k in range(len(a)):
        for j in range (k):
            if a[k] < a[j]:
                a[k], a[j] = a[j], a[k]
    return a



choice = input()
massive = input().split()
numlist = []
for k in massive:
    numlist.append(int(k))


if choice == "min":
    print (min(numlist))
elif choice =="max":
    print (max(numlist))
else:
    print (sort(numlist))


