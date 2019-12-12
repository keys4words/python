def cow_generator():
    yield 'cow'
    for name in ['zoika', 'milka', 'burenka']:
        yield name
    yield 'bob'

for cow in cow_generator():
    print(cow)