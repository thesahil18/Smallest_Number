n = int(input("Enter no of input = "))
num = []
for i in range(n):
    num.append(int(input(f'Enter No {i} : ')))
value = num[-1]
for i in range(n):
    if (num[i] <= value):
        value = num[i]
print(f'The Smallest Number is : {value}')
