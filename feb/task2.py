for x in range (0,2):
    for y in range (0,2):
        for w in range (0,2):
            for z in range (0,2):
                if ((((x<=y)==(z<=w)) or (x and w)) == 0):
                    print (x,y,w,z)