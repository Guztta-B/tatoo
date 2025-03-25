print('Bem-Vindo a area de cadastro')
totalpessoas = int(input('Quantas pessoas irão se hospedar?(max 3)'))
opcao1 = []
opcao2 = []
opcao3 = []
quantidade_hospedes = []
if totalpessoas == opcao1: 
   for numero in range(0,quantidade_hospedes):
    print(numero)
   print('Insira seus dados')
   nome = input('Insira seu nome: ')
   idade = input('Insira sua idade: ')
   print('Seja-Bem vindo', nome)
elif totalpessoas == opcao2: 
   print('Insira seus dados')
   nome = input('Insira seu nome e de seu acompanhante: ')
   idade = input('Insira suas idades: ')
   print('Sejam-Bem vindos', nome)
elif totalpessoas == opcao3: 
   print('Insira seus dados')
   nome = input('Insira seu nome e de seus acompanhantes: ')
   idade = input('Insira suas idades: ')
   print('Sejam-Bem vindos', nome)
print(f'''Opçoes de estadia:
Simples: R$ 100,00 por dia.
Duplo: R$ 150,00 por dia.
Luxo: R$ 250,00 por dia.
 ''')
simples = 'Simples'
Duplu = 'Duplo'
Luxo = 'Luxo'

tempo = int(input('Quantos dias ficarão hospedados? '))
estadia = input('Qual sera a opção do quarto? ')

if estadia == simples:
  print(f'O valor total será de R$ {100 * tempo}')
elif estadia == Duplu:
  print(f'O valor total será de R$ {150 * tempo}')
elif estadia == Luxo:
  print(f'O valor total será de R$ {250 * tempo}')
else: 
   print('Insira um dado valido!')

   
pagamento = input('Qual será o método de pagamento? (1/2/3): ')

if pagamento == '1': 
    print('Gerando QR code...')
elif pagamento == '2': 
    print('Insira os dados do seu cartão')
elif pagamento == '3': 
    print('Gerando boleto...')
else:
    print('Método de pagamento inválido.')

print('Pagamento concluído! Volte sempre!')