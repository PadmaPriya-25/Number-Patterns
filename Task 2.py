def print_pyramid(n):
    num=1
    for i in range(n):
        for j in range(n-i-1):
            print("",end="")
        for k in range(i+1):
            print(num,end="")
            num+=1
        print()
n=int(input("enter the number of rows:"))
print_pyramid(n)
