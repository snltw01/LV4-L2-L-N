import pygame
import random
pygame.init()
sc=pygame.display.set_mode((1000,800))
pygame.display.set_caption('Buổi 1')
white=(255,255,255)
yellow=(255,255,0)
gray=(128,128,128)
cyan=(0,255,255)
red=(255,0,0)
black=(0,0,0)
navy=	(0,0,128)

score=0

car = pygame.Surface((175, 100))
car.fill(navy)
sc_w=1000
sc_h=800
speed=5
car_w=175
car_h=100
car_x=sc_w//2-car_w
car_y=sc_h-car_h





clock = pygame.time.Clock()

score=0
font = pygame.font.Font(None, 36)



def draw_score(score):
    score_text = font.render(f"Điểm: {score}", True, black)
    sc.blit(score_text, (10, 10))



def check_collision(car_rect,enermy):
    if car_rect.colliderect(enermy):
        return True
    return False
enermy_y=1500
enermy1=pygame.draw.rect(sc,red,pygame.Rect(0,enermy_y,car_w,car_h))
running = True
while running:
    sc.fill(yellow)
    if enermy_y>1000 and enermy_y<0:
        a=random.randint(50,950)
        enermy_y=50
    enermy1_x=a
    enermy1_x += speed
    enermy1=pygame.draw.rect(sc,red,pygame.Rect(a,enermy_y,car_w,car_h))



    keys = pygame.key.get_pressed()
    if car_x<950 and car_x>50:
        if keys[pygame.K_LEFT]:
            car_x -= speed
        if keys[pygame.K_RIGHT]:
            car_x += speed

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    car_rect=pygame.Rect(car_x,car_y,car_w,car_h)
    sc.blit(car,(car_x,car_y))

    if check_collision(car_rect,pygame.Rect(a,0,car_w,car_h)):
        print('Game Over')
        running=False

    draw_score(score)
    pygame.display.update()
    clock.tick(60)
pygame.quit()

