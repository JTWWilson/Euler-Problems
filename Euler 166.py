def calculate():
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
    possibles = 0

    for a in range(0, 10):  # a
        for b in range(0, 10):  # a,b
            for c in range(0, 10):  # a,b,c
                for d in range(0, 10):
                    for e in range(0, 10):  # a,b,c,d,e
                        if e > b + c + d or e + (3 * 9) < a + b + c + d: continue
                        for f in range(0, 10):  # a,b,c,d,e,f
                            if f > b + c + d or f + (3 * 9) < a + b + c + d: continue
                            if f > a + c + d: continue
                            if e + f > a + b + c + d: continue
                            for g in range(0, 10):  # a,b,c,d,e,f,g
                                if g > a + b + d or g + (3 * 9) < a + b + c + d: continue
                                if g > a + b + c: continue
                                h = a + b + c + d - e - f - g  # a,b,c,d,e,f,g,h
                                if 0 > h or h > 9: continue
                                if h > a + b + c or h + (3 * 9) < a + b + c + d: continue
                                for i in range(0, 10):  # a,b,c,d,e,f,g,h,i
                                    m = b + c + d - e - i  # a,b,c,d,e,f,g,h,i,m
                                    if 0 > m or m > 9 or m + (3 * 9) < a + b + c + d: continue
                                    j = a + b + c - g - m  # a,b,c,d,e,f,g,h,i,j,m
                                    if 0 > j or j > 9 or j + (3 * 9) < a + b + c + d: continue
                                    if i + j > a + b + c + d: continue
                                    n = a + c + d - f - j  # a,b,c,d,e,f,g,h,i,j,m,n
                                    if 0 > n or n > 9 or n + (3 * 9) < a + b + c + d: continue
                                    if m + n > a + b + c + d: continue
                                    for p in range(0, 10):  # a,b,c,d,e,f,g,h,i,j,m,n,p
                                        if p + (3 * 9) < a + b + c + d: continue
                                        k = b + c + d - f - p  # a,b,c,d,e,f,g,h,i,j,k,m,n,p
                                        if 0 > k or k > 9 or k + (3 * 9) < a + b + c + d: continue
                                        l = a + b + c + d - i - j - k  # a,b,c,d,e,f,g,h,i,j,k,l,m,n,p
                                        if 0 > l or l > 9 or l + (3 * 9) < a + b + c + d: continue
                                        o = a + b + c + d - p - m - n  # a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
                                        if 0 > o or o > 9 or o + (3 * 9) < a + b + c + d: continue
                                        if e + f + g + h == a + b + c + d  and i + j + k + l == a + b + c + d  and m + n + o + p == a + b + c + d  and\
                                            a + e + i + m == a + b + c + d  and b + f + j + n == a + b + c + d  and c + g + k + o == a + b + c + d  and d + h + l + p == a + b + c + d  and \
                                            a + f + k + p == a + b + c + d  and d + g + j + m == a + b + c + d:
                                            #if a + b + c + d > 33:
                                            #    print('\n', a, b, c, d, '\n', e, f, g, h, '\n', i, j, k, l, '\n', m, n, o, p)
                                            possibles += 1
    return possibles

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("calculate()", setup="from __main__ import calculate"))