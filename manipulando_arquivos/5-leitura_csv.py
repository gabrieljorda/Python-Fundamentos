with open("dados/cursos.csv", "r",encoding="utf-8")as file:
    for line in file:
        # line = line.rstrip().split(",")
        # print(line[0])
        # print(line[1])
        linguagem , cateforia = line.rstrip().split(",")
        print(f" {linguagem} -> {cateforia}")
        