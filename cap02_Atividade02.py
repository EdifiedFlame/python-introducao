print('***************************************')
print('****** Adivinhe qual é o número  ******')
print('***************************************')


# Relembrar constantes e variávies
numero_secreto = 83 #constante
tentativa = input('Tente acertar o número: ')
print('Você digitou: ', tentativa)

# é Preciso converte a string para int, de modo a haver comparação correta no if
tentativa_int = int(tentativa)

# Relembrando estrutura de decisão
# Aprveitamos para falar de identação (4 espaços ou tab)
# Identação é parte do código Python e faz total diferança em cógdigo
if (numero_secreto == tentativa_int):
    print("Boa tentativa. ACERTOU!")
else:
    print('Não foi dessa vez. ERROU!')
    # inserindo novas condições. Lembrando que a identação definirá a inserção
    if (tentativa_int > numero_secreto):
        print('Sua tentativa foi MAIOR que o número secreto.')
    else:
        print('Sua tentativa foi MENOR que o número secreto.')
        #finalização do GAME
        print('GAME OVER!')
print('Obrigado por participar!')



# segundo o guia de estilo para Python, é sempre, que possível, necessário melhorar a legibilidade do código.
# Mudaremos i IF para uma  estrutura melhor

acerto = tentativa_int == numero_secreto
ehmaior = tentativa_int > numero_secreto
ehmenor = tentativa_int < numero_secreto

# Nova estrututa de IFs
if acerto:
    print('Boa tentativa. ACERTOU!!!!')
else:
    print('Não foi dessa vez. ERROU!!!!')
    if ehmaior:
        print('Sua tentativa foi MAIOR que o número secreto.')
    if ehmenor:
        print('Sua tentativa foi MENOR que o número secreto.')
    print('GAME OVER!')
print('Obrigado por participar')

# kkkkkkkk oi