import pygame
import sys
pygame.init()
screen_width = 1000
screen_height = 700

max_bullets=3
bullets_left=max_bullets

score=0
points=0

scoreimglist=['text_0.png','text_1.png','text_2.png','text_3.png','text_4.png','text_5.png','text_6.png','text_7.png','text_8.png','text_9.png']

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Basics")
background_color = ('black')

running = True

bg_img=pygame.image.load('assets/bg_wood.png')
bg_img=pygame.transform.scale(bg_img,(1000,700))

curtain1=pygame.image.load('assets/curtain.png')
curtain1=pygame.transform.scale(curtain1,(100,700))

curtain2=pygame.transform.flip(curtain1,True,False)

curtain_len=pygame.image.load('assets/curtain_straight.png')
curtain_len=pygame.transform.scale(curtain_len,(1000,50))

grass=pygame.image.load('assets/grass2.png')
grass=pygame.transform.scale(grass,(100,200))

water1=pygame.image.load('assets/water1.png')

duck1=pygame.image.load('assets/duck_outline_target_white.png')
duck1=pygame.transform.scale(duck1,(100,100))

duck2=pygame.image.load('assets/duck_outline_target_yellow.png')
duck2=pygame.transform.scale(duck2,(100,100))

rifle=pygame.image.load('assets/rifle.png')
rifle=pygame.transform.scale(rifle,(100,150))

shot=pygame.image.load('assets/shot_blue_small.png')
shot=pygame.transform.scale(shot,(20,30))

bullet_full=pygame.image.load('assets/icon_bullet_gold_long.png')
bullet_full=pygame.transform.scale(bullet_full,(20,30))

bullet_empty=pygame.image.load('assets/icon_bullet_empty_long.png')
bullet_empty=pygame.transform.scale(bullet_empty,(20,30))

gameover1=pygame.image.load('assets/HUD/text_gameover.png')
gameover1=pygame.transform.scale(gameover1,(300,90))

scoreimg=pygame.image.load('assets/text_score.png')
scoreimg=pygame.transform.scale(scoreimg,(100,40))

font=pygame.font.SysFont('Impact',35)

target_rect=duck1.get_rect()
target_rect.topleft=(100,300)
target_speed=25

second_target_rect=duck2.get_rect()
second_target_rect.topleft=(100,100)
second_target_speed=10

bullet=[]
bullet_speed=10

rifle_rect=rifle.get_rect()
rifle_rect.midbottom=(550,625)

clock=pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if bullets_left > 0:
                    bullet_rect=shot.get_rect()
                    bullet_rect.midbottom=rifle_rect.midtop
                    bullet.append(bullet_rect)
                    bullets_left-=1

    target_rect.x=target_rect.x+target_speed
    if target_rect.right>=screen_width or target_rect.left<=0:#it is out of screen
        target_speed*=-1

    second_target_rect.x=second_target_rect.x+second_target_speed
    if second_target_rect.right>=screen_width or second_target_rect.left<=0:#it is out of screen
        second_target_speed*=-1


    for i in bullet[:]:
        i.y-=bullet_speed
        if i.bottom<0 :
            bullet.remove(i)
        elif i.colliderect(target_rect):
            bullet.remove(i)
            print('hit')
            points+=2
            bullets_left+=1
        elif i.colliderect(second_target_rect):
            bullet.remove(i)
            print('hit')
            points += 1
            # bullets_left += 1


    screen.fill(background_color)

    x=0

    screen.blit(bg_img,(0,0))
    for i in range(1,12):
        screen.blit(grass,(x,525))
        x=x+100
    x=0
    for i in range(1,12):
        screen.blit(water1,(x,600))
        x=x+132

    screen.blit(curtain1,(0,0))
    screen.blit(curtain2,(900,0))
    screen.blit(curtain_len,(0,0))
    screen.blit(duck1,target_rect)
    screen.blit(duck2,second_target_rect)
    screen.blit(shot, (515, 475))
    screen.blit(rifle,(rifle_rect))
    # screen.blit(shot,(515,475))

    for i in bullet:
        screen.blit(shot, i)

    copy_points=points

    positions = [(860,560),(890,560),(920,560)]

    for j in range(max_bullets):
        x,y=positions[j]
        if j<bullets_left:
            screen.blit(bullet_full,(x,y))
        else:
            screen.blit(bullet_empty,(x,y))

    copy_points = str(copy_points)

    list_num = []  # empty list

    for i in copy_points:
        val = int(i)
        list_num.append(val)

    # print(list_num)
    num=150+15
    for j in list_num:
        path=f"assets/HUD/{scoreimglist[j]}"
        img=pygame.image.load(path)
        img=pygame.transform.scale(img,(35,40))
        screen.blit(img,(num,50))
        num=num+24

    text=font.render(f":  {points}",True,"white")
    screen.blit(scoreimg,(50,50))
    # screen.blit(text,(215,50))

    if bullets_left==0:
        screen.blit(gameover1,(375,300))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    pygame.display.flip()