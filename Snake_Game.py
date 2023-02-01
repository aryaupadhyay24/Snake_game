import random
import pygame
import os



pygame.init()
pygame.mixer.init()




screen_height=900
screen_width=600
screen=pygame.display.set_mode((screen_height,screen_width))

bgimg=pygame.image.load("back.jpg")
bgimg=pygame.transform.scale(bgimg, (screen_height,screen_width)).convert_alpha()
bgwater=pygame.image.load("water.jpg")
bgwater=pygame.transform.scale(bgwater, (screen_height,screen_width)).convert_alpha()

pygame.display.set_caption("Ayush Ka Snake Game")
pygame.display.update()

#game variaable


clock=pygame.time.Clock()


font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    screen.blit(screen_text,[x,y])

def plot_snake(screen, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(screen,color,[x,y,snake_size,snake_size])
def welcome():
    exit_game=False
    while not exit_game:
        screen.fill((224,214,206))
        screen.blit(bgimg,(0,0))
        text_screen("Welcome to Ayush Snake Game",(0,0,0),180,200)
        text_screen("Press Enter to Play",(0,0,0),250,290)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    pygame.mixer.music.load("Excuses.mp3")
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()

def gameloop():
    
    with open("hiscore.py","r") as f:
        hiscore=f.read()
    exit_game=False
    snake_x=40
    velocity_x=0
    velocity_y=0
    init_velocity=6
    snake_y=20
    fps=20
    snake_size=10
    game_over=False
    score=0
    snk_list=[]
    snk_length=1
    food_x,food_y=random.randint(0,screen_width/2),random.randint(0,screen_height/2)

    food_size=10
    
    while not exit_game:
        if game_over:
            
            if(not os.path.exists("hiscore.py")):
                with open("hiscore.py","w") as f:
                    f.write("0")
            with open("hiscore.py","w") as f:
                f.write(str(hiscore))
            screen.fill((0,0,0))
            text_screen("Your Score  :"+"  " +str(score)+"            High score"+str(hiscore),(0,0,255),100,150)
            text_screen("Game Over!!Want next Attempt,PRESS ENTER",(255,0,0),40,250)
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        #velocity_x=init_velocity 
                        #velocity_y=0
                        aise=head[1]
                        temp=False
                        for item in snk_list[-2:-1]:
                            if item==head:
                                pass
                            else: 
                                if item[1]==aise:
                                    temp=True
                        if temp==False:
                            velocity_x=init_velocity 
                            velocity_y=0
                           
                    if event.key==pygame.K_LEFT:
                        #velocity_x=-init_velocity 
                        #velocity_y=0
                        aise=head[1]
                        temp=False
                        for item in snk_list[-2:-1]:
                            if item==head:
                                pass
                            else: 
                                if item[1]==aise:
                                    temp=True
                        if temp==False:
                            velocity_x=-init_velocity 
                            velocity_y=0 
                    if event.key==pygame.K_UP:
                        #velocity_y=-init_velocity 
                        #velocity_x=0
                        aise=head[0]
                        temp=False
                        for item in snk_list[-2:-1]:
                            if item==head:
                                pass
                            else: 
                                if item[0]==aise:
                                    temp=True
                        if temp==False:
                            velocity_y=-init_velocity 
                            velocity_x=0 
                    if event.key==pygame.K_DOWN:
                        #velocity_y=init_velocity 
                        #velocity_x=0 
                        aise=head[0]
                        temp=False
                        for item in snk_list[-2:-1]:
                            if item==head:
                                pass
                            else: 
                                if item[0]==aise:
                                    temp=True
                        if temp==False:
                            velocity_y=init_velocity 
                            velocity_x=0 
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(food_x-snake_x)<6 and abs(food_y-snake_y)<6:
                #pygame.mixer.music.load("beep.mp3")
                #pygame.mixer.music.play()
                score+=10

                food_x,food_y=random.randint(0,screen_width/2),random.randint(0,screen_height/2)
                snk_length+=5
                if score>int(hiscore):
                    hiscore=score

            screen.fill((255,255,255))
            screen.blit(bgwater,(0,0))
            text_screen("Your Score: "+str(score)+"                 High Score : "+str(hiscore),(255,0,0),5,5)
            
            
            pygame.draw.rect(screen, (0,0,0), [snake_x,snake_y,snake_size,snake_size])
            pygame.draw.rect(screen,(255,0,0),[food_x,food_y,food_size,food_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if snake_x<0 or snake_x>screen_height or snake_y<0 or snake_y>screen_width:
                pygame.mixer.music.load("explosion.mp3")
                pygame.mixer.music.play()
                game_over=True
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("explosion.mp3")
                pygame.mixer.music.play()
            plot_snake(screen,(0,0,0),snk_list,snake_size)

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

welcome()
# this is rthe maini reson bheid wrting this code i'm onnt thee train without ticket and ii want this seat to be thid ithris whayt gonint on witn myself in trsain 
# i want tp share something about my self  i've done my worst mistrake by not understandi
# 
pygame