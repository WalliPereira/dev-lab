import sqlite3 

conn = sqlite3.connect("BancoDeDados.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS itens(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL
)
''')
conn.commit()

def adicionar_itens():
    nome = input("Nome:")
    quantidade = int(input("Quantidade:"))
    cursor.execute('INSERT INTO itens (nome, quantidade) VALUES (?, ?)', (nome, quantidade))
    conn.commit()
    print("- Item adicionado!\n")

def listar_itens():
    cursor.execute('SELECT * FROM itens')
    itens = cursor.fetchall()
    if itens:
        print("\n - Lista de Itens:")
        for item in itens:
            print(f"ID: {item[0]} | Nome: {item[1]} | Quantidade: {item[2]}")
    else:
        print("\nNenhum item cadastrado na loja.")
print()

def atualizar_itens():
    listar_itens()
    item_id = input("Digite o ID do Item que deseja atualizar: ")
    novo_item = input("Digite o novo Item: ")
    cursor.execute('UPDATE Itens SET quantidade = ? WHERE id = ?', (novo_item, item_id))
    conn.commit()
    print("- Item atuzalizado.")

def excluir_item():
    listar_itens()
    item_id = input("Digite o ID do item que deseja excluir da loja: ")
    cursor.execute('DELETE FROM itens WHERE id = ?', (item_id,))
    conn.commit()
    print("- Item excluido!\n")

while True:
    print(" --- Itens para o Mercado ---")
    print("1 - Adicionar item a lista")
    print("2 - Listar itens da lista")
    print("3 - Atualizar item da lista")
    print("4 - Excluir item da lista")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_itens()
    elif opcao == "2":
        listar_itens()
    elif opcao == "3":
        atualizar_itens()
    elif opcao == "4":
        excluir_item()
    elif opcao == "0":
        print(" Encerrando o programa. . .")
        break
    else:
        print(" Opcao invalida, tente novamente.\n")
conn.close()