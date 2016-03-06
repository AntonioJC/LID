import pygame
from shooter import shoot

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


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(WHITE)
        largeText = pygame.font.SysFont("comicsansms",90)
        TextSurf, TextRect = text_objects("Main menu", largeText)
        TextRect.center = ((display_width/2),100)
        screen.blit(TextSurf, TextRect)

        button("Level 1",(display_width/2)-50,200,100,50,GREEN,RED,level1)
        button("About",(display_width/2)-50,260,100,50,GREEN,RED,about)
        #button("???",(display_width/2)-50,320,100,50,GREEN,RED,kutta)
        button("Level 2",(display_width/2)-50,320,100,50,GREEN,RED,level2)
        #button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
 
 
# -------- Main Program Loop -----------
def getBackground():
      return pygame.image.load('background.gif'), 5

def level1():

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
				elif event.key == pygame.K_s:
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

                button("Menu",0,0,50,30,WHITE,GREEN,game_intro)
                pygame.draw.rect(screen,AQUA,(200,0,205,30))
                font = pygame.font.Font(None, 20)
                text = font.render("Objective: Collide!!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (300,15)
                screen.blit(text, textpos)


		# desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                #desenhar o detector
		#camadas up
                pygame.draw.rect(screen,WHITE,(100,75,520,5))
                pygame.draw.rect(screen,BLUE,(120,80,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,85,480,10))
                pygame.draw.rect(screen,BLUE,(120,95,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,100,480,10))
                pygame.draw.rect(screen,BLUE,(120,110,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,115,480,10))

                #separadores up
                pygame.draw.rect(screen,BLUE,(210,80,2,45))
                pygame.draw.rect(screen,BLUE,(270,80,2,45))
                pygame.draw.rect(screen,BLUE,(330,80,2,45))
                pygame.draw.rect(screen,BLUE,(390,80,2,45))
                pygame.draw.rect(screen,BLUE,(450,80,2,45))
                pygame.draw.rect(screen,BLUE,(510,80,2,45)) 

                #inner detector
                pygame.draw.rect(screen,GRAY,(120,125,480,175))
                pygame.draw.rect(screen,GOLD,(120,170,480,90))
                
                #camadas down
                pygame.draw.rect(screen,DSBLUE,(120,300,480,10))
                pygame.draw.rect(screen,BLUE,(120,310,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,315,480,10))
                pygame.draw.rect(screen,BLUE,(120,325,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,330,480,10))
                pygame.draw.rect(screen,BLUE,(120,340,480,5))
                pygame.draw.rect(screen,WHITE,(100,345,520,5))

                #separadores down
                pygame.draw.rect(screen,BLUE,(210,300,2,45))
                pygame.draw.rect(screen,BLUE,(270,300,2,45))
                pygame.draw.rect(screen,BLUE,(330,300,2,45))
                pygame.draw.rect(screen,BLUE,(390,300,2,45))
                pygame.draw.rect(screen,BLUE,(450,300,2,45))
                pygame.draw.rect(screen,BLUE,(510,300,2,45)) 
                 
                #barreiras left
                pygame.draw.rect(screen,WHITE,(0,180,100,60))

                pygame.draw.rect(screen,BLUE,(115,80,5,265))
                pygame.draw.rect(screen,WHITE,(110,75,5,270))
                pygame.draw.rect(screen,BLUE,(105,80,5,265))
                pygame.draw.rect(screen,WHITE,(100,75,5,270))

                #barreiras right
                pygame.draw.rect(screen,WHITE,(620,180,90,60))

                pygame.draw.rect(screen,BLUE,(600,80,5,265))
                pygame.draw.rect(screen,WHITE,(605,75,5,270))
                pygame.draw.rect(screen,BLUE,(610,80,5,265))
                pygame.draw.rect(screen,WHITE,(615,75,5,270))
                

		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        hcol = 150
                        hcol2= 200
                        hcol3= 280
                        hcol4=230
                        velcol = 20
                        velcol2 = 40
                        velcol3 = 10
                        velcol4= 30

                        col_xpos = s.collisions(screen,shot,hcol,velcol)
                        col_xpos2 = s.collisions(screen,shot,hcol2,velcol2)
                        col_xpos3 = s.collisions(screen,shot,hcol3,velcol3)
                        col_xpos4 = s.collisions(screen,shot,hcol4,velcol4)

                        s.kutta(screen,shot,B,Ex,Ey)
                        
			shot = False
			
			pos = s.get_ball_pos()                        

                        if ((col_xpos-10)<pos[0]<(col_xpos+10)) and ((hcol-10)<pos[1]<(hcol+10)):
                            victory(level1)
                        elif ((col_xpos2-10)<pos[0]<(col_xpos2+10)) and ((hcol2-10)<pos[1]<(hcol2+10)):
                            victory(level1)
                        elif ((col_xpos3-10)<pos[0]<(col_xpos3+10)) and ((hcol3-10)<pos[1]<(hcol3+10)):
                            victory(level1)
                        elif ((col_xpos4-10)<pos[0]<(col_xpos4+10)) and ((hcol4-10)<pos[1]<(hcol4+10)):
                            victory(level1)
                       
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

def level2():

	#Variaveis importantes 
        B=-5 #campo magnetico default
        Ex=4;
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
				elif event.key == pygame.K_s:
					shot=True
					ball_on_screen=True
                                elif event.key == pygame.K_b:
                                        B=-B
                                elif event.key == pygame.K_e:
                                    Ex=-Ex
                                elif event.key == pygame.K_r:
                                    Ey=-Ey
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
		#camadas up
                pygame.draw.rect(screen,WHITE,(100,75,520,5))
                pygame.draw.rect(screen,BLUE,(120,80,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,85,480,10))
                pygame.draw.rect(screen,BLUE,(120,95,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,100,480,10))
                pygame.draw.rect(screen,BLUE,(120,110,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,115,480,10))

                #separadores up
                pygame.draw.rect(screen,BLUE,(210,80,2,45))
                pygame.draw.rect(screen,BLUE,(270,80,2,45))
                pygame.draw.rect(screen,BLUE,(330,80,2,45))
                pygame.draw.rect(screen,BLUE,(390,80,2,45))
                pygame.draw.rect(screen,BLUE,(450,80,2,45))
                pygame.draw.rect(screen,BLUE,(510,80,2,45)) 

                #inner detector
                pygame.draw.rect(screen,GRAY,(120,125,480,175))
                pygame.draw.rect(screen,GOLD,(120,170,480,90))
                
                #camadas down
                pygame.draw.rect(screen,DSBLUE,(120,300,480,10))
                pygame.draw.rect(screen,BLUE,(120,310,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,315,480,10))
                pygame.draw.rect(screen,BLUE,(120,325,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,330,480,10))
                pygame.draw.rect(screen,BLUE,(120,340,480,5))
                pygame.draw.rect(screen,WHITE,(100,345,520,5))

                #separadores down
                pygame.draw.rect(screen,BLUE,(210,300,2,45))
                pygame.draw.rect(screen,BLUE,(270,300,2,45))
                pygame.draw.rect(screen,BLUE,(330,300,2,45))
                pygame.draw.rect(screen,BLUE,(390,300,2,45))
                pygame.draw.rect(screen,BLUE,(450,300,2,45))
                pygame.draw.rect(screen,BLUE,(510,300,2,45)) 
                 
                #barreiras left
                pygame.draw.rect(screen,WHITE,(0,180,100,60))

                pygame.draw.rect(screen,BLUE,(115,80,5,265))
                pygame.draw.rect(screen,WHITE,(110,75,5,270))
                pygame.draw.rect(screen,BLUE,(105,80,5,265))
                pygame.draw.rect(screen,WHITE,(100,75,5,270))

                #barreiras right
                pygame.draw.rect(screen,WHITE,(620,180,90,60))

                pygame.draw.rect(screen,BLUE,(600,80,5,265))
                pygame.draw.rect(screen,WHITE,(605,75,5,270))
                pygame.draw.rect(screen,BLUE,(610,80,5,265))
                pygame.draw.rect(screen,WHITE,(615,75,5,270))
                

		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        
                        s.kutta(screen,shot,B,Ex,Ey)
                        
			shot = False
			
			pos = s.get_ball_pos()                        
                       
                        detect = False

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

def defeat(level):
    
    lost = True 

    while lost:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.draw.rect(screen,AQUA,((display_width/2)-100,(display_height/2)-50,200,50))
        font = pygame.font.Font(None, 50)
        text = font.render("   You lost!   ", 1, (20, 20, 20))
        textpos = text.get_rect()
        textpos.center = ((display_width/2),(display_height/2)-20)
        screen.blit(text, textpos)
        button("Restart",(display_width/2)-100,(display_height/2),100,50,WHITE,GREEN,level)
        button("Menu",(display_width/2),(display_height/2),100,50,WHITE,GREEN,game_intro)

        pygame.display.update()
        clock.tick(25)  

def victory(level):
    
    win = True 

    while win:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.draw.rect(screen,AQUA,((display_width/2)-100,(display_height/2)-50,200,50))
        font = pygame.font.Font(None, 50)
        text = font.render("   You won!   ", 1, (20, 20, 20))
        textpos = text.get_rect()
        textpos.center = ((display_width/2),(display_height/2)-20)
        screen.blit(text, textpos)
        button("Restart",(display_width/2)-100,(display_height/2),100,50,WHITE,GREEN,level)
        button("Menu",(display_width/2),(display_height/2),100,50,WHITE,GREEN,game_intro)

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
        largeText = pygame.font.SysFont("comicsansms",90)
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

        button("Menu",0,0,50,30,WHITE,GREEN,game_intro)

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
game_intro()
pygame.quit()
quit()

