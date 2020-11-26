
import itertools
for main_course, dessert, drink,  in itertools.product(zip(main_courses,price_main_courses), zip(desserts,price_desserts), zip(drinks, price_drinks)):
    total_cost = main_course[1] + drink[1] + dessert[1]
    if total_cost <= 30:
        print(main_course[0], dessert[0], drink[0], total_cost, sep=' ')
