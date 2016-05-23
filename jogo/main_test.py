import pygame
from pygame.locals import *
from math import sqrt,cos,sin,tan,atan,acos,asin
from shooter2 import shoot
from charge import elec_charge
from resize import resize_screen

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
DARK_GRAY=(131,139,139)

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
    textSurf, textRect = text_objects(msg, smallText,BLACK)
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

                
        screen.fill(BLACK)
        img = pygame.image.load("bgg2.png")
        #img = pygame.image.load("bg_white_2.png")
        screen.blit(img, (0, 0))

        x=90
        y=60
        rad=7
        w=520
        h=90
        #cor_title=DARK_GRAY
        cor_title=GRAY

        pygame.draw.rect(screen, cor_title,(x,y,w,h))
        pygame.draw.circle(screen, cor_title, [x, y+rad], rad)
        pygame.draw.circle(screen, cor_title, [x+w, y+h-rad], rad)
        pygame.draw.circle(screen, cor_title, [x, y+h-rad], rad)
        pygame.draw.circle(screen, cor_title, [x+w, y+rad], rad)
        pygame.draw.rect(screen, cor_title,(x-rad,y+rad,rad,h-2*rad))
        pygame.draw.rect(screen, cor_title,(x+w,y+rad,rad,h-2*rad))

        x=95
        y=65
        rad=7
        w=510
        h=80
        #cor_title=WHITE
        cor_title=BLACK

        pygame.draw.rect(screen, cor_title,(x,y,w,h))
        pygame.draw.circle(screen, cor_title, [x, y+rad], rad)
        pygame.draw.circle(screen, cor_title, [x+w, y+h-rad], rad)
        pygame.draw.circle(screen, cor_title, [x, y+h-rad], rad)
        pygame.draw.circle(screen, cor_title, [x+w, y+rad], rad)
        pygame.draw.rect(screen, cor_title,(x-rad,y+rad,rad,h-2*rad))
        pygame.draw.rect(screen, cor_title,(x+w,y+rad,rad,h-2*rad))

        
        x=100
        y=110
        rad=7
        w=500
        h=25
        cor_title=DARK_GRAY

        pygame.draw.rect(screen, cor_title,(x,y,w,h))
        pygame.draw.circle(screen, cor_title, [x, y+rad], rad)
        pygame.draw.circle(screen, cor_title, [x+w, y+h-rad], rad)
        pygame.draw.circle(screen, cor_title, [x, y+h-rad], rad)
        pygame.draw.circle(screen, cor_title, [x+w, y+rad], rad)
        pygame.draw.rect(screen, cor_title,(x-rad,y+rad,rad,h-2*rad))
        pygame.draw.rect(screen, cor_title,(x+w,y+rad,rad,h-2*rad))
        

        largeText = pygame.font.SysFont("freesans",50,BLACK)
        largeText2 = pygame.font.SysFont("freesans",50,BLACK)
        TextSurf, TextRect = text_objects("Electromagnetism", largeText,DARK_GRAY)
        TextSurf2, TextRect2 = text_objects("Electromagnetism", largeText2,(244,238,224))
        #TextSurf3, TextRect3 = text_objects("Electromagnetism", largeText2,GRAY)
        TextRect.center = ((display_width/2)+5,100-2)
        TextRect2.center = ((display_width/2),100)
        #TextRect3.center = ((display_width/2)-1,100)
        screen.blit(TextSurf, TextRect)
        #screen.blit(TextSurf3, TextRect3)
        screen.blit(TextSurf2, TextRect2)
        

        button("Begin",(display_width/2-150),280,100,50,GOLD,GRAY,game_intro)
        button("About",(display_width/2+50),280,100,50,GOLD,GRAY,about)

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
        TextSurf, TextRect = text_objects("The golden path", largeText,BLACK)
        TextRect.center = ((display_width/2),120)
        screen.blit(TextSurf, TextRect)

        button("Back",0,0,80,40,WHITE,GRAY,game_welcome)
        button("Stage 1",(display_width/2)-50,200,100,50,GOLD,GRAY,stage1)
        button("Stage 2",(display_width/2)-50,260,100,50,GOLD,GRAY,stage2)
        button("Stage 3",(display_width/2)-50,320,100,50,GOLD,GRAY,stage3)

        '''
        button("Level 1",(display_width/2)-110,200,100,50,GOLD,GRAY,level1)
        button("Level 2",(display_width/2)+10,200,100,50,GOLD,GRAY,level2)
        button("Level 3",(display_width/2)-110,260,100,50,GOLD,GRAY,level3)
        button("Level 4",(display_width/2)+10,260,100,50,GOLD,GRAY,level4)
        button("Level 5",(display_width/2)-110,320,100,50,GOLD,GRAY,level5)
        button("Level 6",(display_width/2)+10,320,100,50,GOLD,GRAY,level6)
        button("Level 7",(display_width/2)-110,380,100,50,GOLD,GRAY,level7)
        button("Take me back, I don't want to be amazing",0,0,400,40,WHITE,GRAY,game_welcome)
        #button("Level 3",(display_width/2)-50,380,100,50,GREEN,RED,level3)
        #button("Quit",550,450,100,50,red,bright_red,quitgame)
        '''
        pygame.display.update()
        clock.tick(15)



def stage1():
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(WHITE)

        img = pygame.image.load("bgg.png")                
        screen.blit(img, (0, 0))

        largeText = pygame.font.SysFont("freesans",50)
        TextSurf, TextRect = text_objects("Stage 1", largeText,GOLD)
        TextRect.center = ((display_width/2),120)
        screen.blit(TextSurf, TextRect)

        button("Back",0,0,80,40,WHITE,GRAY,game_intro)

        button("Tutorial ",(display_width/2)-110,200,100,50,GOLD,GRAY,stage1_tut)
        button("Level 1",(display_width/2)+10,200,100,50,GOLD,GRAY,level2)
        button("Level 2",(display_width/2)-110,260,100,50,GOLD,GRAY,level3)
        button("Level 3",(display_width/2)+10,260,100,50,GOLD,GRAY,level4)

        pygame.display.update()
        clock.tick(15)

def stage2():
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(WHITE)

        img = pygame.image.load("bgg3.png")                
        screen.blit(img, (0, 0))

        largeText = pygame.font.SysFont("freesans",50)
        TextSurf, TextRect = text_objects("Stage 2", largeText,GOLD)
        TextRect.center = ((display_width/2),120)
        screen.blit(TextSurf, TextRect)

        button("Back",0,0,80,40,WHITE,GRAY,game_intro)

        button("Tutorial ",(display_width/2)-110,200,100,50,GOLD,GRAY,stage2_tut)
        button("Level 1",(display_width/2)+10,200,100,50,GOLD,GRAY,level5)
        button("Level 2",(display_width/2)-110,260,100,50,GOLD,GRAY,level6)
        button("Level 3",(display_width/2)+10,260,100,50,GOLD,GRAY,level7)

        pygame.display.update()
        clock.tick(15)

def stage3():
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(WHITE)
        largeText = pygame.font.SysFont("freesans",50)
        TextSurf, TextRect = text_objects("Stage 3", largeText,BLACK)
        TextRect.center = ((display_width/2),120)
        screen.blit(TextSurf, TextRect)

        button("Back",0,0,80,40,WHITE,GRAY,game_intro)

        button("Tutorial ",(display_width/2)-110,200,100,50,GOLD,GRAY,level1)
        button("Level 1",(display_width/2)+10,200,100,50,GOLD,GRAY,level5)
        button("Level 2",(display_width/2)-110,260,100,50,GOLD,GRAY,level6)
        button("Level 3",(display_width/2)+10,260,100,50,GOLD,GRAY,level7)

        pygame.display.update()
        clock.tick(15)
 
 
# -------- Main Program Loop -----------
def getBackground():
      return pygame.image.load('background.gif'), 5

def level1():
    

        pygame.key.set_repeat(1,10)

	#Variaveis importantes 
        B=-5 #campo magnetico default
        Ex=4;
        Ey=2.;
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
				if event.key == pygame.K_UP:
					shooter_angle = shooter_angle+0.2
				elif event.key == pygame.K_DOWN:
					shooter_angle = shooter_angle-0.2
				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                elif event.key == pygame.K_b:
                                        B=-B
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

                button("Menu",0,5,50,20,GRAY,WHITE,stage1)
                """
                pygame.draw.rect(screen,GOLD,(150,15,385,30))
                font = pygame.font.SysFont("freesans", 20)
                text = font.render("Objective: Reach the red threshold!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (350,30)
                screen.blit(text, textpos)
                """

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
                textSurf, textRect = text_objects("Objective: Reach the red threshold!", smallText,BLACK)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)


		# desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                #desenhar o detector
		s.draw_detector(screen)
                
                #desenhar moleculas
                pos_sim = s.simulation(screen)

		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        """
                        hcol = 150
                        hcol2= 200
                        hcol3= 280
                        hcol4=230
                        velcol = 30
                        velcol2 = 50
                        velcol3 = 20
                        velcol4= 40

                        col_xpos = s.collisions(screen,shot,hcol,velcol)
                        col_xpos2 = s.collisions(screen,shot,hcol2,velcol2)
                        col_xpos3 = s.collisions(screen,shot,hcol3,velcol3)
                        col_xpos4 = s.collisions(screen,shot,hcol4,velcol4)
                        """
                        s.kutta(screen,shot,B,Ex,Ey)
                        
			shot = False
			col_stop = False

			pos = s.get_ball_pos()
                        vel = s.get_ball_vel()

                        if 0<vel[0]<0.5 or 0<vel[0]<0.5:
                            col_stop = True
                            victory(level1)
                       
                        if (((pos_sim[0]-10)<pos[0]<(pos_sim[0]+10)) and ((pos_sim[1]-10)<pos[1]<(pos_sim[1]+10))) or (((pos_sim[2]-10)<pos[0]<(pos_sim[2]+10)) and ((pos_sim[3]-10)<pos[1]<(pos_sim[3]+10))) or (((pos_sim[4]-10)<pos[0]<(pos_sim[4]+10)) and ((pos_sim[5]-10)<pos[1]<(pos_sim[5]+10))):

                            print "collision"

                            if ((pos_sim[0]-10)<pos[0]<(pos_sim[0]+10)) and ((pos_sim[1]-10)<pos[1]<(pos_sim[1]+10)):
                                s.col_recoil(screen, pos_sim[0], pos_sim[1],col_stop)
                                print "collision red"

                            if ((pos_sim[2]-10)<pos[0]<(pos_sim[2]+10)) and ((pos_sim[3]-10)<pos[1]<(pos_sim[3]+10)):
                                s.col_recoil(screen, pos_sim[2], pos_sim[3],col_stop)
                                print "collision blue"

                            if ((pos_sim[4]-10)<pos[0]<(pos_sim[4]+10)) and ((pos_sim[5]-10)<pos[1]<(pos_sim[5]+10)):
                                s.col_recoil(screen, pos_sim[4], pos_sim[5],col_stop)
                                print "collision green"


                        #if 120<pos[0]<600 and 80<pos[1]<350:
                            #pygame.draw.rect(screen,RED,(600,400,20,20))

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





def stage1_tut():

	pygame.key.set_repeat(1,15)

	#Variaveis importantes 
        B=-5 #campo magnetico default
        Ex=4
        Ey=0.
        vel=0
	s = shoot()


        # Criacao de cargas ########################

        c1 = elec_charge()

        ###Origem do referencial
        Ox=display_width/2
        Oy=display_height/2


        # --- Criar efectivamente as cargas no screen ######
        c1.create_charge(screen,-1000,Ox,Oy,DARK_BLUE)

        c_vec=[]
        c_vec.append(c1)

        


        #c1.create_charge(screen,1000,Ox,Oy,DARK_RED)
        #c2.create_charge(screen,-1000,Ox,Oy,DARK_BLUE)
        #c3.create_charge(screen,-2000,Ox,Oy,DARK_BLUE)



        ###############################################

	shooter_angle=0
	ball_on_screen=False



        ### flags do tutorial

        move_shooter = False #flag para saber se o user ja movimentou o shooter
        first_touch_up=False
        first_touch_down=False
        complete1 = False
        tut_complete1 = False # indica se a primeira parte do tutorial (mexer o shooter) esta completa


        shoot_particle=False
        first_shoot=False
        complete2=False
        tut_complete2=False


        charge_collision=False



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

                                    if(ball_on_screen==False and shooter_angle<1.5): # tenho de impor esta condicao porque quando a bola e disparada eu nao apago a imagem anterior para se ver a trajectoria e por isso se deixar o user mexer no shooter nessa fase, vao ficar varias imagens da posicao do shooter sobrepostas
					shooter_angle = shooter_angle+0.05	
                                    else:
                                        vel=0
                                        ball_on_screen=False #para fazer nova jogada
                                    if(first_touch_up==False and first_touch_down==False):
                                        move_shooter=True
                                        first_touch_up=True

				elif event.key == pygame.K_DOWN:

                                    if(ball_on_screen==False and shooter_angle>=0):
					shooter_angle = shooter_angle-0.05
                                    else:
                                        vel=0
                                        ball_on_screen=False #para fazer nova jogada
                                    if(first_touch_down==False and first_touch_up==False):
                                        move_shooter=True
                                        first_touch_down=True

				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                        if(first_shoot==False):
                                            shoot_particle=True
                                            first_shoot=True

                                elif event.key == pygame.K_b:
                                        B=-B
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					shooter_angle=shooter_angle
					#nao acontece nada ao angulo quando as teclas sao premidas ao mesmo tempo		

                # Set the screen background
                if ball_on_screen == False:
                    bg = pygame.image.load("bg.png") 
                    screen.blit(bg, (0, 0)) 


                if(move_shooter==False and complete1==False):

                    x=65
                    y=5
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the UP or DOWN keys to move the thrower", smallText,RED)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                    screen.blit(textSurf, textRect)


                elif move_shooter==True:
                    complete1=True


                if(complete1==True and move_shooter==True):

                    x=65
                    y=5
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the UP or DOWN keys to move the thrower", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                    screen.blit(textSurf, textRect)


                ###Depois deste if esta complete1=True e move_shooter=False para sempre (VER fim do codigo desta funcao)


                if(tut_complete1==True and complete2==False):

                    x=65
                    y=5
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the SPACE key to throw a + charge and try to hit the red threshold ", smallText,RED)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                    screen.blit(textSurf, textRect)

                                        

                #if(shoot_particle==True):
                    #complete2 = True


                if(tut_complete1==True and shoot_particle==False and complete2==True):

                    x=65
                    y=5
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the SPACE key to throw a + charge and try to hit the red threshold ", smallText,BLACK)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                    screen.blit(textSurf, textRect)

                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the SPACE key to throw a + charge and try to hit the red threshold ", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                    screen.blit(textSurf, textRect)



                button("Menu",0,5,50,20,GRAY,WHITE,stage1)


                if(tut_complete1==True and tut_complete2==True):
                    tutorial_sucess(stage1_tut,stage1)

                ##Informacao sobre o angulo de inclinacao
                """
                pygame.draw.rect(screen,AQUA,(display_width/2+100,15,300,30))
                font = pygame.font.SysFont("freesans", 20)
                info_shooter_angle= "Angle: " + str(shooter_angle)
                text = font.render(info_shooter_angle, 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (display_width/2+200,30)
                screen.blit(text, textpos)
                """

                ###Origem do referencial
                Ox=display_width/2
                Oy=display_height/2


		# --- Criar efectivamente as cargas no screen ######
                c1.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(30))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c1.get_pos()[0]),(c1.get_pos()[1]))
                screen.blit(text, textpos)
                

		# Desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                # Desenhar patamar 
                pos_patamar=(Ox+220,Oy-20)
                width_patamar=50
		pygame.draw.rect(screen,RED,(pos_patamar[0],pos_patamar[1],width_patamar,2))


                ###VER ISTO!!!!!###############
                """
                if ball_on_screen==False:
                    pos = s.get_ball_pos()
                    prev_pos=(pos[0],pos[1])
                    print prev_pos
                """		

		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        #s.kutta(screen,shot,B,Ex,Ey)
                    
                        vel = 10

                        s.motion_in_field(screen,shot,c_vec,vel)

			shot = False
			
			pos = s.get_ball_pos()

                        # verificar se a bola acertou no patamar pretendido
                        if pos_patamar[0]<pos[0]<pos_patamar[0]+width_patamar and pos_patamar[1]-2<pos[1]<pos_patamar[1]+2:
                            complete2=True
                            #victory(level2)


                        #Verificar se a bola colide com as cargas
                        
                        pos_c1 = c1.get_pos()
                        r1 = c1.get_radius()
    

                        # verificar se a bola esta dentro do ecra  
			if 0<pos[0]< display_width and  0<pos[1]<display_height: 
				ball_on_screen=True
			else:
				ball_on_screen=False


                        if pos_c1[0]-r1<pos[0]<pos_c1[0]+r1 and pos_c1[1]-r1<pos[1]<pos_c1[1]+r1:
                            ball_on_screen=False#defeat(level2)

                            x=display_width/2 - 300
                            y=display_height/2-80
                            rad=7
                            w=620
                            h=30
                        
                            smallText = pygame.font.SysFont("freesans",20)
                            #smallText = pygame.font.SysFont("Verdana",20)
                            textSurf, textRect = text_objects("You have to avoid colliding with the - charge!", smallText,RED)
                            textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                            screen.blit(textSurf, textRect)

                            charge_collision=True

                        

 
		# --- Wrap-ups
		# Limit to 180 frames per second
		clock.tick(180)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()


                if(complete1==True and move_shooter==True):
                    move_shooter=False
                    tut_complete1 = True # primeira parte do tutorial completa
                    time.sleep(0.5)


                if(complete2==True and shoot_particle==True):
                    shoot_particle=False
                    time.sleep(0.5)

                if(tut_complete1==True and shoot_particle==False and complete2==True):
                    tut_complete2=True

                if charge_collision==True:
                    time.sleep(2) #para mostrar a mensagem de que nao se pode colidir com a carga -
                    charge_collision=False




def level2():

	pygame.key.set_repeat(1,15)

	#Variaveis importantes 
        B=-5 #campo magnetico default
        Ex=4
        Ey=0.
        vel=0
	s = shoot()


        # Criacao de cargas ########################

        c1 = elec_charge()
        c2 = elec_charge()
        c3 = elec_charge()

        ###Origem do referencial
        Ox=display_width/2
        Oy=display_height/2


        # --- Criar efectivamente as cargas no screen ######
        c1.create_charge(screen,1000,Ox,Oy-100,DARK_RED)
        c2.create_charge(screen,-1000,Ox-100,Oy+100,DARK_BLUE)
        c3.create_charge(screen,-2000,Ox+200,Oy-20,DARK_BLUE)

        c_vec=[]
        c_vec.append(c1)
        c_vec.append(c2)
        c_vec.append(c3)

        


        #c1.create_charge(screen,1000,Ox,Oy,DARK_RED)
        #c2.create_charge(screen,-1000,Ox,Oy,DARK_BLUE)
        #c3.create_charge(screen,-2000,Ox,Oy,DARK_BLUE)



        ###############################################

        n_tries=0 #para contar o nr de tentativas do user
	shooter_angle=0
	ball_on_screen=False

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

                                    if(ball_on_screen==False and shooter_angle<1.5): # tenho de impor esta condicao porque quando a bola e disparada eu nao apago a imagem anterior para se ver a trajectoria e por isso se deixar o user mexer no shooter nessa fase, vao ficar varias imagens da posicao do shooter sobrepostas
					shooter_angle = shooter_angle+0.05	
                                    else:
                                        vel=0
                                        n_tries=n_tries+1
                                        ball_on_screen=False #para fazer nova jogada

				elif event.key == pygame.K_DOWN:

                                    if(ball_on_screen==False and shooter_angle>=0):
					shooter_angle = shooter_angle-0.05
                                    else:
                                        vel=0
                                        n_tries=n_tries+1
                                        ball_on_screen=False #para fazer nova jogada
				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                elif event.key == pygame.K_b:
                                        B=-B
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					shooter_angle=shooter_angle
					#nao acontece nada ao angulo quando as teclas sao premidas ao mesmo tempo		


                # Set the screen background
                if ball_on_screen == False:
                    bg = pygame.image.load("bg.png") 
                    screen.blit(bg, (0, 0)) 


                button("Menu",0,5,50,20,GRAY,WHITE,stage1)
                """
                pygame.draw.rect(screen,GOLD,(150,15,385,30))
                font = pygame.font.SysFont("freesans", 20)
                text = font.render("Objective: Reach the red threshold!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (350,30)
                screen.blit(text, textpos)
                """

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
                textSurf, textRect = text_objects("Objective: Reach the red threshold!", smallText,BLACK)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)





                ##Informacao sobre o angulo de inclinacao
                """
                pygame.draw.rect(screen,AQUA,(display_width/2+100,15,300,30))
                font = pygame.font.SysFont("freesans", 20)
                info_shooter_angle= "Angle: " + str(shooter_angle)
                text = font.render(info_shooter_angle, 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (display_width/2+200,30)
                screen.blit(text, textpos)
                """

                ###Origem do referencial
                Ox=display_width/2
                Oy=display_height/2


		# --- Criar efectivamente as cargas no screen ######
                c1.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(20))
                text = font.render("+", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c1.get_pos()[0]),(c1.get_pos()[1]-3))
                screen.blit(text, textpos)
                

                c2.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(30))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c2.get_pos()[0]),(c2.get_pos()[1]))
                screen.blit(text, textpos)

                c3.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(50))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c3.get_pos()[0]),(c3.get_pos()[1]))
                screen.blit(text, textpos)

                c_vec=[]
                c_vec.append(c1)
                c_vec.append(c2)
                c_vec.append(c3)
                ####################################################

		# Desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                # Desenhar patamar 
                pos_patamar=(Ox+270,Oy-20)
                width_patamar=20
		pygame.draw.rect(screen,RED,(pos_patamar[0],pos_patamar[1],width_patamar,2))


                ###VER ISTO!!!!!###############
                """
                if ball_on_screen==False:
                    pos = s.get_ball_pos()
                    prev_pos=(pos[0],pos[1])
                    print prev_pos
                """		

		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        #s.kutta(screen,shot,B,Ex,Ey)
                    
                        vel = 10

                        s.motion_in_field(screen,shot,c_vec,vel)

			shot = False
			
			pos = s.get_ball_pos()

                        # verificar se a bola acertou no patamar pretendido
                        if pos_patamar[0]<pos[0]<pos_patamar[0]+width_patamar and pos_patamar[1]-2<pos[1]<pos_patamar[1]+2:
                            victory(level2)

                        # verificar as tentativas efectuadas
                        if(n_tries==3):
                            defeat(level2)

                        #Verificar se a bola colide com as cargas
                        
                        pos_c1 = c1.get_pos()
                        r1 = c1.get_radius()
                        pos_c2 = c2.get_pos()
                        r2 = c2.get_radius()
                        pos_c3 = c3.get_pos()
                        r3 = c3.get_radius()
    
                        
                        if((pos_c1[0]-r1<pos[0]<pos_c1[0]+r1 and pos_c1[1]-r1<pos[1]<pos_c1[1]+r1) or (pos_c2[0]-r2<pos[0]<pos_c2[0]+r2 and pos_c2[1]-r2<pos[1]<pos_c2[1]+r2) or (pos_c3[0]-r3<pos[0]<pos_c3[0]+r3 and pos_c3[1]-r3<pos[1]<pos_c3[1]+r3)):
                            defeat(level2)
                        

			
                        # verificar se a bola esta dentro do ecra  
			if 0<pos[0]< display_width and  0<pos[1]<display_height: 
				ball_on_screen=True
			else:
                                n_tries = n_tries+1
				ball_on_screen=False
 
		# --- Wrap-ups
		# Limit to 180 frames per second
		clock.tick(180)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()





def level3():

        pygame.key.set_repeat(1,10)

	#Variaveis importantes 
        B=-5 #campo magnetico default
        Ex=4
        Ey=0.
        vel=0
	s = shoot()
	shooter_angle=0
	ball_on_screen=False
        global pause
        up = False

        c1 = elec_charge()
        c2 = elec_charge()
        c3 = elec_charge()

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

                                    if(ball_on_screen==False and shooter_angle<1.5): # tenho de impor esta condicao porque quando a bola e disparada eu nao apago a imagem anterior para se ver a trajectoria e por isso se deixar o user mexer no shooter nessa fase, vao ficar varias imagens da posicao do shooter sobrepostas
					shooter_angle = shooter_angle+0.05	
                                    else:
                                        vel=0
                                        ball_on_screen=False #para fazer nova jogada

				elif event.key == pygame.K_DOWN:

                                    if(ball_on_screen==False and shooter_angle>=0):
					shooter_angle = shooter_angle-0.05
                                    else:
                                        vel=0
                                        ball_on_screen=False #para fazer nova jogada
				elif event.key == pygame.K_SPACE:
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
                if ball_on_screen == False:
                    bg = pygame.image.load("bg.png")                
                    screen.blit(bg, (0, 0))

                button("Menu",0,5,50,20,GRAY,WHITE,stage1)
                """
                pygame.draw.rect(screen,GOLD,(150,15,385,30))
                font = pygame.font.SysFont("freesans", 20)
                text = font.render("Objective: Reach the red threshold!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (350,30)
                screen.blit(text, textpos)
                """

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
                textSurf, textRect = text_objects("Objective: Reach the red threshold!", smallText,BLACK)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

		# desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                # Desenhar patamar 
		pygame.draw.rect(screen,RED,(display_width/2,display_height/2-20,20,2))

                #criar e desenhar cargas
                c1.create_charge(screen,800,display_width/2-150,display_height/2-20,DARK_RED)
                font = pygame.font.SysFont("freesans", 25)
                text = font.render("+", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((display_width/2-151),(display_height/2-23))
                screen.blit(text, textpos)
                
                c2.create_charge(screen,1000,display_width/2+200,display_height/2-180,DARK_RED)
                font = pygame.font.SysFont("freesans", 25)
                text = font.render("+", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((display_width/2+200),(display_height/2-185))
                screen.blit(text, textpos)
                
                c3.create_charge(screen,-1200,display_width/2+100,display_height/2+100,DARK_BLUE)
                font = pygame.font.SysFont("freesans", 25)
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((display_width/2+100),(display_height/2+100))
                screen.blit(text, textpos)
                
                c_vec=[]
                c_vec.append(c1)
                c_vec.append(c2)
                c_vec.append(c3)

		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        
                        vel = 10
                        s.motion_in_field(screen,shot,c_vec,vel)

			shot = False
			
			pos = s.get_ball_pos()                        

                        if display_width/2-20<pos[0]<display_width/2+20 and display_height/2-21<pos[1]<display_height/2 - 19:
                            victory(level3)                      
                        

                        #Verificar se a bola colide com as cargas
                        
                        pos_c1 = c1.get_pos()
                        r1 = c1.get_radius()
                        pos_c2 = c2.get_pos()
                        r2 = c2.get_radius()
                        pos_c3 = c3.get_pos()
                        r3 = c3.get_radius()
    
                        
                        if((pos_c1[0]-r1<pos[0]<pos_c1[0]+r1 and pos_c1[1]-r1<pos[1]<pos_c1[1]+r1) or (pos_c2[0]-r2<pos[0]<pos_c2[0]+r2 and pos_c2[1]-r2<pos[1]<pos_c2[1]+r2) or (pos_c3[0]-r3<pos[0]<pos_c3[0]+r3 and pos_c3[1]-r3<pos[1]<pos_c3[1]+r3)):
                            defeat(level3)




                        #Verificar se a bola colide com as cargas
                        
                        pos_c1 = c1.get_pos()
                        r1 = c1.get_radius()
                        pos_c2 = c2.get_pos()
                        r2 = c2.get_radius()
                        pos_c3 = c3.get_pos()
                        r3 = c3.get_radius()
    
                        
                        if((pos_c1[0]-r1<pos[0]<pos_c1[0]+r1 and pos_c1[1]-r1<pos[1]<pos_c1[1]+r1) or (pos_c2[0]-r2<pos[0]<pos_c2[0]+r2 and pos_c2[1]-r2<pos[1]<pos_c2[1]+r2) or (pos_c3[0]-r3<pos[0]<pos_c3[0]+r3 and pos_c3[1]-r3<pos[1]<pos_c3[1]+r3)):
                            defeat(level3)



                           
			if 0<pos[0]< display_width and  0<pos[1]<display_height:
				ball_on_screen=True
			else:
				ball_on_screen=False
                                defeat(level3)
 

		# --- Wrap-ups
		# Limit to 180 frames per second
		clock.tick(180)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()






def level4():

	pygame.key.set_repeat(1,10)

	#Variaveis importantes 
        Ex=4
        Ey=0.
        vel=0
	s = shoot()





        time=0


        # Criacao de cargas ########################

        c1 = elec_charge()
        c2 = elec_charge()
        c3 = elec_charge()

        c2.create_charge(screen,800,display_width/2-150,display_height/2-100,DARK_RED)
        c1.create_charge(screen,-1000,display_width/2-200,display_height/2+100,DARK_BLUE)
        c3.create_charge(screen,-3000,display_width/2+100,display_height/2-20,DARK_BLUE)


        ###############################################

	shooter_angle=0
	ball_on_screen=False
        second_shoot=False

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

                                    if(ball_on_screen==False and shooter_angle<1.5): # tenho de impor esta condicao porque quando a bola e disparada eu nao apago a imagem anterior para se ver a trajectoria e por isso se deixar o user mexer no shooter nessa fase, vao ficar varias imagens da posicao do shooter sobrepostas
					shooter_angle = shooter_angle+0.02	
                                    else:
                                        vel=0
                                        ball_on_screen=False #para fazer nova jogada

				elif event.key == pygame.K_DOWN:

                                    if(ball_on_screen==False and shooter_angle>=0):
					shooter_angle = shooter_angle-0.02
                                    else:
                                        vel=0
                                        ball_on_screen=False #para fazer nova jogada
				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                        second_shoot=True
                                elif event.key == pygame.K_b:
                                        B=-B
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					shooter_angle=shooter_angle
					#nao acontece nada ao angulo quando as teclas sao premidas ao mesmo tempo		


                # Set the screen background

                if ball_on_screen == False:
                    screen.fill(BLACK)

                if second_shoot == True:
                    screen.fill(BLACK)
                    second_shoot=False
                    


  
                button("Menu",0,5,50,20,GRAY,WHITE,stage1)
                """
                pygame.draw.rect(screen,GOLD,(150,15,385,30))
                font = pygame.font.SysFont("freesans", 20)
                text = font.render("Objective: Reach the red threshold!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (350,30)
                screen.blit(text, textpos)
                """

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
                textSurf, textRect = text_objects("Objective: Reach the red threshold!", smallText,BLACK)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)




                ###E dificil com o background porque temos de apagar a carga anterior RESOLVER!!!!
                #if ball_on_screen == False:)
                    #bg = pygame.image.load("bg.png")               
                    #screen.blit(bg, (0, 0))



		# --- Criar efectivamente as cargas no screen ######

                c1.erase_charge(screen)

                font = pygame.font.SysFont("freesans", 30)
                text = font.render("-", 1, BLACK)
                textpos = text.get_rect()
                c1_pos=c1.get_pos()
                textpos.center = c1_pos
                screen.blit(text, textpos)

                ##mover a carga
                x = 180*cos(time)
                c1.set_pos(100,250+x)
                # Desenhar a carga e o sinal - depois de movidos
                c1.draw_charge(screen)
                
                time+=0.005

                font = pygame.font.SysFont("freesans", 30)
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                c1_pos=c1.get_pos()
                textpos.center = c1_pos
                screen.blit(text, textpos)


                #######A carga c2 esta agora em movimento!!!############################################################################
                #apagar o desenho da carga anterior e da fonte(sinal -)
                c2.erase_charge(screen)

                font = pygame.font.SysFont("freesans", 20)
                text = font.render("+", 1, BLACK)
                textpos = text.get_rect()
                c2_pos=c2.get_pos()
                textpos.center = c2_pos
                screen.blit(text, textpos)
                
                ##mover a carga
                c2.set_pos(300,250-x)
                # Desenhar a carga e o sinal - depois de movidos
                c2.draw_charge(screen)
                
                font = pygame.font.SysFont("freesans", 20)
                text = font.render("+", 1, WHITE)
                textpos = text.get_rect()
                c2_pos=c2.get_pos()
                textpos.center = c2_pos
                screen.blit(text, textpos)
                
                #verificar se a carga em movimento sai do ecra. Se sair, o jogador perde
                if 0<c2_pos[0]< display_width and  0<c2_pos[1]<display_height: 
                    c2_pos=c2_pos # So para ter alguma coisa no if, nao faz nada, pode continuar
                else:
                    #quer dizer que esta fora do ecra e nao pode continuar
                    defeat(level4)

                ########################################################################################################################
            
                c3.erase_charge(screen)

                font = pygame.font.SysFont("freesans", 30)
                text = font.render("-", 1, BLACK)
                textpos = text.get_rect()
                c3_pos=c3.get_pos()
                textpos.center = c3_pos
                screen.blit(text, textpos)
                
                ##mover a carga
                c3.set_pos(500,250+x)
                # Desenhar a carga e o sinal - depois de movidos
                c3.draw_charge(screen)
                
                font = pygame.font.SysFont("freesans", 30)
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                c3_pos=c3.get_pos()
                textpos.center = c3_pos
                screen.blit(text, textpos)
                ####################################################




                c_vec=[]
                c_vec.append(c1)
                c_vec.append(c2)
                c_vec.append(c3)







		# Desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                # Desenhar patamar 
		pygame.draw.rect(screen,RED,(display_width/2+230,display_height/2-20,20,2))


		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        #s.kutta(screen,shot,B,Ex,Ey)
                    
                        vel = 10 # mudar depois para tornar interativo
                        s.motion_in_field(screen,shot,c_vec,vel)

			shot = False
			
			pos = s.get_ball_pos()

                        # verificar se a bola acertou no patamar pretendido
                        if display_width/2+230<pos[0]<display_width/2+250 and display_height/2-22<pos[1]<display_height/2-20:
                            victory(level4)
                        

                        #Verificar se a bola colide com as cargas
                        
                        pos_c1 = c1.get_pos()
                        r1 = c1.get_radius()
                        pos_c2 = c2.get_pos()
                        r2 = c2.get_radius()
                        pos_c3 = c3.get_pos()
                        r3 = c3.get_radius()
    
                        
                        if((pos_c1[0]-r1<pos[0]<pos_c1[0]+r1 and pos_c1[1]-r1<pos[1]<pos_c1[1]+r1) or (pos_c2[0]-r2<pos[0]<pos_c2[0]+r2 and pos_c2[1]-r2<pos[1]<pos_c2[1]+r2) or (pos_c3[0]-r3<pos[0]<pos_c3[0]+r3 and pos_c3[1]-r3<pos[1]<pos_c3[1]+r3)):
                            defeat(level4)


			
                        # verificar se a bola esta dentro do ecra  
			if 0<pos[0]< display_width and  0<pos[1]<display_height: 
				ball_on_screen=True
			else:
				ball_on_screen=False
 
		# --- Wrap-ups
		# Limit to 180 frames per second
		clock.tick(180)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()




def stage2_tut():

	pygame.key.set_repeat(1,15)

	s = shoot()


        # Criacao de cargas ########################

        c1 = elec_charge()
        c2 = elec_charge()
        c3 = elec_charge()
        c4 = elec_charge()

        ###Origem do referencial
        Ox=display_width/2
        Oy=display_height/2


        # --- Criar efectivamente as cargas no screen ######
        c1.create_charge(screen,-700,Ox-100,Oy-160,DARK_BLUE)
        c2.create_charge(screen,-700,Ox,Oy+150,DARK_BLUE)
        c3.create_charge(screen,-700,Ox+180,Oy-100,DARK_BLUE)
        #c4.create_charge(screen,3000,Ox,Oy,RED)

        c1_pos=c1.get_pos()
        c2_pos=c2.get_pos()
        c3_pos=c3.get_pos()
        #c4_pos=c4.get_pos()

        c_vec=[]
        c_vec.append(c1)
        c_vec.append(c2)
        c_vec.append(c3)



        ###############################################

        counter=0 #conta as colisoes que houve, quando chega a 3 o jogador ganha
        theta = 0.1 ## angulo da onda difundida, inicializa-se a 0.1 para evitar problemas de infinitos

        ####Parametros relativos as trajectorias das cargas
        theta1=0
        theta2=0
        theta3=0
        f_in1=True
        f_in2=True
        f_in3=True
        aux_ang=0
        fi=0
        v_c=0


        n_tries=0 #para contar o nr de tentativas do user
	shooter_angle=0
	ball_on_screen=False

        c1_move=False ##indica se a carga c1 se esta a movimentar
        c2_move=False
        c3_move=False
        collision=False ## da-me informacao sobre se esta ou nao a haver colisao entre fotao e eletrao
        first_entrance=True #Variavel auiliar para definir a trajectoria do fotao apos o choque
        first_entrance2=True

        ##translacoes necessarias para definir a trajectoria do fotao apos a colisao
        transx = 0
        transy = 0



        ### flags do tutorial

        move_shooter = False #flag para saber se o user ja movimentou o shooter
        first_touch_up=False
        first_touch_down=False
        complete1 = False
        tut_complete1 = False # indica se a primeira parte do tutorial (mexer o shooter) esta completa


        shoot_particle=False
        first_shoot=False
        complete2=False
        tut_complete2=False


        shoot_charge=False
        first_charge_shoot=False
        complete3=False
        tut_complete3=False




	# Loop until the user clicks the close button.
	done = False
	while not done:


                # Set the screen background
                bg = pygame.image.load("bg.png") 
                screen.blit(bg, (0, 0))  



		# --- Event Processing
		for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()	

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_UP:

                                    if(ball_on_screen==False and shooter_angle<1.5): # tenho de impor esta condicao porque quando a bola e disparada eu nao apago a imagem anterior para se ver a trajectoria e por isso se deixar o user mexer no shooter nessa fase, vao ficar varias imagens da posicao do shooter sobrepostas
					shooter_angle = shooter_angle+0.05	
                                    else:
                                        vel=0
                                        n_tries=n_tries+1
                                        ball_on_screen=False #para fazer nova jogada
                                    collision=False
                                    if(first_touch_up==False and first_touch_down==False):
                                        move_shooter=True
                                        first_touch_up=True

				elif event.key == pygame.K_DOWN:

                                    if(ball_on_screen==False and shooter_angle>=0):
					shooter_angle = shooter_angle-0.05
                                    else:
                                        vel=0
                                        n_tries=n_tries+1
                                        ball_on_screen=False #para fazer nova jogada
                                    collision=False
                                    if(first_touch_down==False and first_touch_up==False):
                                        move_shooter=True
                                        first_touch_down=True


				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                        s.reset_wavepos() #para que a posicao inicial da onda nao seja a do tiro anterior
                                        transx=0
                                        transy=0
                                        collision=False

                                        if(first_shoot==False):
                                            shoot_particle=True
                                            first_shoot=True

                                elif event.key == pygame.K_b:
                                        B=-B

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					shooter_angle=shooter_angle
					#nao acontece nada ao angulo quando as teclas sao premidas ao mesmo tempo	


                if(move_shooter==False and complete1==False):

                    x=65
                    y=5
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the UP or DOWN keys to move the thrower", smallText,RED)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                    screen.blit(textSurf, textRect)


                elif move_shooter==True:
                    complete1=True

                if(complete1==True and move_shooter==True):

                    x=65
                    y=5
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the UP or DOWN keys to move the thrower", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                    screen.blit(textSurf, textRect)


                ###Depois deste if esta complete1=True e move_shooter=False para sempre (VER fim do codigo desta funcao)


                if(tut_complete1==True and complete2==False and shoot_particle==False):

                    x=65
                    y=5
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the SPACE key to throw a photon", smallText,RED)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                    screen.blit(textSurf, textRect)

                                        

                if(shoot_particle==True):
                    complete2 = True


                if(tut_complete1==True and shoot_particle==True and complete2==True):
                    x=65
                    y=5
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Hit the SPACE key to throw a photon", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                    screen.blit(textSurf, textRect)


                ###Depois deste if esta complete2=True e shoot_particle=False para sempre (VER fim do codigo desta funcao)

                if(collision==True and first_charge_shoot==False):
                    shoot_charge=True
                    first_charge_shoot=True


                if(tut_complete1==True and tut_complete2==True and shoot_charge==False and tut_complete3 == False):


                    x=65
                    y=5
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Finally, try to hit any charge!", smallText,RED)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                    screen.blit(textSurf, textRect)

                

                if (c3.get_pos()[0]<-8 or c3.get_pos()[0] > display_width+8 or  c3.get_pos()[1]<-8 or c3.get_pos()[1] > display_height+8) or (c2.get_pos()[0]<-8 or c2.get_pos()[0] > display_width+8 or  c2.get_pos()[1]<-8 or c2.get_pos()[1] > display_height+8) or (c1.get_pos()[0]<-8 or c1.get_pos()[0] > display_width+8 or c1.get_pos()[1]<-8 or c1.get_pos()[1] > display_height+8):
                    shoot_charge=False
                    tut_complete3=True


                if(tut_complete1==True and tut_complete2==True and complete3==True and shoot_charge==True):


                    x=65
                    y=5
                    rad=7
                    w=620
                    h=30
                        
                    smallText = pygame.font.SysFont("freesans",20)
                    #smallText = pygame.font.SysFont("Verdana",20)
                    textSurf, textRect = text_objects("Finally, try to hit any charge!", smallText,GREEN)
                    textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                    screen.blit(textSurf, textRect)


                if(tut_complete1==True and tut_complete2==True and tut_complete3==True):
                    tutorial_sucess(stage2_tut,stage2)


                button("Menu",0,5,50,20,GRAY,WHITE,stage2)


                ##Informacao sobre o angulo de inclinacao
                #pygame.draw.rect(screen,AQUA,(display_width/2+100,15,300,30))
                #font = pygame.font.SysFont("freesans", 20)
                #info_shooter_angle= "Angle: " + str(shooter_angle)
                #text = font.render(info_shooter_angle, 1, BLACK)
                #textpos = text.get_rect()
                #textpos.center = (display_width/2+200,30)
                #screen.blit(text, textpos)

                ###Origem do referencial
                Ox=display_width/2
                Oy=display_height/2


		# --- Criar efectivamente as cargas no screen ######
                c1.draw_charge(screen)
                c2.draw_charge(screen)
                c3.draw_charge(screen)
                #c4.draw_charge(screen)


                c_vec=[]
                c_vec.append(c1)
                c_vec.append(c2)
                c_vec.append(c3)
                #c_vec.append(c4)
                ####################################################

		# Desenhar o shooter
		s.draw_shooter(screen,shooter_angle)



                ###VER ISTO!!!!!###############
                """
                if ball_on_screen==False:
                    pos = s.get_ball_pos()
                    prev_pos=(pos[0],pos[1])
                    print prev_pos
                """		

                eta = 2
                k=0.2 ## nr de onda da onda incidente 
                w=1.5 ## frequencia da onda incidente


		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        #s.kutta(screen,shot,B,Ex,Ey)

			shot = False


			pos = s.get_wave_pos()#posicao da onda

                        # verificar se a onda esta dentro do ecra  
			#if 0<pos[0]< display_width and  0<pos[1]<display_height: 
			#	ball_on_screen=True
			#else:
			#	ball_on_screen=False


                        
                        c1_pos=c1.get_pos()
                        c2_pos=c2.get_pos()
                        c3_pos=c3.get_pos()
                        #c4_pos=c4.get_pos()

                        color_test = s.get_wave_color()


                        if c1_pos[0]-10<pos[0]<c1_pos[0]+10 and c1_pos[1]-10<pos[1]<c1_pos[1]+10 and first_entrance2==True and color_test==(0,0,255):

                            c1_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel
                            first_entrance=True
                            first_entrance2=False


                        if c2_pos[0]-10<pos[0]<c2_pos[0]+10 and c2_pos[1]-10<pos[1]<c2_pos[1]+10 and first_entrance2==True and color_test==(0,0,255):

                            c2_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel
                            first_entrance=True
                            first_entrance2=False


                        if c3_pos[0]-10<pos[0]<c3_pos[0]+10 and c3_pos[1]-10<pos[1]<c3_pos[1]+10 and first_entrance2==True and color_test==(0,0,255):

                            c3_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel
                            first_entrance=True
                            first_entrance2=False


                        #####NAO QUERO QUE O PROGRAMA ANDE A ENTRAR MAIS QUE UMA VEZ NOS IFS ANTERIORES!!!!!!!!!


                        if (c1_pos[0]-10<pos[0]<c1_pos[0]+10 and c1_pos[1]-10<pos[1]<c1_pos[1]+10) or ( c2_pos[0]-10<pos[0]<c2_pos[0]+10 and c2_pos[1]-10<pos[1]<c2_pos[1]+10) or (c3_pos[0]-10<pos[0]<c3_pos[0]+10 and c3_pos[1]-10<pos[1]<c3_pos[1]+10):
                            first_entrance2=False
                        else:
                            first_entrance2=True



                        if(collision==False):
                            angle = s.get_sh_angle() #angulo da trajectoria da onda
                        if(collision==True and first_entrance==True and color_test == (0,0,255)):
                            theta=0.7
                            angle = s.get_sh_angle()+theta

                            ##translacao necessaria para definir a trajectoria apos colisao
                            col_coord=s.get_wave_before_rot()#coordenada x do ponto onde se da a colisao, antes de ser rodado
                            step=s.get_pos_step()#IMPORTANTE!!

                            transx = (col_coord)*cos(s.get_sh_angle())-col_coord*cos(angle)
                            transy = (col_coord)*sin(s.get_sh_angle())-col_coord*sin(angle)

                            counter+=1
                            first_entrance=False


                        s.wave_motion(screen,shot,transx,transy,k,w,angle,theta,eta)

			

                        # verificar se a onda esta dentro do ecra  
			if 0<=pos[0]<= display_width and  0<=pos[1]<=display_height: 
				ball_on_screen=True
			else:
                                #n_tries = n_tries+1
				ball_on_screen=False





                ####MOVIMENTO DAS CARGAS - verifica-se tambem quando estas saem da tela para parar o movimento
 

                ##Movimento depois da colisao
                if c1_move==True and -8<c1.get_pos()[0]< display_width+8 and  -8<c1.get_pos()[1]<display_height+8: 
                    if(collision==True and f_in1==True):
                        theta1 = theta
                        aux_ang=s.get_sh_angle()
                        f_in1=False

                    fi = aux_ang-atan(2/((1+eta)*tan(theta1)))
                    v_c = sqrt(2*eta*eta*(1-cos(theta1))/(1+eta*(1-cos(theta1))))*w/k 
                    c1.move_charge(v_c*cos(fi),-v_c*sin(fi))
                else:
                    f_in1=True


                        
                if c2_move==True and -8<c2.get_pos()[0]< display_width+8 and  -8<c2.get_pos()[1]<display_height+8: 
                    if(collision==True and f_in2==True):
                        theta2 = theta
                        aux_ang=s.get_sh_angle()
                        f_in2=False

                    fi = aux_ang-atan(2/((1+eta)*tan(theta2)))
                    v_c = sqrt(2*eta*eta*(1-cos(theta2))/(1+eta*(1-cos(theta2))))*w/k 
                    c2.move_charge(v_c*cos(fi),-v_c*sin(fi))
                else:
                    f_in2=True



                if c3_move==True and -8<c3.get_pos()[0]< display_width+8 and  -8<c3.get_pos()[1]<display_height+8: 
                    if(collision==True and f_in3==True):
                        theta3 = theta
                        aux_ang=s.get_sh_angle()
                        f_in3=False

                    fi = aux_ang-atan(2/((1+eta)*tan(theta3)))
                    v_c = sqrt(2*eta*eta*(1-cos(theta3))/(1+eta*(1-cos(theta3))))*w/k 
                    c3.move_charge(v_c*cos(fi),-v_c*sin(fi))
                else:
                    f_in3=True

 

		# --- Wrap-ups
		# Limit to 180 frames per second
		clock.tick(180)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

                if(complete1==True and move_shooter==True):
                    move_shooter=False
                    tut_complete1 = True # primeira parte do tutorial completa
                    time.sleep(0.5)


                if(complete2==True and shoot_particle==True):
                    shoot_particle=False
                    tut_complete2=True
                    time.sleep(0.5)



                if(shoot_charge==True):
                    complete3=True



def level5():

	pygame.key.set_repeat(1,15)

	s = shoot()


        # Criacao de cargas ########################

        c1 = elec_charge()
        c2 = elec_charge()
        c3 = elec_charge()
        c4 = elec_charge()

        ###Origem do referencial
        Ox=display_width/2
        Oy=display_height/2


        # --- Criar efectivamente as cargas no screen ######
        c1.create_charge(screen,-700,Ox-100,Oy-180,DARK_BLUE)
        c2.create_charge(screen,-700,Ox,Oy+200,DARK_BLUE)
        c3.create_charge(screen,-700,Ox+220,Oy-100,DARK_BLUE)
        c4.create_charge(screen,3000,Ox,Oy,RED)

        c1_pos=c1.get_pos()
        c2_pos=c2.get_pos()
        c3_pos=c3.get_pos()
        c4_pos=c4.get_pos()

        c_vec=[]
        c_vec.append(c1)
        c_vec.append(c2)
        c_vec.append(c3)



        ###############################################

        counter=0 #conta as colisoes que houve, quando chega a 3 o jogador ganha
        theta = 0.1 ## angulo da onda difundida, inicializa-se a 0.1 para evitar problemas de infinitos

        ####Parametros relativos as trajectorias das cargas
        theta1=0
        theta2=0
        theta3=0
        f_in1=True
        f_in2=True
        f_in3=True
        aux_ang=0
        fi=0
        v_c=0


        n_tries=0 #para contar o nr de tentativas do user
	shooter_angle=0
	ball_on_screen=False

        c1_move=False ##indica se a carga c1 se esta a movimentar
        c2_move=False
        c3_move=False
        collision=False ## da-me informacao sobre se esta ou nao a haver colisao entre fotao e eletrao
        first_entrance=True #Variavel auiliar para definir a trajectoria do fotao apos o choque
        first_entrance2=True

        ##translacoes necessarias para definir a trajectoria do fotao apos a colisao
        transx = 0
        transy = 0




        tempo=0


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

                                    if(ball_on_screen==False and shooter_angle<1.5): # tenho de impor esta condicao porque quando a bola e disparada eu nao apago a imagem anterior para se ver a trajectoria e por isso se deixar o user mexer no shooter nessa fase, vao ficar varias imagens da posicao do shooter sobrepostas
					shooter_angle = shooter_angle+0.05	
                                    else:
                                        vel=0
                                        n_tries=n_tries+1
                                        ball_on_screen=False #para fazer nova jogada
                                    collision=False

				elif event.key == pygame.K_DOWN:

                                    if(ball_on_screen==False and shooter_angle>=0):
					shooter_angle = shooter_angle-0.05
                                    else:
                                        vel=0
                                        n_tries=n_tries+1
                                        ball_on_screen=False #para fazer nova jogada
                                    collision=False

				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                        s.reset_wavepos() #para que a posicao inicial da onda nao seja a do tiro anterior
                                        transx=0
                                        transy=0
                                        collision=False
                                elif event.key == pygame.K_b:
                                        B=-B
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					shooter_angle=shooter_angle
					#nao acontece nada ao angulo quando as teclas sao premidas ao mesmo tempo		


                # Set the screen background
                #if ball_on_screen == False:
                bg = pygame.image.load("bg.png") 
                screen.blit(bg, (0, 0))           



                # Explicacao do objectivo ##########################

                button("Menu",0,5,50,20,GRAY,WHITE,stage2)
                """
                pygame.draw.rect(screen,GOLD,(150,15,385,30))
                font = pygame.font.SysFont("freesans", 20)
                text = font.render("Objective: Reach the red threshold!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (350,30)
                screen.blit(text, textpos)
                """

                x=65
                y=5
                rad=7
                w=620
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
                textSurf, textRect = text_objects("Use Compton scattering to remove the electrons from the + charge field!", smallText,BLACK)
                textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                screen.blit(textSurf, textRect)


                ##Informacao sobre o angulo de inclinacao
                #pygame.draw.rect(screen,AQUA,(display_width/2+100,15,300,30))
                #font = pygame.font.SysFont("freesans", 20)
                #info_shooter_angle= "Angle: " + str(shooter_angle)
                #text = font.render(info_shooter_angle, 1, BLACK)
                #textpos = text.get_rect()
                #textpos.center = (display_width/2+200,30)
                #screen.blit(text, textpos)

                ###Origem do referencial
                Ox=display_width/2
                Oy=display_height/2


		# --- Criar efectivamente as cargas no screen ######
		# --- Criar efectivamente as cargas no screen ######
                c1.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(23))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c1.get_pos()[0]),(c1.get_pos()[1]))
                screen.blit(text, textpos)

                c2.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(23))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c2.get_pos()[0]),(c2.get_pos()[1]))
                screen.blit(text, textpos)

                c3.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(23))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c3.get_pos()[0]),(c3.get_pos()[1]))
                screen.blit(text, textpos)

                c4.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(30))
                text = font.render("+", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c4.get_pos()[0]),(c4.get_pos()[1]))
                screen.blit(text, textpos)


                c_vec=[]
                c_vec.append(c1)
                c_vec.append(c2)
                c_vec.append(c3)
                c_vec.append(c4)
                ####################################################

		# Desenhar o shooter
		s.draw_shooter(screen,shooter_angle)



                ###VER ISTO!!!!!###############
                """
                if ball_on_screen==False:
                    pos = s.get_ball_pos()
                    prev_pos=(pos[0],pos[1])
                    print prev_pos
                """		

                eta = 2
                k=0.2 ## nr de onda da onda incidente 
                w=1.5 ## frequencia da onda incidente


		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        #s.kutta(screen,shot,B,Ex,Ey)

			shot = False


			pos = s.get_wave_pos()#posicao da onda

                        # verificar se a onda esta dentro do ecra  
			#if 0<pos[0]< display_width and  0<pos[1]<display_height: 
			#	ball_on_screen=True
			#else:
			#	ball_on_screen=False


                        
                        c1_pos=c1.get_pos()
                        c2_pos=c2.get_pos()
                        c3_pos=c3.get_pos()
                        c4_pos=c4.get_pos()



                        color_test = s.get_wave_color()

                        if c1_pos[0]-10<pos[0]<c1_pos[0]+10 and c1_pos[1]-10<pos[1]<c1_pos[1]+10 and first_entrance2==True and color_test==(0,0,255):

                            c1_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel
                            first_entrance=True
                            first_entrance2=False


                        if c2_pos[0]-10<pos[0]<c2_pos[0]+10 and c2_pos[1]-10<pos[1]<c2_pos[1]+10 and first_entrance2==True and color_test==(0,0,255):

                            c2_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel
                            first_entrance=True
                            first_entrance2=False


                        if c3_pos[0]-10<pos[0]<c3_pos[0]+10 and c3_pos[1]-10<pos[1]<c3_pos[1]+10 and first_entrance2==True and color_test==(0,0,255):

                            c3_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel
                            first_entrance=True
                            first_entrance2=False


                        #####NAO QUERO QUE O PROGRAMA ANDE A ENTRAR MAIS QUE UMA VEZ NOS IFS ANTERIORES!!!!!!!!!


                        if (c1_pos[0]-10<pos[0]<c1_pos[0]+10 and c1_pos[1]-10<pos[1]<c1_pos[1]+10) or ( c2_pos[0]-10<pos[0]<c2_pos[0]+10 and c2_pos[1]-10<pos[1]<c2_pos[1]+10) or (c3_pos[0]-10<pos[0]<c3_pos[0]+10 and c3_pos[1]-10<pos[1]<c3_pos[1]+10):
                            first_entrance2=False
                        else:
                            first_entrance2=True



                        if(collision==False):
                            angle = s.get_sh_angle() #angulo da trajectoria da onda
                        if(collision==True and first_entrance==True and color_test==(0,0,255)):
                            theta=0.7
                            angle = s.get_sh_angle()+theta

                            ##translacao necessaria para definir a trajectoria apos colisao
                            col_coord=s.get_wave_before_rot()#coordenada x do ponto onde se da a colisao, antes de ser rodado
                            step=s.get_pos_step()#IMPORTANTE!!

                            transx = (col_coord)*cos(s.get_sh_angle())-col_coord*cos(angle)
                            transy = (col_coord)*sin(s.get_sh_angle())-col_coord*sin(angle)

                            counter+=1
                            first_entrance=False


                        s.wave_motion(screen,shot,transx,transy,k,w,angle,theta,eta)

			

                        # verificar se a onda esta dentro do ecra  
			if 0<=pos[0]<= display_width and  0<=pos[1]<=display_height: 
				ball_on_screen=True
			else:
                                #n_tries = n_tries+1
				ball_on_screen=False





                ####MOVIMENTO DAS CARGAS - verifica-se tambem quando estas saem da tela para parar o movimento
 

                ##Movimento antes da colisao

                #O jogador perde se um dos eletroes for completamente atraido

                c1_pos=c1.get_pos()
                c2_pos=c2.get_pos()
                c3_pos=c3.get_pos()
                c4_pos=c4.get_pos()


                delta=20
                if (c4_pos[0]-delta<c1_pos[0]<c4_pos[0]+delta and c4_pos[1]-delta<c1_pos[1]<c4_pos[1]+delta) or (c4_pos[0]-delta<c2_pos[0]<c4_pos[0]+delta and c4_pos[1]-delta<c2_pos[1]<c4_pos[1]+delta) or (c4_pos[0]-delta<c3_pos[0]<c4_pos[0]+delta and c4_pos[1]-delta<c3_pos[1]<c4_pos[1]+delta):
                    defeat(level5)





                field_lower=100

                if c1_move==False and -8<c1.get_pos()[0]< display_width+8 and  -8<c1.get_pos()[1]<display_height+8: 
                    Ec=c4.get_E_field(c1.get_pos()[0],c1.get_pos()[1])
                    Ex=Ec[0]
                    Ey=Ec[1]
                    step=0.04
                    c1vx = c1.get_vel()[0]+c1.get_charge()/field_lower*Ex*step
                    c1vy = c1.get_vel()[1]+c1.get_charge()/field_lower*Ey*step
                    c1.set_vel(c1vx,c1vy)
                    c1x = step*c1vx
                    c1y = step*c1vy
                    c1.move_charge(c1x,c1y)


                if c2_move==False and -8<c2.get_pos()[0]< display_width+8 and  -8<c2.get_pos()[1]<display_height+8: 
                    Ec=c4.get_E_field(c2.get_pos()[0],c2.get_pos()[1])
                    Ex=Ec[0]
                    Ey=Ec[1]
                    step=0.04
                    c2vx = c2.get_vel()[0]+c2.get_charge()/field_lower*Ex*step
                    c2vy = c2.get_vel()[1]+c2.get_charge()/field_lower*Ey*step
                    c2.set_vel(c2vx,c2vy)
                    c2x = step*c2vx
                    c2y = step*c2vy
                    c2.move_charge(c2x,c2y)

                if c3_move==False and -8<c3.get_pos()[0]< display_width+8 and  -8<c3.get_pos()[1]<display_height+8: 
                    Ec=c4.get_E_field(c3.get_pos()[0],c3.get_pos()[1])
                    Ex=Ec[0]
                    Ey=Ec[1]
                    step=0.04
                    c3vx = c3.get_vel()[0]+c3.get_charge()/field_lower*Ex*step
                    c3vy = c3.get_vel()[1]+c3.get_charge()/field_lower*Ey*step
                    c3.set_vel(c3vx,c3vy)
                    c3x = step*c3vx
                    c3y = step*c3vy
                    c3.move_charge(c3x,c3y)


                if counter!=3 or (-8<c3.get_pos()[0]< display_width+8 and  -8<c3.get_pos()[1]<display_height+8) or (-8<c2.get_pos()[0]< display_width+8 and  -8<c2.get_pos()[1]<display_height+8) or (-8<c1.get_pos()[0]< display_width+8 and -8<c1.get_pos()[1]<display_height+8):
                    a=1 #so para por alguma coisa
                else:
                    victory(level5)



                ##Movimento depois da colisao
                if c1_move==True and -8<c1.get_pos()[0]< display_width+8 and  -8<c1.get_pos()[1]<display_height+8: 
                    if(collision==True and f_in1==True):
                        theta1 = theta
                        aux_ang=s.get_sh_angle()
                        f_in1=False

                    fi = aux_ang-atan(2/((1+eta)*tan(theta1)))
                    v_c = sqrt(2*eta*eta*(1-cos(theta1))/(1+eta*(1-cos(theta1))))*w/k 
                    c1.move_charge(v_c*cos(fi),-v_c*sin(fi))
                else:
                    f_in1=True
                        
                if c2_move==True and -8<c2.get_pos()[0]< display_width+8 and  -8<c2.get_pos()[1]<display_height+8: 
                    if(collision==True and f_in2==True):
                        theta2 = theta
                        aux_ang=s.get_sh_angle()
                        f_in2=False

                    fi = aux_ang-atan(2/((1+eta)*tan(theta2)))
                    v_c = sqrt(2*eta*eta*(1-cos(theta2))/(1+eta*(1-cos(theta2))))*w/k 
                    c2.move_charge(v_c*cos(fi),-v_c*sin(fi))
                else:
                    f_in2=True

                if c3_move==True and -8<c3.get_pos()[0]< display_width+8 and  -8<c3.get_pos()[1]<display_height+8: 
                    if(collision==True and f_in3==True):
                        theta3 = theta
                        aux_ang=s.get_sh_angle()
                        f_in3=False

                    fi = aux_ang-atan(2/((1+eta)*tan(theta3)))
                    v_c = sqrt(2*eta*eta*(1-cos(theta3))/(1+eta*(1-cos(theta3))))*w/k 
                    c3.move_charge(v_c*cos(fi),-v_c*sin(fi))
                else:
                    f_in3=True

 
		# --- Wrap-ups
		# Limit to 180 frames per second
		clock.tick(180)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()



def level6():

	pygame.key.set_repeat(1,15)

	s = shoot()


        # Criacao de cargas ########################

        c1 = elec_charge()
        c2 = elec_charge()
        c3 = elec_charge()
        c4 = elec_charge()

        ###Origem do referencial
        Ox=display_width/2
        Oy=display_height/2


        # --- Criar efectivamente as cargas no screen ######
        c1.create_charge(screen,-700,Ox-100,Oy-180,DARK_BLUE)
        c2.create_charge(screen,-700,Ox-49,Oy+200,DARK_BLUE)
        c3.create_charge(screen,-700,Ox+200,Oy-49,DARK_BLUE)
        c4.create_charge(screen,3000,Ox,Oy,RED)

        c1_pos=c1.get_pos()
        c2_pos=c2.get_pos()
        c3_pos=c3.get_pos()
        c4_pos=c4.get_pos()

        c_vec=[]
        c_vec.append(c1)
        c_vec.append(c2)
        c_vec.append(c3)



        ###############################################
        time=0 #para parametrizar o movimento da carga positiva c4


        counter=0 #conta as colisoes que houve, quando chega a 3 o jogador ganha
        theta = 0.1 ## angulo da onda difundida, inicializa-se a 0.1 para evitar problemas de infinitos

        ####Parametros relativos as trajectorias das cargas
        theta1=0
        theta2=0
        theta3=0
        f_in1=True
        f_in2=True
        f_in3=True
        aux_ang=0
        fi=0
        v_c=0


        n_tries=0 #para contar o nr de tentativas do user
	shooter_angle=0
	ball_on_screen=False

        c1_move=False ##indica se a carga c1 se esta a movimentar
        c2_move=False
        c3_move=False
        collision=False ## da-me informacao sobre se esta ou nao a haver colisao entre fotao e eletrao
        first_entrance=True #Variavel auiliar para definir a trajectoria do fotao apos o choque
        first_entrance2=True

        ##translacoes necessarias para definir a trajectoria do fotao apos a colisao
        transx = 0
        transy = 0





        ####Condicoes iniciais do movimento das cargas
        v=9.5
        alfa=atan((c1.get_pos()[1]-c4.get_pos()[1])/(c1.get_pos()[0]-c4.get_pos()[0]))
        v0x=-v*sin(alfa)
        v0y=v*cos(alfa)
        c1.set_vel(v0x,v0y)


        v=9.5
        alfa=atan((c2.get_pos()[1]-c4.get_pos()[1])/(c2.get_pos()[0]-c4.get_pos()[0]))
        v0x=-v*sin(alfa)
        v0y=v*cos(alfa)
        c2.set_vel(v0x,v0y)


        v=9.5
        alfa=atan((c3.get_pos()[1]-c4.get_pos()[1])/(c3.get_pos()[0]-c4.get_pos()[0]))
        v0x=-v*sin(alfa)
        v0y=v*cos(alfa)
        c3.set_vel(v0x,v0y)



        
        tempo=0 ###para o countdown


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

                                    if(ball_on_screen==False and shooter_angle<1.5): # tenho de impor esta condicao porque quando a bola e disparada eu nao apago a imagem anterior para se ver a trajectoria e por isso se deixar o user mexer no shooter nessa fase, vao ficar varias imagens da posicao do shooter sobrepostas
					shooter_angle = shooter_angle+0.05	
                                    else:
                                        vel=0
                                        n_tries=n_tries+1
                                        ball_on_screen=False #para fazer nova jogada
                                    collision=False

				elif event.key == pygame.K_DOWN:

                                    if(ball_on_screen==False and shooter_angle>=0):
					shooter_angle = shooter_angle-0.05
                                    else:
                                        vel=0
                                        n_tries=n_tries+1
                                        ball_on_screen=False #para fazer nova jogada
                                    collision=False

				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                        s.reset_wavepos() #para que a posicao inicial da onda nao seja a do tiro anterior
                                        transx=0
                                        transy=0
                                        collision=False
                                elif event.key == pygame.K_b:
                                        B=-B
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					shooter_angle=shooter_angle
					#nao acontece nada ao angulo quando as teclas sao premidas ao mesmo tempo		


                # Set the screen background
                #if ball_on_screen == False:
                bg = pygame.image.load("bg.png") 
                screen.blit(bg, (0, 0))    



                tempo += 1
                countdown = 500-tempo


                x=0
                y=100
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

                if countdown == 0:
                    defeat(level6)       



                # Explicacao do objectivo ##########################

                button("Menu",0,5,50,20,GRAY,WHITE,stage2)
                """
                pygame.draw.rect(screen,GOLD,(150,15,385,30))
                font = pygame.font.SysFont("freesans", 20)
                text = font.render("Objective: Reach the red threshold!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (350,30)
                screen.blit(text, textpos)
                """

                x=65
                y=5
                rad=7
                w=620
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
                textSurf, textRect = text_objects("Use Compton scattering to remove the electrons from the + charge field!", smallText,BLACK)
                textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                screen.blit(textSurf, textRect)


                ##Informacao sobre o angulo de inclinacao
                #pygame.draw.rect(screen,AQUA,(display_width/2+100,15,300,30))
                #font = pygame.font.SysFont("freesans", 20)
                #info_shooter_angle= "Angle: " + str(shooter_angle)
                #text = font.render(info_shooter_angle, 1, BLACK)
                #textpos = text.get_rect()
                #textpos.center = (display_width/2+200,30)
                #screen.blit(text, textpos)

                ###Origem do referencial
                Ox=display_width/2
                Oy=display_height/2


		# --- Criar efectivamente as cargas no screen ######
		# --- Criar efectivamente as cargas no screen ######
                c1.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(23))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c1.get_pos()[0]),(c1.get_pos()[1]))
                screen.blit(text, textpos)

                c2.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(23))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c2.get_pos()[0]),(c2.get_pos()[1]))
                screen.blit(text, textpos)

                c3.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(23))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c3.get_pos()[0]),(c3.get_pos()[1]))
                screen.blit(text, textpos)

                c4.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(30))
                text = font.render("+", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c4.get_pos()[0]),(c4.get_pos()[1]))
                screen.blit(text, textpos)


                c_vec=[]
                c_vec.append(c1)
                c_vec.append(c2)
                c_vec.append(c3)
                c_vec.append(c4)
                ####################################################

		# Desenhar o shooter
		s.draw_shooter(screen,shooter_angle)



                ###VER ISTO!!!!!###############
                """
                if ball_on_screen==False:
                    pos = s.get_ball_pos()
                    prev_pos=(pos[0],pos[1])
                    print prev_pos
                """		

                eta = 2
                k=0.2 ## nr de onda da onda incidente 
                w=1.5 ## frequencia da onda incidente


		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        #s.kutta(screen,shot,B,Ex,Ey)

			shot = False

			pos = s.get_wave_pos()#posicao da onda

                        # verificar se a onda esta dentro do ecra  
			#if 0<pos[0]< display_width and  0<pos[1]<display_height: 
			#	ball_on_screen=True
			#else:
			#	ball_on_screen=False


                        
                        c1_pos=c1.get_pos()
                        c2_pos=c2.get_pos()
                        c3_pos=c3.get_pos()
                        c4_pos=c4.get_pos()


                        color_test = s.get_wave_color()



                        if c1_pos[0]-10<pos[0]<c1_pos[0]+10 and c1_pos[1]-10<pos[1]<c1_pos[1]+10 and first_entrance2==True and color_test==(0,0,255):

                            c1_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel
                            first_entrance=True
                            first_entrance2=False


                        if c2_pos[0]-10<pos[0]<c2_pos[0]+10 and c2_pos[1]-10<pos[1]<c2_pos[1]+10 and first_entrance2==True and color_test==(0,0,255):

                            c2_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel
                            first_entrance=True
                            first_entrance2=False


                        if c3_pos[0]-10<pos[0]<c3_pos[0]+10 and c3_pos[1]-10<pos[1]<c3_pos[1]+10 and first_entrance2==True and color_test==(0,0,255):

                            c3_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel
                            first_entrance=True
                            first_entrance2=False


                        #####NAO QUERO QUE O PROGRAMA ANDE A ENTRAR MAIS QUE UMA VEZ NOS IFS ANTERIORES!!!!!!!!!


                        if (c1_pos[0]-10<pos[0]<c1_pos[0]+10 and c1_pos[1]-10<pos[1]<c1_pos[1]+10) or ( c2_pos[0]-10<pos[0]<c2_pos[0]+10 and c2_pos[1]-10<pos[1]<c2_pos[1]+10) or (c3_pos[0]-10<pos[0]<c3_pos[0]+10 and c3_pos[1]-10<pos[1]<c3_pos[1]+10):
                            first_entrance2=False
                        else:
                            first_entrance2=True



                        if(collision==False):
                            angle = s.get_sh_angle() #angulo da trajectoria da onda
                        if(collision==True and first_entrance==True and color_test==(0,0,255)):
                            theta=0.7
                            angle = s.get_sh_angle()+theta

                            ##translacao necessaria para definir a trajectoria apos colisao
                            col_coord=s.get_wave_before_rot()#coordenada x do ponto onde se da a colisao, antes de ser rodado
                            step=s.get_pos_step()#IMPORTANTE!!

                            transx = (col_coord)*cos(s.get_sh_angle())-col_coord*cos(angle)
                            transy = (col_coord)*sin(s.get_sh_angle())-col_coord*sin(angle)

                            counter+=1
                            first_entrance=False


                        s.wave_motion(screen,shot,transx,transy,k,w,angle,theta,eta)

			

                        # verificar se a onda esta dentro do ecra  
			if 0<=pos[0]<= display_width and  0<=pos[1]<=display_height: 
				ball_on_screen=True
			else:
                                #n_tries = n_tries+1
				ball_on_screen=False





                ####MOVIMENTO DAS CARGAS - verifica-se tambem quando estas saem da tela para parar o movimento
 

                ##Movimento antes da colisao

                #O jogador perde se um dos eletroes for completamente atraido

                c1_pos=c1.get_pos()
                c2_pos=c2.get_pos()
                c3_pos=c3.get_pos()
                c4_pos=c4.get_pos()


                delta=20
                if (c4_pos[0]-delta<c1_pos[0]<c4_pos[0]+delta and c4_pos[1]-delta<c1_pos[1]<c4_pos[1]+delta) or (c4_pos[0]-delta<c2_pos[0]<c4_pos[0]+delta and c4_pos[1]-delta<c2_pos[1]<c4_pos[1]+delta) or (c4_pos[0]-delta<c3_pos[0]<c4_pos[0]+delta and c4_pos[1]-delta<c3_pos[1]<c4_pos[1]+delta):
                    defeat(level6)


                field_lower=50


                if c1_move==False and -8<c1.get_pos()[0]< display_width+8 and  -8<c1.get_pos()[1]<display_height+8: 
                    Ec=c4.get_E_field(c1.get_pos()[0],c1.get_pos()[1])
                    Ex=Ec[0]
                    Ey=Ec[1]
                    step=0.08
                    c1vx = c1.get_vel()[0]+c1.get_charge()/field_lower*Ex*step 
                    c1vy = c1.get_vel()[1]+c1.get_charge()/field_lower*Ey*step 
                    c1.set_vel(c1vx,c1vy)
                    c1x = step*c1vx
                    c1y = step*c1vy
                    c1.move_charge(c1x,c1y)

                    #d14 = sqrt((c1.get_pos()[0]-c4.get_pos()[0])*(c1.get_pos()[0]-c4.get_pos()[0]) + (c1.get_pos()[1]-c4.get_pos()[1])*(c1.get_pos()[1]-c4.get_pos()[1]))
                    #x = d14*cos(time)+c4.get_pos()[0]
                    #y = d14*sin(time)+c4.get_pos()[1]
                    #c1.set_pos(x,y)


                if c2_move==False and -8<c2.get_pos()[0]< display_width+8 and  -8<c2.get_pos()[1]<display_height+8: 
                    Ec=c4.get_E_field(c2.get_pos()[0],c2.get_pos()[1])
                    Ex=Ec[0]
                    Ey=Ec[1]
                    step=0.08
                    c2vx = c2.get_vel()[0]+c2.get_charge()/field_lower*Ex*step
                    c2vy = c2.get_vel()[1]+c2.get_charge()/field_lower*Ey*step
                    c2.set_vel(c2vx,c2vy)
                    c2x = step*c2vx
                    c2y = step*c2vy
                    c2.move_charge(c2x,c2y)




                    #d24 = sqrt((c2.get_pos()[0]-c4.get_pos()[0])*(c2.get_pos()[0]-c4.get_pos()[0]) + (c2.get_pos()[1]-c4.get_pos()[1])*(c2.get_pos()[1]-c4.get_pos()[1]))
                    #x = d24*cos(time-2.5)+c4.get_pos()[0]
                    #y = d24*sin(time-2.5)+c4.get_pos()[1]
                    #c2.set_pos(x,y)



                if c3_move==False and -8<c3.get_pos()[0]< display_width+8 and  -8<c3.get_pos()[1]<display_height+8: 
                    Ec=c4.get_E_field(c3.get_pos()[0],c3.get_pos()[1])
                    Ex=Ec[0]
                    Ey=Ec[1]
                    step=0.08
                    c3vx = c3.get_vel()[0]+c3.get_charge()/field_lower*Ex*step
                    c3vy = c3.get_vel()[1]+c3.get_charge()/field_lower*Ey*step
                    c3.set_vel(c3vx,c3vy)
                    c3x = step*c3vx
                    c3y = step*c3vy
                    c3.move_charge(c3x,c3y)

                    #d34 = sqrt((c3.get_pos()[0]-c4.get_pos()[0])*(c3.get_pos()[0]-c4.get_pos()[0]) + (c3.get_pos()[1]-c4.get_pos()[1])*(c3.get_pos()[1]-c4.get_pos()[1]))
                    #x = d34*cos(time-4)+c4.get_pos()[0]
                    #y = d34*sin(time-4)+c4.get_pos()[1]
                    #c3.set_pos(x,y)


                time+=0.02



                if counter!=3 or (-8<c3.get_pos()[0]< display_width+8 and  -8<c3.get_pos()[1]<display_height+8) or (-8<c2.get_pos()[0]< display_width+8 and  -8<c2.get_pos()[1]<display_height+8) or (-8<c1.get_pos()[0]< display_width+8 and -8<c1.get_pos()[1]<display_height+8):
                    a=1 #so para por alguma coisa
                else:
                    victory(level6)



                ##Movimento depois da colisao
                if c1_move==True and -8<c1.get_pos()[0]< display_width+8 and  -8<c1.get_pos()[1]<display_height+8: 
                    if(collision==True and f_in1==True):
                        theta1 = theta
                        aux_ang=s.get_sh_angle()
                        f_in1=False

                    fi = aux_ang-atan(2/((1+eta)*tan(theta1)))
                    v_c = sqrt(2*eta*eta*(1-cos(theta1))/(1+eta*(1-cos(theta1))))*w/k 
                    c1.move_charge(v_c*cos(fi),-v_c*sin(fi))
                else:
                    f_in1=True
                        
                if c2_move==True and -8<c2.get_pos()[0]< display_width+8 and  -8<c2.get_pos()[1]<display_height+8: 
                    if(collision==True and f_in2==True):
                        theta2 = theta
                        aux_ang=s.get_sh_angle()
                        f_in2=False

                    fi = aux_ang-atan(2/((1+eta)*tan(theta2)))
                    v_c = sqrt(2*eta*eta*(1-cos(theta2))/(1+eta*(1-cos(theta2))))*w/k 
                    c2.move_charge(v_c*cos(fi),-v_c*sin(fi))
                else:
                    f_in2=True

                if c3_move==True and -8<c3.get_pos()[0]< display_width+8 and  -8<c3.get_pos()[1]<display_height+8: 
                    if(collision==True and f_in3==True):
                        theta3 = theta
                        aux_ang=s.get_sh_angle()
                        f_in3=False

                    fi = aux_ang-atan(2/((1+eta)*tan(theta3)))
                    v_c = sqrt(2*eta*eta*(1-cos(theta3))/(1+eta*(1-cos(theta3))))*w/k 
                    c3.move_charge(v_c*cos(fi),-v_c*sin(fi))
                else:
                    f_in3=True

 
		# --- Wrap-ups
		# Limit to 180 frames per second
		clock.tick(180)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()




def level7():

	pygame.key.set_repeat(1,15)

	s = shoot()


        # Criacao de cargas ########################

        c1 = elec_charge()
        c2 = elec_charge()
        c3 = elec_charge()
        c4 = elec_charge()


        ## cargas criadas pelos obstaculos
        c_obs = []
        c_obs_counter=0
        obs1_entrance=True #variavel util para chamar if so uma vez
        obs_draw_first_entrance=False
        charge_obs_draw=False # Se true, permite desenhar as cargas criadas a cada iteracao
        flag_obs=False #Para indicar quando a perda de energia da onda vem de uma carga proveniente do obstaculo
        phasex=0
        phasey=0
        time_obs=[]
        f_in_obs=[]
        c_obs_on_screen=[]
        c_obs_collision=[]
        phase=[]

        #### Posicoes dos obstaculos
        ob1x=200
        ob1y=-7


        ###Origem do referencial
        Ox=display_width/2
        Oy=display_height/2


        # --- Criar efectivamente as cargas no screen ######
        c1.create_charge(screen,-700,Ox-100,Oy-180,DARK_BLUE)
        c2.create_charge(screen,-700,Ox-49,Oy+200,DARK_BLUE)
        c3.create_charge(screen,-700,Ox+200,Oy-49,DARK_BLUE)
        c4.create_charge(screen,3000,Ox,Oy,RED)

        c1_pos=c1.get_pos()
        c2_pos=c2.get_pos()
        c3_pos=c3.get_pos()
        c4_pos=c4.get_pos()

        c_vec=[]
        c_vec.append(c1)
        c_vec.append(c2)
        c_vec.append(c3)


        ####Condicoes iniciais do movimento das cargas
        v=9.5
        alfa=atan((c1.get_pos()[1]-c4.get_pos()[1])/(c1.get_pos()[0]-c4.get_pos()[0]))
        v0x=-v*sin(alfa)
        v0y=v*cos(alfa)
        c1.set_vel(v0x,v0y)


        v=9.5
        alfa=atan((c2.get_pos()[1]-c4.get_pos()[1])/(c2.get_pos()[0]-c4.get_pos()[0]))
        v0x=-v*sin(alfa)
        v0y=v*cos(alfa)
        c2.set_vel(v0x,v0y)


        v=9.5
        alfa=atan((c3.get_pos()[1]-c4.get_pos()[1])/(c3.get_pos()[0]-c4.get_pos()[0]))
        v0x=-v*sin(alfa)
        v0y=v*cos(alfa)
        c3.set_vel(v0x,v0y)



        
        tempo=0 ###para o countdown




        ###############################################
        time=0 #para parametrizar o movimento da carga positiva c4


        counter=0 #conta as colisoes que houve, quando chega a 3 o jogador ganha
        theta = 0.1 ## angulo da onda difundida, inicializa-se a 0.1 para evitar problemas de infinitos

        ####Parametros relativos as trajectorias das cargas
        theta1=0
        theta2=0
        theta3=0
        f_in1=True
        f_in2=True
        f_in3=True
        aux_ang=0
        fi=0
        v_c=0


        # flags de indicacao de vitoria 
        flag_obs_win=True
        flag_win=False


        n_tries=0 #para contar o nr de tentativas do user
	shooter_angle=0
	ball_on_screen=False

        c1_move=False ##indica se a carga c1 se esta a movimentar
        c2_move=False
        c3_move=False
        collision=False ## da-me informacao sobre se esta ou nao a haver colisao entre fotao e eletrao
        first_entrance=True #Variavel auiliar para definir a trajectoria do fotao apos o choque
        first_entrance2=True

        ##translacoes necessarias para definir a trajectoria do fotao apos a colisao
        transx = 0
        transy = 0



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

                                    if(ball_on_screen==False and shooter_angle<1.5): # tenho de impor esta condicao porque quando a bola e disparada eu nao apago a imagem anterior para se ver a trajectoria e por isso se deixar o user mexer no shooter nessa fase, vao ficar varias imagens da posicao do shooter sobrepostas
					shooter_angle = shooter_angle+0.05	
                                    else:
                                        vel=0
                                        n_tries=n_tries+1
                                        ball_on_screen=False #para fazer nova jogada
                                    collision=False
                        

				elif event.key == pygame.K_DOWN:

                                    if(ball_on_screen==False and shooter_angle>=0):
					shooter_angle = shooter_angle-0.05
                                    else:
                                        vel=0
                                        n_tries=n_tries+1
                                        ball_on_screen=False #para fazer nova jogada
                                    collision=False


				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                        s.reset_wavepos() #para que a posicao inicial da onda nao seja a do tiro anterior
                                        transx=0
                                        transy=0
                                        collision=False

                                elif event.key == pygame.K_b:
                                        B=-B
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					shooter_angle=shooter_angle
					#nao acontece nada ao angulo quando as teclas sao premidas ao mesmo tempo		


                # Set the screen background
                #if ball_on_screen == False:
                bg = pygame.image.load("bg.png") 
                screen.blit(bg, (0, 0))




                tempo += 1
                countdown = 800-tempo


                x=0
                y=100
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

                if countdown == 0:
                    defeat(level6)       


           



                # Explicacao do objectivo ##########################

                button("Menu",0,5,50,20,GRAY,WHITE,stage2)
                """
                pygame.draw.rect(screen,GOLD,(150,15,385,30))
                font = pygame.font.SysFont("freesans", 20)
                text = font.render("Objective: Reach the red threshold!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (350,30)
                screen.blit(text, textpos)
                """

                x=65
                y=5
                rad=7
                w=620
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
                textSurf, textRect = text_objects("Use Compton scattering to remove the electrons from the + charge field!", smallText,BLACK)
                textRect.center = ( (x+(w/2)+4), (y+(h/2)) )
                screen.blit(textSurf, textRect)


                ##Informacao sobre o angulo de inclinacao
                #pygame.draw.rect(screen,AQUA,(display_width/2+100,15,300,30))
                #font = pygame.font.SysFont("freesans", 20)
                #info_shooter_angle= "Angle: " + str(shooter_angle)
                #text = font.render(info_shooter_angle, 1, BLACK)
                #textpos = text.get_rect()
                #textpos.center = (display_width/2+200,30)
                #screen.blit(text, textpos)

                ###Origem do referencial
                Ox=display_width/2
                Oy=display_height/2


		# --- Criar efectivamente as cargas no screen ######
		# --- Criar efectivamente as cargas no screen ######
                c1.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(23))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c1.get_pos()[0]),(c1.get_pos()[1]))
                screen.blit(text, textpos)

                c2.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(23))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c2.get_pos()[0]),(c2.get_pos()[1]))
                screen.blit(text, textpos)

                c3.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(23))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c3.get_pos()[0]),(c3.get_pos()[1]))
                screen.blit(text, textpos)

                c4.draw_charge(screen)
                font = pygame.font.SysFont("freesans", int(30))
                text = font.render("+", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c4.get_pos()[0]),(c4.get_pos()[1]))
                screen.blit(text, textpos)


                c_vec=[]
                c_vec.append(c1)
                c_vec.append(c2)
                c_vec.append(c3)
                c_vec.append(c4)
                ####################################################

		# Desenhar o shooter
		s.draw_shooter(screen,shooter_angle)



                ###VER ISTO!!!!!###############
                """
                if ball_on_screen==False:
                    pos = s.get_ball_pos()
                    prev_pos=(pos[0],pos[1])
                    print prev_pos
                """		

                eta = 2
                k=0.2 ## nr de onda da onda incidente 
                w=1.5 ## frequencia da onda incidente


		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        #s.kutta(screen,shot,B,Ex,Ey)

			shot = False


			pos = s.get_wave_pos()#posicao da onda

                        # verificar se a onda esta dentro do ecra  
			#if 0<pos[0]< display_width and  0<pos[1]<display_height: 
			#	ball_on_screen=True
			#else:
			#	ball_on_screen=False


                        
                        c1_pos=c1.get_pos()
                        c2_pos=c2.get_pos()
                        c3_pos=c3.get_pos()
                        c4_pos=c4.get_pos()


                        color_test = s.get_wave_color()


                        if c1_pos[0]-10<pos[0]<c1_pos[0]+10 and c1_pos[1]-10<pos[1]<c1_pos[1]+10 and first_entrance2==True and color_test==(0,0,255):

                            c1_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel
                            first_entrance=True
                            first_entrance2=False

                            flag_obs=False


                        if c2_pos[0]-10<pos[0]<c2_pos[0]+10 and c2_pos[1]-10<pos[1]<c2_pos[1]+10 and first_entrance2==True and color_test==(0,0,255):

                            c2_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel
                            first_entrance=True
                            first_entrance2=False

                            flag_obs=False


                        if c3_pos[0]-10<pos[0]<c3_pos[0]+10 and c3_pos[1]-10<pos[1]<c3_pos[1]+10 and first_entrance2==True and color_test==(0,0,255):

                            c3_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel
                            first_entrance=True
                            first_entrance2=False

                            flag_obs=False


                        #####NAO QUERO QUE O PROGRAMA ANDE A ENTRAR MAIS QUE UMA VEZ NOS IFS ANTERIORES!!!!!!!!!


                        if (c1_pos[0]-10<pos[0]<c1_pos[0]+10 and c1_pos[1]-10<pos[1]<c1_pos[1]+10) or ( c2_pos[0]-10<pos[0]<c2_pos[0]+10 and c2_pos[1]-10<pos[1]<c2_pos[1]+10) or (c3_pos[0]-10<pos[0]<c3_pos[0]+10 and c3_pos[1]-10<pos[1]<c3_pos[1]+10):
                            first_entrance2=False
                        else:
                            first_entrance2=True



                        if(collision==False):
                            angle = s.get_sh_angle() #angulo da trajectoria da onda
                        if(collision==True and first_entrance==True and color_test == (0,0,255)):
                            theta=0.7
                            angle = s.get_sh_angle()+theta


                            ##translacao necessaria para definir a trajectoria apos colisao
                            col_coord=s.get_wave_before_rot()#coordenada x do ponto onde se da a colisao, antes de ser rodado
                            step=s.get_pos_step()#IMPORTANTE!!

                            transx = (col_coord)*cos(s.get_sh_angle())-col_coord*cos(angle)
                            transy = (col_coord)*sin(s.get_sh_angle())-col_coord*sin(angle)


                            if(flag_obs==True):#Quando a perda de energia provem do efeito fotoeletrico nao quero por angulo na onda
                                angle=0
                                transx=0
                                transy=0
                                theta=0


                            #counter+=1
                            first_entrance=False


                        s.wave_motion(screen,shot,transx,transy,k,w,angle,theta,eta)

			

                        # verificar se a onda esta dentro do ecra  
			if 0<=pos[0]<= display_width and  0<=pos[1]<=display_height: 
				ball_on_screen=True
			else:
                                #n_tries = n_tries+1
				ball_on_screen=False





                ####MOVIMENTO DAS CARGAS - verifica-se tambem quando estas saem da tela para parar o movimento
 

                ##Movimento antes da colisao

                #O jogador perde se um dos eletroes for completamente atraido

                c1_pos=c1.get_pos()
                c2_pos=c2.get_pos()
                c3_pos=c3.get_pos()
                c4_pos=c4.get_pos()


                delta=20
                if (c4_pos[0]-delta<c1_pos[0]<c4_pos[0]+delta and c4_pos[1]-delta<c1_pos[1]<c4_pos[1]+delta) or (c4_pos[0]-delta<c2_pos[0]<c4_pos[0]+delta and c4_pos[1]-delta<c2_pos[1]<c4_pos[1]+delta) or (c4_pos[0]-delta<c3_pos[0]<c4_pos[0]+delta and c4_pos[1]-delta<c3_pos[1]<c4_pos[1]+delta):
                    defeat(level7)


                field_lower=50


                if c1_move==False and -8<c1.get_pos()[0]< display_width+8 and  -8<c1.get_pos()[1]<display_height+8: 
                    Ec=c4.get_E_field(c1.get_pos()[0],c1.get_pos()[1])
                    Ex=Ec[0]
                    Ey=Ec[1]
                    step=0.08
                    c1vx = c1.get_vel()[0]+c1.get_charge()/field_lower*Ex*step 
                    c1vy = c1.get_vel()[1]+c1.get_charge()/field_lower*Ey*step 
                    c1.set_vel(c1vx,c1vy)
                    c1x = step*c1vx
                    c1y = step*c1vy
                    c1.move_charge(c1x,c1y)

                    #d14 = sqrt((c1.get_pos()[0]-c4.get_pos()[0])*(c1.get_pos()[0]-c4.get_pos()[0]) + (c1.get_pos()[1]-c4.get_pos()[1])*(c1.get_pos()[1]-c4.get_pos()[1]))
                    #x = d14*cos(time)+c4.get_pos()[0]
                    #y = d14*sin(time)+c4.get_pos()[1]
                    #c1.set_pos(x,y)


                if c2_move==False and -8<c2.get_pos()[0]< display_width+8 and  -8<c2.get_pos()[1]<display_height+8: 
                    Ec=c4.get_E_field(c2.get_pos()[0],c2.get_pos()[1])
                    Ex=Ec[0]
                    Ey=Ec[1]
                    step=0.08
                    c2vx = c2.get_vel()[0]+c2.get_charge()/field_lower*Ex*step
                    c2vy = c2.get_vel()[1]+c2.get_charge()/field_lower*Ey*step
                    c2.set_vel(c2vx,c2vy)
                    c2x = step*c2vx
                    c2y = step*c2vy
                    c2.move_charge(c2x,c2y)




                    #d24 = sqrt((c2.get_pos()[0]-c4.get_pos()[0])*(c2.get_pos()[0]-c4.get_pos()[0]) + (c2.get_pos()[1]-c4.get_pos()[1])*(c2.get_pos()[1]-c4.get_pos()[1]))
                    #x = d24*cos(time-2.5)+c4.get_pos()[0]
                    #y = d24*sin(time-2.5)+c4.get_pos()[1]
                    #c2.set_pos(x,y)



                if c3_move==False and -8<c3.get_pos()[0]< display_width+8 and  -8<c3.get_pos()[1]<display_height+8: 
                    Ec=c4.get_E_field(c3.get_pos()[0],c3.get_pos()[1])
                    Ex=Ec[0]
                    Ey=Ec[1]
                    step=0.08
                    c3vx = c3.get_vel()[0]+c3.get_charge()/field_lower*Ex*step
                    c3vy = c3.get_vel()[1]+c3.get_charge()/field_lower*Ey*step
                    c3.set_vel(c3vx,c3vy)
                    c3x = step*c3vx
                    c3y = step*c3vy
                    c3.move_charge(c3x,c3y)

                    #d34 = sqrt((c3.get_pos()[0]-c4.get_pos()[0])*(c3.get_pos()[0]-c4.get_pos()[0]) + (c3.get_pos()[1]-c4.get_pos()[1])*(c3.get_pos()[1]-c4.get_pos()[1]))
                    #x = d34*cos(time-4)+c4.get_pos()[0]
                    #y = d34*sin(time-4)+c4.get_pos()[1]
                    #c3.set_pos(x,y)


                time+=0.02


                #if counter==3 and c3.get_pos()[0]<-8 and c3.get_pos()[0] > display_width+8 and  c3.get_pos()[1]<-8 and c3.get_pos()[1] > display_height+8 and c2.get_pos()[0]<-8 and c2.get_pos()[0] > display_width+8 and  c2.get_pos()[1]<-8 and c2.get_pos()[1] > display_height+8 and c1.get_pos()[0]<-8 and c1.get_pos()[0] > display_width+8 and  c1.get_pos()[1]<-8 and c1.get_pos()[1] > display_height+8 and flag_obs_win==True:
                    #victory(level7)




                ##Movimento depois da colisao
                if c1_move==True and -8<c1.get_pos()[0]< display_width+8 and  -8<c1.get_pos()[1]<display_height+8  and theta!=0: 
                    if(collision==True and f_in1==True):
                        theta1 = theta
                        aux_ang=s.get_sh_angle()
                        f_in1=False

                    fi = aux_ang-atan(2/((1+eta)*tan(theta1)))
                    v_c = sqrt(2*eta*eta*(1-cos(theta1))/(1+eta*(1-cos(theta1))))*w/k 
                    c1.move_charge(v_c*cos(fi),-v_c*sin(fi))


                else:
                    f_in1=True


                        
                if c2_move==True and -8<c2.get_pos()[0]< display_width+8 and  -8<c2.get_pos()[1]<display_height+8  and theta!=0: 
                    if(collision==True and f_in2==True):
                        theta2 = theta
                        aux_ang=s.get_sh_angle()
                        f_in2=False

                    fi = aux_ang-atan(2/((1+eta)*tan(theta2)))
                    v_c = sqrt(2*eta*eta*(1-cos(theta2))/(1+eta*(1-cos(theta2))))*w/k 
                    c2.move_charge(v_c*cos(fi),-v_c*sin(fi))

                else:
                    f_in2=True



                if c3_move==True and -8<c3.get_pos()[0]< display_width+8 and  -8<c3.get_pos()[1]<display_height+8  and theta!=0: 
                    if(collision==True and f_in3==True):
                        theta3 = theta
                        aux_ang=s.get_sh_angle()
                        f_in3=False

                    fi = aux_ang-atan(2/((1+eta)*tan(theta3)))
                    v_c = sqrt(2*eta*eta*(1-cos(theta3))/(1+eta*(1-cos(theta3))))*w/k 
                    c3.move_charge(v_c*cos(fi),-v_c*sin(fi))


                else:
                    f_in3=True






                ##### ----- Obstaculos --- #####

                pygame.draw.rect(screen,BLUE,(ob1x,ob1y,10,100))


                if(-8<ob1x< display_width+8 and  -8<ob1y<display_height+8): 
                    ob1y += 5
                else:
                    ob1x=200#reset dos valores quando ele sai da tela
                    ob1y=-7  
                    obs1_entrance=True

                if ob1x-10<s.get_wave_pos()[0]<ob1x+10 and ob1y<s.get_wave_pos()[1]<ob1y+100 and obs1_entrance==True:

                    c = elec_charge()
                    c_obs.append(c)

                    time_obs.append(0)
                    f_in_obs.append(True)
                    c_obs_on_screen.append(True)
                    c_obs_collision.append(False)

                    c_obs[c_obs_counter].create_charge(screen,-700,ob1x,ob1y,GREEN)

                    c_obs_counter+=1
                    obs1_entrance=False
                    charge_obs_draw=True
                    obs_draw_first_entrance=True


                    flag_obs=True
                    collision=True
                    first_entrance=True


                if charge_obs_draw==True:
                    for i in range(c_obs_counter):

                        if(c_obs_on_screen[i]==True):

                            c_obs[i].draw_charge(screen)


                            Ec=c4.get_E_field(c_obs[i].get_pos()[0],c_obs[i].get_pos()[1])
                            Ex=Ec[0]
                            Ey=Ec[1]
                            step=0.04
                            cvx = c_obs[i].get_vel()[0]+c_obs[i].get_charge()/field_lower*Ex*step 
                            cvy = c_obs[i].get_vel()[1]+c_obs[i].get_charge()/field_lower*Ey*step 
                            c_obs[i].set_vel(cvx,cvy)
                            cx = step*cvx
                            cy = step*cvy
                            c_obs[i].move_charge(cx,cy)

                        
                            posx=c_obs[i].get_pos()[0]
                            posy = c_obs[i].get_pos()[1]
                            c4x = c4.get_pos()[0]
                            c4y = c4.get_pos()[1]
                            
                            d = sqrt((posx-c4x)*(posx-c4x) + (posy-c4y)*(posy-c4y))
                            
                            if(obs_draw_first_entrance==True and i==c_obs_counter-1):
                                collision=True
                                first_entrance=True
                                #phase.append(-acos((posx-c4x)/d))
                                c_obs[i].set_vel(5,-5)
                                

                            """
                            x = d*cos(-time_obs[i]+phase[i])+c4x
                            y = -d*sin(-time_obs[i]+phase[i])+c4y

                            #print x

                            if(c_obs_collision[i]==False):
                                c_obs[i].set_pos(x,y)
                            """

                            time_obs[i]+=0.02



                            if -8<posx< display_width+8  and  -8<posy<display_height+8: 
                                wx = s.get_wave_pos()[0]
                                wy = s.get_wave_pos()[1]

                                if( posx - 10 < wx < posx + 10 and posy-10 < wy < posy+10  and color_test==(0,0,255)):
                                    
                                    c_obs_collision[i]=True
                                    flag_obs_win=True


                                    if(f_in_obs[i]==True):
                                        aux_ang=s.get_sh_angle()
                                        th=0.7
                                        fi = aux_ang-atan(2/((1+eta)*tan(th)))
                                        v_c = sqrt(2*eta*eta*(1-cos(th))/(1+eta*(1-cos(th))))*w/k 
                                        
                                        collision=True
                                        first_entrance=True
                                        flag_obs=False

                                        f_in_obs[i]=False
                                else:
                                    f_in_obs[i]=True


                                if(c_obs_collision[i]==True):
                                    c_obs[i].move_charge(v_c*cos(fi),-v_c*sin(fi))

                                delta=20
                                if (c4x-delta<posx<c4x+delta and c4y-delta<posy<c4y+delta):
                                    defeat(level7)
                                    
                            else:
                                c_obs_on_screen[i]=False
                                 

                obs_draw_first_entrance=False # as fases so interessam ser calculadas uma vez para saber a pos inicial


                counter2=0
                for i in range(c_obs_counter):
                    if(c_obs_on_screen[i] == False):
                        counter2+=1

                if(counter2==c_obs_counter):
                    flag_obs_win=True
                else:
                    flag_obs_win=False


                if (c3.get_pos()[0]<0 or c3.get_pos()[0] > display_width+0 or  c3.get_pos()[1]<0 or c3.get_pos()[1] > display_height+0) and (c2.get_pos()[0]<0 or c2.get_pos()[0] > display_width+0 or  c2.get_pos()[1]<0 or c2.get_pos()[1] > display_height+0) and (c1.get_pos()[0]<0 or c1.get_pos()[0] > display_width+0 or c1.get_pos()[1]<0 or c1.get_pos()[1] > display_height+0):
                    flag_win=True


                #print "flag_win"
                #print flag_win
                #print "flag_obs_win"
                #print flag_obs_win
                #print "\n"


                if(flag_win==True and flag_obs_win==True):
                    victory(level7)


 
		# --- Wrap-ups
		# Limit to 180 frames per second
		clock.tick(180)
 
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
        textSurf, textRect = text_objects("You lost!", smallText,BLACK)
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
        textSurf, textRect = text_objects("You won!", smallText,BLACK)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)

        #screen.blit(text, textpos)
        button("Restart",(display_width/2)-120,(display_height/2),110,50,WHITE,GRAY,level)
        button("Menu",(display_width/2)+10,(display_height/2),110,50,WHITE,GRAY,game_intro)



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

def about():

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(WHITE)
        largeText = pygame.font.SysFont("freesans",90)
        TextSurf, TextRect = text_objects("About", largeText,BLACK)
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

        button("Back",0,0,80,40,WHITE,GRAY,game_welcome)

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
