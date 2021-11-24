tamanho = int(input('Tamanho em metros quadrados: '))

litros = tamanho / 3

if tamanho % 54 == 0:
    latas = tamanho / 5
    
    
else: 

    latas = int(tamanho / 54) + 1

preco = latas * 560
print ('%d latas' %latas)
print ('R$ %.2f' %preco)
print ('%d litros ' %litros)
