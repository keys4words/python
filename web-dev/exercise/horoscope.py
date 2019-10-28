import random

times = ["Утром", "Днём", "Вечером", "Ночью"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей", "встреч", "неожиданного праздника"]

def generate_prophecies(total_num=5, num_sentences=3):
    prophecies = []
    i = 0
    while i < total_num:
        j = 0
        forecast = ""
        while j < num_sentences:
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = t.title() + " " + a + " " + p
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence
            j = j + 1
        prophecies.append(forecast)
        i = i + 1
    return prophecies


def generate_body(header, paragraph):
    body = "<h1>" + header + "</h1>"
    for p in paragraph:
        body += "<p>" + p + "</p>"
    return "<body>" + body + "</body>"