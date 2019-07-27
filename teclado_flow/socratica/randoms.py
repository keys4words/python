import random

#print(help(random.random))
def my_random():
    return 3 + 4 * random.random()

#
# for i in range(10):
#     #print(my_random())
#     print(random.uniform(3, 7))

# for i in range(20):
#     print(random.normalvariate(0, 1))

# for i in range(20):
#     print(random.randint(1, 6))

outcomes = ['rock', 'paper', 'scissors']
for i in range(10):
    print(random.choice(outcomes))