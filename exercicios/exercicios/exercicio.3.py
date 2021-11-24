nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
freq = float(input('informe sua frequencia:'))


media = (nota1 + nota2) / 2
print('Sua media foi: ',(media))

print('Calculando')
if (media >= 70 ) and (freq >=75):
    print ("aluno foi Aprovado!")

elif (media < 50 ) and (freq < 75):
    print('aluno foi Reprovado!')

elif (media >= 50) and (media < 70) and (freq > 50 ) and (freq <75 ):
    print('aluno está de Recuperação!')
    




