import pygame as pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
polygon(screen, (80, 80, 255), [(0,0), (0,400),
                               (800,400), (800,0)])


polygon(screen, (20, 200, 0), [(0,400), (0,800),
                               (800,800), (800,400)])

a=400
b=400
#рисуем пони
#хвост
def poni(a,b,i,h,k):
   
#туловище и ноги
    pygame.draw.ellipse(screen, (255, 255, 255), (a-i*k*10-h*k*170, b, k*170,k*70),0)

    rect(screen, (255, 255, 255), (a+i*k*10-h*k*3, b+k*30, k*13, k*100))
    rect(screen, (255, 255, 255), (a+i*k*30-h*k*3, b+k*30, k*13, k*110))
    rect(screen, (255, 255, 255), (a+i*k*120-h*k*3, b+k*30, k*13, k*100))
    rect(screen, (255, 255, 255), (a+i*k*140-h*k*3, b+k*30, k*13, k*110))

    rect(screen, (255, 255, 255), (a+i*k*120-h*k*30, b-k*40, k*30, k*70))
    pygame.draw.ellipse(screen, (255, 255, 255), (a+i*k*116-h*k*50, b-k*65, k*50,k*30),0)
    pygame.draw.ellipse(screen, (255, 255, 255), (a+i*k*149-h*k*36, b-k*55, k*36,k*20),0)
#гoлobа и рог
    circle(screen, (241, 79, 193), (a+i*k*150, b-k*55), k*7, 0)
    circle(screen, (0, 0, 0), (a+i*k*152, b-k*53), k*4, 0)
    polygon(screen, (216, 78, 193), [(a+i*k*135, b-k*65), (a+k*i*135,b-k*115),
                               (a+i*k*143, b-k*65)], 0)
#грива
    pygame.draw.ellipse(screen, (255, 143, 193), (a-i*k*62-h*40, b+k*80, k*40,k*9),0)
    pygame.draw.ellipse(screen, (255, 143, 193), (a-i*k*50-h*k*60, b+k*50, k*60,k*9),0)
    pygame.draw.ellipse(screen, (255, 143, 193), (a-i*k*48-h*k*40, b+k*10, k*40,k*30),0)

    pygame.draw.ellipse(screen, (191, 143, 193), (a-i*k*55-h*k*50, b+k*10, k*50,k*20),0)

    pygame.draw.ellipse(screen, (191, 79, 193), (a-i*k*30-h*k*25, b, k*25,k*13),0)
    
    pygame.draw.ellipse(screen, (191, 143, 193), (a-i*k*50-h*k*40, b+k*50, k*40,k*9),0)
    pygame.draw.ellipse(screen, (191, 143, 193), (a-i*k*45-h*k*36, b+k*68, k*36,k*16),0)

    pygame.draw.ellipse(screen, (191, 79, 193), (a-i*k*65-h*k*36, b+k*90, k*36,k*26),0)
    pygame.draw.ellipse(screen, (191, 79, 193), (a-i*k*35-h*k*36, b+k*46, k*36,k*14),0)
    pygame.draw.ellipse(screen, ((191, 79, 193)), (a-i*k*57-h*k*26, b+k*51, k*26,k*20),0)

    pygame.draw.ellipse(screen, (254, 142, 193), (a-i*k*27-h*k*26, b+k*21, k*26,k*20),0)
    pygame.draw.ellipse(screen, (254, 142, 193), (a-i*k*37-h*k*26, b+k*51, k*26,k*20),0)
    pygame.draw.ellipse(screen, (254, 142, 193), (a-i*k*45-h*k*26, b+k*31, k*26,k*20),0)


#хвост
    
    pygame.draw.ellipse(screen, (191, 79, 193), (a-i*k*62+i*k*140-h*k*40, b+k*80-k*70, k*40,k*9),0)
    pygame.draw.ellipse(screen, (191, 79, 193), (a-i*k*50+i*k*140-h*k*60, b+k*50-k*70, k*60,k*9),0)
    pygame.draw.ellipse(screen, (191, 79, 193), (a-i*k*48+i*k*140-h*k*40, b+k*10-k*70, k*40,k*30),0)
    
    pygame.draw.ellipse(screen, (191, 79, 193), (a-i*k*30-h*k*25+i*k*140, b-k*70, k*25,k*13),0)

    pygame.draw.ellipse(screen, (255, 143, 193), (a-i*k*55+i*k*140-h*k*50, b+k*10-k*70, k*50,k*20),0)
    pygame.draw.ellipse(screen, (255, 143, 193), (a-i*k*50+i*k*140-h*k*40, b+k*50-k*70, k*40,k*9),0)
    pygame.draw.ellipse(screen, (255, 143, 193), (a-i*k*45+k*i*140-k*h*36, b+k*68-k*70, k*36,k*16),0)

    pygame.draw.ellipse(screen, (254, 142, 193), (a-i*k*65+i*k*140-h*k*36, b+k*90-k*70, k*36,k*26),0)
    pygame.draw.ellipse(screen, (254, 142, 193), (a-i*k*35+i*k*140-h*k*36, b+k*46-k*70, k*36,k*14),0)
    pygame.draw.ellipse(screen, (254, 142, 193), (a-i*k*57+i*k*140-h*k*26, b+k*51-k*70, k*26,k*20),0)

    pygame.draw.ellipse(screen, (191, 143, 193), (a-i*k*27+i*k*140-h*k*26, b+k*21-k*70, k*26,k*20),0)
    pygame.draw.ellipse(screen, (191, 143, 193), (a-i*k*37+i*k*140-h*k*26, b+k*51-k*70, k*26,k*20),0)
    pygame.draw.ellipse(screen, (191, 143, 193), (a-i*k*45+i*k*140-h*k*26, b+k*31-k*70, k*26,k*20),0)



poni(350,630,1,0,0.9)



#дерево
rect(screen, (255, 255, 255), (90, 660, 23, 60))
rect(screen, (255, 255, 255), (280, 530, 23, 60))
pygame.draw.ellipse(screen, (120, 255, 10), (100, 180, 120,100),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (100, 180, 120,100),3)
pygame.draw.ellipse(screen, (120, 25, 10), (130, 210, 20,25),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (130, 210, 20,25),2)
pygame.draw.ellipse(screen, (120, 25, 10), (160, 210,25,20),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (160, 210, 25,20),2)


pygame.draw.ellipse(screen, (120, 255, 10), (60, 260, 180,90),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (60, 260, 180,90),3)
pygame.draw.ellipse(screen, (120, 25, 10), (90, 280, 20,25),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (90, 280, 20,25),2)



pygame.draw.ellipse(screen, (120, 255, 10), (110, 310, 120,40),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (110, 310, 120,40),3)
pygame.draw.ellipse(screen, (120, 25, 10), (150, 320, 26,20),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (150, 320, 26,20),2)

pygame.draw.ellipse(screen, (120, 255, 10), (40, 330, 120,60),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (40, 330, 120,60),3)
pygame.draw.ellipse(screen, (120, 25, 10), (60, 340, 20,27),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (60, 340, 20,27),2)

pygame.draw.ellipse(screen, (120, 255, 10), (70, 380, 190,70),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (70, 380, 190,70),3)
pygame.draw.ellipse(screen, (120, 25, 10), (110, 390, 28,20),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (110, 390, 28,20),2)


pygame.draw.ellipse(screen, (120, 255, 10), (50, 420, 120,50),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (50, 420, 120,50),3)
pygame.draw.ellipse(screen, (120, 25, 10), (140, 400, 20,27),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (140, 400, 20,27),2)

pygame.draw.ellipse(screen, (120, 255, 10), (60, 460, 140,70),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (60, 460, 140,70),3)
pygame.draw.ellipse(screen, (120, 25, 10), (100, 470, 20,25),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (100, 470, 20,25),2)

pygame.draw.ellipse(screen, (120, 255, 10), (50, 520, 190,80),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (50, 520, 190,80),3)
pygame.draw.ellipse(screen, (120, 25, 10), (100, 530, 25,20),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (100, 530, 25,20),2)

pygame.draw.ellipse(screen, (120, 255, 10), (20, 570, 120,60),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (20, 570, 120,60),3)
pygame.draw.ellipse(screen, (120, 25, 10), (150, 570, 25,20),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (150, 570, 25,20),2)





pygame.draw.ellipse(screen, (120, 255, 10), (-40, 620, 240,60),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (-40, 620, 240,60),3)
pygame.draw.ellipse(screen, (120, 25, 10), (130, 630, 29,20),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (130, 630, 29,20),2)
#дерево поменьше
pygame.draw.ellipse(screen, (120, 255, 10), (230, 490, 120,43),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (230, 490, 120,43),3)
pygame.draw.ellipse(screen, (120, 25, 10), (260, 500, 20,25),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (260, 500, 20,25),2)


pygame.draw.ellipse(screen, (120, 255, 10), (210, 450, 140,53),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (210, 450, 140,53),3)
pygame.draw.ellipse(screen, (120, 25, 10), (240, 460, 20,25),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (240, 460, 20,25),2)

pygame.draw.ellipse(screen, (120, 255, 10), (240, 410, 130,53),0)
pygame.draw.ellipse(screen,  (20, 200, 0), (240, 410, 130,53),3)
pygame.draw.ellipse(screen, (120, 25, 10), (270, 430, 20,25),0)
pygame.draw.ellipse(screen,  (255, 255, 255), (270, 430, 20,25),2)

for i in range(1,200,1):
    pygame.draw.ellipse(screen,  (255-175/200*i, 255-175/200*i, 2.55/2*i), (650-i, 100-i, 2*i,2*i),2)


pygame.transform.flip(screen, True, True)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
