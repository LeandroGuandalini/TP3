#%%
#1
print([int(x)**2 for x in input('Digite uma lista de números separados por espaço: ').split()])
# %%
print([0 if int(x) < 10 else int(x) for x in input('Digite uma lista de números separados por espaço: ').split()])
# %%
print([len(frase.split()) for frase in input('Conte sua história com múltiplas frases (separadas por "."): ').split('. ')])
# %%
print([sum(1 for c in frase.lower() if c in "aeiou") for frase in ["Frase um exemplo", "Mais uma frase", "A terceira frase"]])
# %%
idades = {
  'Leandro': 24,
  'João': 30,
  'Roberto': 40,
  'Carla': 15,
  "Alice": 17
}

maiores_de_idade = {nome: idade for nome, idade in idades.items() if idade > 18}

print(maiores_de_idade)
# %%
def remover_palavras_indesejadas(frase, palavras_indesejadas):
  '''
  Remove palavras indesejadas de uma string.

  Parâmetros:
  frase (string): String com palavras separadas por espaço.
  palavras_indesejadas (string): Lista de palavras a serem removidas.

  Return:
  Nova string sem as palavras indesejadas
  '''

  palavras = frase.split()
  palavras_filtradas = [x for x in palavras if x not in palavras_indesejadas]
  return ' '.join(palavras_filtradas)

frase = "O gato correu rápido para pegar o rato"
indesejadas = ["gato", "rato"]

nova_frase = remover_palavras_indesejadas(frase, indesejadas)
print(nova_frase)
# %% 3
def alternar_maiuscula(lista):
  '''
  Alterna letras para maiúscula e minúscula.

  Parâmetros:
  Lista (string): uma lista de palavras

  Return:
  Nova string com letras alternadas
  '''
  resultado = []
  maiuscula = True

  for letra in lista:
    if letra.isalpha():
      if maiuscula:
        resultado.append(letra.upper())
      else: 
        resultado.append(letra.lower())
      maiuscula = not maiuscula
    else:
      resultado.append(letra)
  return ''.join(resultado)

entrada = 'Desenvolendo habilidades'
saida = alternar_maiuscula(entrada)
print(saida)
# %% 4
def separar_elementos_unicos(lista):
  '''
  Função que receba uma lista de listas e retorne uma nova lista apenas com os elementos únicos presentes nessas listas.

  Parâmetros:
  Lista: uma lista de números

  Return:
  Lista de elementos únicos.
  '''

  filtro = []

  for x in lista:
    if x in filtro:
      pass
    else:
      filtro.append(x)

  return filtro

lista = [4,5,6,5,6,4,3,2,1]
saida = separar_elementos_unicos(lista)
print(saida)

# %% 5
def intercalar_listas(lista1, lista2):
  '''
  Recebe duas listas de palavras e retorna uma string onde as palavras das duas listas foram intercaladas.
  Se uma lista for maior que a outra, a função deve adicionar os elementos restantes ao final da string resultante.

  Parâmetros:
  lista1: lista 1 de palavras
  lista2: lista 2 de palavras

  Return:
  A nova string com palavras intercaladas
  '''
  nova_lista = []
  
  for x, y in zip(lista1, lista2):
      nova_lista.append(x)
      nova_lista.append(y)
  
  nova_lista.extend(lista1[len(nova_lista)//2:])  
  nova_lista.extend(lista2[len(nova_lista)//2:])  

  
  return ' '.join(nova_lista)

lista1 = ['olá', 'tudo', 'bem', 'com', 'você']
lista2 = ['Eu', 'estou', 'bem']

nova_string = intercalar_listas(lista1, lista2)
print(nova_string)
# %% 6
def separar_listas_por_tamanho(lista1,indice):
  '''
  A função tem como objetivo receber duas listas, uma com palavras e um número inteiro, se separar a lista de palavras em duas listas, uma com palavras menores, ou iguais, que o índice e outra com palavras maiores

  Parâmetros:
  lista1: lista de palavras
  indice: um número inteiro

  Return:
  duas listas com palavras menores ou iguais, ou maiores que o índice
  '''
  lista_maior = []
  lista_menor_igual = []

  for palavra in lista1:
    if len(palavra) <= indice:
      lista_menor_igual.append(palavra.lower())
    else:
      lista_maior.append(palavra.lower())

  return lista_maior,lista_menor_igual

lista1 = ['olá', 'palavra', 'tamanho', 'teste', 'quadrado']
indice = 5

lista_maior, lista_menor_igual = separar_listas_por_tamanho(lista1, indice)

print(f'A lista de palavras com tamanho menor ou igual ao {indice} é: {lista_menor_igual}. A lista de palavras maior que o índice é: {lista_maior}')
# %% 7
def inserir_palavra(lista, nova_palavra):
  """
  Insere uma nova palavra em uma posição específica da lista.
  Se a lista tiver menos de três elementos, adiciona automaticamente no final.

  Parâmetros:
  - lista (list): Lista de palavras existente.
  - nova_palavra (str): Nova palavra a ser inserida.

  Retorna:
  - lista (list): Lista atualizada.
  """
  if len(lista) < 3:
      print("A lista tem menos de 3 elementos. A nova palavra será adicionada ao final.")
      lista.append(nova_palavra)
  else:
      try:
          posicao = int(input(f"A lista atual é: {lista}\nDigite a posição onde deseja inserir a palavra '{nova_palavra}': "))
          if 0 <= posicao <= len(lista):
              lista.insert(posicao, nova_palavra)
          else:
              print(f"Posição inválida! '{nova_palavra}' será adicionada ao final da lista.")
              lista.append(nova_palavra)
      except ValueError:
          print(f"Entrada inválida! '{nova_palavra}' será adicionada ao final da lista.")
          lista.append(nova_palavra)

  return lista

lista_inicial = ['Python', 'JavaScript','C', 'C#']
nova_palavra = 'Java'

lista_atualizada = inserir_palavra(lista_inicial, nova_palavra)
print(f"Lista atualizada: {lista_atualizada}")
# %% 8 
def combinar_listas(lista1, lista2):
  """
  Combina duas listas de números em uma única lista usando o método extend.

  Parâmetros:
  - lista1 (list): A primeira lista de números.
  - lista2 (list): A segunda lista de números.

  Retorna:
  - list: A lista combinada.
  """
  lista1.extend(lista2)
  return lista1

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista_combinada = combinar_listas(lista1, lista2)
print(f"Lista combinada: {lista_combinada}")
# %% 9
def remover_duplicatas(lista):
  """
  Remove palavras duplicadas de uma lista, mantendo apenas a primeira ocorrência.

  Parâmetros:
  - lista (list): Lista de palavras.

  Retorna:
  - list: Lista sem duplicatas.
  """
  nova_lista = []
  for x in lista:
    if x not in nova_lista:
      nova_lista.append(x)
  return nova_lista

lista_palavras = ['python', 'java', 'python', 'c++', 'java', 'javascript']
resultado = remover_duplicatas(lista_palavras)
print(f"Lista sem duplicatas: {resultado}")
# %%
def gerenciar_compras (lista):
  """
  Permite remover o último item da lista de compras, simulando o cancelamento da última compra.

  Parâmetros:
  - lista (list): Lista de itens de compras.

  Exibe:
  - A lista atualizada após a remoção.
  - Mensagem indicando que a lista está vazia, se for o caso.
  """
  if lista:
    item_removido = lista.pop()
    print(f"Item removido: {item_removido}")
    print(f"Lista atualizada: {lista_compras}")
  else:
    print("Não há mais itens para remover. A lista está vazia.")

lista_compras = ['maçã', 'banana', 'leite', 'pão']
gerenciar_compras(lista_compras)
gerenciar_compras(lista_compras)
gerenciar_compras(lista_compras)
gerenciar_compras(lista_compras)
gerenciar_compras(lista_compras)
# %% 11
def manipular_string(texto):
  """
  Realiza operações de manipulação em uma string:
  1. Exibe a string original.
  2. Solicita ao usuário um índice de início e um índice de fim.
  3. Exibe a substring correspondente aos índices fornecidos.

  Parâmetros:
  - texto (str): A string original a ser manipulada.
  """
  print(f'A string original é: {texto}')

  try:
    inicio = int(input("Digite o índice de início: "))
    fim = int(input("Digite o índice de fim: "))

    if 0 <= inicio <= fim <= len(texto):
        substring = texto[inicio:fim]
        print(f"Substring correspondente: {substring}")
    else:
        print("Os índices fornecidos são inválidos. Certifique-se de que 0 <= início <= fim <= tamanho da string.")
  except ValueError:
      print("Por favor, insira valores inteiros para os índices.")
  
manipular_string("Python é incrível!")

# %% 12
def gerenciar_lista_compras (lista_compras):
  """
  Gerencia uma lista de compras permitindo operações de adicionar, remover e encerrar.

  Parâmetros:
  - lista_compras (list): A lista inicial de compras.

  Operações permitidas:
  - Digitar "fim" para encerrar o programa.
  - Digitar "remover <produto>" ou "remover <índice>" para remover um item.
  - Digitar "adicionar <índice> <produto>" para adicionar um produto em uma posição específica.
  """
  print(f"Lista inicial: {lista_compras}")

  while True:
    comando = input("\nDigite um comando (adicionar, remover, fim): ").strip()

    if comando.lower() == "fim":
        print("\nEncerrando o programa...")
        break

    elif comando.lower().startswith("remover"):
        try:
            _, arg = comando.split(maxsplit=1)
            if arg.isdigit(): 
                indice = int(arg)
                if 0 <= indice < len(lista_compras):
                    item_removido = lista_compras.pop(indice)
                    print(f"\nItem '{item_removido}' removido com sucesso.")
                else:
                    print("\nÍndice fora do alcance da lista.")
            else:  
                if arg in lista_compras:
                    lista_compras.remove(arg)
                    print(f"\nItem '{arg}' removido com sucesso.")
                else:
                    print(f"\nItem '{arg}' não encontrado na lista.")
        except ValueError:
            print("\nComando inválido. Use 'remover <produto>' ou 'remover <índice>'.")

    elif comando.lower().startswith("adicionar"):
        try:
            _, indice, produto = comando.split(maxsplit=2)
            indice = int(indice)
            if 0 <= indice <= len(lista_compras):
                lista_compras.insert(indice, produto)
                print(f"\nItem '{produto}' adicionado na posição {indice}.")
            else:
                print("\nÍndice fora do alcance da lista.")
        except ValueError:
            print("\nComando inválido. Use 'adicionar <índice> <produto>'.")

    else:
        print("\nComando inválido. Tente 'adicionar', 'remover' ou 'fim'.")

    print(f"\nLista final: {lista_compras}")

lista_inicial = ["maçã", "banana", "leite", "arroz"]
gerenciar_lista_compras(lista_inicial)
    
# %%
