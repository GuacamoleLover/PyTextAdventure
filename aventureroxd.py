#Extremely simple text adventure
#by me :)
#Sorry coause it's in spanish, hope you get what the code is about

import sys

paginas = {
    0: {
        'mensaje': 'Te despierta un rayo de luz proveniendo de la entrada a la cueva.',
        'acciones': [('derecha', 1), ('izquierda', 2)],
    },
    1: {
        'estado': 'moriste',
        'mensaje': 'Oyes un sonido extremadamente alto y sientes algo caliente en tu cuello. Pisaste una mina.',
    },
    2: {
        'mensaje': 'Encuentras la salida, pero ves un oso cerca de la entrada.',
        'acciones': [('pelear', 3), ('hacerte el muerto', 4)],
    },
    3: {
        'mensaje': 'De alguna manera consigues asustar al oso y te deja en paz.',
        'acciones': [('irse', 5), ('quedarte donde estás', 6)],
    },
    4: {
        'mensaje': 'Te tiras al suelo y aguantas la respiración. El oso te ignora y se va.',
        'acciones': [('levantarse', 5), ('quedarte donde estás', 6)],
    },
    5: {
        'mensaje': 'Ves un barco, pero hay gente cerca. Tienen armas, pero encontraste un revolver detras de un arbol',
        'acciones': [('acercarse', 7), ('alejarse', 8)],
    },
    6: {
        'estado': 'moriste',
        'mensaje': 'moriste', 'Un meteorito cae sobre tu cabeza. No te dio tiempo a asustarte.',
    },
    7: {
        'estado': 'ganaste',
        'mensaje': 'Te acercas lentamente, y un meteorito cae unos diez metros de donde estas. Te levantas en la enfermería del barco.',
    },
    8: {
        'estado': 'moriste',
        'mensaje': 'moriste','Corres hacia la distancia y mueres de deshidratacion unos días después.',
    },
}


def salir():
    salir = None
    while salir is None:
        salir = input('salir (sí o no)?').lower()
        if salir not in ["sí", "no"]:
            print("Escribe un comando correcto.")
            salir = None
        if salir == "sí":
            sys.exit()
    return salir

respuesta = None

while respuesta is None:
    respuesta = input(f'salir ({paginaActual[1]} o {paginaActual[2]})?').lower()
    if respuesta != paginaActual[1] and respuesta != paginaActual[2]:
        print("Escribe un comando correcto.")
        respuesta = None
    if respuesta == paginaActual[1]:
        paginaActual = paginaActual[3]
    elif respuesta == paginaActual[2]:
        paginaActual = paginaActual[4]
    elif paginaActual[0] == ('moriste'):
        print('Fin...')
        print('====================')
        print('')
        print('Tristemente no encontraste un final feliz...')
        print('Pero prueba de nuevo!')
        print('salir = "s"')
        salir()
    elif paginaActual[0] == ('ganaste'):
        print('Fin!')
        print('====================')
        print('')
        print('Escapaste! Finalmente podrás reunirte con tu familia...')
        print('O lo que queda de ella... Parece ser que viajaste en el tiempo hacia el futuro')
        print('y tu único relativo vivo es tu nieta Antonieta. Mejor que nada!')
        salir()













