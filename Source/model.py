import os
class arq:
    def __init__(self, path):
        self.path = os.path.join(path)
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
        self.continued = False
        #print(os.getcwd()  + ("\\Source" if "Source" not in os.getcwd() else "") + "\\Data\\partys")
        self.ps = arq(os.getcwd()  + ("\\Source" if "Source" not in os.getcwd() else "") + "\\Data\\partys")
        self.pr = arq(os.getcwd()  + ("\\Source" if "Source" not in os.getcwd() else "") + "\\Data\\progress")
        
        self.partys = []
        if self.ps.content == "":
            print("Sem chapas")
            return None
        else:
            for i in self.ps.read(0):
                p = party(i.replace("\n", ""))
                self.partys.append(p)

    def continue_election(self, progress_content):
        progress_lines = progress_content.split("\n")
        self.partys = []
        for line in progress_lines:   
            index = 0
            separed_line = line.split(" : ")
            p = party(separed_line[0])
            p.points = (int(separed_line[1].split(" ")[0]) if separed_line[1].split(" ")[0].isdigit() else 0)
            self.partys.append(p)
            index += 1
        self.continued = True

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
                    

    def progress(self, status="Running"):
        output = ""
        for p in self.partys:
            output += p.name + " : " + str(p.points) + (" votos" if p.points != 1 else " voto") + "\n"
        self.pr.write(output + status)
        return output
    
    def finish(self):
        self.progress("Finished")


