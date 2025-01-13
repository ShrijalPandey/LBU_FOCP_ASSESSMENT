'''
Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by
another to yield the original).
'''

def factors(num):
    list=[]
    for i in range(1, num + 1):
        if num % i == 0:
            list.append(i)

    return list
fact=factors(56)
print("The factors of 18 are:",fact)