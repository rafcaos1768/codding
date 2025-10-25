import customtkinter as ctk

##------------- Funções 

def calcular_media():
    n1 = float(nota1.get())
    n2 = float(n2.get())
    n3 = float(n3.get())
    media = (n1 + n2 + n3)/3

    if(media >= 7):
        resultado.configure(text = f'Você passou ! Sua média é : {media:.1f}')  
        
        
     
##------------- Criar Janela 

janela =ctk.CTk()
janela.geometry( '650 x 450')
janela.title('Sistema Escolar')
##Icon?
janela.configure(fg_color = 'blue')

##--------- Corpo da janela 


title = ctk.CTkLabel(
    janela, 
    text= 'Sistema Escolar para calcular nota ',
    text_color= 'black',
    font= ('calibri')
).pack(pady= 30)

nota1 = ctk.CTkEntry(
    janela,
    height= 20,
    width= 400,
    placeholder_text= 'Digite a primeira nota',
    fg_color= 'white',
    text_color= 'black'
).pack(pady= 30)


resultado = ctk.CTkLabel(
    ##janela,

)


##------- Inicio 

janela.mainloop()

