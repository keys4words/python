area = lambda ar: ar ** 2 * 3.19
print(area(2))

PI = 3.141592653589793
PI = format(PI, '.4f')
print(float(PI))

countries = {'us': 'United States of America', 'br': 'Brazil', 'de': 'Germany', 'at': 'Austria'}
keys = sorted(countries.keys())
for k in keys:
    print(countries[k])