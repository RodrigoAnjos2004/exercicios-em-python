salario = float(input('Salário do colaborador: '))

print ('------------------------------')
print ('*     organizações:          *')
print ('*                            *')
print ('*       A                    *')
print ('*           B                *')
print ('*               C            *')
print ('------------------------------')

if (salario <= 980) :
        percentual = 20
elif (salario >= 981) and (salario <= 1700) :
        percentual = 15
elif (salario >= 1701) and (salario <= 2500):
        percentual = 10
else:percentual = 5

print('Salario inicial: R$ ', salario)
print('Percentual: ',percentual,'%')

percentual = percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento
    
print('Aumento: R$ ',aumento)
print('Novo salário: R$ ', novo_salario)


