def f(x):
    return 3*x + 1


print(f(3))

x_ = lambda x: 3 * x + 1
print(x_(3))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name('       MAX ', 'zharnikov'))

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C.Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]
# print(help(scifi_authors.sort))

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)