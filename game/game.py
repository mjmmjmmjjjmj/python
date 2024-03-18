import sys
import pygame

class AlienInvasion:
    """게임 자원과 동작을 전체적으로 관리하는 클래스"""

pygame.init()
screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
image = pygame.image.load('./game/images/ship.bmp')

screen_rect = screen.get_rect()
ship_rect = image.get_rect()
# image.left = 1280/2
# image.top = 600
# rect = pygame.Rect((1280/2, 720/2), (400, 200))
ship_rect.midbottom = screen.get_rect().midbottom

def create_bullet (ship_rect) :
    bullet = pygame.Rect(0,0,5,50)
    bullet.midtop = ship_rect.midtop
    bullet.top -= ship_rect.height
    return bullet

bullets = []
bullet = create_bullet(ship_rect)
bullet_color = (225, 0, 0)
bullets.append (bullet)



while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_rect.left -= 10
            elif event.key == pygame.K_RIGHT :
                ship_rect.right += 10
                # alt + shift + ↓ : 밑에 복사됨
            elif event.key == pygame.K_UP :
                ship_rect.top -= 10
            elif event.key == pygame.K_DOWN :
                if ship_rect.top + ship_rect.height <= screen_rect.height :
                    ship_rect.bottom += 10
            elif event.key == pygame.K_SPACE :
                b = create_bullet(ship_rect)
                bullets.append(b)

    screen.fill("black")  # Fill the display with a solid color

    # Do logical updates here.
    def update_bullets(screen_rect, bullets):
        new_bullets = []
        for bullet in bullets :
            if screen_rect.top < bullet.top :
                bullet.top -= 1
                new_bullets.append(bullet)
        return new_bullets
    

    def render(screen, image, ship_rect, new_bullets) :
        screen.blit(image, ship_rect)
        for bullet in new_bullets:
            pygame.draw.rect(screen, bullet_color, bullet)
    # ...

    screen.blit(image, ship_rect)

    for bullet in bullets:
        bullet.top -= 1
        pygame.draw.rect(screen, bullet_color, bullet)


    # Render the graphics here.
    # ...
    # new_bullets 
    
    
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
