import random

# COLORES
blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)
naranja = (255,125,0)
amarillo = (255,255,0)
verde = (0,255,0)
azul = (0,0,255)

# TAMAÑO DE PANTALLA
long_x = 600
long_y = 600
size = (long_x,long_y)

# SPRITES
fondos = ["F1.png", "F2.png", "F3.png", "F4.png"]
personajes = ["J1.png", "J2.png", "J3.png", "J4.png"]
objetos = ["O1.png", "O2.png", "O3.png", "O4.png"]
objects = ["MANZANAS", "COCOS", "METEORITOS", "BAYAS"]
i = random.randint(0,3)