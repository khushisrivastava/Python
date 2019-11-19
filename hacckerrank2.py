N, M=input().split()
n=int(N)
m=int(M)
S=[]
L=[]
s1=[]
while m-1!=0:
    u,v=input().split()
    U=int(u)
    V=int(v)
    if U in range(1,n+1):
        S.append(U)
    if V in range(1,n+1):
        L.append(V)
    m=m-1
s=set(S)
l=set(L)
for num in s:
    if num not in l:
        s1.append(num)

S1=set(s1)
f=' '.join(str(e) for e in S1)
print(f)
