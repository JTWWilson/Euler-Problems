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
possibles=0
for x in range(0,37):
    for a in range(0,10):#a
        for b in range(0,10):#a,b
            if a+b>x: continue
            for c in range(0,10):#a,b,c
                d=x-a+b+c#a,b,c,d
                if 0>d or d>9: continue
                #if a+b+c+d!=x: continue #unnecessary?
                for e in range(0,10):#a,b,c,d,e
                    if a+e>x: continue
                    for f in range(0,10):#a,b,c,d,e,f
                        if a+f>x: continue
                        if b+f>x: continue
                        if e+f>x: continue
                        for g in range(0,10):#a,b,c,d,e,f,g
                            if c+g>x: continue
                            if d+g>x: continue
                            h=x-e-f-g#a,b,c,d,e,f,g,h
                            if 0>h or h>9: continue
                            if d+h>x: continue
                            #if e+f+g+h!=x: continue
                            for i in range(0,10):#a,b,c,d,e,f,g,h,i
                                m=x-a-e-i#a,b,c,d,e,f,g,h,i,m
                                if 0>m or m>9: continue
                                #if a+e+i+m!=x: continue
                                j=x-d-g-m#a,b,c,d,e,f,g,h,i,j,m
                                if 0>j or j>9: continue
                                #if d+g+j+m!=x: continue
                                if i+j>x: continue
                                n=x-b-f-j#a,b,c,d,e,f,g,h,i,j,m,n
                                if 0>n or n>9: continue
                                #if b+f+j+n!=x: continue
                                if m+n>x: continue
                                for p in range(0,10):#a,b,c,d,e,f,g,h,i,j,m,n,p
                                    if possibles==151758:
                                        print('final')
                                    k=x-a-f-p#a,b,c,d,e,f,g,h,i,j,k,m,n,p
                                    if 0>k or k>9: continue
                                    #if a+f+k+p!=x: continue
                                    l=x-i-j-k#a,b,c,d,e,f,g,h,i,j,k,l,m,n,p
                                    if 0>l or l>9: continue
                                    #if i+j+k+l!=x: continue
                                    o=x-p-m-n#a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
                                    if 0>o or o>9: continue
                                    #if m+n+o+p!=x: continue
                                    print('',a,b,c,d,'\n',e,f,g,h,'\n',i,j,k,l,'\n',m,n,o,p)
                                    possibles+=1
print(possibles)
