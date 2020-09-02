first_digit = 1
second_digit =1
li = []
n = int(input('Enter no of digits required: '))
li.append(first_digit)
li.append(second_digit)
for i in range(1, n+1):
    sum = first_digit + second_digit
    li.append(sum)
    first_digit = second_digit
    second_digit = sum
print(li)
