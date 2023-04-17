import sqlite3
from tkinter import *
from tkinter import ttk

# Criação do banco de dados
conn = sqlite3.connect('estoque.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS produtos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              nome TEXT NOT NULL,
              lote TEXT NOT NULL,
              quantidade INTEGER NOT NULL,
              vencimento TEXT NOT NULL,
              data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)''')

conn.commit()
conn.close()

# Inserção de produto
def inserir_produto():
    conn = sqlite3.connect('estoque.db')
    c = conn.cursor()
    nome = nome_entry.get()
    lote = lote_entry.get()
    quantidade = quantidade_entry.get()
    vencimento = vencimento_entry.get()
    c.execute("INSERT INTO produtos (nome, lote, quantidade, vencimento) VALUES (?, ?, ?, ?)",
              (nome, lote, quantidade, vencimento))
    conn.commit()
    conn.close()
    nome_entry.delete(0, END)
    lote_entry.delete(0, END)
    quantidade_entry.delete(0, END)
    vencimento_entry.delete(0, END)

# # Listagem de produtos
# def listar_produtos():
#     conn = sqlite3.connect('estoque.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM produtos ORDER BY data DESC")
#     produtos = c.fetchall()
#     for produto in produtos:
#         print(produto)
#     conn.close()

# Listar produtos
def listar_produtos():
    conn = sqlite3.connect('estoque.db')
    c = conn.cursor()
    c.execute("SELECT * FROM produtos")
    produtos = c.fetchall()
    tree.delete(*tree.get_children())
    for produto in produtos:
        tree.insert('', END, values=produto)
    conn.close()


# Busca de produto
def buscar_produto():
    conn = sqlite3.connect('estoque.db')
    c = conn.cursor()
    nome = nome_busca_entry.get()
    c.execute("SELECT * FROM produtos WHERE nome LIKE ?", ('%'+nome+'%',))
    produtos = c.fetchall()
    for produto in produtos:
        print(produto)
    conn.close()

# Edição de produto
def editar_produto():
    conn = sqlite3.connect('estoque.db')
    c = conn.cursor()
    id = id_entry.get()
    nome = nome_entry.get()
    lote = lote_entry.get()
    quantidade = quantidade_entry.get()
    vencimento = vencimento_entry.get()
    c.execute("UPDATE produtos SET nome = ?, lote = ?, quantidade = ?, vencimento = ? WHERE id = ?",
              (nome, lote, quantidade, vencimento, id))
    conn.commit()
    conn.close()
    id_entry.delete(0, END)
    nome_entry.delete(0, END)
    lote_entry.delete(0, END)
    quantidade_entry.delete(0, END)
    vencimento_entry.delete(0, END)

# Exclusão de produto
def excluir_produto():
    conn = sqlite3.connect('estoque.db')
    c = conn.cursor()
    id = id_entry.get()
    c.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    id_entry.delete(0, END)
    nome_entry.delete(0, END)
    lote_entry.delete(0, END)
    quantidade_entry.delete(0, END)
    vencimento_entry.delete(0, END)


#Agora, vamos criar a interface gráfica utilizando o Tkinter. Vamos criar um formulário para inserir, listar, buscar, editar e excluir produtos.

# Interface gráfica
root = Tk()
root.title('Controle de Estoque')
root.geometry('500x400')

# Labels
nome_label = Label(root, text='Nome:')
nome_label.grid(row=0, column=0, padx=10, pady=10)

lote_label = Label(root, text='Lote:')
lote_label.grid(row=1, column=0, padx=10, pady=10)

quantidade_label = Label(root, text='Quantidade:')
quantidade_label.grid(row=2, column=0, padx=10, pady=10)

vencimento_label = Label(root, text='Vencimento:')
vencimento_label.grid(row=3, column=0, padx=10, pady=10)

nome_busca_label = Label(root, text='Buscar por nome:')
nome_busca_label.grid(row=5, column=0, padx=10, pady=10)

id_label = Label(root, text='ID:')
id_label.grid(row=6, column=0, padx=10, pady=10)

# Entries
nome_entry = Entry(root, width=30)
nome_entry.grid(row=0, column=1, padx=10, pady=10)

lote_entry = Entry(root, width=30)
lote_entry.grid(row=1, column=1, padx=10, pady=10)

quantidade_entry = Entry(root, width=30)
quantidade_entry.grid(row=2, column=1, padx=10, pady=10)

vencimento_entry = Entry(root, width=30)
vencimento_entry.grid(row=3, column=1, padx=10, pady=10)

nome_busca_entry = Entry(root, width=30)
nome_busca_entry.grid(row=5, column=1, padx=10, pady=10)

id_entry = Entry(root, width=30)
id_entry.grid(row=6, column=1, padx=10, pady=10)

# Treeview
tree = ttk.Treeview(root, columns=('id', 'nome', 'lote', 'quantidade', 'vencimento'), show='headings')
tree.heading('id', text='ID')
tree.heading('nome', text='Nome')
tree.heading('lote', text='Lote')
tree.heading('quantidade', text='Quantidade')
tree.heading('vencimento', text='Vencimento')
tree.column('id', width=30)
tree.column('nome', width=150)
tree.column('lote', width=70)
tree.column('quantidade', width=70)
tree.column('vencimento', width=100)
tree.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

# Buttons
inserir_button = Button(root, text='Inserir', command=inserir_produto)
inserir_button.grid(row=4, column=0, padx=10, pady=10)

listar_button = Button(root, text='Listar', command=listar_produtos)
listar_button.grid(row=4, column=1, padx=10, pady=10)

buscar_button = Button(root, text='Buscar', command=buscar_produto)
buscar_button.grid(row=5, column=2, padx=10, pady=10)

editar_button = Button(root, text='Editar', command=editar_produto)
editar_button.grid(row=7, column=0, padx=10, pady=10)

excluir_button = Button(root, text='Excluir', command=excluir_produto)
excluir_button.grid(row=7, column=1, padx=10, pady=10)

# Main loop
root.mainloop()
