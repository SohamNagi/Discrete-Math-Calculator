from math import floor

def next_row(row1, row2):
    q = floor(row1[2]/row2[2])
    a= row1[0]- (q * row2[0])
    b = row1[1]- (q * row2[1])
    r = row1[2]- (q * row2[2])
    new_row = [a,b,r,q]
    return new_row

def eea(x,y):
    row_1 = [1,0, x ,0]
    row_2 = [0,1, y ,0]
    data = [row_1,row_2]
    a=0
    b=1    
    while(True):
        new_row =  next_row(data[a], data[b])
        data.append(new_row)
        a += 1
        b += 1
        if (new_row[2] == 0):
            break
        
    headers = ["a","b","r","q"]
    format_row = "{:>5}" * (len(headers) + 1)
    print(format_row.format("", *headers))
    for team, row in zip(headers, data):
        print(format_row.format(team, *row))
    return 1   
eea(40,3)