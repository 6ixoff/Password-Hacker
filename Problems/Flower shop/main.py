import itertools
my_iter = itertools.combinations(flower_names,1)
for i in itertools.combinations(flower_names,1):
    print(next(my_iter))
my_iter = itertools.combinations(flower_names,2)
for i in itertools.combinations(flower_names,2):
    print(next(my_iter))
my_iter = itertools.combinations(flower_names,3)
for i in itertools.combinations(flower_names,3):
    print(next(my_iter))
