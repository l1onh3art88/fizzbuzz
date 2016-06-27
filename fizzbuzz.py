#Fizzbuzz Thinkful Challenge with Extra Challenge using inputs

import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv)))


try:
    x=sys.argv[1]
   
    for x in range(1,int(x)):
        if x%15==0:
            print("fizzbuzz")
        elif x%5==0: 
            print ("buzz")
        elif x%3==0:
            print ("fizz")
        else:
            print(x)
except:
    n = input("pick a number\n")
    for n in range(1,int(n)):
        if n%15==0:
            print ("fizzbuzz")
        elif n%5==0: 
            print ("buzz")
        elif n%3==0:
            print ("fizz")
        else:
            print(n)
