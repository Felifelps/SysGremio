from tkinter import *
import sys, os
sys.path.append(os.getcwd().replace("View", "Model"))
from base import *

class GUI:
    def __init__(self):
        self.root = Tk()
        self.election = election()
        self.main_page()

    def popup(self, Text):
        screen = Toplevel()
        screen.title(Text)
        screen.resizable(0, 0)
        Label(screen, text=Text, font="Times 15", width=20).pack()
        Button(screen, text="Ok", padx=15, pady=5, command=lambda: screen.destroy()).pack()
        screen.mainloop()

    def vote_page(self):
        screen = Toplevel()
        screen.geometry("%dx%d+0+0" % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        screen.overrideredirect(True)

        partys = Listbox(screen,
                         selectmode="single",
                         height=len(self.election.partys)
                         )

        for party in self.election.partys:
            partys.insert(self.election.partys.index(party), party.name)
        partys.pack()


        screen.mainloop()

    def settings_page(self):
        self.popup("Settings")
    
    def main_page(self):
        self.root.title("Tela de Controle")
        self.root.geometry("%dx%d+0+0" % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.overrideredirect(True)

        #Check password
        def check_password(Password, button="v"):
            if Password == "infortop":
                if button == "v":
                    self.vote_page()
                elif button == "s":
                    self.settings_page()
            else:
                self.popup("Senha inválida!")
                

        #Elements
        title = Label(self.root,
                      text="SysGremio",
                      font="Times 35 bold",
                      width=100,
                      pady=20
                      )
        
        password = Entry(self.root,
                         width=50,
                         show="*"
                         )

        settings = Button(self.root,
                          text="Configurações",
                          font="Times 12",
                          padx=20,
                          command=lambda: check_password(password.get(), "s")
                          )

        vote = Button(self.root,
                      text="Votação",
                      font="Times 12",
                      padx=20,
                      command=lambda: check_password(password.get(), "v")
                      )
        
        credit = Label(self.root,
                       text="Desenvolvido pelo curso de informática.",
                       font="Times 12",
                       height=16,
                       pady=5,
                       anchor=S
                       )


        #Layout
        title.pack()
        Label(self.root, text="Digite a senha: ", font="Times 15", height=12, anchor=S).pack()
        password.pack()
        password.focus()
        Label(self.root, text="\n", height=2).pack()
        settings.pack()
        Label(self.root, text="").pack()
        vote.pack()
        credit.pack()
        


        #Mainloop
        self.root.mainloop()


app = GUI()


        
