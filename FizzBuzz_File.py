import numpy as np

def FizzBuzz(start, finish):

    numvec = np.arange(start, finish + 1)

    result = np.array(numvec, dtype=object)

    fizz = (numvec % 3 == 0)
    buzz = (numvec % 5 == 0)

    result[fizz] = "fizz"
    result[buzz] = "buzz"
    result[fizz & buzz] = "fizzbuzz"

    return result

print(FizzBuzz(16, 30))