# 利用函数计算 24 + 34/100 - 1023
def add(a,b):
    print ("a: %r, b: %r" % (a,b))
    return a + b

def divide(a,b):
    print ("a: %r, b: %r" % (a,b))
    return a / b
	
def substarct(a,b):
    print ("a: %r, b: %r" % (a,b))
    return a - b

second = float(divide(340,100))
first = float(add(24,second))
third = float(substarct(first,1023))

print (first+second-third)
