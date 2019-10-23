import random
times = ["Утром", "Днём", "Вечером", "Ночью"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей", "встреч", "неожиданного праздника"]
i = 0
while i < 3:
    t = random.choice(times)
    a = random.choice(advices)
    p = random.choice(promises)
    print(t + " " + a + " " + p)
    i = i + 1