def main():
    grid = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    possibles = []
    n=0
    for i in range(0,144):
        for s1 in grid[0]:
            for s2 in grid[1]:
                if s1+s2<=i:
                    for s3 in grid[2]:
                        if s1+s2+s3<=i:
                            for s4 in grid[3]:
                                if sum([s1,s2,s3,s4])==i:
                                    for s5 in grid[4]:
                                        if s1+s5<=i:
                                            for s6 in grid[5]:
                                                if s2+s6<=i:
                                                    if s1+s6<=i:
                                                        for s7 in grid[6]:
                                                            if s3+s7<=i:
                                                                for s8 in grid[7]:
                                                                    if s4+s8<=i:
                                                                        if sum([s5,s6,s7,s8])==i:
                                                                            for s9 in grid[8]:
                                                                                if s1+s5+s9<=i:
                                                                                    for s10 in grid[9]:
                                                                                        if s2+s6+s10<=i:
                                                                                            if s4+s7+s10<=i:
                                                                                                for s11 in grid[10]:
                                                                                                    if s1+s6+s11<=i:
                                                                                                        if s3+s7+s11<=i:
                                                                                                            for s12 in grid[11]:
                                                                                                                if s4+s8+s12<=i:
                                                                                                                    for s13 in grid[12]:
                                                                                                                        if sum([s9,s10,s11,s12])==i:
                                                                                                                            if sum([s4,s7,s10,s13])==i:
                                                                                                                                if sum([s1,s5,s9,s13])==i:
                                                                                                                                    for s14 in grid[13]:
                                                                                                                                        if sum([s2,s6,s10,s14])==i:
                                                                                                                                            for s15 in grid[14]:
                                                                                                                                                if sum([s3,s7,s11,s15])==i:
                                                                                                                                                    for s16 in grid[15]:
                                                                                                                                                        n+=1
                                                                                                                                                        if sum([s1,s2,s3,s4])==i and sum([s5,s6,s7,s8])==i and sum([s9,s10,s11,s12])==i and sum([s13,s14,s15,s16])==i and sum([s1,s5,s9,s13])==i and sum([s2,s6,s10,s14])==i and sum([s3,s7,s11,s15])==i and sum([s4,s8,s12,s16])==i and sum([s1,s6,s11,s16])==i and sum([s4,s7,s10,s13])==i:
                                                                                                                                                            possibles.append([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16])
        print(i,possibles[0],possibles[-1])
    print(len(possibles))
    print('Fin')
    print(possibles)
main()

def compact():
    grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
    loopVars = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16]
    possibles = []
    for i
    for j in loopVars:
        for loopVars[j] in grid[j]:
            if sum([s1,s2,s3,s4])==i and sum([s5,s6,s7,s8])==i and sum([s9,s10,s11,s12])==i and sum([s13,s14,s15,s16])==i and sum([s1,s5,s9,s13])==i and sum([s2,s6,s10,s14])==i and sum([s3,s7,s11,s15])==i and sum([s4,s8,s12,s16])==i and sum([s1,s6,s11,s16])==i and sum([s4,s7,s10,s13])==i:
                possibles.append([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16])
    print(possibles)
