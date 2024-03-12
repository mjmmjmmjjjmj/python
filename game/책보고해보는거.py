import sys
import pygame

class AlienInvasion:
    """게임 자원과 동작을 전체적으로 관리하는 클래스"""

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
image = pygame.image.load('./game/images/ship.bmp')

screen_rect = screen.get_rect()
# rect = pygame.Rect(500, 500, 100, 100)
# rect = screen.get_rect()
# rect = image.get_rect()

image_rect = image.get_rect()
# image.left = 1280/2
# image.top = 600
# rect = pygame.Rect((1280/2, 720/2), (400, 200))
image_rect.midbottom = screen_rect().midbottom

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # raise SystemExit
            
    # Do logical updates here.
    # ...

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    screen.blit(image, image_rect)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
