'''
**Projeto: Gerenciador de Despesas**

Objetivo:
Desenvolver um programa em Python que ajude os usuários a registrar suas despesas diárias e a calcular o total de gastos.

Requisitos:

1. O programa deve solicitar ao usuário que insira informações sobre suas despesas diárias, como descrição da despesa e valor gasto.
2. Deve permitir ao usuário adicionar quantas despesas quiser.
3. Deve fornecer opções para o usuário visualizar todas as despesas registradas e o total de gastos.
4. O programa deve garantir que o usuário forneça entradas válidas, como números para os valores das despesas.
5. Deve permitir ao usuário encerrar o programa quando desejar.

Sugestões para implementação:

- Use listas ou dicionários para armazenar as informações sobre as despesas.
- Implemente funções para adicionar despesas, visualizar todas as despesas e calcular o total de gastos.
- Use estruturas de repetição para permitir que o usuário adicione múltiplas despesas.
- Utilize tratamento de erros para lidar com entradas inválidas do usuário.
- Forneça um menu de opções para facilitar a interação do usuário com o programa.

Isso deve fornecer um desafio interessante para você elaborar um projeto completo em Python, aplicando conceitos como entrada e saída de dados, estruturas de dados, funções e tratamento de erros. Se precisar de ajuda ou tiver alguma dúvida durante a implementação, estou aqui para ajudar!
'''
from datetime import datetime


def registrar_data_arquivo(func):
    def wrapper(*args, **kwargs):
        data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('data_execucao.txt', 'a') as arquivo:
            arquivo.write(f'{data_atual} - {func.__name__} chamada\n')
        return func(*args, **kwargs)
    return wrapper


class Despesa:
    def __init__(self, categoria, descricao, valor):
        self.categoria = categoria
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f"Data: {self.data}, Categoria: {self.categoria}, Descrição: {self.descricao}, Valor: {self.valor}"


class ListaDeDespesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesa(self, despesa):
        self.despesas.append(despesa)
        print(f'Despesa adicionada: {despesa}')

    @registrar_data_arquivo
    def alterar_despesa(self, indice, nova_categoria=None, nova_descricao=None, novo_valor=None):
        if 0 <= indice < len(self.despesas):
            despesa = self.despesas[indice]
            if nova_categoria:
                despesa.categoria = nova_categoria
            if nova_descricao:
                despesa.descricao = nova_descricao
            if novo_valor:
                despesa.valor = novo_valor
            print(f'Despesa alterada: {despesa}')
        else:
            print('Índice de despesa inválido.')
 
    @registrar_data_arquivo
    def excluir_despesa(self, indice):
        if 0 <= indice < len(self.despesas):
            despesa_removida = self.despesas.pop(indice)
            print(f'Despesa removida: {despesa_removida}')
        else:
            print('Índice de despesa inválido.')

    @registrar_data_arquivo
    def listar_despesas(self):
        for despesa in self.despesas:
            print(despesa)

    def __str__(self):
        return '\n'.join(str(despesa) for despesa in self.despesas)


def menu():
    print("""
==================================================
                Gestor de Despesas
==================================================

Bem-vindo à nossa aplicação! Aqui estão algumas
informações importantes:

    1. Adicionar despesa
    2. Alterar despesa
    3. Excluir despesa
    4. Visualizar despesas
    0. Sair

Por favor, escolha uma das opções acima para
continuar.

==================================================
""")


def Sistema_Gerenciamento():
    menu()
    lista_de_despesas = ListaDeDespesas()

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                categoria = input("Categoria da despesa: ")
                descricao = input("Descrição da despesa: ")
                valor = float(input("Valor da despesa: "))
                nova_despesa = Despesa(categoria, descricao, valor)
                lista_de_despesas.adicionar_despesa(nova_despesa)

            elif opcao == 2:
                indice = int(input("Índice da despesa a alterar: "))
                nova_categoria = input("Nova categoria (ou deixe em branco para manter): ")
                nova_descricao = input("Nova descrição (ou deixe em branco para manter): ")
                novo_valor = input("Novo valor (ou deixe em branco para manter): ")
                novo_valor = float(novo_valor) if novo_valor else None
                lista_de_despesas.alterar_despesa(indice, nova_data, nova_categoria, nova_descricao, novo_valor)

            elif opcao == 3:
                indice = int(input("Índice da despesa a excluir: "))
                lista_de_despesas.excluir_despesa(indice)

            elif opcao == 4:
                lista_de_despesas.listar_despesas()

            elif opcao == 0:
                break

        except ValueError:
            print("Por favor, insira um número válido.")
        print()
        # Exibir o menu novamente após cada operação para referência
        menu()


if __name__ == "__main__":
    Sistema_Gerenciamento()
