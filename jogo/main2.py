import pygame
from shooter2 import shoot
from charge import elec_charge

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_RED = (178,34,34)
CORN_BLUE = (100,149,237)
AQUA = (127,255,212)
DSBLUE = (0,191,255)
DARK_BLUE = (72,61,139)
 
pygame.init()
 
# Set the height and width of the screen
display_width = 700
display_height = 500
size = [display_width, display_height]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Bouncing Rectangle")
 
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
        button("???",(display_width/2)-50,320,100,50,GREEN,RED,kutta)
        #button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
 

# -------- Main Program Loop -----------
def level1():


	#Variaveis importantes 
        B=-5 #campo magnetico default
        Ex=4;
        Ey=0.;
	s = shoot()


        # Criacao de cargas ########################

        c1 = elec_charge()
        c2 = elec_charge()
        c3 = elec_charge()

        ###############################################

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
                                    if(ball_on_screen==False): # tenho de impor esta condicao porque quando a bola e disparada eu nao apago a imagem anterior para se ver a trajectoria e por isso se deixar o user mexer no shooter nessa fase, vao ficar varias imagens da posicao do shooter sobrepostas
					shooter_angle = shooter_angle+0.05
                                    else:
                                        ball_on_screen=False #para fazer nova jogada
				elif event.key == pygame.K_DOWN:
                                    if(ball_on_screen==False):
					shooter_angle = shooter_angle-0.05
                                    else:
                                        ball_on_screen=False #para fazer nova jogada
				elif event.key == pygame.K_s:
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
                    #screen.fill(BLACK)
                    bg = pygame.image.load("bg.png")                
                    screen.blit(bg, (0, 0))



                # Explicacao do objectivo ##########################
                pygame.draw.rect(screen,AQUA,(10,15,385,30))
                font = pygame.font.Font(None, 30)
                text = font.render("Objective: Reach the red threshold!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (200,30)
                screen.blit(text, textpos)



		# --- Criar efectivamente as cargas no screen ######
                c1.create_charge(screen,1000,display_width/2,display_height/2-100,DARK_RED)
                font = pygame.font.Font(None, 30)
                text = font.render("+", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((display_width/2),(display_height/2-103))
                screen.blit(text, textpos)

                c2.create_charge(screen,-1000,display_width/2-100,display_height/2+100,DARK_BLUE)
                font = pygame.font.Font(None, 30)
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((display_width/2-100),(display_height/2+98))
                screen.blit(text, textpos)

                c3.create_charge(screen,-2000,display_width/2+200,display_height/2-20,DARK_BLUE)
                font = pygame.font.Font(None, 50)
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((display_width/2+200),(display_height/2-22))
                screen.blit(text, textpos)

                c_vec=[]
                c_vec.append(c1)
                c_vec.append(c2)
                c_vec.append(c3)
                ####################################################

		# Desenhar o shooter
		s.draw_shooter(screen,shooter_angle)

                # Desenhar patamar 
		pygame.draw.rect(screen,RED,(display_width/2+270,display_height/2-20,20,2))
		
		
		if ball_on_screen==True:
			#s.draw_ball(screen,shot)
                        #s.kutta(screen,shot,B,Ex,Ey)
                    
                        s.motion_in_field(screen,shot,c_vec)

			shot = False
			
			pos = s.get_ball_pos()

                        if display_width/2+270<pos[0]<display_width/2+290 and display_height/2-22<pos[1]<display_height/2-20:
                            victory()
			
			if 0<pos[0]< display_width and  0<pos[1]<display_height:
				ball_on_screen=True
			else:
				ball_on_screen=False
 
		# --- Wrap-ups
		# Limit to 60 frames per second
		clock.tick(180)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

def victory():
    
    lost = True 

    while lost:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.draw.rect(screen,AQUA,((display_width/2)-100,(display_height/2)-50,200,50))
        font = pygame.font.Font(None, 50)
        text = font.render("   You win!   ", 1, (20, 20, 20))
        textpos = text.get_rect()
        textpos.center = ((display_width/2),(display_height/2)-20)
        screen.blit(text, textpos)
        button("Again",(display_width/2)-100,(display_height/2),100,50,WHITE,GREEN,level1)
        button("Menu",(display_width/2),(display_height/2),100,50,WHITE,GREEN,game_intro)

        pygame.display.update()
        clock.tick(10)
 
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
        TextRect.center = ((display_width/2),50)
        font = pygame.font.Font(None, 26)
	text = font.render("This is a game that desires to stimulate the", 1, (10, 10, 10))
        text2 = font.render("passion of young people for physic related subjects,", 1, (10, 10, 10))
        text3 = font.render("using for that purpose a variety of levels regarding", 1, (10, 10, 10))
        text4 = font.render("various fields of this science.", 1, (10, 10, 10))
        textpos = text.get_rect()
        text2pos = text2.get_rect()
        text3pos = text3.get_rect()
        text4pos = text4.get_rect()
	textpos.center = ((display_width/2),150)
        text2pos.center = ((display_width/2),170)
        text3pos.center = ((display_width/2),190)
        text4pos.center = ((display_width/2),210)
        screen.blit(TextSurf, TextRect)
        screen.blit(text, textpos)
        screen.blit(text2, text2pos)
        screen.blit(text3, text3pos)
        screen.blit(text4, text4pos)

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

