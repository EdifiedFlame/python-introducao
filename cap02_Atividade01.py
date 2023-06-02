print('***************************************')
print('****** Adivinhe qual é o número  ******')
print('***************************************')


# Relembrar constantes e variávies
NUMERO_SECRETO = 83 #constante
tentativa = input('Tente acertar o número: ')
print('Você digitou: ', tentativa)

# é Preciso converte a string para int, de modo a haver comparação correta no if
tentativa_int = int(tentativa)

# Relembrando estrutura de decisão
# Aprveitamos para falar de identação (4 espaços ou tab)
# Identação é parte do código Python e faz total diferança em cógdigo
if (NUMERO_SECRETO == tentativa_int):
    print("Boa tentativa. ACERTOU!")
else:
    print('Não foi dessa vez. ERROU!')

#finalização do GAME
print('GAME OVER!')
print('Obrigado por participar!')


#   oiiiiiiiii