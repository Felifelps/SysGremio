class arq:
    def __init__(self, path):
        self.path = path
        try:
            with open(self.path, "r") as arq:
                read = arq.readlines()
        except:
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
            elif "a" in mode:
                arq.write(self.content + ('\n' if mode == 'al' else '') + text)
            else:
                print("The mode can be:\na:add text, without rewriting\nal: add the text in a new line\ne: erase the current text, rewriting everything")
        with open(self.path, "r") as arq:
            read = arq.readlines()
        self.content = "".join(read)


class party:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def one(self):
        self.points += 1


class election:
    def __init__(self):
        self.ps = arq("chapas")
        self.pr = arq("progress")
        self.partys = []
        if self.ps.content == "":
            print("Sem chapas")
            return None
        else:
            for i in self.ps.read(0):
                p = party(i.replace("\n", ""))
                self.partys.append(p)

    def vote(self, pid):
        n = 1
        if self.partys == []:
            print("Sem chapas")
            return 0
        elif pid < 1 or pid > len(self.partys):
            text = "\nID fora do alcance\n$IDs das Chapas"
            for i in self.partys:
                text += "\n [" + i.name + "] : " + str(n)
                n += 1
            print(text + "\n")
        else:
            for p in self.partys:
                if pid == n:
                    p.one()
                    break
                n += 1
            self.progress()
                    

    def progress(self):
        output = ""
        for p in self.partys:
            output += p.name + ": " + str(p.points) + (" votos" if p.points != 1 else "  voto") + "\n"
        self.pr.write(output)
        c = arq("progress.txt")
        c.write(output)
        return output
