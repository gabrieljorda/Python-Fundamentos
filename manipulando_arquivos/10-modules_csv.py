import csv

cursos = []

with open("dados/cursos.csv", "r",encoding="utf-8")as file:
    reader = csv.DictReader(file)
    for i in reader:
        cursos.append({
            "language": i['language'],
            "category": i["category"]

        })
print(cursos)


