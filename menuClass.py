import os, time

def clear():
    # Esta funcion Limpia la pantalla en tiempo de ejecucion
    os.system("cls")

def tiempo(t):
    # Esta funcion parara el tiempo de ejcucion por t segundos
    time.sleep(t)

def imprimirMenu():
    clear()
    print("-------------------------------------------------\n",
        "{: ^50}\n".format('╔══╗            ',),
        "{: ^50}\n".format('╚╗╔╬╦╦╦═╦═╗     ',),
        "{: ^50}\n".format('─║║╔╣║║═╣╬║     ',),
        "{: ^50}\n".format('─╚╩╝╚═╩═╩═╝     ',),
        "{: ^50}\n".format('╔═╦═╗────╔╗     ',),
        "{: ^50}\n".format('║║║║╠═╗╔═╬╬═╦═╗ ',),
        "{: ^50}\n".format('║║║║║╬╚╣╬║║═╣╬║ ',),
        "{: ^50}\n".format('╚╩═╩╩══╬╗╠╩═╩═╝ ',),
        "{: ^50}\n".format('───────╚═╝      ',),
        "-------------------------------------------------\n",  
        "(1){: ^47}\n".format("Iniciar Partida"),
        "(2){: ^47}\n".format("Creditos"),
        "(3){: ^47}\n".format("Terminar"),
        "-------------------------------------------------\n",sep=""
    )

def terminar():
    clear()
    print(
        "-------------------------------------------------\n",
        "{: ^50}\n".format("              __                "),
        "{: ^50}\n".format("        _..-''--'----_.         "),
        "{: ^50}\n".format("      ,''.-''| .---/ _`-._      "),
        "{: ^50}\n".format("    ,' \ \  ;| | ,/ / `-._`-.   "),
        "{: ^50}\n".format("  ,' ,',\ \( | |// /,-._  / /   "),
        "{: ^50}\n".format("  ;.`. `,\ \`| |/ / |   )/ /    "),
        "{: ^50}\n".format(" / /`_`.\_\ \| /_.-.'-''/ /     "),
        "{: ^50}\n".format("/ /_|_:.`. \ |;'`..')  / /      "),
        "{: ^50}\n".format("`-._`-._`.`.;`.\  ,'  / /       "),
        "{: ^50}\n".format("    `-._`.`/    ,'-._/ /        "),
        "{: ^50}\n".format("      : `-/     \`-.._/         "),
        "{: ^50}\n".format("      |  :      ;._ (           "),
        "{: ^50}\n".format("      :  |      \  ` \          "),
        "{: ^50}\n".format("       \         \   |          "),
        "{: ^50}\n".format("        :        :   ;          "),
        "{: ^50}\n".format("        |           /           "),
        "{: ^50}\n".format("        ;         ,'            "),
        "{: ^50}\n".format("       /         /              "),
        "{: ^50}\n".format("      /         /               "),
        "{: ^50}\n".format("               / Adiós          "),
        "-------------------------------------------------\n", sep=''
    )
    tiempo(3)
    clear()

def opcionNoEncontrada():
    clear()
    print("-------------------------------------------------\n",
        "{: ^50}\n".format("Opcion no encontrada"),
        "-------------------------------------------------\n", sep='')
    tiempo(1)          

def creditos():
    clear()
    print("-------------------------------------------------",
        '───────────────────────────────────────',
        '───▐▀▄───────▄▀▌───▄▄▄▄▄▄▄─────────────',
        '───▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄──────────',
        '──▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄────────',
        '──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄──────',
        '▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────',
        '▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───▄▄',
        '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒█',
        '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀─',
        '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀───',
        '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌────',
        '─▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐─────',
        '─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────',
        '──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──────',
        '──▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌──────',
        '────▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀────────',
        "Programa desarrollador por", 
        "Fabian Dario Florez Raigoso",
        "-------------------------------------------------\n",
        sep='\n'
    )
    tiempo(2)

def bienvenida():
    clear()
    imprimirCorazon()
    tiempo(2)
    clear()

def imprimirCorazon():
    print(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░░░█░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░░█░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░██▄▄▄▄█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░▐░░░░░░░▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░▌░░░░░░░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░░░░░░░▄▄▀▀▀░▀▄▄▄░░░░░▄▄▄▄▄▄▄░░░░░░░░░',
        '░░░░░░░░░▌░░░░░░░░░█░░███████████░░░░░░░',
        '░░░░░░░░█▌░░░▒▒▒▒▒▒▒█████████████▌░░░░░░',
        '░░░░░░░▐░░░▒▒████████████████████▌░░░░░░',
        '░░░░░░░░█░▒▒█████████████████████░░░░░░░',
        '░░░░░░░░▐░▒▒████████████████████▌░░░░░░░',
        '░░░░░░░░░█▒█████████████████████░░░░░░░░',
        '░░░░░░░░░░█████████████████████░░░░░░░░░',
        '░░░░░░░░░░░███████████████████░░░░░░░░░░',
        '░░░░░░░░░░░░█████████████████░░░░░░░░░░░',
        '░░░░░░░░░░░░░███████████████░░░░░░░░░░░░',
        '░░░░░░░░░░░░░░▀███████████▀░░░░░░░░░░░░░',
        '░░░░░░░░░░░░░░░░█████████▀░░░░░░░█░░░░░░',
        '░░░░░░░░░░░░░░░░░██████▀░░░░░░░░█░█░░░░░',
        '░░░░░░░░░░░░░░░░░░░███░░░░░░░░░█░░░█░░░░',
        '░░░░░░░░░░░░░░░░░░░░▀░░░░░░░░░██▄▄▄▄█░░░',
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐░░░░░░░▌░░',
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌░░░░░░░▀░░',
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        sep='\n'
    )

def mensajeServidorNoEncontrado():
    print(
        "-------------------------------------------------\n",
        "{: ^50}\n".format("El servidor no se encuentra"),
        "{: ^50}\n".format("Intenta nuevamente"),
        "-------------------------------------------------\n",sep=""
    )
    tiempo(3)
    clear()

def mensajeServidorEncontrado():
    print(
        "-------------------------------------------------\n",
        "{: ^50}\n".format("El servidor se encontro"),
        "{: ^50}\n".format("Iniciando partida..."),
        "-------------------------------------------------\n",sep=""
    )
    tiempo(2)
    clear()

def mensajeCartaFueraRango():
    print(
        "-------------------------------------------------\n",
        "{: ^50}\n".format("La carta esta fuera del rango"),
        "{: ^50}\n".format("Escoje otra"),
        "-------------------------------------------------\n",sep=""
    )
    tiempo(1)
    clear()

def mensajeNumeroUsuario():
    print(
        "-------------------------------------------------\n",
        "{: ^50}\n".format("Escoje un numero entre 0 y 100"),
        "{: ^50}\n".format("Memoriza tu carta, y no la olvides"),
        "{: ^50}\n".format('Tu carta es secreta'),
        "-------------------------------------------------\n",sep=""
    )
    tiempo(3)
    clear()

def mostrarCartaUsuario(numero):
    mostrarMago(numero)
    print("{: ^50}\n".format("Ya lo pensé, y tu carta es"),
        "{: ^50}\n".format(numero),
        "-------------------------------------------------\n",sep=""
    )
    tiempo(7)

def mostrarMago(numero):
    clear()
    print(
        "-------------------------------------------------\n",
        "{: ^50}\n".format("              _,._      "),
        "{: ^50}\n".format("  .||,        /_ _\ \   "),
        "{: ^50}\n".format(" \.`',/       |'L'| |   "),
        "{: ^50}\n".format(" = {: >3} =      | -,| L   ".format(numero)),
        "{: ^50}\n".format(" / || \    ,-'\ /,'`.   "),
        "{: ^50}\n".format("   ||     ,'   `,,. `.  "),
        "{: ^50}\n".format("   ,|____,' , ,;' \| |  "),
        "{: ^50}\n".format("  (3|\    _/|/'   _| |  "),
        "{: ^51}\n".format("   ||/,-''  | >-'' _,\ \ "),
        "{: ^50}\n".format("   ||'      ==\ ,-'  ,' "),
        "{: ^50}\n".format("   ||       |  V \ ,|   "),
        "{: ^50}\n".format("   ||       |    |` |   "),
        "{: ^50}\n".format("   ||       |    |   \  "),
        "{: ^50}\n".format("   ||       |    \    \ "),
        "{: ^51}\n".format("   ||       |     |    \ "),
        "{: ^50}\n".format("   ||       |      \_,-'"),
        "{: ^51}\n".format('   ||       |___,,--")_\ '),
        "{: ^50}\n".format("   ||         |_|   ccc/"),
        "{: ^50}\n".format("   ||        ccc/       "),
        "{: ^50}\n".format("   ||                   "),
        "-------------------------------------------------\n", sep=''
    )

















