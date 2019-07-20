from requests import get

print(get('https://stepik.org/favicon.ico').headers['Server'])