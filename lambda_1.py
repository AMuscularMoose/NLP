remainder = lambda num: num%2
print(remainder(5))

def testfunc(num):
    #print(num)
    return lambda x: x*num

result1 = testfunc(10)
result2 = testfunc(100)

print(result1(9))
print(result2(9))