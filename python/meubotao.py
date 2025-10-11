import tkinter as tk
from tkinter import Toplevel, Label

# Classe para criar a dica de ferramenta (Tooltip)
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        # Vincula eventos do mouse ao widget
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        # Cria a janela da dica (tooltip)
        x = self.widget.winfo_rootx() + self.widget.winfo_width()
        y = self.widget.winfo_rooty()
        self.tooltip = Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)  # Remove a borda e a barra de título
        self.tooltip.wm_geometry(f"+{x+5}+{y}")
        
        label = Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1,
                      font=("Arial", 10), justify="left")
        label.pack(padx=1, pady=1)

    def hide_tooltip(self, event=None):
        # Esconde a janela da dica
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

# Função principal para criar a interface
def criar_interface():
    janela = tk.Tk()
    janela.title("Exemplo de Dica")
    janela.geometry("300x100")

    # Frame para agrupar os widgets
    frame = tk.Frame(janela, padx=10, pady=10)
    frame.pack()

    # Rótulo "Peso:"
    label_peso = tk.Label(frame, text="Peso:")
    label_peso.pack(side=tk.LEFT)

    # Campo de entrada para o peso
    entry_peso = tk.Entry(frame)
    entry_peso.pack(side=tk.LEFT, padx=(5, 0))

    # Botão de dica
    botao_dica = tk.Label(frame, text="?", relief="raised", width=2, cursor="question_arrow")
    botao_dica.pack(side=tk.LEFT, padx=(5, 0))

    # Adiciona a funcionalidade de dica ao botão
    Tooltip(botao_dica, "Use quilogramas (kg) para o peso do produto.")

    janela.mainloop()

# Executa a função
if __name__ == "__main__":
    criar_interface()
