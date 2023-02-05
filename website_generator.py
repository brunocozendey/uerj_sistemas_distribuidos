import random, string, sys


def urlGenerator():
    end = [".uol.com.br",".com", ".com.br", ".de", ".fr", ".net"]
    names = []
    for i in range(random.randint(1,5)):
        name = ""
        for j in range(random.randint(1,5)):
            name = name+random.choice(string.ascii_letters)
        names.append(name)
    if (random.randint(0,1) == 0):
        protocol = "http://"
    else:
        protocol = "https://"
    return protocol+".".join(names)+end[random.randint(0,len(end)-1)]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        with open("data/data"+"_"+str(n)+".txt", "w") as file:
            for i in range(n):
                file.write(urlGenerator()+"\n")
    else:
        print("You forget the number of lines")

