#Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
'''
def eval_dict(d):
    res = 1
    for (base,exponent) in d.items():
        res = res*(base**exponent)
    return res


def eval_combination(d):
    res = 1
    for idx,char in enumerate(d):
        if idx==0:
            base = 2
        elif idx==1:
            base = 3
        else:
            base = 5

        res *= base**int(char)
    return res



#print(eval_dict({2:3,3:1,5:2}))
print(eval_combination('101'))

def nthUglyNumber(n):
    if n==1:
        return 1

    res = [ [i for i in range(n)] for x in range(3)]
    return res

print(nthUglyNumber(2))
'''
def maxDivide(num,denom):
    while num%denom==0:
        num = num/denom
    return num

def is_ugly(number):
    number = maxDivide(number,2)
    number = maxDivide(number, 3)
    number = maxDivide(number, 5)
    return 1 if number ==1 else 0

print(is_ugly(1))