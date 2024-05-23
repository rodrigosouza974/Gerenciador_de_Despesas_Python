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

#despesas diárias, como descrição da despesa e valor gasto.

# função input
nome_despesa = input("qual o nome da despesa:")

despesa_descricao = input("qual descrição deseja adicionar para essa despesa:")

valor_despesa = input("qual o valor da despesa:")

# função print
print(f"olá {nome}")