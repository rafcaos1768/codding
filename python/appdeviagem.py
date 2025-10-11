##app de consumo de viagem : digitar a distanica da viagem, digitar o consumo do veículo, igite o preço do combustivel e calcular 
##Total de litros = Distância total da viagem (km) ÷ Consumo médio (km/l)
##Custo total = Total de litros × Preço do combustível por litro 
##400 km ÷ 10 km/l = 40 litros
##400 km ÷ 10 km/l = 40 litros

import customtkinter as ctk
ctk.set_appearance_mode("dark")

def calcular_Consumo():
    print

janela = ctk.CTk()
janela.title('app de consumo de viagem')
janela.geometry('600x450')

##elementos da janela 
ctk.CTkLabel(janela, 
             text = 'Vamos economizar!\nDigite os valores para calcular',
             text_color= 'white',
             font= ('calibri', 45)
             ).pack()

distancia = ctk.CTkEntry(janela,
                         width= 500,
                         height= 10,
                         border_width=2,
                         placeholder_text= 'Digite a distancia da viagem',
                         fg_color= 'white',
                         text_color= 'black')

distancia.pack()

consumo = ctk.CTkEntry(janela,
                         width= 500,
                         height= 10,
                         border_width=2,
                         placeholder_text= 'Digite o consumo em km/l',
                         fg_color= 'white',
                         text_color= 'black')

consumo.pack(pady=0.5)

preco = ctk.CTkEntry(janela,
                         width= 500,
                         height= 10,
                         border_width=2,
                         placeholder_text= 'Digite o preço do combustível',
                         fg_color= 'white',
                         text_color= 'black')

preco.pack(pady=0.5)

botao= ctk.CTkButton(janela,
                     text='calcular',
                     width=200,
                     height=40,
                     fg_color='white',
                     text_color="#000000",
                     font=('arial',30),
                     command= calcular_Consumo)
botao.pack(pady=10)

resultado = ctk.CTkLabel(janela,
                         text='',
                         text_color = 'white',
                         font =('verdana', 10),)

resultado.pack(pady=0.5)

##chamada da janela 
janela.mainloop()