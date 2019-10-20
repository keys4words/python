#wrong method
def unique(iterable, seen=set()):
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc

def unique2(iterable, seen=None):
    seen = set(seen or [])
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc

xs = [1, 1, 2, 3]
print(unique2(xs))
print(unique2(xs))
print(unique2.__defaults__)

