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

def prime(p):
    prime=False
    if (int(p)==2 or int(p)==1):
        prime=False
    for number in range(2, int(p)):
        val=int(p)/int(number)
        if val.is_integer():
            prime=True
            break
    if (prime==True):
        print(p,"num is not prime")
        return False
    else:
        print(p,"num is prime")
        return True
#prime(3)
#prime(100)
#prime(43)
def prime_factor(fpf):
    pflst=[]
    for number in range(2, math.ceil(math.sqrt(fpf))):
        val=int(fpf)/int(number)
        if val.is_integer() and prime(number)==True:
            pflst.append(number)
    print("The prime factors for", fpf,"are: ",pflst)
    return pflst

def print_factors(x):
   retval=[]
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           retval.append(i)
   print("The factors for", x,"are: ",retval)
   return retval
#print_factors(10)

def coprime(x,y):
    x_factors=print_factors(x)
    y_factors=print_factors(y)
    same=0
    for elem in x_factors:
        if elem in y_factors:
            same=same+1
    if same==1:
        print(x,"and", y, "are coprime")
        return True
        
    else:
        print(x,"and", y, "are not coprime")
        return False

#coprime(9,90)

def remainder(big,small):
    print("The remainder of", big, "and",small,"is",int(big)%int(small))
    return int(big)%int(small)
#remainder(15,4)
import time

print('''
  _      _                                  _            _                 __    _____      _            _       _             
 | |    (_)                           /\   | |          | |               /_ |  / ____|    | |          | |     | |            
 | |     _ _ __   ___  __ _ _ __     /  \  | | __ _  ___| |__  _ __ __ _   | | | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |    | | '_ \ / _ \/ _` | '__|   / /\ \ | |/ _` |/ _ \ '_ \| '__/ _` |  | | | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |____| | | | |  __/ (_| | |     / ____ \| | (_| |  __/ |_) | | | (_| |  | | | |___| (_| | | (__| |_| | | (_| | || (_) | |   
 |______|_|_| |_|\___|\__,_|_|    /_/    \_\_|\__, |\___|_.__/|_|  \__,_|  |_|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                               __/ |                                                                           
                                              |___/                                                                            
    ''')
while (True):
    time.sleep(3)
    val=int(input('''Input 1 for gcd\nInput 2 for Extended Euclidean Table\nInput 3 for Prime Number Checker\nInput 4 for Linear Diophantine Equation Solver\nInput 5 for Prime Factor List\nInput 6 for Factor List\nInput 7 for Remainder Calculator\nInput 8 for Coprime Checker\nInput 9 for Modulus Calculator\nInput 10 to Quit\nInput:'''))
    if(val == 1):
        num1 = int(input("What's your first number: "))
        num2 = int(input("What's your second number: "))
        print("The gcd for your numbers is:", gcd(num1,num2))
    elif (val == 2):
        num1 = int(input("What's your first number: "))
        num2 = int(input("What's your second number: "))
        eea(num1,num2)
    elif (val == 3):
        num1 = int(input("What's your number: "))
        prime(num1)
    elif (val == 4):
        num1 = int(input("What's your a value: "))
        num2 = int(input("What's your b value: "))
        num3 = int(input("What's your c value: "))
        LDE(num1,num2,num3)
    elif (val == 5):
        p=int(input("Integer:"))
        prime_factor(p)
    elif (val == 6):
         num1 = int(input("What's your number: "))
         print_factors(num1)
    elif (val == 7):
       num1 = int(input("What's your bigger number: "))
       num2 = int(input("What's your smaller number: "))
       print("The remainder for your numbers is:", remainder(num1,num2)) 
    elif (val == 8):
        num1 = int(input("What's your first number: "))
        num2 = int(input("What's your second number: "))
        coprime(num1,num2)
    elif (val == 9):
        num1 = int(input("x=a(mod y)\na: "))
        num2 = int(input("y: "))
        print("x:", remainder(num1,num2)) 
    elif val == 10:
        break