data = input('Enter data with space:- ')
lst = []
lst = data.split()
l = len(lst)
for i in range(l):
    for j in range(0, l-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print('Sorted array is:- ')
for i in range(len(lst)):
    print(lst[i])
