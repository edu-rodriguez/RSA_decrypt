#coding utf-8

def rsa_decrypt():
    mensaje_claro = ''

    return mensaje_claro


if __name__ == '__main__':
    alf = 'abcdefghijklmn˜nopqrstuvwxyzABCDEFGHIJKLMNNÑOPQRSTUVWXYZáéíóúAÁÉÍÓU0123456789 ,.:!-¿?()' 

    mensaje_cifrado = 'wVBñú94wAU9gaÓc66:YCúVIwAlk)U9ULBMQ)-7caóNS8nvB08h 8úÍtÑJ)¿sYqLBÁ4duCsfkóx)aKE9(3:Hf(¿NmoGñ!DABBÑ6eÑrGUPábCñtdawqbíVWPbéecJÑM)LAc¿2ywRrñrth,896u6on?7b5J81v(LFTÉóN?sNB!ñr,:b877da4ñ4??8hdG '

    # Pepa envia el mensaje a Benito
    pepa_n = 62439738695706104201747
    pepa_e = 356812573
    pepa_factorizacion = 249879448303 * 249879448349

    benito_n = 743330222539755158153
    benito_e = 80263681
    benito_factorizacion = 27264083009 * 27264083017

    mensaje_claro = rsa_decrypt()

    print(mensaje_claro)