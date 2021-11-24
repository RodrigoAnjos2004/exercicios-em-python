sexo  = str(input('informe seu sexo '))
altura = float(input('informe sua altura'))

if  sexo == "M":
 peso = (altura -100) * 0.90
 print('O seu peso ideal e: ', peso)

elif  sexo == "F":
 peso = (altura -100) * 0.85
 print('O seu peso ideal e: ', peso)
    

