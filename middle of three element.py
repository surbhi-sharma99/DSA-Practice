print("Enter three element")
A,B,C = input().split()
if (A<B and C>B) or (A>B and C<B):
    print(B)
elif (A>B and C>A) or (A<B and A>C):
    print(A)
else:
    print(C)
