def one():
    s = 'a' + 'b'
    raise Exception('message from func one')

def two():
    n = 'a'>1
    if True:
        raise Exception


def three():
    two()

try:
    one()
    two()
    three()
except:
    print('....')
