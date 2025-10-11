import customtkinter as ctk

ctk.set_appearance_mode('dark')

janela = ctk.CTk("#26199c")
janela . geometry('600x450')
janela.title("SENAI")
janela.iconbitmap('C:/Users/aluno.den/Downloads/aula dia 04 10 25/tela senai/book.ico')

#--------corpo da janela--------

ctk.CTkLabel(janela,
             text='Sistema de Acesso - Senai',
             text_color='white',
             font=('Times new roman',40)).pack(pady=30)



login = ctk.CTkEntry(janela,
                     width=400,
                     height=20,
                     placeholder_text= 'Digite o seu login',
                     border_color='black',
                     fg_color='white',
                     border_width=2,
                     text_color= 'black'
                     )
login.pack()
password = ctk.CTkEntry(janela,
                     width=400,
                     height=20,
                     placeholder_text= 'Digite sua senha putinha',
                     border_color='black',
                     fg_color='white',
                     border_width=2,
                     text_color= 'black',
                     show='•'
                     )


password.pack(pady=0.5)

botao= ctk.CTkButton(janela,
                     text='acessar',
                     width=200,
                     height=40,
                     fg_color='white',
                     text_color='#26199c',
                     font=('arial',30))
botao.pack(pady=20)





janela.mainloop()
