import pygame
# Khởi tạo
pygame.init()
# cài đặt thông tin cửa sổ
sc=pygame.display.set_mode((600,600))
# đặt tiêu đề cửa sổ
pygame.display.set_caption('Buổi 1')
# đặt incon
# icon=pygame.image.load("Logo.png")
# pygame.display.set_icon(icon)
white=(255,255,255)
yellow=(255,255,0)
gray=(128,128,128)
cyan=(0,255,255)
red=(255,0,0)
black=(0,0,0)
navy=	(0,0,128)
running= True
while running:
    sc.fill(cyan)
    # font = pygame.font.Font(None, 36)
    # text = font.render("Điểm: 0", True, black)
    # sc.blit(text, (10, 10))
    # vẽ hình chữ nhật
    pygame.draw.rect(sc,navy,pygame.Rect(100,100,100,100))
    # vẽ hình tròn
    pygame.draw.circle(sc, navy, (250, 250),300, 10)
    # vẽ hình tam giác
    point=[(400,400),(200,200),(150,250)]
    pygame.draw.polygon(sc,navy,point)
    # vẽ hình đa giác
    point1=[(120,120),(124,124),(213,321),(123,234),(232,127),(321,120)]
    pygame.draw.polygon(sc,white,point1)
    # Vẽ đường thẳng
    start_point=(200,450)
    end_point=(400,450)
    pygame.draw.line(sc,black,start_point,end_point)


    # lấy những sự kiện đang diễn ra trong pygame
    for event in pygame.event.get():
        # xét bấm nút tắt
        if event.type==pygame.QUIT:
            running=False   
    # cập nhật màn hình
    pygame.display.update()

    