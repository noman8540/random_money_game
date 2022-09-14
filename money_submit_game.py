import random

test_seed = int(input("Create a seed number: \n"))
random.seed(test_seed)


names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")


num_items = len(names)

random_choise = random.randint(0, num_items-1)
person_who_will_pay = names[random_choise]
print(person_who_will_pay + " is going to buy the meal today!")