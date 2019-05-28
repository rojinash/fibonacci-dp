
def fib(num):
    arr = [0,1]
    while(len(arr)<num+1):
        arr.append(0)
    if(num==0 or num==1):
        return 1
    else:
        arr[0]=1
        arr[1]=1
        for i in range(2,num+1):
            arr[i]=arr[i-1]+arr[i-2]
        return arr[num]

print("Hello World")
print(fib(3))
    
