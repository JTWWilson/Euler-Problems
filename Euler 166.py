"""
Algebra
Call the grid
a,b,c,d,
e,f,g,h,
i,j,k,l,
m,n,o,p
call the sum of each line x

a,b,c,e,f,g,i,p are needed to imply the rest
because:
d=x-a-b-c
h=x-e-f-g
m=x-a-e-i
j=x-d-g-m
n=x-b-f-j
o=x-p-m-n
k=x-a-f-p
l=x-i-j-k
"""
x=12
possibles=0
for a in range(0,10):#a
    for b in range(0,10):#a,b
        if a+b>x: break
        for c in range(0,10):#a,b,c
            d=x-a+b+c#a,b,c,d
            if 0>d or d>9: break
            if a+b+c+d!=x: break
            for e in range(0,10):#a,b,c,d,e
                if a+e>x: break
                for f in range(0,10):#a,b,c,d,e,f
                    if a+f>x: break
                    if b+f>x: break
                    if e+f>x: break
                    for g in range(0,10):#a,b,c,d,e,f,g
                        if c+g>x: break
                        if d+g>x: break
                        h=x-e-f-g#a,b,c,d,e,f,g,h
                        if 0>h or h>9: break
                        if d+h>x: break
                        if e+f+g+h!=x: break
                        for i in range(0,10):#a,b,c,d,e,f,g,h,i
                            m=x-a-e-i#a,b,c,d,e,f,g,h,i,m
                            if 0>m or m>9: break
                            if a+e+i+m!=x: break
                            j=x-d-g-m#a,b,c,d,e,f,g,h,i,j,m
                            if 0>j or j>9: break
                            if d+g+j+m!=x: break
                            if i+j>x: break
                            n=x-b-f-j#a,b,c,d,e,f,g,h,i,j,m,n
                            if 0>n or n>9: break
                            if b+f+j+n!=x: break
                            if m+n<x: break
                            for p in range(0,10):#a,b,c,d,e,f,g,h,i,j,m,n,p
                                k=x-a-f-p#a,b,c,d,e,f,g,h,i,j,k,m,n,p
                                if 0>k or k>9: break
                                if a+f+k+p!=x: break
                                l=x-i-j-k#a,b,c,d,e,f,g,h,i,j,k,l,m,n,p
                                if 0>l or l>9: break
                                if i+j+k+l!=x: break
                                o=x-p-m-n#a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
                                if 0>o or o>9: break
                                if m+n+o+p!=x: break
                                print('',a,b,c,d,'\n',e,f,g,h,'\n',i,j,k,l,'\n',m,n,o,p)
                                possibles+=1
print(possibles)