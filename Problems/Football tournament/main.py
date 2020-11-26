
import itertools
import math
my_iter = itertools.combinations(teams, 2)
for i in itertools.combinations(teams, 2):
    print(next(my_iter))
