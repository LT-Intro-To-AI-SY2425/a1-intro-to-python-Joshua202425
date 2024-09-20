# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"
#Fahrenheit to celsius converter
def converter(n:float):
    print((5/9)*(n-32))
    return (5/9)*(n-32)
#Fibonacci sequence up to user input term
def fibo(n:int):
    r=1
    c=1
    for x in range(n):
       if n ==0:
        return 0
       elif n==1:
           return 1
       r+=c
       c=r-1
    
    return r
#Letter Checker
def letter(s,st):
    num=0
    for x in range(len(st)):
        print(st[x])
        print(s)
        if st[x]==s:
            num+=1
    return num
    

assert converter(68)==20.0,"con fail"
assert fibo(3)==5,"nacci fail"
assert letter("s","ersty")==1,"fail"
