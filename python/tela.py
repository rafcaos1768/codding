import customtkinter as ctk

ctk.set_appearance_mode('dark')

janela = ctk.CTk("#63db63")
janela.geometry('600x450')
janela.title("Aplicativo de Saúde - 2025")
janela.iconbitmap("C:/Users/aluno.den/Downloads/aula dia 04 10 25/imc/muscle.ico")

def acessar():
    print("botão clicado")

ctk.CTkLabel(janela,
             text='Calculo do IMC',
             text_color='white',
             font=('Times new roman',40)).pack(pady=30)

altura = ctk.CTkEntry(janela,
                     width=400,
                     height=20,
                     placeholder_text= 'Digite a sua altura',
                     border_color='black',
                     fg_color='white',
                     border_width=2,
                     text_color= 'black'
                     )
altura.pack(pady=4)

peso = ctk.CTkEntry(janela,
                     width=400,
                     height= 20,    
                     placeholder_text= 'Digite o seu peso',
                     border_color= 'black',
                     fg_color='white',
                     border_width=2,
                     text_color= 'black'
                     )

peso.pack()

botao= ctk.CTkButton(janela,
                     text='calcular',
                     width=200,
                     height=40,
                     fg_color='black',
                     text_color="#f1f1f1",
                     font=('arial',30),
                     command= acessar())
botao.pack(pady=20)

janela.mainloop()
