from app import books

USER_CHOICE = '''Enter one of the following
- 'b'  to look at 5-star books
- 'c'  to look at the cheapest books
- 'n'  to get next available books on the page
- 'q'  to quit

Your input: '''

def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


def print_best_expensive_books():
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price * -1))[:10]
    for book in best_books:
        print(book)

books_generator = (x for x in books)

def get_next_books():
    print(next(books_generator))

user_choice = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_books
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in {'b', 'c', 'n'}:
            user_choice[user_input]()
        else:
            print('Please choose a valid command')
        user_input = input(USER_CHOICE)


menu()