from tkinter import *
from tkinter import ttk
class tkinter_GUI:
    def __init__(self):
        pass
    #------------------------------------------------------------------------------------------------------------------------------
    def popup(self, Text):
        screen = Toplevel()
        screen.grab_set()
        screen.title(Text)
        screen.resizable(0, 0)
        Label(screen, text=Text, font="Times 15", height=len(Text.split("\n")) + 1, padx=10, pady=10).pack()
        Button(screen, text="Ok", padx=15, pady=5, command=lambda: screen.destroy()).pack()
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    def confirm_screen(self, Text:str, yes_function, no_function=lambda: print("NO")):
        screen = Toplevel()
        screen.grab_set()
        screen.title(Text)
        screen.resizable(0, 0)
        #Returning option
        def selected_option(option:int):
            screen.destroy()
            if option == 1:
                return yes_function()
            elif option == 0:
                return no_function()
        Label(screen, text=Text, font="Times 15", width=20).grid(row=0, columnspan=2)
        Button(screen, text="Sim", padx=15, pady=5, command=lambda: selected_option(1)).grid(row=1, column=0)
        Button(screen, text="Não", padx=15, pady=5, command=lambda: selected_option(0)).grid(row=1, column=1)
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    def text_input_screen(self, Title, Instruction, function, first_button_text="Confirmar"):
        screen = Toplevel()
        screen.grab_set()
        screen.title(Title)
        screen.resizable(0, 0)
        def exit(textinput):
            function(textinput)
            screen.destroy()
        Label(screen, text=Title, font="Times 15", width=20).grid(row=0, columnspan=2)
        Label(screen, text=Instruction, width=30, anchor=W).grid(row=1, columnspan=2)
        entry = Entry(screen, width=30)
        entry.focus()
        entry.grid(row=2, columnspan=2)
        Button(screen, text=first_button_text, padx=5, command=lambda: exit(entry.get())).grid(row=3, column=0)
        Button(screen, text="Cancelar", padx=5, command=lambda: screen.destroy()).grid(row=3, column=1)
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    def combobox_screen(self, Title, Instruction, Options, function, first_button_text="Escolher"):
        screen = Toplevel()
        screen.grab_set()
        screen.title(Title)
        screen.resizable(0, 0)
        def exit(option):
            function(option)
            screen.destroy()
        Label(screen, text=Title, font="Times 15", width=20).grid(row=0, columnspan=2)
        Label(screen, text=Instruction, width=30, anchor=W).grid(row=1, columnspan=2)
        Partys = ttk.Combobox(screen, state="readonly", values=Options)
        Partys.current(0)
        Partys.grid(row=2, columnspan=2)
        Button(screen, text=first_button_text, padx=5, command=lambda: exit(Partys.get())).grid(row=3, column=0)
        Button(screen, text="Cancelar", padx=5, command=lambda: screen.destroy()).grid(row=3, column=1)
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------


