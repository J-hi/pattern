n=int(input())
i=1
while(i<=n):
    j=1
    if i!=n:
        while(j<=i): 
                print("*", end=' ')
                print(' ', end=' ')
            j+=1
        print()
    else:
        while(j<=i):
            print("*", end=' ')           
            j+=1
        
    i+=1
