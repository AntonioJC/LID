import pygame
from shooter import shoot
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


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesans",20)
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
        largeText = pygame.font.SysFont("freesans",90)
        TextSurf, TextRect = text_objects("Main menu", largeText)
        TextRect.center = ((display_width/2),100)
        screen.blit(TextSurf, TextRect)

        button("Level 1",(display_width/2)-50,200,100,50,GREEN,RED,level1)
        button("About",(display_width/2)-50,260,100,50,GREEN,RED,about)
        #button("???",(display_width/2)-50,320,100,50,GREEN,RED,kutta)
        button("Level 2",(display_width/2)-50,320,100,50,GREEN,RED,level2)
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
                pygame.draw.rect(screen,AQUA,(180,0,225,30))
                font = pygame.font.Font(None, 20)
                text = font.render("Objective: Collide until it stops!!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (300,15)
                screen.blit(text, textpos)


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
                        """
                        if ((col_xpos-10)<pos[0]<(col_xpos+10)) and ((hcol-10)<pos[1]<(hcol+10)):
                            victory(level1)
                        elif ((col_xpos2-10)<pos[0]<(col_xpos2+10)) and ((hcol2-10)<pos[1]<(hcol2+10)):
                            victory(level1)
                        elif ((col_xpos3-10)<pos[0]<(col_xpos3+10)) and ((hcol3-10)<pos[1]<(hcol3+10)):
                            victory(level1)
                        elif ((col_xpos4-10)<pos[0]<(col_xpos4+10)) and ((hcol4-10)<pos[1]<(hcol4+10)):
                            victory(level1)
                       """
                       
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

                            #victory(level1)
            

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
                        
                        """
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
                        """                
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

def level2():

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
                
                pygame.draw.rect(screen,AQUA,(150,15,385,30))
                font = pygame.font.SysFont("freesans", 20)
                text = font.render("Objective: Reach the red threshold!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (250,30)
                screen.blit(text, textpos)

		# desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                #criar e desenhar cargas
                c1.create_charge(screen,1000,display_width/2,display_height/2-100,DARK_RED)
                font = pygame.font.SysFont("freesans", 30)
                text = font.render("+", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((display_width/2),(display_height/2-103))
                screen.blit(text, textpos)

                c2.create_charge(screen,-1000,display_width/2-100,display_height/2+100,DARK_BLUE)
                font = pygame.font.SysFont("freesans", 30)
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((display_width/2-100),(display_height/2+98))
                screen.blit(text, textpos)

                c3.create_charge(screen,-2000,display_width/2+200,display_height/2-20,DARK_BLUE)
                font = pygame.font.SysFont("freesans", 50)
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((display_width/2+200),(display_height/2-22))
                screen.blit(text, textpos)

                c_vec=[]
                c_vec.append(c1)
                c_vec.append(c2)
                c_vec.append(c3)

		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        
                        vel = 100
                        s.motion_in_charge_field(screen,shot,c_vec,vel)

			shot = False
			
			pos = s.get_ball_pos()                        

                        if display_width/2+270<pos[0]<display_width/2+290 and display_height/2-22<pos[1]<display_height/2-20:
                            victory()                      
                        
                           
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

