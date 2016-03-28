def main():
    grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
    possibles = [[]]
    for s1 in grid[0]:
        for s2 in grid[1]:
            if s1+s2<12:
                for s3 in grid[2]:
                    if s1+s2+s3<12:
                        for s4 in grid[3]:
                            print(len(possibles),possibles[-1])
                            if sum([s1,s2,s3,s4])==12:
                                print(s1,s2,s3,s4)
                                for s5 in grid[4]:
                                    if s1+s5<12:
                                        for s6 in grid[5]:
                                            if s2+s6<12:
                                                if s1+s6<12:
                                                    for s7 in grid[6]:
                                                        if s3+s7<12:
                                                            for s8 in grid[7]:
                                                                if s4+s8<12:
                                                                    if sum([s5,s6,s7,s8])==12:
                                                                        for s9 in grid[8]:
                                                                            if s1+s5+s9<12:
                                                                                for s10 in grid[9]:
                                                                                    if s2+s6+s10<12:
                                                                                        if s4+s7+s10<12:
                                                                                            for s11 in grid[10]:
                                                                                                if s1+s6+s11<12:
                                                                                                    if s3+s7+s11<12:
                                                                                                        for s12 in grid[11]:
                                                                                                            if s4+s8+s12<12:
                                                                                                                for s13 in grid[12]:
                                                                                                                    if sum([s9,s10,s11,s12])==12:
                                                                                                                        for s14 in grid[13]:
                                                                                                                            for s15 in grid[14]:
                                                                                                                                for s16 in grid[15]:
                                                                                                                                    if sum([s1,s2,s3,s4])==12 and sum([s5,s6,s7,s8])==12 and sum([s9,s10,s11,s12])==12 and sum([s13,s14,s15,s16])==12 and sum([s1,s5,s9,s13])==12 and sum([s2,s6,s10,s14])==12 and sum([s3,s7,s11,s15])==12 and sum([s4,s8,s12,s16])==12 and sum([s1,s6,s11,s16])==12 and sum([s4,s7,s10,s13])==12:
                                                                                                                                        possibles.append([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16])
    print(len(possibles))
main()