'''
table=int(input("Enter any times table"))
for num in range(1,11):
    product=table*num
    print(f'{table}x{num}={product}')
'''
'''
3x1=3
3x2=6
3x3=9
3x4=12
'''
for num in range(10):
    if num%2==0:
        print(num,"Number is Even")
    else:
        print("invalid")
