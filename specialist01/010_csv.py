import csv

with open(r'C:\Users\User\PycharmProjects\python\specialist01\res2.csv', 'a+', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    writer = csv.writer(f, delimiter=',')
    # for row in reader:
    #     print(row)
    writer.writerow([])
    writer.writerow(['Pete Dow', 'CEO', 'December'])
