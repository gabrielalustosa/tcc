import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

class AutoFinanceCtx:
    def __init__(self):
        self._entrada_senha:str
        self._entrada_usuario:str
        self._users = {
            "gabriela": "senha123",
        }
        
    def interface(self):
        janela = ctk.CTk()
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        janela.geometry("500x300")
        janela.title("AutoFinance")
        ctk.CTkLabel(janela, text="Faça seu login").pack(padx=10, pady=10)
        ctk.CTkLabel(janela, text="Usuário:").pack()
        self._entrada_usuario = ctk.CTkEntry(janela)
        self._entrada_usuario.pack()

        ctk.CTkLabel(janela, text="Senha:").pack()
        self._entrada_senha = ctk.CTkEntry(janela, show="*")
        self._entrada_senha.pack()

        ctk.CTkButton(janela, text="Entrar", command=self.verificar_login).pack(pady=10)
        
        image_path = "caminho/para/sua/imagem.png"  # substitua pelo caminho real
        pil_image = Image.open(image_path)

        # Cria um CTkImage
        ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(200, 200))

        # Exibe a imagem em um CTkLabel
        image_label = ctk.CTkLabel(app, image=ctk_image, text="")  # text="" para não mostrar texto junto
        image_label.pack(pady=20)

        janela.mainloop()

    def verificar_login(self):
        usuario = self._entrada_usuario.get()
        senha = self._entrada_senha.get()

        if usuario in self._users and self._users[usuario] == senha:
            messagebox.showinfo("Login", "Acesso permitido!")
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")
            
teste = AutoFinanceCtx()
teste.interface()
teste.verificar_login()