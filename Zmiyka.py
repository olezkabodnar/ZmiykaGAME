import pygame
import random

class SnakeGame:
    x = 300
    y = 300
    xMove = 0.4
    yMove = 0.4
    appleCoords = (0,0)
    gameOver = False
    run = True

    def __init__(self, width, height):
        pygame.init()
        self.root = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Zmiyka")
    def draw(self):
        self.root.fill("white")
        pygame.draw.circle(self.root, (125, 245, 74), (self.x, self.y), 20)
        pygame.draw.circle(self.root,(255,0 , 0),self.appleCoords,20)


    def play(self):
        self.apple()
        while self.run:
            if not self.gameOver:
                self.control()
                self.move()
                self.draw()
            else:
                font = pygame.font.SysFont("Arial", 72)
                text = font.render("Game Over", True, (0, 0, 0))
                self.root.blit(text,(250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

    def move(self):
        self.x += self.xMove
        self.y += self.yMove
        if self.x > self.root.get_width()-40 or self.x <=20 or self.y >= self.root.get_height()-20 or self.y <= 20 :
            self.gameOver = True
    def control(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.xMove = -0.4
            self.yMove = 0
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.xMove = 0.4
            self.yMove = 0
        elif pygame.key.get_pressed()[pygame.K_UP]:
            self.xMove = 0
            self.yMove = -0.4
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.xMove = 0
            self.yMove = 0.4

    def apple(self):
        x = random.randint(20, self.root.get_width()-20)
        y = random.randint(20, self.root.get_height()-20)
        self.appleCoords = (x,y)

snakeGame = SnakeGame(800, 600)
snakeGame.play()




