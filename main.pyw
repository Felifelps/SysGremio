from PySimpleGUI import *
import source

senha = "inforTop"
chapas = source.chapasBase
print(chapas)
with open("source.py", "w") as arq:
    arq.write("chapas = [{}, {}]".format(chapas[1], chapas[0]))
import source
chapas = source.chapasBase
print(chapas)   
with open("source.txt", "w") as arq:
    arq.write(": 0 votos \n".join(chapas) + ": 0 votos")

##Auxiliar functions##
def semN(string):
    return string.replace("\n", "")

layout = [
[Text(("\n"*12) + (" "*144) + "Aguarde...")]
]
tela = Window("Aguarde...", layout, no_titlebar=True, finalize=True, disable_close=True)
tela.maximize()
telax = tela.size[0]
tela.close()


def tp(value, base=248): #transpose space position
    totalSpaces = int(telax/4.19)
    output = int((value/base) * totalSpaces)
    return output


##Telas##
def chapas():
    with open("source.txt", "r") as arq:
        lines = arq.readlines()
    layout = [
    [Text("\n")],
    [Text(" "*tp(90)), Text("Configurações", font="Arial 30")],
    [Text("\n"*12)],
    [Text(" "*tp(102)), Button("Andamento da votação")],
    [Text("")],
    [Text(" "*tp(105)), Button("Finalizar a votação")],
    [Text("")],
    [Text(" "*tp(105)), Button("Configurar chapas")],
    [Text("")],
    [Text(" "*tp(107)), Button("Voltar ao menu")],
    [Text("\n"*9)],
    [Text(" "*tp(90)), Text("Desenvolvido pelo curso de informática")]
    ]
    
    tela = Window("Andamento da votação", layout, no_titlebar=True, finalize=True, disable_close=True)
    tela.maximize()
    
    run = 1
    while run:
        eventos = tela.read()
        for event in eventos:
            if event == "Voltar ao menu":
                run = 0
            elif event == "Andamento da votação":
                popup("".join(lines))
            elif event == "Finalizar a votação":
                popup("".join(lines))
                return 0
            
    tela.close()
    return 1
    
        
def config():
    with open("source.txt", "r") as arq:
        lines = arq.readlines()
    layout = [
    [Text("\n")],
    [Text(" "*tp(90)), Text("Configurações", font="Arial 30")],
    [Text("\n"*12)],
    [Text(" "*tp(102)), Button("Andamento da votação")],
    [Text("")],
    [Text(" "*tp(105)), Button("Finalizar a votação")],
    [Text("")],
    [Text(" "*tp(105)), Button("Configurar chapas")],
    [Text("")],
    [Text(" "*tp(107)), Button("Voltar ao menu")],
    [Text("\n"*9)],
    [Text(" "*tp(90)), Text("Desenvolvido pelo curso de informática")]
    ]
    
    tela = Window("Andamento da votação", layout, no_titlebar=True, finalize=True, disable_close=True)
    tela.maximize()
    
    run = 1
    while run:
        eventos = tela.read()
        for event in eventos:
            if event == "Voltar ao menu":
                run = 0
            elif event == "Andamento da votação":
                popup("".join(lines))
            elif event == "Finalizar a votação":
                popup("".join(lines))
                return 0
            
    tela.close()
    return 1

def voto():
    c = [0, 0]
    layout = [
    [Text("\n")],
    [Text(" "*tp(102)), Text("Votação", font="Arial 30")],
    [Text("\n"*11)],
    [Text(" "*tp(82)), Text("\n\nSelecione sua chapa e aperte em 'Confirmar' abaixo")],
    [Text(" "*tp(65)), Radio("FD - Força Democrática", "chapa", default=False,  key="a"), Text(" "*2), Radio("PUMA - Para Um Melhor Aprendizado", "chapa", default=False, key="b")],
    [Text("\n"*4)],
    [Text(" "*tp(110)), Button("Confirmar")],
    [Text("\n"*9)],
    [Text(" "*tp(90)), Text("Desenvolvido pelo curso de informática")]
    ]

        
    tela = Window("Tela de votação", layout, no_titlebar=True, finalize=True, disable_close=True)
    tela.maximize()

    run = 1
    while run:
        eventos = tela.read()
        for event in eventos:
            if event == "Confirmar":
                for i in eventos:
                    if isinstance(i, dict):
                        if i["a"]:
                            c[0] = 1
                            run = 0
                        elif i["b"]:
                            c[1] = 1
                            run = 0
    tela.hide()
    tela.close()
    return c 

       
def main():
    cA = 0
    cB = 0
    layout = [
    [Text("\n")],
    [Text(" "*tp(50)), Text("SysGrêmio - TEC.INFORMÁTICA", font="Arial 30")],
    [Text("\n"*12)],
    [Text(" "*tp(72)), Text("Senha:"), Input(key="senha", password_char="*")],
    [Text("\n"*5)],
    [Text(" "*tp(72)),Button("Verificar Senha"), Text(" "*49), Button("Votação")],
    [Text("\n"*11)],
    [Text(" "*tp(95)), Text("Desenvolvido pelo curso de informática")]
    ]
    
    tela = Window("Tela de controle", layout, no_titlebar=True, finalize=True, disable_close=True)
    tela.maximize()

    run = 1
    while run:
        eventos = tela.read()
        for event in eventos:
            if event == WIN_CLOSED or event == "Exit":
                run = 0
            elif event == "Verificar Senha":
                for i in eventos:
                    if isinstance(i, dict):
                        if i["senha"] == senha:
                            layout[3][2].update("") #input
                            run = config()
                        elif i["senha"] == "":
                            popup("Digite algo")
                        else:
                            popup("Senha incorreta")
                        break
            elif event == "Votação":
                layout[3][2].update("") #input
                v = voto()
                cA += v[0]
                cB += v[1]
                with open("source.txt", "w") as arq:
                    arq.write("FD - Força Democrática: " + str(cA) + " voto" + ("" if cA == 1 else "s") + "\nPUMA - Para Um Melhor Aprendizado: " + str(cB) + " voto" + ("" if cB == 1 else "s"))
        tela.BringToFront()
    tela.close()       

main()
#config()

