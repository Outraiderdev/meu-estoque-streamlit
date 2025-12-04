# Criamos o dicionário para guardar os itens: {nome: quantidade}
estoque = {}

while True:
    print("""
========= SISTEMA DE CONTROLE DE ESTOQUE SENAI - TAGUATINGA DF =========
1 - Adicionar um item
2 - Adicionar preço
3 - Remover um item
4 - Atualizar quantidades
5 - Listar estoque
6 - Sair
""")
    
    opcao = input("Escolha uma opção,por gentileza!: ")

    if opcao == "1":
        nome = input("Nome do item: ").lower()
        quantidade = int(input("Quantidade: "))
        if nome in estoque:
            estoque[nome]["quantidade"] += quantidade
        else:
            estoque[nome] = {"quantidade": quantidade, "preco": 0.0}
        print(f"✔ Item '{nome}' adicionado/atualizado com sucesso!\n")

    elif opcao == "2":
        nome = input("Nome do item para adicionar preço: ").lower()
        if nome in estoque:
            preco = float(input("Digite o preço do item (R$): "))
            estoque[nome]["preco"] = preco
            print(f"✔💵 Preço do item '{nome}' atualizado com sucesso!\n")
        else:
            print("❌ Item não encontrado.\n")

    elif opcao == "3":
        nome = input("Nome do item a remover: ").lower()
        if nome in estoque:
            del estoque[nome]
            print(f"✔ Item '{nome}' removido!\n")
        else:
            print("❌ Item não encontrado.\n")

    elif opcao == "4":
        nome = input("Nome do item: ").lower()
        if nome in estoque:
            nova_qtd = int(input("Nova quantidade: "))
            estoque[nome]["quantidade"] = nova_qtd
            print(f"✔ Quantidade de '{nome}' atualizada!\n")
        else:
            print("❌ Item não existe no estoque.\n")

    elif opcao == "5":
        print("\n🚩===== ESTOQUE ATUAL =====🚩")
        if len(estoque) == 0:
            print("Estoque vazio.")
        else:
            for item, dados in estoque.items():
                print(f"- {item}: {dados['quantidade']} unidades | R$ {dados['preco']:.2f}")
        print()

    elif opcao == "6":
        print("Saindo do sistema... Até mais!")
        break

    else:
        print("❌ Opção inválida! Tente novamente.\n")

from google.colab import files
files.download("app.py")


