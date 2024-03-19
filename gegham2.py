# 3.Given N number. Write a recursive function
# that should print from 1 to N numbers.


#     if n > 0:
#         printNumber(n - 1)
#         # print n
#         print(n, end=' ')
#
#
# n = 50
#
# printNumber(n)

def printNumber(x):
    if x > 0:
        printNumber(x - 1)

        print(x, end=' ')


x = 50
printNumber(x)
