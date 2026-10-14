 #0(1) constant time complexity space complexity
n=int(input("Enter a number:"))
print(n+100)

#0(n) - Linear time complexity
'''n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i,end=' ')'''

#o(n) -Linear time complexity linear space complexity 0(1)
'''n=int(input("Enter a number:"))
arr = []
for i in range(n):
    num = int(input("Enter a value:"))
    arr.append(num)
print("List",arr)'''

'''n=int(input("Enter a number:"))
num=1
for i in range(n):
    for i in range(i):
        print(num,end= '  ')
        num+=1
    print(n)'''

#Logarthmic TC
'''n=int(input("Enter a number:"))
while n>1:
    print(n)
    n//=2
print(1)'''

'''def count(n):
    if n==0:
        return 1
    return count(n-1) + count(n-1)
n= int(input("Enter a number:"))
print("result:",count(n))'''
       
