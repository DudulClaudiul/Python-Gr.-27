
import random
from lib.core import even_numbers, is_even

# print(random.sample(range(0, 1000), 15))

random_numbers = [265, 581, 110, 652, 28, 466, 746, 468, 801, 870, 763, 576, 173, 372, 604]

#filter(), map(), reduce(), zip() - functii built in

#lamda functions: este efemera




def mult_2(param1):
    return param1 * 2

print(mult_2(10))

square = lambda x: x * 2

print(square(10))

#filtrati toate numerele multiplu de 7

rezultat = list(filter(lambda x: x%7 == 0, random_numbers))
print(rezultat)

rezultat2 = list(filter(is_even, random_numbers))
print(rezultat2)