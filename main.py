# coding utf-8
import math

# def rsa_encrypt():


def codificacion_numerica(alf):
    codificacion_numerica = dict()
    i = 0
    for char in alf:
        codificacion_numerica.setdefault(char, i)
        i += 1

    return codificacion_numerica

def base2(decimal):
    return bin(decimal).replace("0b","") 

def rsa_decrypt(k, numero_simbolos, mensaje_cifrado, alf, info_receptor):
    mensaje_claro = ''
    codificacion = codificacion_numerica(alf)
    # PASO 1: Dividir el mensaje cifrado en bloques de k+1
    bloques = []
    bloque = []
    for char in mensaje_cifrado:
        bloque.append(char)
        if len(bloque) == k + 1:
            bloques.append(bloque)
            bloque = []

    bloques_numericos = []
    # PASO 2: Obtencion de los bloques numericos
    for bloque in bloques:
        cod_numerica = []
        for char in bloque:
            cod_numerica.append(codificacion[char])
        bloques_numericos.append(cod_numerica)

    # --------------------------------------------------------------------------------[OK]

    enteros_cifrados = []
    position = k
    for bloque in bloques_numericos:
        m = 0
        for num in bloque:
            m = m + (num * pow(numero_simbolos, position, info_receptor['n']))
            position = position - 1
        
        enteros_cifrados.append(m)

    #PASO 3: Calcular la clave privada del receptor => d = e ^ -1
    fi_n = (info_receptor['factorizacion'][0] - 1) % info_receptor['n'] * (info_receptor['factorizacion'][1] - 1) % info_receptor['n'];
    d = pow(info_receptor['e'], -1, fi_n)

    print("c =", enteros_cifrados)
    print("d =", d)
    print("n =", info_receptor['n'])

    #--------------------------------------------------------------------------------------------[OK]

    #PASO 4: Sacar los enteros en claro
    enteros_claros = []
    for entero in enteros_cifrados:
        print(pow(entero, int(d)))
        # potencia = pow(entero, int(d))
        # print(potencia)
        # enteros_claros.append(pow(entero, int(d)) % info_receptor['n'])
    
    # print(enteros_claros)

    #------------------------------------------------------------------------------------------------[OK]
    # cocientes = []
    # restos = []
    # cociente = int(enteros_claros[0] / numero_simbolos)
    # resto = int(enteros_claros[0] % numero_simbolos)
    # while cociente > numero_simbolos and resto > numero_simbolos :
    #     cocientes.append(cociente)
    #     restos.append(resto)
    #     print("Cociente: ", cociente)
    #     print("Resto: ",resto)
    #     cociente = int(enteros_claros[0] / numero_simbolos)
    #     resto = int(enteros_claros[0] % numero_simbolos)
    bloque_claro = []
    # bloque_claro.append(cocientes[0])
    # bloque_claro.append(restos[0])

        
    
    print(bloque_claro)

    # for number in bloque_claro:
    #     mensaje_claro += alf[number]
    # print(46306954071 % 10057)
    #Se hace la tabla
        # la fila de a esta formada por los cuadrados de c
        # la fila b determina las etapas 
        # m es el resultado de c * m  en el caso de que b[-1] sea 1
    
    # b = d[::-1]

    # etapas = [] # etapas == b
    # for item in b:
    #     etapas.append(int(item))
    

    #     a = []
    #     aux = entero
    #     a.append(entero)
    #     for i in range(1, len(etapas)):
    #         a.append(pow())


    # enteros_cifrados = []
    # for num in enteros:
    #     c = pow(num, info_receptor['e'],info_receptor['n'])
    #     enteros_cifrados.append(c)

    # # Descifrar el entero c
    # enteros_claros = []
    # #Paso 1: Calcular la clave privada del receptor 
    
    # print("Clave privada del receptor: ", d) 

    # #Paso 2: Hallar los enteros en claro c ^ d mod n

    

    # print(c)


    
    
    # #Obtener a
    # for entero in enteros_cifrados:
    #     a = []
    #     numero = entero
    #     for i in range(0, len(etapas)):
    #         print(numero)
    #         a.append(numero)
    #         numero = pow(numero, 2, info_receptor['n'])
        
    #     print(a)
    #     m = []
    #     m.append(1)
    #     operando1 = a[0]
    #     operando2 = 1

    #     for j in range(1, len(etapas)):
    #         if etapas[j - 1] == 1:
    #             m.append((operando1 * operando2) % info_receptor['n'])
    #             operando1 = a[j]
    #             operando2 = operando1 * operando2 % info_receptor['n']
    #         else: 
    #             m.append("")

    #     entero_claro_final = 0
    #     for k in range(0, len(etapas)):
    #         if m[k] != '':
    #             entero_claro_final = m[k]
    #         enteros_claros.append(entero_claro_final)
            
    #     print("Etapa   |        a               |           b              |           m          ")
    #     print("-----------------------------------------------------------------------------------")
    #     for x in range(0, len(etapas) - 1):
    #         print(str(x) + "  "+ str(a[x]) +"     "+ str(etapas[x]) +"                         "  + str(m[x]) +" ")
        
    #     for claro in enteros_claros:
    #         aux = claro
    #         cociente = aux / numero_simbolos
    #         resto = aux % numero_simbolos
    #         print("Entero en claro: ", claro)
    #         print("Cociente: " , cociente)
    #         print("resto: " , resto)

    # break

    #     # break

            
    return mensaje_claro.replace('  ', "\n")


if __name__ == '__main__':
    alf = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNNÑOPQRSTUVWXYZáéíóúAÁÉÍÓU0123456789 ,.:!-¿?()'
    # alf = "ABCDEFGHIJKLMNNOPQRSTUVWXYZ"
    mensaje_cifrado = 'wVBñú94wAU9gaÓc66:YCúVIwAlk)U9ULBMQ)-7caóNS8nvB08h 8úÍtÑJ)¿sYqLBÁ4duCsfkóx)aKE9(3:Hf(¿NmoGñ!DABBÑ6eÑrGUPábCñtdawqbíVWPbéecJÑM)LAc¿2ywRrñrth,896u6on?7b5J81v(LFTÉóN?sNB!ñr,:b877da4ñ4??8hdG '

    # mensaje_cifrado = "EYA"
    # Pepa envia el mensaje a Benito
    # pepa_n = 62439738695706104201747
    # pepa_e = 356812573
    # pepa_factorizacion = 249879448303 * 249879448349

    info_emisor = {
        'n': 62439738695706104201747,
        'e': 356812573,
        'factorizacion': [249879448303 , 249879448349]
    }

    # benito_n = 743330222539755158153
    # benito_e = 80263681
    # benito_factorizacion = 27264083009 * 27264083017

    # info_receptor = {
    #     'n': 10057,
    #     'e': 6571,
    #     'factorizacion': [89 , 113]
    # }

    info_receptor = {
        'n': 743330222539755158153,
        'e': 80263681,
        'factorizacion': [27264083009 , 27264083017]
    }

    numero_simbolos = len(alf)
    print("Número de símbolos: ", numero_simbolos)

    k = int(math.log(info_receptor['n'], numero_simbolos))
    print("Tamaño del bloque: ", k)

    mensaje_claro = rsa_decrypt(k, numero_simbolos, mensaje_cifrado, alf, info_receptor)

    print(mensaje_claro)
