import pygame
import math
from shooter2 import shoot
from charge import elec_charge

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

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
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

        button("Level 1",(display_width/2)-110,200,100,50,GOLD,GRAY,level1)
        button("Level 2",(display_width/2)+10,200,100,50,GOLD,GRAY,level2)
        button("Level 3",(display_width/2)-110,260,100,50,GOLD,GRAY,level1)
        button("Level 4",(display_width/2)+10,260,100,50,GOLD,GRAY,level2)
        button("Take me back, I don't want to be amazing",0,0,400,40,WHITE,GRAY,game_welcome)
        #button("Level 3",(display_width/2)-50,380,100,50,GREEN,RED,level3)
        #button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
 
 
# -------- Main Program Loop -----------
def getBackground():
      return pygame.image.load('background.gif'), 5

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
				if event.key == pygame.K_UP:
					shooter_angle = shooter_angle+0.2
				elif event.key == pygame.K_DOWN:
					shooter_angle = shooter_angle-0.2
				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                elif event.key == pygame.K_a:
                                        B=14
                                elif event.key == pygame.K_n:
                                        B=0
                                elif event.key == pygame.K_d:
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
                
                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("B= " + str(B), smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)


		# desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                # Desenhar patamar 
		pygame.draw.rect(screen,RED,(680,340,2,70))

		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                       
                        s.magkutta(screen,shot,B,Ex,Ey)
                        
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
				if event.key == pygame.K_UP:
					shooter_angle = shooter_angle+0.2
				elif event.key == pygame.K_DOWN:
					shooter_angle = shooter_angle-0.2
				elif event.key == pygame.K_SPACE:
					shot=True
					ball_on_screen=True
                                elif event.key == pygame.K_a:
                                        B=14
                                elif event.key == pygame.K_n:
                                        B=0
                                elif event.key == pygame.K_d:
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
                
                smallText = pygame.font.SysFont("freesans",20)
                #smallText = pygame.font.SysFont("Verdana",20)
                textSurf, textRect = text_objects("B= " + str(B), smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)


		# desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                # Desenhar patamar 
		pygame.draw.rect(screen,RED,(620,40,2,70))

		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                       
                        s.magkutta(screen,shot,B,Ex,Ey)
                        
			shot = False

			pos = s.get_ball_pos()
                        vel = s.get_ball_vel()

                        if 675<pos[0]<685 and 338<pos[1]<412:
                            victory(level1)   

                        #if (0<pos[0]<186 and 420<pos[1]<436) or (380<pos[0]<400 and 122<pos[1]<520) or (114<pos[0]<390 and 300<pos[1]<316) or (112<pos[0]<128 and 122<pos[1]<308) or (200<pos[0]<280 and 15<pos[1]<185) or (513<pos[0]<550 and 300<pos[1]<400) or (513<pos[0]<820 and 300<pos[1]<320) or (513<pos[0]<620 and 120<pos[1]<200) or (680<pos[0]<682 and 340<pos[1]<410) or (600<pos[0]<680 and 5<pos[1]<35):
                            #defeat(level1)
                        

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
