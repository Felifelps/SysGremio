from tkinter import *
from base import *

class GUI:
    def __init__(self):
        self.root = Tk()
        self.main_menu()
    #------------------------------------------------------------------------------------------------------------------------------
    def popup(self, Text):
        screen = Toplevel()
        screen.title(Text)
        screen.resizable(0, 0)
        Label(screen, text=Text, font="Times 15", width=20).pack()
        Button(screen, text="Ok", padx=15, pady=5, command=lambda: screen.destroy()).pack()
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    def confirm_screen(self, Text):
        screen = Toplevel()
        screen.title(Text)
        screen.resizable(0, 0)
        #Returning option
        def option(option):
            screen.destroy()
            return option
        Label(screen, text=Text, font="Times 15", width=20).grid(row=0, columnspan=2)
        Button(screen, text="Sim", padx=15, pady=5, command=lambda: option(True)).grid(row=1, column=0)
        Button(screen, text="Não", padx=15, pady=5, command=lambda: option(False)).grid(row=1, column=1)
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    def voting_screen(self):
        self.popup("Wait for voting screen")
    #------------------------------------------------------------------------------------------------------------------------------
    def election_result_screen(self):
        self.popup("Wait for result screen")
    #------------------------------------------------------------------------------------------------------------------------------
    def voting_menu(self):
        self.election = election()

        screen = Toplevel()
        screen.title("VotingPage")
        screen.geometry("%dx%d+0+0" % (screen.winfo_screenwidth(), screen.winfo_screenheight()))
        screen.overrideredirect(True)

        #Checking password
        def check_password(Password, mode):
            if Password == "":
                if mode == "v": #vote
                    self.voting_screen()
                elif mode == "f": #finish 
                    if self.confirm_screen("Finalizar votação?"):
                        self.election_result_screen()
                    
            else:
                self.popup("Senha inválida")

        #Elements
        title = Label(
            screen,
            text="Votação",
            font="Times 35 bold",
            width=100,
            height=6,
            anchor=N,
            pady=20
        )

        password = Entry(
            screen,
            show="*"
        )
        
        vote = Button(
            screen,
            text="Votar",
            font="Times 12",
            padx=20,
            command=lambda: check_password(password.get(), "v")
        )

        finish_election = Button(
            screen,
            text="Finalizar votação",
            font="Times 12",
            padx=20,
            command=lambda: check_password(password.get(), "f")
        )
        
        #Layout
        title.pack()
        Label(screen, text="Digite a senha para finalizar a votação:", font="Times 12").pack()
        password.pack()
        password.focus()
        Label(screen, text="").pack()
        vote.pack()
        Label(screen, text="").pack()
        finish_election.pack()
        Label(screen, text="Desenvolvido pelo curso de informática.", font="Times 12", height=16, pady=5, anchor=S).pack()

        #Mainloop
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    def settings_page(self):
        self.popup("Wait for Settings")
    #------------------------------------------------------------------------------------------------------------------------------
    def main_menu(self):
        self.root.title("MainMenu")
        self.root.geometry("%dx%d+0+0" % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.overrideredirect(True)

        #Elements
        title = Label(
            self.root,
            text="SysGremio",
            font="Times 35 bold",
            width=100,
            height=6,
            anchor=N,
            pady=20
        )
        
        start_election = Button(
            self.root,
            text="Iniciar votação",
            font="Times 12",
            padx=20,
            command=lambda: self.voting_menu()
        )

        change_partys = Button(
            self.root,
            text="Alterar chapas",
            font="Times 12",
            padx=20,
            command=lambda: print("inda não")
        )
        
        exit = Button(
            self.root,
            text="Sair",
            font="Times 12",
            padx=20,
            command=lambda: self.root.destroy()

        )
        credit = Label(
            self.root,
            text="Desenvolvido pelo curso de informática.",
            font="Times 12",
            height=16,
            pady=5,
            anchor=S
        )

        #Layout
        title.pack()
        start_election.pack()
        Label(self.root, text="").pack()
        change_partys.pack()
        Label(self.root, text="").pack()
        exit.pack()
        Label(self.root, text="Desenvolvido pelo curso de informática.", font="Times 12", height=16, pady=5, anchor=S).pack()

        #Mainloop
        self.root.mainloop()


app = GUI()


        
