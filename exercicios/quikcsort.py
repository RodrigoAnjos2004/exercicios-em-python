n = int(input('Digite a quantidade de palavras: '))
valores = list()
for R in range(1, n + 1):
    x = str(input(f'Digite o {R}ª palavra: '))
    valores.append(x)
valores.sort()
print()
#quick list started
def quicksort(list):   # 1. Seleção do pivô. # 2. Particionamento do arranjo.
    if not list:
        return []
    return (quicksort([x for x in list[1:] if x <  list[0]])
            + [list[0]] +
            quicksort([x for x in list[1:] if x >= list[0]]))

#O algoritmo quicksort é um método de ordenação muito rápido e eficiente
print(quicksort(valores))
#QuickSort
#No QuickSort, escolhemos um elemento arbitrário (que chamamos de pivô), e particionamos o arranjo de entrada de modo que todos os 
# elementos menores que o pivô apareçam antes dele no arranjo e os elementos maiores que ele apareçam depois dele no arranjo. Assim, 
# o Quicksort pode ser dividida em três etapas:
#Seleção do pivô.
#Particionamento (reorganização) dos elementos do arranjo em torno do pivô.
#Ordenação recursiva das partes obtidas no passo anterior.
#Os passos acima podem ser traduzidos para código da seguinte forma: