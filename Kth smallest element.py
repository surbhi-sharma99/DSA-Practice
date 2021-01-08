'''
from an array find kth smallest element:-
 example -
 arr = [2,4,6,3,9]
 k = 2
 than we have to find 2nd smallest element in array.
 '''
arr = list(map(int,input().strip().split()))
n = int(input())
arr.sort()
print(arr[n-1])
