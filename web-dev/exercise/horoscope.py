import random

times = ["Утром", "Днём", "После обеда", "Ночью"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого.", "приятных перемен.", "встреч со старыми знакомыми."]

def generate_prophecies(total_num=5, num_sentences=3):
    prophecies = []
    for i in range(total_num):
        forecast = ""
        for j in range(num_sentences):
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = f'{t.title()} {a} {p}'
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence
        prophecies.append(forecast)
    return prophecies


