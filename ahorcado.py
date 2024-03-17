import random
import time

lista = ["hola", "adios", "casa", "perro", "gato", "libro", "amarillo", "rojo", "azul", "verde", "manzana", "naranja", "platano", "pelota", "jugar", "correr", "caminar", "comer", "beber", "agua", "leche", "taza", "mesa", "silla", "ventana", "puerta", "coche", "avion", "bicicleta", "viajar", "montaña", "playa", "sol", "luna", "estrella", "cielo", "nube", "lluvia", "nieve", "frio", "calor", "fuego", "tierra", "aire", "flor", "arbol", "hoja", "raiz", "hombre", "mujer", "niño", "niña", "amigo", "amiga", "familia", "padre", "madre", "hermano", "hermana", "abuelo", "abuela", "tio", "tia", "primo", "prima", "bebe", "trabajo", "escuela", "maestro", "estudiante", "clase", "leccion", "examen", "pregunta", "respuesta", "problema", "solucion", "computadora", "telefono", "internet", "redes", "social", "musica", "cancion", "pelicula", "teatro", "arte", "pintura", "escultura", "danza", "deporte", "futbol", "baloncesto", "tenis", "nadar", "yoga", "meditar","pajaro", "celular", "mochila", "guitarra", "llave", "pelicula", "vela", "arcoiris", "reloj", "cafe", "radio", "carpeta", "pastel", "pluma", "jardin", "tenedor", "foto", "puente", "chocolate", "televisor", "cielo", "pintura", "piano", "dinosaurio", "avion", "patineta", "sueño", "regalo", "globo", "camisa", "piscina", "sopa", "camion", "gafas", "mapa", "zapato", "tren", "camara", "almohada", "espejo", "cereal", "lapiz", "pizza", "ciudad", "tienda", "cable", "botella", "solucion", "maleta", "habitacion", "relampago", "cajon", "te", "caracol", "maiz", "aventura", "tarjeta", "vuelo", "naranja", "pirata", "pijama", "revista", "dragon", "pan", "pintor", "juego", "cine", "boligrafo", "solitario", "alumno", "elefante", "flor", "ciencia", "fotografia", "amarillo", "rio", "diamante", "cuchillo", "estudiar", "caminar", "arco", "luz", "espacio", "fruta", "musico", "llama", "diente", "concierto", "isla", "volar", "telefono", "traje", "heroe", "salsa", "caballo", "oceano", "fantasma", "volcan", "desierto", "flecha", "sandia", "oso", "navegador", "helicoptero", "zoologico", "cometa", "caballero", "fogata", "teatro", "campeon", "papa", "carrera", "serpiente", "piramide", "tesoro", "limon", "palabra", "templo", "prisma", "trebol", "murcielago", "mapache", "temporada", "abogado", "volante", "juramento", "buho", "roca", "pantera", "capsula", "luna","caballito", "copa", "antiguo", "carnaval", "quimica", "sandalia","burro", "jirafa", "galaxia", "observatorio", "delfin", "francotirador", "rayo", "maravilla", "abeja", "acrobata", "aguacate", "alfiler", "almeja", "araña", "ardilla", "arroz", "astronauta", "atomo", "balon", "banana", "baston", "boton", "brocoli", "burbuja", "cacahuate", "cama", "camello", "camiseta", "caramelo", "cebra", "cerdo", "cereza", "champu", "chimpance", "churro", "clavel", "cobija", "coliflor", "conejo", "corbata", "cortina", "cubo", "cuervo", "cuña", "dalmata", "dedal", "dedo", "dinero", "doctor", "escalera", "espada", "espina", "faro", "foca", "folleto", "fresa", "gorila", "granja", "grillo", "grua", "jabon", "jardin", "kiwi", "koala", "leon", "loro", "lupa", "mancha", "mango", "medusa", "melon", "mono", "nariz", "ojo", "paleta", "papa", "pato", "payaso", "peluca", "pingüino", "platano", "rabano", "rosa", "sabana", "salsa", "sapo", "serpiente", "tigre", "tortuga", "uva", "vaca", "vapor", "yate", "zapato", "zorro", "aguila", "bailarina", "bufanda", "calabaza", "cochecito", "duende", "hamburguesa", "heladero", "laberinto", "murcielago", "navaja", "paraguas", "piña", "repollo", "trineo", "unicornio"]
estado = 0;
euclimedes = [
        '''
            +---+
            |   |
                |
                |
                |
                |
        ========''',
        '''
            +---+
            |   |
            O   |
                |
                |
                |
        ========''',
        '''
            +---+
            |   |
            O   |
            |   |
                |
                |
        ========''',
        '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
        ========''',
        '''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
        ========''',
        '''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
        ========''',
        '''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
        ========'''
    ]


palabra = random.choice(lista)
indexWord = len(palabra)

print(f'La palabra a encontrar tiene {len(palabra)} letras')
adivWord = [''] * indexWord
print(adivWord)

time.sleep(1)

#1er intento
print('Elija la letra que piense que esta:')
letra1 = input()
fallos = 0
fallosmax = 6
nounagrup = "".join(adivWord)
palasep = list(palabra)
while palasep != adivWord:
    if fallos == fallosmax:
        break
    elif letra1 in palabra:
        for i in range(indexWord):
            if letra1 == palabra[i]:
                adivWord[i] = letra1
        print('Le atinaste')
        print(adivWord)
        print(euclimedes[estado])
        print(f'Tienes {fallos} fallos')
        letra1 = input('Elija otra letra: ')
    else:
        print('Fallaste')
        fallos += 1
        estado += 1
        print(adivWord)
        print(euclimedes[estado])
        print(f'Tienes {fallos} fallos')
        letra1 = input('Elija otra letra: ')
time.sleep(1)

#revelword
if fallos == fallosmax:
    print(f'Fallaste la palabra era {palabra}')
if adivWord == palasep:
    print('GANASTE!!!!!')