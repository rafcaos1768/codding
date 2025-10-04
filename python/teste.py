import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode('dark')

janela = ctk.CTk("#26199c")
janela.geometry('600x450')
janela.title("SENAI")
janela.iconbitmap('C:/Users/aluno.den/Downloads/aula dia 04 10 25/read_book_study_icon-icons.com_51077.ico')


# Carrega a imagem de fundo (coloque o caminho correto da sua imagem)
imagem_fundo = Image.open("C:/Users/aluno.den/Downloads/depositphotos_3477954-stock-photo-abstract-blue-background-wave-veil.jpg")
imagem_fundo = imagem_fundo.resize((600, 450))  # Ajusta o tamanho da imagem à janela
imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

# Label que vai conter a imagem de fundo
label_fundo = ctk.CTkLabel(janela, image=imagem_fundo_tk)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Criar o label vazio inicialmente
titulo = ctk.CTkLabel(janela,
                      text='',
                      text_color='white',
                      font=('Times new roman', 40))
titulo.pack(pady=30)

texto_completo = 'Sistema de Acesso - Senai'

def escrever_titulo(texto, index=0):
    if index <= len(texto):
        titulo.configure(text=texto[:index])  # Atualiza o texto mostrando até o index atual
        index += 1
        # Chama essa mesma função após 100ms
        janela.after(100, escrever_titulo, texto, index)

# Começa a animação do título
escrever_titulo(texto_completo)

login = ctk.CTkEntry(janela,
                     width=400,
                     height=20,
                     placeholder_text='Digite o seu login',
                     border_color='black',
                     fg_color='white',
                     border_width=2,
                     text_color='black')
login.pack()

password = ctk.CTkEntry(janela,
                        width=400,
                        height=20,
                        placeholder_text='Digite sua senha putinha',
                        border_color='black',
                        fg_color='white',
                        border_width=2,
                        text_color='black',
                        show='•')
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
