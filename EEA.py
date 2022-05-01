from math import floor
from math import gcd
import math

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

from sqlalchemy import false, true



def prime(p):
    print("p=",p)
    prime=false
    if (int(p)==2 or int(p)==1):
        prime=false
    for number in range(2, int(p)):
        print("number=",number)
        val=int(p)/int(number)
        print("val=",val)
        if val.is_integer():
            prime=true
            print("done")
            break
    if (prime==true):
        print(p,"num is not prime")
        return false
    else:
        print(p,"num is prime")
        return true
#prime(3)
#prime(100)
#prime(43)
def prime_factor(fpf):
    pflst=[]
    for number in range(2, math.ceil(math.sqrt(fpf))):
        val=int(fpf)/int(number)
        print("val=",val)
        if val.is_integer() and prime(number)==true:
            pflst.append(number)
    print(pflst)
    return pflst

def print_factors(x):
   retval=[]
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           retval.append(i)
   print(retval)
   return retval
#print_factors(10)

def coprime(x,y):
    x_factors=print_factors(x)
    y_factors=print_factors(y)
    same=0
    for elem in x_factors:
        if elem in y_factors:
            print (elem,"is in ylst")
            same=same+1
    if same==1:
        print(x,"and", y, "are coprime")
        return true
        
    else:
        print(x,"and", y, "are not coprime")
        return false

#coprime(9,90)

def remainder(big,small):
    print("the remainder of", big, "and",small,"is",int(big)%int(small))
    return int(big)%int(small)
remainder(15,4)