from base import party, arq, election
import os

def clear_terminal() -> None:
    os.system("cls")

def check_is_digit(text: str) -> bool:
    return text.isdigit()

def menu(title: str, options: [str], middle: str=""):
    if options == []:
        Exception("No options provided")
    clear_terminal()
    print("===", title, "===" + (middle if middle == "" else "\n") + middle)
    index = 1
    for option in options:
        print(str(index) + "." + option)
        index += 1
    return input("Digite o número da opção: ")
    
password = "infortop"   

while 1:
    ans = menu("Bem-vindo", ["Iniciar votação", "Alterar chapas", "Sair"])
    if ans == "1":
        e = election()
        if len(e.ps.read(0)) == 0:
            clear_terminal()
            input("Não tem como votar sem chapas.\nAperte enter para voltar: ")
            continue
        vote = 1
        while vote:
            ans = menu("Controle", ["Votar", "Opções"])
            if ans == "1":
                while 1:
                    ans = menu("Votação", e.ps.read(0))
                    if check_is_digit(ans) and int(ans) <= len(e.partys):
                        e.vote(int(ans))
                        print(e.progress())
                        break
                    else:
                        clear_terminal()
                        input("Não tem essa opção.\nAperte enter para voltar: ")
            elif ans == "2":
                clear_terminal()
                s = input("Digite a senha: ")
                if s == password:
                    while 1:
                        ans = menu("Opções", ["Finalizar votação", "Voltar à votação"])
                        if ans == "1":
                            clear_terminal()
                            print("Votação finalizada.\n" + e.progress())
                            input("Aperte enter para voltar: ")
                            vote = 0
                            break
                        elif ans == "2":
                            break
                        else:
                            input("Não tem essa opção.\nAperte enter para voltar: ")
    
                else:
                    input("Senha incorreta.\nAperte enter para voltar: ")
            else:
                input("Não tem essa opção.\nAperte enter para voltar: ")

    elif ans == "2":
        partys = 1
        ps = arq(r"Data\partys")
        while partys:
            ans = menu("Chapas", ["Adicionar", "Excluir", "Voltar"], ps.content)
            if ans in "12":
                while 1:
                    if ans == "1":
                        clear_terminal()
                        print("=== Adicionando chapa ===")
                        name = input("Digite o nome da nova chapa: ")
                        yn = input("Adicionar {}? s/n ".format(name))
                        if yn in "sS":
                            ps.write(name + ("" if ps.read(0)[0] == "" else "\n"), "a")
                            input("Chapa adicionada!\nAperte enter para voltar: ")
                            break
                        else:
                            pass
                    elif ans == "2":
                        if len(ps.read(0)) == 0:
                            clear_terminal()
                            input("Não há chapas para excluir.\nAperte enter para voltar: ")
                            break
                        n = menu("Excluindo chapa", ps.read(0))
                        if check_is_digit(ans) and int(n) - 1 <= len(ps.read(0)):
                            yn = input("Excluir {}? s/n ".format(ps.read(0)[int(n) - 1]))
                            if yn in "sS":
                                rew = []
                                for p in ps.read(0):
                                    if p == ps.read(0)[int(n) - 1]:
                                        continue
                                    rew.append(p)
                                ps.write("".join(rew))
                                input("Chapa excluída!\nAperte enter para voltar: ")
                                break
                            else:
                                pass
                        else:
                            input("Não tem essa opção.\nAperte enter para voltar: ")
                        

            elif ans == "3":
                partys = 0
            else:
                input("Não tem essa opção.\nAperte enter para voltar: ")
        
    elif ans == "3":
        break
    else:
        input("Não tem essa opção.\nAperte enter para voltar: ")
                        
            
    
    
S