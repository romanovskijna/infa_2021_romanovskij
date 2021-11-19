import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
sc = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
M=[]    #массив в котором хранятся все данные о шариках в виде кортежей
Q=[]
name=input('введите ваше имя: ')

def new_quadrat():
    global x, y, r, color
    color = COLORS[randint(0, 5)]
    x = randint(0, 1100)
    y = randint(0, 800)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    rect(sc, color, (x, y, r, r), 0)
    
def quadrat(x, y, r, color):
    rect(sc, color, (x, y, r, r), 0)
    
def new_ball():
    '''рисует новый шарик
       x, y - координаты центра
       r - радиус
       color - цвет
    '''
    global x, y, r, color
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(sc, color, (x, y), r)
    
def ball(x, y, r, color):
    '''рисует шарик
       x, y - координаты центра
       r - радиус
       color - цвет
    '''
    circle(sc, color, (x, y), r)
    
k=0
n=10 #количество шариков
for i in range(n):
    new_ball()
    M.append([x, y, r, color, randint(-100, 100) / 20, randint(-100, 100) / 20])
p11=10
for i in range(p11):
    new_quadrat()
    Q.append([x, y, r, color, randint(-100, 100) / 20, randint(-100, 100) / 20])

    

pygame.display.update()
clock = pygame.time.Clock()
finished = False


f1 = pygame.font.Font(None, 36)
text1 = f1.render('Число очков ', True,(180, 180, 0))
p=str()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            a=event.pos[0]
            b=event.pos[1]
            for i in range(n):
                if (((M[i - 1][0] - a)**2 + (M[i - 1][1] - b)**2) < M[i - 1][2]**2):
                    M[i - 1][2]=0
                    k=k + 1
                    n=n+1
                    p = str(k)
                    new_ball()
                    M.append([x, y, r, color, randint(-100, 100) / 20, randint(-100, 100) / 20])
            
            for i in range(p11):
                if (((a - Q[i - 1][0])<r) and ((a - Q[i - 1][0])>0) and ((b - Q[i - 1][1]) < r) and ((b - Q[i - 1][1])>0)):
                    print('попал!')
                    Q[i - 1][2]=0
                    k=k - 2
                    p11=p11+1
                    p = str(k)
                    new_quadrat()
                    Q.append([x, y, r, color, randint(-100, 100) / 20, randint(-100, 100) / 20])


    for i in range (1, p11+1  , 1):
        if (Q[i - 1][0] < (1200 - Q[i - 1][2]) and  Q[i - 1][0] > 0):
            Q[i - 1][0] = Q[i - 1][0] + Q[i - 1][4]
        else:
            Q[i - 1][4] = - Q[i - 1][4]
            Q[i - 1][0] = Q[i - 1][0] + 2 * Q[i - 1][4]
            
        if (Q[i - 1][1] < (900 - Q[i - 1][2]) and Q[i - 1][1] > 0):
            Q[i - 1][1] = Q[i -1 ][1] + Q[i - 1][5]
        else:
            Q[i - 1][5] = - Q[i - 1][5]
            Q[i - 1][1] = Q[i - 1][1] + 2 * Q[i - 1][5]

            
    for i in range (1, n+1 , 1):
        if (M[i - 1][0] < (1200 - M[i - 1][2]) and  M[i - 1][0] > M[i - 1][2]):
            M[i - 1][0] = M[i - 1][0] + M[i - 1][4]
        else:
            w = randint(10,500) / 250
            M[i - 1][4] = - M[i - 1][4] * w
            M[i - 1][0] = M[i - 1][0] + 2 * M[i - 1][4]/w
            
        if (M[i - 1][1] < (900 - M[i - 1][2]) and M[i - 1][1] > M[i - 1][2]):
            M[i - 1][1] = M[i -1 ][1] + M[i - 1][5]
        else:
            w = randint(10,500) / 250
            M[i - 1][5] = - M[i - 1][5] * w
            M[i - 1][1] = M[i - 1][1] + 2 * M[i - 1][5] / w 
    
    sc.fill(BLACK)
    for i in range (n):
        ball(M[i - 1][0], M[i - 1][1], M[i - 1][2], M[i - 1][3])
    for i in range (p11):
        quadrat(Q[i - 1][0], Q[i - 1][1], Q[i - 1][2], Q[i - 1][3])
    sc.blit(text1 , (10, 20))
    text2 = f1.render(p, True, (180, 180, 0))
    sc.blit(text2, (300, 20))    
    pygame.display.update()
    sc.fill(BLACK)
print('Поздравляем, ваш счет:', k)


f = open("results.txt", "a")
f.write('\n')
f.write( str(k))
f.write( '          :        ')
f.write(name)
f.close()


with open("results.txt") as file:
    array = [row.strip() for row in file]   

d = dict()
for i in range(len(array)):
    d[array[i-1]]=int(array[i-1][0] + array[i-1][1] + array[i-1][2] + array[i-1][3])

sorted_dict = {}
sorted_keys = sorted(d, key=d.get, reverse = True)

for w in sorted_keys:
    sorted_dict[w] = d[w]

print(sorted_dict)


f = open("results.txt", "w")
for i in sorted_keys:
    f.write(i)
    f.write('\n')
lines = file.readlines()
del lines[-1]
f.close()

pygame.quit()
