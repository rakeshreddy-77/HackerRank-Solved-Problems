def powerof(a,b):
    if(b==0):
        return 1
    if(b==1):
        return a
    r=powerof(a,b//2)
    if(b%2==0):
        return r*r
    else:
        return a*r*r
def myfun(X,n,s=0,num=1):
    c=0
    p=powerof(num,n)
    while(p+s<X):
        c+=myfun(X,n,s+p,num+1)
        num+=1
        p=powerof(num,n)
    if(p+s==X):
        c+=1
    return c
X=int(input())
n=int(input())
print(myfun(X,n))
