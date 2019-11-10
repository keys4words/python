from exercise.horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page(head, body):
    return f"""<!DOCTYPE html>
        <html lang="ru">
        {head}
        {body}
        </html>"""

def generate_head(title):
    head = f"""
         <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
            integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="style.css">
        <script src="https://code.jquery.com/jquery-3.4.1.min.js"
            integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
            crossorigin="anonymous"></script>
        <title>{title}</title>"""
    return f'<head>{head}</head>'

def generate_body(header, paragraphs):
    body = f"""<div class="container">
        <h1>{header}</h1>"""
    for p in paragraphs:
        body += f"<p>{p}</p>"
    return f"<body>{body}</div></body>"

def save_page(title, header, paragraphs, output="index.html"):
    fp = open('index.html', 'w', encoding="utf8")
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header, paragraphs=paragraphs)
    )
    print(page, file=fp)
    fp.close()

today = dt.now().date()
save_page(
    title="Гороскоп на сегодня",
    header="Что день " + str(today) + " готовит",
    paragraphs=generate_prophecies(),
)