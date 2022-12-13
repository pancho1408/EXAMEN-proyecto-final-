import random
import pygame
from ajustes import *


# CLASE DEL JUGADOR:
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(personajes[i]).convert()
        self.image.set_colorkey(blanco)
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = 500


# CLASE DE LOS OBJETOS:
class Objeto(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(objetos[i]).convert()
        self.image.set_colorkey(blanco)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 3
        if self.rect.y > long_y:
            self.rect.y = - 10
            self.rect.x = random.randrange(long_x - 50)


# CLASE DEL JUEGO
class Game(object):
    def __init__(self):
        self.GameOver = False
        self.lista_sprites = pygame.sprite.Group()
        self.lista_objeto = pygame.sprite.Group()
        self.score = 0
        self.num = random.randint(5,15)
        for j in range(self.num):
            objeto = Objeto()
            objeto.rect.x = random.randint(50,(long_x - 50))
            objeto.rect.y = random.randint(0,long_y - 100)
            self.lista_objeto.add(objeto)
            self.lista_sprites.add(objeto)
        self.jugador = Jugador()
        self.lista_sprites.add(self.jugador)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.GameOver:
                    self.__init__()
        return False

    def logica(self):
        if not self.GameOver:
            self.lista_sprites.update()
            lista_obj_hit = pygame.sprite.spritecollide(self.jugador, self.lista_objeto, True)
            for obj in lista_obj_hit:
                self.score += 1
            if len(self.lista_objeto) == 0:
                self.GameOver = True

    def display(self,screen):
        fondo = pygame.image.load(fondos[i]).convert()
        screen.blit(fondo, (0,0))
        if self.GameOver:
            font = pygame.font.SysFont("arial",25)
            text = font.render(f"FELICIDADES! ATRAPASTE {self.num} {objects[i]}!",True,rojo)
            x = (long_x // 2) - (text.get_width() // 2)
            y = (long_y // 2) - (text.get_height() // 2)
            pygame.draw.rect(screen,blanco,(x,y,text.get_width(),40))
            screen.blit(text, (x,y))
        else:
            font = pygame.font.SysFont("arial",25)
            text = font.render(f"CUENTA L@S {objects[i]} QUE CAIGAN", True, azul)
            text1 = font.render(f"{self.score}!", True, azul)
            x = (long_x // 2) - (text.get_width() // 2)
            y = 30
            pygame.draw.rect(screen,blanco, (x,y,text.get_width(),25))
            screen.blit(text, (x,y))
            if self.score >= 1:
                if self.score < self.num:
                    pygame.draw.rect(screen,blanco,(long_x//2, 100,30,30))
                    screen.blit(text1, (long_x // 2, 100))
            self.lista_sprites.draw(screen)
        pygame.display.flip()


def juego_principal():
    screen = pygame.display.set_mode(size)
    pygame.init()
    game_over = False
    clock = pygame.time.Clock()
    juego = Game()
    while not game_over:
        game_over = juego.events()
        juego.logica()
        juego.display(screen)

        clock.tick(30)
    pygame.QUIT
