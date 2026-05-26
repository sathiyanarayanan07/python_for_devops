import sys

def add(num1, num2):
    add = num1+num2
    return add

def sub(num1 ,num2):
    sub = num1-num2
    return sub

def mul(num1 ,num2):
    m = num1*num2
    return m

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    execute = add(num1,num2)
    print(execute)
elif operation == "sub":
    execute = sub(num1,num2)
    print(execute)
elif operation == "mul":
    execute = mul(num1,num2)
    print(execute)
else:
    print("error")