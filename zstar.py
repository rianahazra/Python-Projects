'''
n = int(input("How much space do you want indented for the triangle? "))
for i in range(1, 11):
    # Set the repetition count for the 10th row
    repeat = 7 if i == 10 else i
    print(' ' * (n - i) + (str(i) + ' ') * repeat)
'''



