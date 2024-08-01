def fib():
    res = fib.fib1 + fib.fib2
    fib.fib1, fib.fib2 = fib.fib2, res
    yield res
fib.fib1 = 0
fib.fib2 = 1

### or
# def fib():
#    fib1, fib2 = 1, 1
#    while 1:
#        yield fib1
#        fib1, fib2 = fib2, fib1 + fib2
    
# testing code
import types
if type(fib()) == types.GeneratorType:
    counter = 0
    for f in fib():
        print(f)
        counter += 1
        if counter == 10:
            break

import random
def lottery():
    for i in range(6):
        yield random.randint(1, 40)

    # the 7th number between 1 and 15 (exc)
    yield random.randint(1, 15)

for random_number in lottery():
       print("And the next number is... %d" % random_number)
