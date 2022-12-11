import pygame

pygame.init()
root = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ping pong")
run = True
x, y = 300, 300
x_move, y_move = 0.4, 0.5
xPlatform = 200
xEnemy = 300
score = 0
enemyscore = 0


def ball():
    global x, y, x_move, y_move
    x += x_move
    y += y_move
    if x > 785 or x < 15:
        x_move = x_move * (-1)
    if y > 565 or y < 15:
        y_move = y_move * (-1)
    pygame.draw.circle(root, (255, 255, 255), (x, y), 15)
def platform():
    global xPlatform, y_move, score, enemyscore
    if pygame.key.get_pressed()[pygame.K_LEFT]and xPlatform > 0:
        xPlatform -= 0.5
    if pygame.key.get_pressed()[pygame.K_RIGHT] and xPlatform  < 595:
        xPlatform += 0.5
    if xPlatform < x < xPlatform + 200 and 475 < y < 500:
        y_move = y_move*(-1)
        score += 1
    pygame.draw.rect(root,(0, 0, 255),(xPlatform, 500, 200, 25))

def enemy():
    global xEnemy, y_move, xPlatform ,x ,y, enemyscore, score
    pygame.draw.rect(root, (255, 0, 0), (xEnemy, 95, 200, 25))
    if x < xEnemy + 100 and y > 200 and xEnemy > 0:
        xEnemy -= 0.8
    if x > xEnemy + 100 and y > 15 and xEnemy < 600:
        xEnemy += 0.8
    if xEnemy < x < xEnemy + 200 and 80 < y < 145 : # AND 100 < 200
        y_move = y_move * (-1)
        enemyscore += 1

while run:
    root.fill("black")
    ball()
    platform()
    enemy()
    font = pygame.font.SysFont("Arial", 30)
    text = font.render(f"You: {score}", True, (0, 0,255))
    text2 = font.render(f"Enemy: {enemyscore}", True, (255, 0, 0))
    root.blit(text,(10,450))
    root.blit(text2,(10, 5))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False