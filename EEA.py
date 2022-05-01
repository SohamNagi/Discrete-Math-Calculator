from math import floor
from math import gcd

def next_row(row1, row2):
    q = floor(row1[2]/row2[2])
    a= row1[0]- (q * row2[0])
    b = row1[1]- (q * row2[1])
    r = row1[2]- (q * row2[2])
    new_row = [a,b,r,q]
    return new_row

def eea(x,y):
    headers = ["a","b","r","q"]
    block = ["---","---","---","---"]
    block2 = ["-----","-----","-----","-----"]
    row_1 = [1,0, x ,0]
    row_2 = [0,1, y ,0]
    data = [block, headers,block,row_1,row_2]
    a=3
    b=4    
    while(True):
        new_row =  next_row(data[a], data[b])
        data.append(new_row)
        a += 1
        b += 1
        if (new_row[2] == 0):
            data.append(block)
            break
        
    for row in data:
        print('| {:^5} | {:^5} | {:^5} | {:^5} |'.format(*row))
    return data[b-1]     

def LDE(a,b, c):
    if ((c % gcd(a,b)) != 0):
        print("A solution does not exist!")
    else:
        row = eea(a,b)
        cd = c/gcd(a,b)
        out_a = row[0]*cd
        out_b = row[1]*cd
        print(out_a,"a + ",out_b, "b = ", c)

LDE(84,35,63)