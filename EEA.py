from math import floor

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
    return 1     
eea(789,55)