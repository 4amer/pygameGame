import pygame
pygame.init()

width = 600
height = 400

sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("sadfsaf")

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

player = pygame.image.load('GreenPlayer.png').convert()
playerRect = player.get_rect(center=(width//2, height//2))

player = pygame.transform.scale(player, (player.get_width()//3, player.get_height()//3))

sc.blit(player, playerRect)
pygame.display.update()

print("hui")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)

