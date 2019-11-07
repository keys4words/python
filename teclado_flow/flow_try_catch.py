def main():
    d = {'website': 'google', 'url': 'yandex.ru'}
    try:
        data = d['url']
    except:
        data = 'https://'
    else:
        data = data.upper()
    print(data)


main()
