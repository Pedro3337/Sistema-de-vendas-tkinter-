import tkinter as tk
from tkinter import messagebox
import json
import os

CAMINHO_PRODUTOS = 'produtos.json'
CAMINHO_CARRINHO = 'carrinho.json'

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistem de vendas")
        self.master.geometry('300x400')

        self.produtos = self.carregar_produtos()
        self.carrinho = self.carregar_carrinho()

        self.tela_principal()

    def carregar_produtos(self):
        if (os.path.exists(CAMINHO_PRODUTOS)):
            try:
                with open(CAMINHO_PRODUTOS, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}
    
    def salvar_produtos(self, dados):
        with open(CAMINHO_PRODUTOS, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    
    def carregar_carrinho(self):
        if (os.path.exists(CAMINHO_CARRINHO)):
            try:
                with open(CAMINHO_CARRINHO, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def salvar_carrinho(self, dados):
        with open(CAMINHO_CARRINHO, 'w',encoding='utf-8') as f:
            json.dump(dados, f,indent=4,ensure_ascii=False)
    
    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def tela_principal(self):
        self.limpar_tela()

        box_titulo = tk.Frame(self.master, bg='red', bd=2, relief='solid')
        box_titulo.pack(fill='both')

        box_venda = tk.Frame(self.master, bd=2, relief='solid')
        box_venda.pack(expand=True,fill='both')

        tk.Label(box_titulo, text="Sistema de vendas", font=('Arial', 20), bg='red', fg='white').pack(pady=20)

        self.btn_cadastrar = tk.Button(box_venda, text='Cadastrar produto', font=('Arial',16), command=self.tela_cadastro)
        self.btn_cadastrar.pack(pady=10)

        self.btn_carrinho = tk.Button(box_venda, text='Adicionar ao carrinho', font=('Arial',16),command=self.tela_adicionar_carrinho)
        self.btn_carrinho.pack(pady=10)

        self.btn_ver_carrinho = tk.Button(box_venda, text='Ver carrinho', font=('Arial', 16), command=self.tela_ver_carrinho)
        self.btn_ver_carrinho.pack(pady=10)

        self.btn_finalizar_venda = tk.Button(box_venda, text='Finalizar venda', font=('Arial', 16), command=self.finalizar_venda)
        self.btn_finalizar_venda.pack(pady=10)

    def tela_cadastro(self):
        self.limpar_tela()

        box_titulo_cadastro = tk.Frame(self.master,bg='red', bd=2, relief='solid')
        box_titulo_cadastro.pack(fill='both')

        box_cadastro = tk.Frame(self.master, bd=2, relief='solid')
        box_cadastro.pack(expand=True, fill='both')

        tk.Button(box_titulo_cadastro, text='<-', command=self.tela_principal).pack(side='left')

        tk.Label(box_titulo_cadastro, text='Cadastro do produto',font=('Arial', 20),fg='white', bg='red').pack(pady=20)

        tk.Label(box_cadastro, text='Código do produto', font=('Arial', 16)).pack(pady=10)
        self.entry_codigo = tk.Entry(box_cadastro,font=('Arial', 16))
        self.entry_codigo.pack()

        tk.Label(box_cadastro, text='Nome do produto', font=('Arial', 16)).pack(pady=10)
        self.entry_nome = tk.Entry(box_cadastro, font=('Arial', 16))
        self.entry_nome.pack()

        tk.Label(box_cadastro, text='Preço do produto', font=('Arial', 16)).pack(pady=10)
        self.entry_preco = tk.Entry(box_cadastro, font=('Arial', 16))
        self.entry_preco.pack()

        tk.Button(box_cadastro, text='Cadastrar produto', font=('Arial', 16), command=self.cadastrar).pack(pady=20)

    def tela_adicionar_carrinho(self):
        self.limpar_tela()

        box_titulo_carrinho = tk.Frame(self.master, bd=2, bg='red', relief='solid')
        box_titulo_carrinho.pack(fill='both')

        tk.Button(box_titulo_carrinho, text='<-', command=self.tela_principal).pack(side='left')

        box_adicinar_carrinho = tk.Frame(self.master, bd=2, relief='solid')
        box_adicinar_carrinho.pack(expand=True, fill='both')

        tk.Label(box_titulo_carrinho, text='Adicionar ao carrinho',bg='red',fg='white', font=('Arial', 20)).pack(pady=10)

        tk.Label(box_adicinar_carrinho, text='Código do produto', font=('Arial', 16)).pack(pady=10)

        self.entry_codigo_produto = tk.Entry(box_adicinar_carrinho, font=('Arial', 16))
        self.entry_codigo_produto.pack()

        tk.Button(box_adicinar_carrinho, text='Adicionar', font=('Arial', 16), command=self.adicionar_carrinho).pack(pady=10)

    def tela_ver_carrinho(self):
        self.limpar_tela()

        box_titiulo_ver_carrinho = tk.Frame(self.master, bd=2 , relief='solid', bg='red')
        box_titiulo_ver_carrinho.pack(fill='both')

        tk.Button(box_titiulo_ver_carrinho, text='<-', command=self.tela_principal).pack(side='left')

        box_carrinho = tk.Frame(self.master, bd=2, relief='solid')
        box_carrinho.pack(expand=True,fill='both')

        tk.Label(box_titiulo_ver_carrinho, text='Carrinho', font=('Arial', 20, 'bold'),fg='white',bg='red').pack(pady=20)

        def limpar_tela_carrinho():
            for widget in box_carrinho.winfo_children():
                widget.destroy()

        total = 0

        limpar_tela_carrinho()

        for i,produto in enumerate(self.carrinho):
            total += produto['preco']

            box_produto = tk.Frame(box_carrinho, bd=2, relief='solid',bg='grey')
            box_produto.pack(pady=5,fill='both')

            tk.Label(box_produto, text=f"Produto: {produto['nome']} \n preço: R$ {produto['preco']:.2f}", fg='white',font=('Arial', 14),bg='grey').pack(side='left',pady=10)
            btn_excluir = tk.Button(box_produto, bd=2, relief='solid',text='Remover', command=lambda i=i: remover_produto(i))
            btn_excluir.pack(side='right', padx=10)

        def remover_produto(index):
            self.carrinho.pop(index)
            self.salvar_carrinho(self.carrinho)
            self.tela_ver_carrinho()

        tk.Label(self.master, text=f'Preço total: R${total:.2f}', font=('Arial', 14, 'bold')).pack(side='bottom')

    def finalizar_venda(self):
        if not self.produtos or not self.carrinho:
            messagebox.showerror("Erro","Nenhum produto para finalizar a venda!")
            return
            
        total = sum(produto['preco'] for produto in self.carrinho)
        menssagem = "\n".join([f"Produto: {produto['nome']} - Preço: R${produto['preco']:.2f}" for produto in self.carrinho])
        menssagem += f"\n\n Total: R${total:.2f}"
        messagebox.showinfo("Venda finalizada! ",menssagem)
        self.carrinho = []
        self.salvar_carrinho(self.carrinho)

    def cadastrar(self):
        codigo = self.entry_codigo.get()
        nome = self.entry_nome.get()

        try:
            preco = float(self.entry_preco.get())

            for n in self.produtos:
                if (n == codigo):
                    messagebox.showinfo('Aviso1',"Produto ja existente!")
                    return

            if (codigo and nome):
                self.produtos[codigo] = {'nome': nome, 'preco': preco}
                messagebox.showinfo("Sucesso","Produto cadastrado com sucesso!")
                self.salvar_produtos(self.produtos)
                print(self.produtos)
                self.entry_codigo.delete(0, tk.END)
                self.entry_nome.delete(0, tk.END)
                self.entry_preco.delete(0, tk.END)
            else:
                messagebox.showerror("Erro","Preencha os campos!")
        except ValueError:
            messagebox.showerror("Erro", "Analise os dados!")

    def adicionar_carrinho(self):
        try:
            codigo = self.entry_codigo_produto.get().strip()

            if not(codigo):
                messagebox.showerror("Erro","Preencha o campo")
                return
            
            if not(codigo in self.produtos):
                messagebox.showerror("Erro","Produto não existe!")
                return

            for item in self.carrinho:
                if (item.get('nome') in self.produtos[codigo]['nome']):
                    messagebox.showwarning("Aviso!","Poduto ja adicionado no carrinho!")
                    return  
                    
            if (codigo in self.produtos):
                self.carrinho.append(self.produtos[codigo])
                messagebox.showinfo("Sucesso!", f"Produto adicionado com sucesso!")
                self.salvar_carrinho(self.carrinho)
                self.entry_codigo_produto.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Erro",f"Erro: {e}")

root = tk.Tk()
app = App(root)
root.mainloop()