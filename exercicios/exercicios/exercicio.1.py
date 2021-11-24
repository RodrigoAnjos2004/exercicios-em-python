import datetime

print("  _________ __                 __     ")
print(" /   _____//  |______    ____ |  | __ ")
print(" \_____  \\   __\__  \ _/ ___\|  |/ / ")
print(" /        \|  |  / __ \\  \___|    <  ")
print("/_______  /|__| (____  /\___  >__|_ \ ")
print("        \/           \/     \/     \/ ")
print("             loja de tenis            ")

compra = str(input("informe a daat de compra : (utitlize barrras) exemplo xx/xx/xx"))

datadecompra = datetime.datetime.strptime(compra, "%d/%m/%Y")

quant_dias = int(input("Quantos dias? "))

entrega = datadecompra + datetime.timedelta(quant_dias)

#Python tempo strftime () função recebe uma tupla tempo e retorna uma representação de string do horário local em um formato legível determinada pelo formato de parâmetro.
print ("Data incicial°:  \n",                datadecompra.strftime("%d/%m/%Y"))

print ("Quantidade de dias°: \n",                quant_dias)

print ("A data de entrega foi°: \n",                entrega.strftime("%d/%m/%Y"))
