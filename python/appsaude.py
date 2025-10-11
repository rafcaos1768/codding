import customtkinter as ctk 
ctk.set_appearance_mode('dark') ##determinar o tema 

##criacai da funcao para o calculo
def calcular_imc():
    p = int(peso.get())
    a = float(altura.get())
    imc = p / (a*a)
    if imc < 18.5: 
        situacao = 'magreza'
    elif imc >= 18.5 and imc <25:
        situacao = 'peso ideal'
    elif imc >= 25 and imc < 30:
        situacao = 'sobrepeso'
    else:
        situacao = ' obesidade'

    resultado.configure(text= f'o seu imc é {imc:.1f}\nvocê está na stuacao de {situacao}', ) ##altera um paramentro no local chamado 
    

##--janela-- 
## 1º definir o tamanho da janela
## chamar a função da janela no final do código -- SEMPRE   
janela = ctk.CTk() ##essa variavel janela armazena a variavel toda
janela.title('saude') ##alterar o nome da janela 
janela.geometry('600x450')

#--elementos da janela--
ctk.CTkLabel(janela,
             text='APP saúde',
             text_color = 'white',
             font=('verdana', 45) 
             ).pack()

peso = ctk.CTkEntry(janela,
                     width=400,
                     height=20,
                     placeholder_text= 'Digite o seu peso',
                     border_color='black',
                     fg_color='white',
                     border_width=2,
                     text_color= 'black')

peso.pack()

altura = ctk.CTkEntry(janela,
                     width=400,
                     height=20,
                     placeholder_text= 'Digite seu altura',
                     border_color='black',
                     fg_color='white',
                     border_width=2,
                     text_color= 'black'
                     )

altura.pack(pady =0.5)  ##pady define a distania que atencede

botao= ctk.CTkButton(janela,
                     text='calcular',
                     width=200,
                     height=40,
                     fg_color='white',
                     text_color="#000000",
                     font=('arial',30),
                     command= calcular_imc)
botao.pack(pady=10)

resultado = ctk.CTkLabel(janela,
                         text='',
                         text_color = 'white',
                         font =('verdana', 10),
                         )

resultado.pack(pady=10)

##criar o componentes que farão parte da janela 

janela.mainloop()





