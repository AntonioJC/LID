import pygame
import math
from math import sqrt,cos,sin,tan,atan,acos,asin
from shooter2 import shoot
from charge import elec_charge

import time

#cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255,165,0)
AQUA = (127,255,212)
DSBLUE = (0,191,255)
BLUE = (119,136,153)
BROWN = (255,228,181)
GRAY = (211,211,211)
GOLD = (255,215,0)
DARK_RED = (178,34,34)
CORN_BLUE = (100,149,237)
DARK_BLUE = (72,61,139)

pygame.init()
 
# Set the height and width of the screen
display_width = 700
display_height = 500
size = [display_width, display_height]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Electromagnetism for dummies")
tcol=4 
pause = False 

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def text_objects(text, font,color=BLACK):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

wait_for_response=1  #se nao houver clique, fica-se a espera de um - wait_for_response=1! Isto indica que se click[0]=1, ou seja, se houver um clique, realiza-se a action(). Como so queremos realiza-la uma vez por clique, quando a action() e chamada poe-se imediatamente wait_for_response=0. Assim, so quando o user deixar de premir o botao e que se entra outra vez neste if, aguardando nova resposta (wait_for_response=1, novamente)

def button(msg,x,y,w,h,ic,ac,action=None):

    global wait_for_response

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if click[0]!=1:
        wait_for_response=1

    rad=5

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        pygame.draw.circle(screen, ac, [x, y+rad], rad)
        pygame.draw.circle(screen, ac, [x+w, y+h-rad], rad)
        pygame.draw.circle(screen, ac, [x, y+h-rad], rad)
        pygame.draw.circle(screen, ac, [x+w, y+rad], rad)
        pygame.draw.rect(screen, ac,(x-rad,y+rad,rad,h-2*rad))
        pygame.draw.rect(screen, ac,(x+w,y+rad,rad,h-2*rad))

        if click[0] == 1 and action != None and wait_for_response==1:
            wait_for_response=0
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        pygame.draw.circle(screen, ic, [x, y+rad], rad)
        pygame.draw.circle(screen, ic, [x+w, y+h-rad], rad)
        pygame.draw.circle(screen, ic, [x, y+h-rad], rad)
        pygame.draw.circle(screen, ic, [x+w, y+rad], rad)
        pygame.draw.rect(screen, ic,(x-rad,y+rad,rad,h-2*rad))
        pygame.draw.rect(screen, ic,(x+w,y+rad,rad,h-2*rad))

    smallText = pygame.font.SysFont("freesans",20)
    #smallText = pygame.font.SysFont("Verdana",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


def game_welcome():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(WHITE)
        largeText = pygame.font.SysFont("freesans",60)
        TextSurf, TextRect = text_objects("Are you", largeText)
        TextSurf2, TextRect2 = text_objects("ready?", largeText)
        TextRect.center = ((display_width/2),100)
        TextRect2.center = ((display_width/2),180)
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf2, TextRect2)

        button("Begin",(display_width/2-150),250,100,50,GREEN,GRAY,game_intro)
        button("About",(display_width/2+50),250,100,50,GREEN,GRAY,about)

        pygame.display.update()
        clock.tick(15)
 

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(WHITE)
        largeText = pygame.font.SysFont("freesans",50)
        TextSurf, TextRect = text_objects("The golden path", largeText)
        TextRect.center = ((display_width/2),120)
        screen.blit(TextSurf, TextRect)

        button("Tutorial",(display_width/2)-110,200,100,50,GOLD,GRAY,stage3_tut)
        button("Level 1",(display_width/2)+10,200,100,50,GOLD,GRAY,level1)
        button("Level 2",(display_width/2)-110,260,100,50,GOLD,GRAY,level2)
        button("Level 3",(display_width/2)+10,260,100,50,GOLD,GRAY,level3)
        button("Take me back, I don't want to be amazing",0,0,400,40,WHITE,GRAY,game_welcome)
        #button("Level 3",(display_width/2)-50,380,100,50,GREEN,RED,level3)
        #button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
 
 
# -------- Main Program Loop -----------
def getBackground():
      return pygame.image.load('background.gif'), 5


def stage3_tut():

	pygame.key.set_repeat(1,15)

	#Variaveis importantes 
        B=0 #campo magnetico default
        Ex=0
        Ey=0.
        vel=0
	s = shoot()
        shooter_angle=0
	ball_on_screen=False

        ###Origem do referencial
        Ox=display_width/2
        Oy=display_height/2

        ##############################################

        ### flags do tutorial

        move_shooter=False
        throw_charge=False
        click_a=False
        click_s=False
        click_d=False
        click_Ex=False
        click_Ey=False

        b_up=False
        b_null=False
        b_down=False

        Ex_down=False
        Ex_up=False
        Ey_down=False
        Ey_up=False
        Ex_test=False
        Ey_test=False

	# Loop until the user clicks the close button.
	done = False
	while not done:

                keys = pygame.key.get_pressed()  #checking pressed keys
                if keys[pygame.K_LEFT]:
                    Ex -= 1
                    Ex_down=True
                    if(ball_on_screen==True):
                        click_Ex = True
                if keys[pygame.K_RIGHT]:
                    Ex += 1
                    Ex_up=True
                    if(ball_on_screen==True):
                        click_Ex = True
                if keys[pygame.K_DOWN]:
                    Ey += 1
                    Ey_down=True
                    if(ball_on_screen==True):
                        click_Ey = True
                if keys[pygame.K_UP]:
                    Ey -= 1
                    Ey_up=True
                    if(ball_on_screen==True):
                        click_Ey = True

		# --- Event Processing
		for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()	

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_o:

                                    if(ball_on_screen==False and shooter_angle<1.5): # tenho de impor esta condicao porque quando a bola e disparada eu nao apago a imagem anterior para se ver a trajectoria e por isso se deixar o user mexer no shooter nessa fase, vao ficar varias imagens da posicao do shooter sobrepostas
                                        shooter_angle = shooter_angle+0.05	
                                    else:
                                        vel=0
                                        ball_on_screen=False #para fazer nova jogada

                                    move_shooter=True
                    

				elif event.key == pygame.K_l:

                                    if(ball_on_screen==False and shooter_angle>=0):
					shooter_angle = shooter_angle-0.05
                                    else:
                                        vel=0
                                        ball_on_screen=False #para fazer nova jogada

                                    move_shooter=True



				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                        throw_charge=True
                                elif event.key == pygame.K_d:
                                        B=14
                                        b_up = True
                                        if(ball_on_screen==True):
                                            click_d = True
                                elif event.key == pygame.K_s:
                                        B=0
                                        b_null=True

                                        if(ball_on_screen==True):
                                            click_s = True
                                elif event.key == pygame.K_a:
                                        B=-14
                                        b_down=True

                                        if(ball_on_screen==True):
                                            click_a = True


			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					shooter_angle=shooter_angle
					#nao acontece nada ao angulo quando as teclas sao premidas ao mesmo tempo		

                # Set the screen background
                #if ball_on_screen == False:
                bg = pygame.image.load("bg.png") 
                screen.blit(bg, (0, 0)) 




                trans=-100

                if(move_shooter==False):


                    x=trans
                    y=5
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Move the thrower: 'o' (UP) or 'l' (DOWN) keys", smallText,RED)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)
                else:

                    x=trans
                    y=5
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Move the thrower: 'o' (UP) or 'l' (DOWN) keys", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)


                if(throw_charge==False):

                    x=trans
                    y=35
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Throw a + charge: 'SPACE'", smallText,RED)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)

                else:

                    x=trans
                    y=35
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Throw a + charge: 'SPACE'", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)

                if(click_a==False):

                    x=trans
                    y=65
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Magnetic field pointing out of the computer: 'a' ", smallText,RED)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)

                else:

                    x=trans
                    y=65
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Magnetic field pointing out of the computer: 'a' ", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)


                if(click_d==False):

                    x=trans
                    y=95
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Magnetic field pointing into the computer: 'd' ", smallText,RED)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)

                else:

                    x=trans
                    y=95
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Magnetic field pointing into the computer: 'd' ", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)



                if(click_s==False):

                    x=trans
                    y=125
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Null magnetic field: 's' ", smallText,RED)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)

                else:

                    x=trans
                    y=125
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Null magnetic field: 's' ", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)


                if(click_Ex==False):

                    x=trans
                    y=155
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the left and right arrows to change Ex", smallText,RED)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)

                else:

                    x=trans
                    y=155
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the left and right arrows to change Ex", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)


                if(click_Ey==False):
                    x=trans
                    y=185
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the up and down arrows to change Ey", smallText,RED)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)

                else:

                    x=trans
                    y=185
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the up and down arrows to change Ey", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)


                if(move_shooter==True and throw_charge==True and click_a==True and click_s==True and click_d==True and click_Ex==True and click_Ey==True):
                    x=trans
                    y=215
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Keep practicing! Leave the tutorial when ready", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)+50) )
                    screen.blit(textSurf, textRect)




                

                button("Menu",0,5,50,20,GRAY,WHITE,game_intro)

                ###Origem do referencial
                Ox=display_width/2
                Oy=display_height/2

		# Desenhar o shooter
		s.draw_shooter(screen,shooter_angle)
                
                x=490-10
                y=5
                rad=7
                w=50
                h=30
                test_color_Ex=RED
                
                if Ex_down==False or Ex_up==False:
                    test_color_Ex=RED
                else:
                    test_color_Ex=GREEN
                    Ex_test=True

                pygame.draw.rect(screen, test_color_Ex,(x,y,w,h))
                pygame.draw.circle(screen, test_color_Ex, [x, y+rad], rad)
                pygame.draw.circle(screen, test_color_Ex, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, test_color_Ex, [x, y+h-rad], rad)
                pygame.draw.circle(screen, test_color_Ex, [x+w, y+rad], rad)
                pygame.draw.rect(screen, test_color_Ex,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, test_color_Ex,(x+w,y+rad,rad,h-2*rad))

                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                if Ex>0:
                    textSurf, textRect = text_objects("+Ex ", smallText)
                elif Ex==0:
                    textSurf, textRect = text_objects("Ex ", smallText)
                elif Ex<0:
                    textSurf, textRect = text_objects("-Ex ", smallText)
                textRect.center = ( (x-10+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

                x=490+50
                y=5
                rad=7
                w=50
                h=30
                test_color_Ey=RED
                
                if Ey_up==False or Ey_down==False:
                    test_color_Ey=RED
                else:
                    test_color_Ey=GREEN
                    Ey_test=True

                pygame.draw.rect(screen, test_color_Ey,(x,y,w,h))
                pygame.draw.circle(screen, test_color_Ey, [x, y+rad], rad)
                pygame.draw.circle(screen, test_color_Ey, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, test_color_Ey, [x, y+h-rad], rad)
                pygame.draw.circle(screen, test_color_Ey, [x+w, y+rad], rad)
                pygame.draw.rect(screen, test_color_Ey,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, test_color_Ey,(x+w,y+rad,rad,h-2*rad))

                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                if Ey>0:
                    textSurf, textRect = text_objects("-Ey ", smallText)
                elif Ey==0:
                    textSurf, textRect = text_objects("Ey ", smallText)
                elif Ey<0:
                    textSurf, textRect = text_objects("+Ey ", smallText)
                textRect.center = ( (x-10+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)


                pygame.draw.rect(screen, BLACK,(525-10,9,14,21))
                
                if 0<Ex<=2 or -2<=Ex<0:
                    pygame.draw.rect(screen, GOLD,(527-10,23,10,5))
                elif 2<Ex<=4 or -4<=Ex<-2:
                     pygame.draw.rect(screen, ORANGE,(527-10,17,10,5))
                     pygame.draw.rect(screen, GOLD,(527-10,23,10,5))
                elif Ex>4 or Ex<-4:
                    pygame.draw.rect(screen, RED,(527-10,11,10,5))
                    pygame.draw.rect(screen, ORANGE,(527-10,17,10,5))
                    pygame.draw.rect(screen, GOLD,(527-10,23,10,5))

                pygame.draw.rect(screen, BLACK,(575,9,14,21))

                if 0<Ey<=2 or -2<=Ey<0:
                    pygame.draw.rect(screen, GOLD,(577,23,10,5))
                elif 2<Ey<=4 or -4<=Ey<-2:
                     pygame.draw.rect(screen, ORANGE,(577,17,10,5))
                     pygame.draw.rect(screen, GOLD,(577,23,10,5))
                elif Ey>4 or Ey<-4:
                    pygame.draw.rect(screen, RED,(577,11,10,5))
                    pygame.draw.rect(screen, ORANGE,(577,17,10,5))
                    pygame.draw.rect(screen, GOLD,(577,23,10,5))

                x=600
                y=5
                rad=7
                w=80
                h=30

                if b_null==False or b_up==False or b_down==False:
                    test_color_B=RED
                else:
                    test_color_B=GREEN

                pygame.draw.rect(screen, test_color_B,(x,y,w,h))
                pygame.draw.circle(screen, test_color_B, [x, y+rad], rad)
                pygame.draw.circle(screen, test_color_B, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, test_color_B, [x, y+h-rad], rad)
                pygame.draw.circle(screen, test_color_B, [x+w, y+rad], rad)
                pygame.draw.rect(screen, test_color_B,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, test_color_B,(x+w,y+rad,rad,h-2*rad))
                
                if B==14:
                    pygame.draw.circle(screen, BLACK, [650,20],10)
                    pygame.draw.circle(screen, WHITE, [650,20],8)
                    pygame.draw.circle(screen, BLACK, [650,20],3)
                elif B==-14:
                    pygame.draw.circle(screen, BLACK, [650,20],10)
                    pygame.draw.circle(screen, WHITE, [650,20],8)
                    smallText2 = pygame.font.SysFont("freesans",18)
                    textSurf2, textRect2 = text_objects("X", smallText2)
                    textRect2.center = ( (650), (20) )
                    screen.blit(textSurf2, textRect2)
                elif B==0:
                    smallText2 = pygame.font.SysFont("freesans",20)
                    textSurf2, textRect2 = text_objects(" = 0", smallText2)
                    textRect2.center = ( (650), (20) )
                    screen.blit(textSurf2, textRect2)

                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("B ", smallText)
                textRect.center = ( (x-10+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)







                pos_meita=500
                yyy=60
                pygame.draw.circle(screen, BLACK, [pos_meita,yyy],10)
                pygame.draw.circle(screen, WHITE, [pos_meita,yyy],8)
                pygame.draw.circle(screen, BLACK, [pos_meita,yyy],3)

                pygame.draw.circle(screen, BLACK, [pos_meita,yyy+20],10)
                pygame.draw.circle(screen, WHITE, [pos_meita,yyy+20],8)
                smallText3 = pygame.font.SysFont("freesans",18)
                textSurf3, textRect3 = text_objects("X", smallText3)
                textRect3.center = ( (pos_meita), (yyy+20) )
                screen.blit(textSurf3, textRect3)
                smallText3 = pygame.font.SysFont("freesans",18)
                textSurf3, textRect3 = text_objects("Out of the computer", smallText3,WHITE)
                textRect3.center = ( (pos_meita+100), (yyy) )
                screen.blit(textSurf3, textRect3)
                smallText3 = pygame.font.SysFont("freesans",18)
                textSurf3, textRect3 = text_objects("Into the computer", smallText3,WHITE)
                textRect3.center = ( (pos_meita+90), (yyy+20) )
                screen.blit(textSurf3, textRect3)



		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        #s.kutta(screen,shot,B,Ex,Ey)
                    
                        vel = 10

                        s.electromagkutta(screen,shot,B,Ex,Ey)

			shot = False

                        """
                        tempo = s.counter(shot,detect)
                        countdown = 120-tempo

                        x=0
                        y=55
                        rad=7
                        w=80
                        h=30

                        cor=GOLD

                        if countdown < 60:
                            cor = ORANGE
                        if countdown < 30:
                            cor = RED

                        pygame.draw.rect(screen, cor,(x,y,w,h))
                        pygame.draw.circle(screen, cor, [x, y+rad], rad)
                        pygame.draw.circle(screen, cor, [x+w, y+h-rad], rad)
                        pygame.draw.circle(screen, cor, [x, y+h-rad], rad)
                        pygame.draw.circle(screen, cor, [x+w, y+rad], rad)
                        pygame.draw.rect(screen, cor,(x-rad,y+rad,rad,h-2*rad))
                        pygame.draw.rect(screen, cor,(x+w,y+rad,rad,h-2*rad))
                     
                        smallText = pygame.font.SysFont("freesans",20)
                        #smallText = pygame.font.SysFont("Verdana",20)
                        textSurf, textRect = text_objects(str(countdown), smallText)
                        textRect.center = ( (x+(w/2)), (y+(h/2)) )
                        screen.blit(textSurf, textRect)
                        """
			
			pos = s.get_ball_pos()

                        # verificar se a bola acertou no patamar pretendido
                        #if pos_patamar[0]<pos[0]<pos_patamar[0]+width_patamar and pos_patamar[1]-2<pos[1]<pos_patamar[1]+2:

                        # verificar se a bola esta dentro do ecra  
			if 0<pos[0]< display_width and  0<pos[1]<display_height: 
				ball_on_screen=True
			else:
				ball_on_screen=False
                                

                #if(tut_complete1==True and tut_complete2==True and tut_complete3==True and tut_complete4==True):
                 #   tutorial_sucess(stage3_tut,game_intro)

                # --- Wrap-ups
		# Limit to 180 frames per second
		clock.tick(180)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

def level1():
    
        pygame.key.set_repeat(1,10)

	#Variaveis importantes 
        B=0   #campo magnetico default
        Ex=0;
        Ey=0;
	s = shoot()
	shooter_angle=0
	ball_on_screen=False
        global pause

	# Loop until the user clicks the close button.
	done = False
	while not done:

		# --- Event Processing
		for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()	

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_o:
                                    if(shooter_angle<1.5):
					shooter_angle = shooter_angle+0.05
				elif event.key == pygame.K_l:
                                    if(shooter_angle>=0):
					shooter_angle = shooter_angle-0.05
				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                elif event.key == pygame.K_d:
                                        B=14
                                elif event.key == pygame.K_s:
                                        B=0
                                elif event.key == pygame.K_a:
                                        B=-14
                                elif event.key == pygame.K_e:
                                        Ex=-Ex
                                elif event.key == pygame.K_p:
                                    pause =  True
                                    paused(level1)
                                        
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					shooter_angle=shooter_angle
					#nao acontece nada ao angulo quando as teclas sao premidas ao mesmo tempo		
 
		# --- Drawing
                
		# Set the screen background
		#screen.fill(BLACK)
                bg = pygame.image.load("bg.png")                
                screen.blit(bg, (0, 0))
                
                button("Menu",0,0,50,30,GRAY,GREEN,game_intro)
               
                #desenhar caminho
                rad=8
                pygame.draw.rect(screen, DSBLUE,(0,420,180,16))
                pygame.draw.circle(screen, DSBLUE, [180,420+rad],rad)

                rad=10
                x=380
                y=120
                pygame.draw.rect(screen, DSBLUE,(x,y+rad,20,400))
                pygame.draw.circle(screen, DSBLUE, [x+rad,y+rad],rad)

                rad=8
                x=120
                y=300
                pygame.draw.rect(screen, DSBLUE,(x,y,270,16))
                pygame.draw.circle(screen, DSBLUE, [x,y+rad],rad)

                pygame.draw.rect(screen, DSBLUE,(x-rad,120+rad,16,180))
                pygame.draw.circle(screen, DSBLUE, [x,120+rad],rad)

                #pygame.draw.arc(screen, DSBLUE,[x, 0, 130, 300], math.pi, 3*math.pi/2, 2)

                x=220
                y=15
                rad=20
                w=40
                h=170
        
                pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
                pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
                pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))

                x=520
                y=300
                rad=7
                w=30
                h=100
        
                pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
                pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
                pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))

                x=520
                y=300
                rad=7
                w=300
                h=20
        
                pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
                pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
                pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))

                x=520
                y=120
                rad=7
                w=100
                h=80
        
                pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
                pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
                pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))

                #objectivo e leitor
                x=150
                y=5
                rad=7
                w=385
                h=30
        
                pygame.draw.rect(screen, GOLD,(x,y,w,h))
                pygame.draw.circle(screen, GOLD, [x, y+rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+rad], rad)
                pygame.draw.rect(screen, GOLD,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, GOLD,(x+w,y+rad,rad,h-2*rad))

                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("Objective: Reach the lower right corner!", smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)


                x=600
                y=5
                rad=7
                w=80
                h=30
        
                pygame.draw.rect(screen, GOLD,(x,y,w,h))
                pygame.draw.circle(screen, GOLD, [x, y+rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+rad], rad)
                pygame.draw.rect(screen, GOLD,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, GOLD,(x+w,y+rad,rad,h-2*rad))
                
                if B==14:
                    pygame.draw.circle(screen, BLACK, [650,20],10)
                    pygame.draw.circle(screen, WHITE, [650,20],8)
                    pygame.draw.circle(screen, BLACK, [650,20],3)
                elif B==-14:
                    pygame.draw.circle(screen, BLACK, [650,20],10)
                    pygame.draw.circle(screen, WHITE, [650,20],8)
                    smallText2 = pygame.font.SysFont("freesans",18)
                    textSurf2, textRect2 = text_objects("X", smallText2)
                    textRect2.center = ( (650), (20) )
                    screen.blit(textSurf2, textRect2)
                elif B==0:
                    smallText2 = pygame.font.SysFont("freesans",20)
                    textSurf2, textRect2 = text_objects(" = 0", smallText2)
                    textRect2.center = ( (650), (20) )
                    screen.blit(textSurf2, textRect2)

                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("B", smallText)
                textRect.center = ( (x-15+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)


		# desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                # Desenhar patamar 
		pygame.draw.rect(screen,RED,(680,340,2,70))

		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                       
                        s.magkutta(screen,shot,B)
                        
			shot = False

			pos = s.get_ball_pos()
                        vel = s.get_ball_vel()

                        if 675<pos[0]<685 and 338<pos[1]<412:
                            victory(level1)   

                        if (0<pos[0]<186 and 420<pos[1]<436) or (380<pos[0]<400 and 122<pos[1]<520) or (114<pos[0]<390 and 300<pos[1]<316) or (112<pos[0]<128 and 122<pos[1]<308) or (200<pos[0]<280 and 15<pos[1]<185) or (513<pos[0]<550 and 300<pos[1]<400) or (513<pos[0]<820 and 300<pos[1]<320) or (513<pos[0]<620 and 120<pos[1]<200) or (680<pos[0]<682 and 340<pos[1]<410) or (600<pos[0]<680 and 5<pos[1]<35):
                            defeat(level1)
                        

			if 0<pos[0]< display_width and  0<pos[1]<display_height:
				ball_on_screen=True
			else:
				ball_on_screen=False
                                defeat(level1)

		# --- Wrap-ups
		# Limit to 60 frames per second
		clock.tick(60)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

def level2():
    
        pygame.key.set_repeat(1,10)

	#Variaveis importantes 
        B=0   #campo magnetico default
        Ex=0;
        Ey=0;
	s = shoot()
	shooter_angle=0
	ball_on_screen=False
        global pause

	# Loop until the user clicks the close button.
	done = False
	while not done:

		# --- Event Processing
		for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()	

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_o:
                                    if(shooter_angle<1.5):
					shooter_angle = shooter_angle+0.05
				elif event.key == pygame.K_l:
                                    if(shooter_angle>=0):
					shooter_angle = shooter_angle-0.05
				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                elif event.key == pygame.K_d:
                                        B=14
                                elif event.key == pygame.K_s:
                                        B=0
                                elif event.key == pygame.K_a:
                                        B=-14
                                elif event.key == pygame.K_e:
                                        Ex=-Ex
                                elif event.key == pygame.K_p:
                                    pause =  True
                                    paused(level1)
                                        
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					shooter_angle=shooter_angle
					#nao acontece nada ao angulo quando as teclas sao premidas ao mesmo tempo		
 
		# --- Drawing
                
		# Set the screen background
		#screen.fill(BLACK)
                bg = pygame.image.load("bg.png")                
                screen.blit(bg, (0, 0))
                
                button("Menu",0,0,50,30,GRAY,GREEN,game_intro)
               
                #desenhar caminho
                rad=8
                pygame.draw.rect(screen, DSBLUE,(0,290,100,16))
                pygame.draw.circle(screen, DSBLUE, [100,290+rad],rad)

                rad=8
                x=210
                y=320
                pygame.draw.rect(screen, DSBLUE,(x,y,300,16))
                pygame.draw.circle(screen, DSBLUE, [x,y+rad],rad)
                pygame.draw.circle(screen, DSBLUE, [x+300,y+rad],rad)

                x=250
                y=120
                pygame.draw.rect(screen, DSBLUE,(x,y,16,300))
                pygame.draw.circle(screen, DSBLUE, [x+rad,y],rad)
                pygame.draw.circle(screen, DSBLUE, [x+rad,y+300],rad)

                x=100
                y=0
                pygame.draw.rect(screen, DSBLUE,(x,y,16,200))
                pygame.draw.circle(screen, DSBLUE, [x+rad,y+200],rad)

                x=400
                y=420
                rad=20
                w=50
                h=100
        
                pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
                pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
                pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))

                x=370
                y=15
                rad=20
                w=50
                h=200

                pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
                pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
                pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))

                x=550
                y=120
                rad=20
                w=150
                h=50
        
                pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
                pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
                pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))

                x=680
                y=120
                rad=20
                w=15
                h=140
        
                pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
                pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
                pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))

                #speeders

                x=315
                y=150
                rad=7
                w=28
                h=40
                speed=AQUA

                pygame.draw.rect(screen, speed,(x,y,w,h))
                pygame.draw.circle(screen, speed, [x, y+rad], rad)
                pygame.draw.circle(screen, speed, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, speed, [x, y+h-rad], rad)
                pygame.draw.circle(screen, speed, [x+w, y+rad], rad)
                pygame.draw.rect(screen, speed,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, speed,(x+w,y+rad,rad,h-2*rad))


                smallText = pygame.font.SysFont("freesans",12)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("E down", smallText)
                textRect.center = ( (308+(42/2)), (150+(40/2)) )
                screen.blit(textSurf, textRect)

                x=350
                y=350
                rad=7
                w=28
                h=40
                speed=AQUA

                pygame.draw.rect(screen, speed,(x,y,w,h))
                pygame.draw.circle(screen, speed, [x, y+rad], rad)
                pygame.draw.circle(screen, speed, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, speed, [x, y+h-rad], rad)
                pygame.draw.circle(screen, speed, [x+w, y+rad], rad)
                pygame.draw.rect(screen, speed,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, speed,(x+w,y+rad,rad,h-2*rad))


                smallText = pygame.font.SysFont("freesans",12)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("E left", smallText)
                textRect.center = ( (350+(28/2)), (350+(40/2)) )
                screen.blit(textSurf, textRect)

                x=387
                y=215
                rad=7
                w=26
                h=42
                speed=AQUA

                pygame.draw.rect(screen, speed,(x,y,w,h))
                pygame.draw.circle(screen, speed, [x, y+rad], rad)
                pygame.draw.circle(screen, speed, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, speed, [x, y+h-rad], rad)
                pygame.draw.circle(screen, speed, [x+w, y+rad], rad)
                pygame.draw.rect(screen, speed,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, speed,(x+w,y+rad,rad,h-2*rad))


                smallText = pygame.font.SysFont("freesans",12)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("E right", smallText)
                textRect.center = ( (387+(26/2)), (215+(42/2)) )
                screen.blit(textSurf, textRect)

                #pygame.draw.polygon(screen, BLACK, ((387+10, 215+7+10), (387+10, 215+10+10), (387+10+10, 215+10+10), (387+10+10, 215+13+10), (387+15+10, 215+7.5+10), (387+10+10, 215+13), (387+10+10, 215+7+10)))

                x=150
                y=350
                rad=7
                w=28
                h=40
                speed=AQUA

                pygame.draw.rect(screen, speed,(x,y,w,h))
                pygame.draw.circle(screen, speed, [x, y+rad], rad)
                pygame.draw.circle(screen, speed, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, speed, [x, y+h-rad], rad)
                pygame.draw.circle(screen, speed, [x+w, y+rad], rad)
                pygame.draw.rect(screen, speed,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, speed,(x+w,y+rad,rad,h-2*rad))


                smallText = pygame.font.SysFont("freesans",10)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("E up", smallText)
                textRect.center = ( (150+(28/2)), (350+(40/2)) )
                screen.blit(textSurf, textRect)

               
                #objectivo e leitor
                x=150
                y=5
                rad=7
                w=385
                h=30
        
                pygame.draw.rect(screen, GOLD,(x,y,w,h))
                pygame.draw.circle(screen, GOLD, [x, y+rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+rad], rad)
                pygame.draw.rect(screen, GOLD,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, GOLD,(x+w,y+rad,rad,h-2*rad))

                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("Objective: Reach the upper right corner!", smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)


                x=600
                y=5
                rad=7
                w=80
                h=30
        
                pygame.draw.rect(screen, GOLD,(x,y,w,h))
                pygame.draw.circle(screen, GOLD, [x, y+rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+rad], rad)
                pygame.draw.rect(screen, GOLD,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, GOLD,(x+w,y+rad,rad,h-2*rad))
                
                if B==14:
                    pygame.draw.circle(screen, BLACK, [650,20],10)
                    pygame.draw.circle(screen, WHITE, [650,20],8)
                    pygame.draw.circle(screen, BLACK, [650,20],3)
                elif B==-14:
                    pygame.draw.circle(screen, BLACK, [650,20],10)
                    pygame.draw.circle(screen, WHITE, [650,20],8)
                    smallText2 = pygame.font.SysFont("freesans",18)
                    textSurf2, textRect2 = text_objects("X", smallText2)
                    textRect2.center = ( (650), (20) )
                    screen.blit(textSurf2, textRect2)
                elif B==0:
                    smallText2 = pygame.font.SysFont("freesans",20)
                    textSurf2, textRect2 = text_objects(" = 0", smallText2)
                    textRect2.center = ( (650), (20) )
                    screen.blit(textSurf2, textRect2)

                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("B ", smallText)
                textRect.center = ( (x-10+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)


		# desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                # Desenhar patamar 
		pygame.draw.rect(screen,RED,(620,40,2,70))

                if ball_on_screen==True:
                       
                        detect=True
                        s.electromagkutta(screen,shot,B,Ex,Ey)
                        
			shot = False
                        tempo = s.counter(shot,detect)
                        countdown = 120-tempo

                        x=0
                        y=55
                        rad=7
                        w=80
                        h=30

                        cor=GOLD

                        if countdown < 60:
                            cor = ORANGE
                        if countdown < 30:
                            cor = RED

                        pygame.draw.rect(screen, cor,(x,y,w,h))
                        pygame.draw.circle(screen, cor, [x, y+rad], rad)
                        pygame.draw.circle(screen, cor, [x+w, y+h-rad], rad)
                        pygame.draw.circle(screen, cor, [x, y+h-rad], rad)
                        pygame.draw.circle(screen, cor, [x+w, y+rad], rad)
                        pygame.draw.rect(screen, cor,(x-rad,y+rad,rad,h-2*rad))
                        pygame.draw.rect(screen, cor,(x+w,y+rad,rad,h-2*rad))
                     
                        smallText = pygame.font.SysFont("freesans",20)
                        #smallText = pygame.font.SysFont("Verdana",20)
                        textSurf, textRect = text_objects(str(countdown), smallText)
                        textRect.center = ( (x+(w/2)), (y+(h/2)) )
                        screen.blit(textSurf, textRect)

			pos = s.get_ball_pos()
                        vel = s.get_ball_vel()

                        if 615<pos[0]<625 and 38<pos[1]<112:
                            victory(level2)   

                        Ey=0
                        if (266+42)<pos[0]<(266+84) and 150<pos[1]<180:
                            Ey=70
                        elif 143<pos[0]<(143+42) and 350<pos[1]<390:
                            Ey=-60

                        Ex=0
                        if 380<pos[0]<410 and 215<pos[1]<(215+52):
                            Ex=80
                        elif 343<pos[0]<(343+42) and 350<pos[1]<390:
                            Ex=-70

                        if countdown == 0:
                            defeat(level2)

                        if (0<pos[0]<106 and 290<pos[1]<306) or (204<pos[0]<516 and 320<pos[1]<336) or (250<pos[0]<266 and 114<pos[1]<426) or (100<pos[0]<116 and 0<pos[1]<206) or (380<pos[0]<470 and 420<pos[1]<520) or (350<pos[0]<440 and 15<pos[1]<200) or (530<pos[0]<700 and 120<pos[1]<170) or (660<pos[0]<695 and 120<pos[1]<260):
                            defeat(level2)
                        

			if 0<pos[0]< display_width and  0<pos[1]<display_height:
				ball_on_screen=True
			else:
				ball_on_screen=False
                                defeat(level2)

		# --- Wrap-ups
		# Limit to 60 frames per second
		clock.tick(60)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

def level3():
    
        pygame.key.set_repeat(1,10)

	#Variaveis importantes 
        B=0   #campo magnetico default
        Ex=0;
        Ey=0;
	s = shoot()
	shooter_angle=0
	ball_on_screen=False
        global pause

        time=0
        
        c2 = elec_charge()
        c2.create_charge(screen,1200,display_width/2-150,display_height/2-100,BROWN)

	# Loop until the user clicks the close button.
	done = False
	while not done:

                keys = pygame.key.get_pressed()  #checking pressed keys
                if keys[pygame.K_LEFT]:
                    Ex -= 1
                if keys[pygame.K_RIGHT]:
                    Ex += 1
                if keys[pygame.K_DOWN]:
                    Ey += 1
                if keys[pygame.K_UP]:
                    Ey -= 1

		# --- Event Processing
		for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()	

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_o:
                                    if(shooter_angle<1.5):
					shooter_angle = shooter_angle+0.05
				elif event.key == pygame.K_l:
                                    if(shooter_angle>=0):
					shooter_angle = shooter_angle-0.05
				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                elif event.key == pygame.K_d:
                                        B=14
                                elif event.key == pygame.K_s:
                                        B=0
                                elif event.key == pygame.K_a:
                                        B=-14

                                elif event.key == pygame.K_p:
                                    pause =  True
                                    paused(level3)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					shooter_angle=shooter_angle
					#nao acontece nada ao angulo quando as teclas sao premidas ao mesmo tempo		
 
		# --- Drawing
                
		# Set the screen background
		#screen.fill(BLACK)
                bg = pygame.image.load("bg.png")                
                screen.blit(bg, (0, 0))
                
                button("Menu",0,0,50,30,GRAY,GREEN,game_intro)
               
                #desenhar caminho
                rad=8
                pygame.draw.rect(screen, DSBLUE,(0,290,100,16))
                pygame.draw.circle(screen, DSBLUE, [100,290+rad],rad)

                rad=8
                x=210
                y=320
                pygame.draw.rect(screen, DSBLUE,(x,y,300,16))
                pygame.draw.circle(screen, DSBLUE, [x,y+rad],rad)
                pygame.draw.circle(screen, DSBLUE, [x+300,y+rad],rad)

                x=250
                y=120
                pygame.draw.rect(screen, DSBLUE,(x,y,16,300))
                pygame.draw.circle(screen, DSBLUE, [x+rad,y],rad)
                pygame.draw.circle(screen, DSBLUE, [x+rad,y+300],rad)

                x=100
                y=0
                pygame.draw.rect(screen, DSBLUE,(x,y,16,200))
                pygame.draw.circle(screen, DSBLUE, [x+rad,y+200],rad)

                x=400
                y=420
                rad=20
                w=50
                h=100
        
                pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
                pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
                pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))

                x=370
                y=15
                rad=20
                w=50
                h=200

                pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
                pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
                pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))

                x=550
                y=120
                rad=20
                w=150
                h=50
        
                pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
                pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
                pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))

                x=680
                y=120
                rad=20
                w=15
                h=140
        
                pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
                pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
                pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
                pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))
               
                #objectivo e leitor
                x=90
                y=5
                rad=7
                w=385
                h=30
        
                pygame.draw.rect(screen, GOLD,(x,y,w,h))
                pygame.draw.circle(screen, GOLD, [x, y+rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+rad], rad)
                pygame.draw.rect(screen, GOLD,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, GOLD,(x+w,y+rad,rad,h-2*rad))

                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("Objective: Reach the upper right corner!", smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

                x=490
                y=5
                rad=7
                w=100
                h=30
        
                pygame.draw.rect(screen, GOLD,(x,y,w,h))
                pygame.draw.circle(screen, GOLD, [x, y+rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+rad], rad)
                pygame.draw.rect(screen, GOLD,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, GOLD,(x+w,y+rad,rad,h-2*rad))

                pygame.draw.rect(screen, BLACK,(525,9,14,21))
                
                if 0<Ex<=2 or -2<=Ex<0:
                    pygame.draw.rect(screen, GOLD,(527,23,10,5))
                elif 2<Ex<=4 or -4<=Ex<-2:
                     pygame.draw.rect(screen, ORANGE,(527,17,10,5))
                     pygame.draw.rect(screen, GOLD,(527,23,10,5))
                elif Ex>4 or Ex<-4:
                    pygame.draw.rect(screen, RED,(527,11,10,5))
                    pygame.draw.rect(screen, ORANGE,(527,17,10,5))
                    pygame.draw.rect(screen, GOLD,(527,23,10,5))

                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                if Ex>0:
                    textSurf, textRect = text_objects("+Ex ", smallText)
                elif Ex==0:
                    textSurf, textRect = text_objects("Ex ", smallText)
                elif Ex<0:
                    textSurf, textRect = text_objects("-Ex ", smallText)
                textRect.center = ( (x-32+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

                pygame.draw.rect(screen, BLACK,(575,9,14,21))

                if 0<Ey<=2 or -2<=Ey<0:
                    pygame.draw.rect(screen, GOLD,(577,23,10,5))
                elif 2<Ey<=4 or -4<=Ey<-2:
                     pygame.draw.rect(screen, ORANGE,(577,17,10,5))
                     pygame.draw.rect(screen, GOLD,(577,23,10,5))
                elif Ey>4 or Ey<-4:
                    pygame.draw.rect(screen, RED,(577,11,10,5))
                    pygame.draw.rect(screen, ORANGE,(577,17,10,5))
                    pygame.draw.rect(screen, GOLD,(577,23,10,5))

                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                if Ey>0:
                    textSurf, textRect = text_objects("-Ey ", smallText)
                elif Ey==0:
                    textSurf, textRect = text_objects("Ey ", smallText)
                elif Ey<0:
                    textSurf, textRect = text_objects("+Ey ", smallText)
                textRect.center = ( (x+19+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

                x=600
                y=5
                rad=7
                w=80
                h=30
        
                pygame.draw.rect(screen, GOLD,(x,y,w,h))
                pygame.draw.circle(screen, GOLD, [x, y+rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x, y+h-rad], rad)
                pygame.draw.circle(screen, GOLD, [x+w, y+rad], rad)
                pygame.draw.rect(screen, GOLD,(x-rad,y+rad,rad,h-2*rad))
                pygame.draw.rect(screen, GOLD,(x+w,y+rad,rad,h-2*rad))
                
                if B==14:
                    pygame.draw.circle(screen, BLACK, [650,20],10)
                    pygame.draw.circle(screen, WHITE, [650,20],8)
                    pygame.draw.circle(screen, BLACK, [650,20],3)
                elif B==-14:
                    pygame.draw.circle(screen, BLACK, [650,20],10)
                    pygame.draw.circle(screen, WHITE, [650,20],8)
                    smallText2 = pygame.font.SysFont("freesans",18)
                    textSurf2, textRect2 = text_objects("X", smallText2)
                    textRect2.center = ( (650), (20) )
                    screen.blit(textSurf2, textRect2)
                elif B==0:
                    smallText2 = pygame.font.SysFont("freesans",20)
                    textSurf2, textRect2 = text_objects(" = 0", smallText2)
                    textRect2.center = ( (650), (20) )
                    screen.blit(textSurf2, textRect2)

                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("B ", smallText)
                textRect.center = ( (x-10+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

                #carga
                c2.erase_charge(screen)

                ##mover a carga
                x = 180*cos(time)
                c2.set_pos(300,250-x)
                # Desenhar a carga e o sinal - depois de movidos
                c2.draw_charge(screen)
                
                time+=0.01

                font = pygame.font.SysFont("freesans", 25)
                text = font.render("+", 1, BLACK)
                textpos = text.get_rect()
                c2_pos=c2.get_pos()
                textpos.center = c2_pos
                screen.blit(text, textpos)
                
                c_vec=[]
                c_vec.append(c2)
                
		# desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                # Desenhar patamar 
		pygame.draw.rect(screen,RED,(620,40,2,70))

                if ball_on_screen==True:
                       
                        detect=True
                        s.electromagkutta_charge(screen,shot,B,Ex,Ey,c_vec)
                        
			shot = False
                        tempo = s.counter(shot,detect)
                        countdown = 105-tempo

                        x=0
                        y=55
                        rad=7
                        w=80
                        h=30

                        cor=GOLD

                        if countdown < 60:
                            cor = ORANGE
                        if countdown < 30:
                            cor = RED

                        pygame.draw.rect(screen, cor,(x,y,w,h))
                        pygame.draw.circle(screen, cor, [x, y+rad], rad)
                        pygame.draw.circle(screen, cor, [x+w, y+h-rad], rad)
                        pygame.draw.circle(screen, cor, [x, y+h-rad], rad)
                        pygame.draw.circle(screen, cor, [x+w, y+rad], rad)
                        pygame.draw.rect(screen, cor,(x-rad,y+rad,rad,h-2*rad))
                        pygame.draw.rect(screen, cor,(x+w,y+rad,rad,h-2*rad))
                     
                        smallText = pygame.font.SysFont("freesans",20)
                        #smallText = pygame.font.SysFont("Verdana",20)
                        textSurf, textRect = text_objects(str(countdown), smallText)
                        textRect.center = ( (x+(w/2)), (y+(h/2)) )
                        screen.blit(textSurf, textRect)

			pos = s.get_ball_pos()
                        vel = s.get_ball_vel()

                        if 615<pos[0]<625 and 38<pos[1]<112:
                            victory(level3)   

                        if countdown == 0:
                            defeat(level3)

                        #Verificar se a bola colide com a carga
                        pos_c2 = c2.get_pos()
                        r2 = c2.get_radius()
                        
                        if (pos_c2[0]-r2<pos[0]<pos_c2[0]+r2 and pos_c2[1]-r2<pos[1]<pos_c2[1]+r2):
                            defeat(level3)

                        #Barreiras
                        if (0<pos[0]<106 and 290<pos[1]<306) or (204<pos[0]<516 and 320<pos[1]<336) or (250<pos[0]<266 and 114<pos[1]<426) or (100<pos[0]<116 and 0<pos[1]<206) or (380<pos[0]<470 and 420<pos[1]<520) or (350<pos[0]<440 and 15<pos[1]<200) or (530<pos[0]<700 and 120<pos[1]<170) or (660<pos[0]<695 and 120<pos[1]<260):
                            defeat(level3)
                        

			if 0<pos[0]< display_width and  0<pos[1]<display_height:
				ball_on_screen=True
			else:
				ball_on_screen=False
                                defeat(level3)

		# --- Wrap-ups
		# Limit to 60 frames per second
		clock.tick(60)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()


def defeat(level):
    
    lost = True 

    while lost:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            """
            pygame.draw.rect(screen,AQUA,((display_width/2)-100,(display_height/2)-50,200,50))
            font = pygame.font.Font(None, 50)
            text = font.render("   You lost!   ", 1, (20, 20, 20))
            textpos = text.get_rect()
            textpos.center = ((display_width/2),(display_height/2)-20)
            """       

        x=(display_width/2-120)
        y=(display_height/2-120)
        rad=14
        w=240
        h=200

        pygame.draw.rect(screen, WHITE,(x,y,w,h))
        pygame.draw.circle(screen, WHITE, [x, y+rad], rad)
        pygame.draw.circle(screen, WHITE, [x+w, y+h-rad], rad)
        pygame.draw.circle(screen, WHITE, [x, y+h-rad], rad)
        pygame.draw.circle(screen, WHITE, [x+w, y+rad], rad)
        pygame.draw.rect(screen, WHITE,(x-rad,y+rad,rad,h-2*rad))
        pygame.draw.rect(screen, WHITE,(x+w,y+rad,rad,h-2*rad))

        x=(display_width/2-90)
        y=(display_height/2-100)
        rad=14
        w=180
        h=50

        pygame.draw.rect(screen, DSBLUE,(x,y,w,h))
        pygame.draw.circle(screen, DSBLUE, [x, y+rad], rad)
        pygame.draw.circle(screen, DSBLUE, [x+w, y+h-rad], rad)
        pygame.draw.circle(screen, DSBLUE, [x, y+h-rad], rad)
        pygame.draw.circle(screen, DSBLUE, [x+w, y+rad], rad)
        pygame.draw.rect(screen, DSBLUE,(x-rad,y+rad,rad,h-2*rad))
        pygame.draw.rect(screen, DSBLUE,(x+w,y+rad,rad,h-2*rad))
       
       
        smallText = pygame.font.SysFont("freesans",20)
        #smallText = pygame.font.SysFont("Verdana",20)
        textSurf, textRect = text_objects("You lost!", smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)

        #screen.blit(text, textpos)
        button("Restart",(display_width/2)-120,(display_height/2),110,50,WHITE,GRAY,level)
        button("Menu",(display_width/2)+10,(display_height/2),110,50,WHITE,GRAY,game_intro)

        pygame.display.update()
        clock.tick(25)  

def victory(level):
    
    win = True 

    while win:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        """
        pygame.draw.rect(screen,AQUA,((display_width/2)-100,(display_height/2)-50,200,50))
        font = pygame.font.Font(None, 50)
        text = font.render("   You won!   ", 1, (20, 20, 20))
        textpos = text.get_rect()
        textpos.center = ((display_width/2),(display_height/2)-20)
        screen.blit(text, textpos)
        button("Restart",(display_width/2)-100,(display_height/2),100,50,WHITE,GREEN,level)
        button("Menu",(display_width/2),(display_height/2),100,50,WHITE,GREEN,game_intro)
        """
        x=(display_width/2-120)
        y=(display_height/2-120)
        rad=14
        w=240
        h=200

        pygame.draw.rect(screen, WHITE,(x,y,w,h))
        pygame.draw.circle(screen, WHITE, [x, y+rad], rad)
        pygame.draw.circle(screen, WHITE, [x+w, y+h-rad], rad)
        pygame.draw.circle(screen, WHITE, [x, y+h-rad], rad)
        pygame.draw.circle(screen, WHITE, [x+w, y+rad], rad)
        pygame.draw.rect(screen, WHITE,(x-rad,y+rad,rad,h-2*rad))
        pygame.draw.rect(screen, WHITE,(x+w,y+rad,rad,h-2*rad))

        x=(display_width/2-90)
        y=(display_height/2-100)
        rad=14
        w=180
        h=50

        pygame.draw.rect(screen, GOLD,(x,y,w,h))
        pygame.draw.circle(screen, GOLD, [x, y+rad], rad)
        pygame.draw.circle(screen, GOLD, [x+w, y+h-rad], rad)
        pygame.draw.circle(screen, GOLD, [x, y+h-rad], rad)
        pygame.draw.circle(screen, GOLD, [x+w, y+rad], rad)
        pygame.draw.rect(screen, GOLD,(x-rad,y+rad,rad,h-2*rad))
        pygame.draw.rect(screen, GOLD,(x+w,y+rad,rad,h-2*rad))
       
       
        smallText = pygame.font.SysFont("freesans",20)
        #smallText = pygame.font.SysFont("Verdana",20)
        textSurf, textRect = text_objects("You won!", smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)

        #screen.blit(text, textpos)
        button("Restart",(display_width/2)-120,(display_height/2),110,50,WHITE,GRAY,level)
        button("Menu",(display_width/2)+10,(display_height/2),110,50,WHITE,GRAY,game_intro)



        pygame.display.update()
        clock.tick(25)  

def unpause():
    global pause 
    pause = False

def paused(level):

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.draw.rect(screen,AQUA,((display_width/2)-150,(display_height/2)-50,300,50))
        font = pygame.font.Font(None, 50)
        text = font.render("   Game Paused   ", 1, (20, 20, 20))
        textpos = text.get_rect()
        textpos.center = ((display_width/2),(display_height/2)-20)
        screen.blit(text, textpos)
        button("Continue",(display_width/2)-150,(display_height/2),100,50,WHITE,GREEN,unpause)
        button("Restart",(display_width/2)-50,(display_height/2),100,50,WHITE,GREEN,level)
        button("Menu",(display_width/2)+50,(display_height/2),100,50,WHITE,GREEN,game_intro)

        pygame.display.update()
        clock.tick(25)  

def tutorial_sucess(level,stage):
    
    win = True 

    while win:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        """
        pygame.draw.rect(screen,AQUA,((display_width/2)-100,(display_height/2)-50,200,50))
        font = pygame.font.Font(None, 50)
        text = font.render("   You won!   ", 1, (20, 20, 20))
        textpos = text.get_rect()
        textpos.center = ((display_width/2),(display_height/2)-20)
        screen.blit(text, textpos)
        button("Restart",(display_width/2)-100,(display_height/2),100,50,WHITE,GREEN,level)
        button("Menu",(display_width/2),(display_height/2),100,50,WHITE,GREEN,game_intro)
        """
        x=(display_width/2-170)
        y=(display_height/2-120)
        rad=14
        w=350
        h=200

        pygame.draw.rect(screen, WHITE,(x,y,w,h))
        pygame.draw.circle(screen, WHITE, [x, y+rad], rad)
        pygame.draw.circle(screen, WHITE, [x+w, y+h-rad], rad)
        pygame.draw.circle(screen, WHITE, [x, y+h-rad], rad)
        pygame.draw.circle(screen, WHITE, [x+w, y+rad], rad)
        pygame.draw.rect(screen, WHITE,(x-rad,y+rad,rad,h-2*rad))
        pygame.draw.rect(screen, WHITE,(x+w,y+rad,rad,h-2*rad))

        x=(display_width/2-150)
        y=(display_height/2-100)
        rad=14
        w=300
        h=50

        pygame.draw.rect(screen, GOLD,(x,y,w,h))
        pygame.draw.circle(screen, GOLD, [x, y+rad], rad)
        pygame.draw.circle(screen, GOLD, [x+w, y+h-rad], rad)
        pygame.draw.circle(screen, GOLD, [x, y+h-rad], rad)
        pygame.draw.circle(screen, GOLD, [x+w, y+rad], rad)
        pygame.draw.rect(screen, GOLD,(x-rad,y+rad,rad,h-2*rad))
        pygame.draw.rect(screen, GOLD,(x+w,y+rad,rad,h-2*rad))
       
       
        smallText = pygame.font.SysFont("freesans",20)
        #smallText = pygame.font.SysFont("Verdana",20)
        textSurf, textRect = text_objects("You have completed the tutorial!", smallText,BLACK)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)

        #screen.blit(text, textpos)
        button("Restart",(display_width/2)-120,(display_height/2),110,50,WHITE,GRAY,level)
        button("Levels",(display_width/2)+10,(display_height/2),110,50,WHITE,GRAY,stage)



        pygame.display.update()
        clock.tick(25)  


def about():

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(WHITE)
        largeText = pygame.font.SysFont("freesans",90)
        TextSurf, TextRect = text_objects("About", largeText)
        TextRect.center = ((display_width/2),80)
        font = pygame.font.Font(None, 26)
	text = font.render("This is a game that desires to stimulate the", 1, (10, 10, 10))
        text2 = font.render("passion of young people for electromagnetism,", 1, (10, 10, 10))
        text3 = font.render("using for that purpose a variety of levels.", 1, (10, 10, 10))
        text4 = font.render("Created by Antonio Costa and Miguel Goncalves", 1, (10, 10, 10))
        textpos = text.get_rect()
        text2pos = text2.get_rect()
        text3pos = text3.get_rect()
        text4pos = text4.get_rect()
	textpos.center = ((display_width/2),150)
        text2pos.center = ((display_width/2),170)
        text3pos.center = ((display_width/2),190)
        text4pos.center = ((display_width/2),250)
        screen.blit(TextSurf, TextRect)
        screen.blit(text, textpos)
        screen.blit(text2, text2pos)
        screen.blit(text3, text3pos)
        screen.blit(text4, text4pos)

        button("Menu",0,0,50,30,WHITE,GREEN,game_welcome)

        pygame.display.update()
        clock.tick(15)



def kutta():

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(WHITE)

        s = shoot()

        s.kutta()

# Close everything down
game_welcome()
pygame.quit()
quit()

"""
def level3():

        pygame.key.set_repeat(1,10)

	#Variaveis importantes 
        B=-5 #campo magnetico default
        Ex=0;
        qEy=400;
	s = shoot()
	shooter_angle=0
	ball_on_screen=False
        global pause
        up = False

	# Loop until the user clicks the close button.
	done = False
	while not done:

		# --- Event Processing
		for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()	

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					shooter_angle = shooter_angle+0.2
				elif event.key == pygame.K_DOWN:
					shooter_angle = shooter_angle-0.2
				elif event.key == pygame.K_s:
					shot=True
					ball_on_screen=True
                                elif event.key == pygame.K_b:
                                        B=-B
                                elif event.key == pygame.K_e:
                                    Ex=-Ex
                                elif event.key == pygame.K_r:
                                    qEy=-qEy
                                elif event.key == pygame.K_p:
                                    pause =  True
                                    paused(level2)
                                        
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					shooter_angle=shooter_angle
					#nao acontece nada ao angulo quando as teclas sao premidas ao mesmo tempo		
 
		# --- Drawing
                
		# Set the screen background
		#screen.fill(BLACK)
                bg = pygame.image.load("bg.png")                
                screen.blit(bg, (0, 0))

                button("Menu",0,0,50,30,WHITE,GREEN,game_intro)
                pygame.draw.rect(screen,AQUA,(200,0,205,30))
                font = pygame.font.Font(None, 20)
                text = font.render("Objective: Reach the 4s!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (300,15)
                screen.blit(text, textpos)

		# desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                #desenhar o detector
	
                s.draw_detector(screen)

                wire_pos = 215

		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        
                        s.ElectricFieldWire(screen,shot,B,Ex,qEy,wire_pos)

			shot = False
			
			pos = s.get_ball_pos()                        

                        #print pos[1]
                       
                        detect = False
                        
                        if pos[1]<215 and up == False:
                            qEy=-qEy
                            up = True
                            #print qEy
                        
                        
                        if 120<pos[0]<600 and 80<pos[1]<350:
                            detect = True
                            #pygame.draw.rect(screen,RED,(600,400,20,20))

                            count = s.counter(shot,detect)
                            font = pygame.font.Font(None, 50)
                            text = font.render(str(count-2), 1, (20, 20, 20))
                            textpos = text.get_rect()
                            textpos.center = (200,200)
                            screen.blit(text, textpos)

                            if 4.0<=(count-2)<=4.2:
                                victory(level2)
                                        
			if 0<pos[0]< display_width and  0<pos[1]<display_height:
				ball_on_screen=True
			else:
				ball_on_screen=False
                                defeat(level2)
 

		# --- Wrap-ups
		# Limit to 60 frames per second
		clock.tick(60)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
"""
