'''
dutch natioanl flag problem
'''
a= list(map(int, input().strip().split()))
n = len(a)
l = 0
m = 0
h = n-1
while m<=h:
    if a[m] ==0:
        a[l],a[m]=a[m],a[l]
        l = l+1
        m = m+1
    elif a[m]==1:
        m = m+1
    else:
        a[m],a[h]=a[h],a[m]
        h = h-1
print(a)
        
