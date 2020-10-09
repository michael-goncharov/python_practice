from sys import argv
import math

if len(argv) < 4: raise Exception('you should specify 3 arguments, you entered: {}'.format(len(argv)-1))

a = int(argv[1])
b = int(argv[2])
c = int(argv[3])

if a<=0: raise Exception('a should be greater than 0, you entered: {}'.format(a))
if b<=0: raise Exception('a should be greater than 0, you entered: {}'.format(b))
if c<=0: raise Exception('a should be greater than 0, you entered: {}'.format(c))

p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))

print(s)
