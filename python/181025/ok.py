import customtkinter as ctk

##------------- Funções 

def calcular_media():
    try:
        n1 = float(entry_nota1.get())
        n2 = float(entry_nota2.get())
        n3 = float(entry_nota3.get())
        media = (n1 + n2 + n3) / 3
        if media >= 7:
            resultado.configure(text=f'Você passou! Sua média é: {media:.1f}')
        else:
            resultado.configure(text=f'Você não passou. Sua média é: {media:.1f}')
    except ValueError:
        resultado.configure(text='Por favor, digite números válidos nas notas.')

##------------- Criar Janela 

janela = ctk.CTk()
janela.geometry('650x450')
janela.title('Sistema Escolar')
janela.configure(fg_color='blue')

##--------- Corpo da janela 

title = ctk.CTkLabel(
    janela, 
    text='Sistema Escolar para calcular nota',
    text_color='black',
    font=('Calibri', 20)
)
title.pack(pady=30)

entry_nota1 = ctk.CTkEntry(
    janela,
    height=30,
    width=400,
    placeholder_text='Digite a primeira nota',
    fg_color='white',
    text_color='black'
)
entry_nota1.pack(pady=5)

entry_nota2 = ctk.CTkEntry(
    janela,
    height=30,
    width=400,
    placeholder_text='Digite a segunda nota',
    fg_color='white',
    text_color='black'
)
entry_nota2.pack(pady=5)

entry_nota3 = ctk.CTkEntry(
    janela,
    height=30,
    width=400,
    placeholder_text='Digite a terceira nota',
    fg_color='white',
    text_color='black'
)
entry_nota3.pack(pady=5)

btn_calcular = ctk.CTkButton(
    janela,
    text='Calcular Média',
    command=calcular_media
)
btn_calcular.pack(pady=20)

resultado = ctk.CTkLabel(
    janela,
    text='',
    text_color='black',
    font=('Calibri', 16)
)
resultado.pack(pady=20)

##------- Inicio 

janela.mainloop()
