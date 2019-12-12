print('code before outer try')
try:
    n = '1'
    print('code before inner try')
    try:
        s = 'a' > 1
    except:
        print('inner except')
        raise Exception('exception from inner')
    finally:
        print('inner finally')
    print('code after inner try')
except Exception as e:
    print('outer except', e)
finally:
    print('outer finally')
print('code after outer try')
