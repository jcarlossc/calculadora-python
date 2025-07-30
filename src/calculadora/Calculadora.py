import tkinter as tk

class Calculadora:
    def __init__(self) -> None:
        self.janela = tk.Tk()
        self.janela.title("Calculadora Python")
        self.janela.config(bg="#3c3c3d")
        self.janela.geometry("300x400")
        self.janela.resizable(False,False)
        self.expressao_numerica = tk.StringVar()

    def criar_interface(self) -> None:
        def clicar(botao):
            atual = self.expressao_numerica.get()
            self.expressao_numerica.set(atual + botao)

        def calcular() -> None:
            try:
                resultado = eval(self.expressao_numerica.get())
                self.expressao_numerica.set(resultado)
            except:
                self.expressao_numerica.set("Erro")

        def limpar() -> None:
            self.expressao_numerica.set("")

        entrada = tk.Entry(self.janela, textvariable=self.expressao_numerica, font=("Arial", 20, "bold"), bd=2, relief="ridge", justify="right", bg="#626263")
        entrada.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.15)

        # Botões numéricos
        tecla9 = tk.Button(self.janela, text = ' 9 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('9'))
        tecla9.place(relx = 0.45, rely = 0.25, relheight = 0.15, relwidth = 0.15)

        tecla8 = tk.Button(self.janela, text = ' 8 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('8'))
        tecla8.place(relx = 0.25, rely = 0.25,relheight = 0.15, relwidth = 0.15)

        tecla7 = tk.Button(self.janela, text = ' 7 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('7'))
        tecla7.place(relx = 0.05, rely = 0.25, relheight = 0.15, relwidth = 0.15)

        tecla6 = tk.Button(self.janela, text = ' 6 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('6'))
        tecla6.place(relx = 0.45, rely = 0.45, relheight = 0.15, relwidth = 0.15)

        tecla5 = tk.Button(self.janela, text = ' 5 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('5'))
        tecla5.place(relx = 0.25, rely = 0.45, relheight = 0.15, relwidth = 0.15)

        tecla4 = tk.Button(self.janela, text = ' 4 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('4'))
        tecla4.place(relx = 0.05, rely = 0.45, relheight = 0.15, relwidth = 0.15)

        tecla3 = tk.Button(self.janela, text = ' 3 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('3'))
        tecla3.place(relx = 0.45, rely = 0.65, relheight = 0.15, relwidth = 0.15)

        tecla2 = tk.Button(self.janela, text = ' 2 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('2'))
        tecla2.place(relx = 0.25, rely = 0.65, relheight = 0.15, relwidth = 0.15)

        tecla1 = tk.Button(self.janela, text = ' 1 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('1'))
        tecla1.place(relx = 0.05, rely = 0.65, relheight = 0.15, relwidth = 0.15)

        tecla0 = tk.Button(self.janela, text = ' 0 ', fg = 'black', font=("Arial", 20, "bold"), bg = 'gainsboro', command = lambda: clicar('0'))
        tecla0.place(relx = 0.25, rely = 0.85, relheight = 0.1, relwidth = 0.15)

        tecla_ponto = tk.Button(self.janela, text = '.', fg = 'white', font=("Arial", 20, "bold"), bg = 'gray', command = lambda: clicar('.'))
        tecla_ponto.place(relx = 0.05, rely = 0.85, relheight = 0.1, relwidth = 0.15)

        # Tecla de limpar (C)
        tecla_limpar = tk.Button(self.janela, text=' C ', fg='white', font=("Arial", 20, "bold"), bg = 'orange', bd = 3, command = limpar)
        tecla_limpar.place(relx = 0.45, rely = 0.85, relheight = 0.1, relwidth = 0.15)

        # Operadores (+, -, *, /)
        tecla_soma = tk.Button(self.janela, text = ' + ', fg = 'white', font=("Arial", 20, "bold"), bg = 'gray', command = lambda: clicar("+"))
        tecla_soma.place(relx = 0.65, rely = 0.25, relheight = 0.15, relwidth = 0.15)

        tecla_sub = tk.Button(self.janela, text = '-', fg = 'white', font=("Arial", 20, "bold"), bg = 'gray', command = lambda: clicar("-"))
        tecla_sub.place(relx = 0.65, rely = 0.45, relheight = 0.15, relwidth = 0.15)

        tecla_div = tk.Button(self.janela, text = '/', fg = 'white', font=("Arial", 20, "bold"), bg = 'gray', command = lambda: clicar("/"))
        tecla_div.place(relx = 0.65, rely = 0.65, relheight = 0.15, relwidth = 0.15)

        tecla_mult = tk.Button(self.janela, text = '*', fg = 'white', font=("Arial", 20, "bold"), bg = 'gray', command = lambda: clicar("*"))
        tecla_mult.place(relx = 0.65, rely = 0.85, relheight = 0.1, relwidth = 0.15)

        # Resultado (=)
        tecla_igual = tk.Button(self.janela, text = ' = ', fg = 'white', font=("Arial", 20, "bold"), bg = 'gray', command = calcular)
        tecla_igual.place(relx = 0.86, rely = 0.25, relheight = 0.7, relwidth = 0.1)

        return self.janela.mainloop()
    
    def avaliar_expressao(self, expressao: str) -> str:
        try:
            resultado = eval(expressao)
            return str(resultado)
        except:
            return "Erro"
