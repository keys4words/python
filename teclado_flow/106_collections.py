from collections import Counter, defaultdict

device_temperatures = [13.4, 5.0, 2.6, 65.4, 13.4]
temperature_counter = Counter(device_temperatures)
print(temperature_counter[13.4])

print(Counter({'hey': 5, 'hi': 3})['hi'])

print('==========')
coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'),
             ('Charlie', 'Manchester')]
alma_maters = defaultdict(list)

for coworker, place in coworkers:
    alma_maters[coworker].append(place)


print(alma_maters['Rolf'])
print(alma_maters['Ann'])

print('===============')
my_company = 'Teclado'
coworkers_new = ['Jen', 'Li', 'Charlie', 'Kris']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworkers_companies = defaultdict(lambda: my_company)
for person, company in other_coworkers:
    coworkers_companies[person] = company


print(coworkers_companies[coworkers_new[0]])
print(coworkers_companies['Rolf'])
