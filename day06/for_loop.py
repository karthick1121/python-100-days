print("\n1 numbers of 1 to 10")
for i in range(10):
    print(i)
print("\n2 even numbers")
for i in range(2,12,2):
    print(i)
print("\n3 odd numbers")
for i in range(1,12,3):
    print(i)
print("\n4 multiplication table")
num=int(input("enter a number:"))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")  
print("\n5 reverse counting")
for i in range(12,10,-1):
    print(i)
print("\n6 sum of first N number")
n=int(input("enter a number:"))
total=0
for i in range(1,n+1):
    total+=i
    print("sum=",total)
print("\n factorial")
num=int(input("enter a number"))
fact=1
for i in range(i,n+1):
    fact+=i
    print("factorial=",fact)    
