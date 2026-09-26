import tkinter as tk
from tkinter import messagebox
import json

produtos = []

ARQUIVO = "produtos.json"


def salvarProdutos():
    with open(ARQUIVO, "w") as arquivo:
        json.dump(produtos, arquivo, indent=4)


def carregarProdutos():
    global produtos

    try:
        with open(ARQUIVO, "r") as arquivo:
            produtos = json.load(arquivo)

    except (FileNotFoundError, json.JSONDecodeError):
        produtos = []


def limparCampos():
    entrada_nome.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)


def cadastrarProduto():
    nome = entrada_nome.get()
    preco = entrada_preco.get()
    quantidade = entrada_quantidade.get()

    if nome == "" or preco == "" or quantidade == "":
        messagebox.showwarning(
            "Aviso",
            "Preencha todos os campos!"
        )
        return

    try:
        preco = float(preco)
        quantidade = int(quantidade)

    except:
        messagebox.showerror(
            "Erro",
            "Digite valores válidos para preço e quantidade!"
        )
        return

    if preco <= 0 or quantidade <= 0:
        messagebox.showwarning(
            "Aviso",
            "Preço e quantidade devem ser maiores que zero!"
        )
        return

    produto = [nome, preco, quantidade]

    produtos.append(produto)

    salvarProdutos()

    messagebox.showinfo(
        "Sucesso",
        "Produto cadastrado!"
    )

    limparCampos()


def abrirProdutos():
    janela_produtos = tk.Toplevel(janela)

    janela_produtos.title("Produtos Cadastrados")
    janela_produtos.geometry("600x450")

    titulo = tk.Label(
        janela_produtos,
        text="Produtos Cadastrados",
        font=("Arial", 18)
    )
    titulo.pack(pady=20)

    if len(produtos) == 0:

        mensagem = tk.Label(
            janela_produtos,
            text="Nenhum produto cadastrado."
        )
        mensagem.pack(pady=20)

    else:

        for produto in produtos:

            nome = produto[0]
            preco = produto[1]
            quantidade = produto[2]

            texto = f"{nome} - R$ {preco:.2f} - Quantidade: {quantidade}"

            produto_label = tk.Label(
                janela_produtos,
                text=texto,
                font=("Arial", 11)
            )
            produto_label.pack(pady=5)

    botao_voltar = tk.Button(
        janela_produtos,
        text="Voltar",
        command=janela_produtos.destroy
    )
    botao_voltar.pack(pady=20)


def pesquisarProduto():
    nome_pesquisa = entrada_nome.get()

    if nome_pesquisa == "":
        messagebox.showwarning(
            "Aviso",
            "Digite o nome do produto para pesquisar!"
        )
        return

    encontrados = []

    for produto in produtos:

        if produto[0].lower() == nome_pesquisa.lower():
            encontrados.append(produto)

    if len(encontrados) == 0:

        messagebox.showinfo(
            "Pesquisa",
            "Produto não encontrado."
        )

        return

    produto = encontrados[0]

    entrada_nome.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)

    entrada_nome.insert(0, produto[0])
    entrada_preco.insert(0, produto[1])
    entrada_quantidade.insert(0, produto[2])


def editarProduto():
    nome_atual = entrada_nome.get()
    novo_preco = entrada_preco.get()
    nova_quantidade = entrada_quantidade.get()

    if nome_atual == "" or novo_preco == "" or nova_quantidade == "":
        messagebox.showwarning(
            "Aviso",
            "Preencha todos os campos!"
        )
        return

    try:
        novo_preco = float(novo_preco)
        nova_quantidade = int(nova_quantidade)

    except:
        messagebox.showerror(
            "Erro",
            "Digite valores válidos para preço e quantidade!"
        )
        return

    if novo_preco <= 0 or nova_quantidade <= 0:
        messagebox.showwarning(
            "Aviso",
            "Preço e quantidade devem ser maiores que zero!"
        )
        return

    encontrado = False

    for produto in produtos:

        if produto[0].lower() == nome_atual.lower():

            produto[1] = novo_preco
            produto[2] = nova_quantidade

            encontrado = True

            break

    if encontrado:

        salvarProdutos()

        messagebox.showinfo(
            "Sucesso",
            "Produto atualizado!"
        )

        limparCampos()

    else:

        messagebox.showinfo(
            "Aviso",
            "Produto não encontrado."
        )


def excluirProduto():
    nome = entrada_nome.get()

    if nome == "":
        messagebox.showwarning(
            "Aviso",
            "Digite o nome do produto que deseja excluir!"
        )
        return

    for produto in produtos:

        if produto[0].lower() == nome.lower():

            confirmar = messagebox.askyesno(
                "Confirmar exclusão",
                "Deseja realmente excluir este produto?"
            )

            if confirmar:

                produtos.remove(produto)

                salvarProdutos()

                messagebox.showinfo(
                    "Sucesso",
                    "Produto excluído!"
                )

                limparCampos()

            return

    messagebox.showinfo(
        "Aviso",
        "Produto não encontrado."
    )


janela = tk.Tk()

carregarProdutos()

janela.title("Gerenciador de Estoque")
janela.geometry("500x550")


titulo = tk.Label(
    janela,
    text="Gerenciador de Estoque",
    font=("Arial", 20)
)
titulo.pack(pady=20)


label_nome = tk.Label(
    janela,
    text="Nome do produto:"
)
label_nome.pack()

entrada_nome = tk.Entry(
    janela,
    width=35
)
entrada_nome.pack(pady=5)


label_preco = tk.Label(
    janela,
    text="Preço:"
)
label_preco.pack()

entrada_preco = tk.Entry(
    janela,
    width=35
)
entrada_preco.pack(pady=5)


label_quantidade = tk.Label(
    janela,
    text="Quantidade:"
)
label_quantidade.pack()

entrada_quantidade = tk.Entry(
    janela,
    width=35
)
entrada_quantidade.pack(pady=5)


botao_cadastrar = tk.Button(
    janela,
    text="Cadastrar Produto",
    command=cadastrarProduto
)
botao_cadastrar.pack(pady=10)


botao_pesquisar = tk.Button(
    janela,
    text="Pesquisar Produto",
    command=pesquisarProduto
)
botao_pesquisar.pack(pady=5)


botao_editar = tk.Button(
    janela,
    text="Editar Produto",
    command=editarProduto
)
botao_editar.pack(pady=5)


botao_excluir = tk.Button(
    janela,
    text="Excluir Produto",
    command=excluirProduto
)
botao_excluir.pack(pady=5)


botao_limpar = tk.Button(
    janela,
    text="Limpar Campos",
    command=limparCampos
)
botao_limpar.pack(pady=5)


botao_produtos = tk.Button(
    janela,
    text="Ver Produtos",
    command=abrirProdutos
)
botao_produtos.pack(pady=10)


janela.mainloop()