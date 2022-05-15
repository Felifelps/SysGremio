class party:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def one(self):
        self.points += 1

class election:
    def __init__(self, partys):
        self.partys = partys

    def vote(self, partyNumber):
        self.partys[partyNumber - 1].one()

    def finalize(self):
        output = ""
        for party in self.partys:
            output += party.name + ": " + str(party.points) + (" votos" if party.points != 1 else "  voto") + "\n"
        return output


class arq:
    def __init__(self, path):
        self.path = path
        with open(self.path, "w") as arq:
            arq.write("")
        with open(self.path, "r") as arq:
            read = arq.readlines()
        self.content = "".join(read)

    def read(self, string=1):
        with open(self.path, "r") as arq:
            read = arq.readlines()
        if string:
            return "".join(read)
        return read

    def write(self, text, mode="e"):
        with open(self.path, "w") as arq:
            if mode == "e":
                arq.write(text)
            elif mode == "a":
                with open(self.path, "r") as arq:
                    r = "".join(arq.readlines())
                arq.write(r + text)
            else:
                print("The mode can be:\na:add text, without rewriting\ne:rewrite everything")
        with open(self.path, "r") as arq:
            read = arq.readlines()
        self.content = "".join(read)



source = arq("source.txt")
fd = party("FD - Força Democrática")
puma = party("PUMA - Para Um Melhor Aprendizado")
c3 = party("Chapa 3")

e = election([fd, puma, c3])
e.vote(3)
print(e.finalize())
