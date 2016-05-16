import pygame
from pygame.locals import *
from math import sqrt,cos,sin
from shooter2 import shoot
from charge import elec_charge
from resize import resize_screen

import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_RED = (178,34,34)
CORN_BLUE = (100,149,237)
AQUA = (127,255,212)
DSBLUE = (0,191,255)
DARK_BLUE = (72,61,139)
GOLD = (255,215,0)
 
pygame.init()
 
###### Set the height and width of the screen

infoObject = pygame.display.Info() #Tenho de pedir as informacoes logo no inicio do programa porque se pedir a seguir ao screen default ele vai buscar as informacoes do screen default e nao me diz o tamanho da tela inteira


######## Default Screen ########################################
display_width = 700
display_height = 500
size = [display_width, display_height]
screen = pygame.display.set_mode(size)



#infoObject = pygame.display.Info()
#display_width = infoObject.current_w
#display_height = infoObject.current_h-50
#screen=pygame.display.set_mode((int(display_width), int(display_height)))
 
pygame.display.set_caption("Bouncing Rectangle")
 
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
 
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
            

        if click[0] == 1 and action != None and wait_for_response==1:
            wait_for_response=0 
            action() 


    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)



#########Programa principal#######################################
def game_screen():

    intro = True

    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

        screen.fill(WHITE)
        largeText = pygame.font.SysFont("comicsansms",90)
        TextSurf, TextRect = text_objects("Choose screen size", largeText)
        TextRect.center = ((display_width/2),100)
        screen.blit(TextSurf, TextRect)

        button("Default Screen",(display_width/2)-50,200,100,50,GREEN,RED,game_intro) 
        button("Full Screen",(display_width/2)-50,260,100,50,GREEN,RED,resize)

        pygame.display.update()
        clock.tick(15)


def resize():

    global display_width
    global display_height
    global screen

    display_width = infoObject.current_w #o infoObject esta declarado no inicio do programa para obter informacoes antes de ser criado qualquer screen
    display_height = infoObject.current_h-50
    screen=pygame.display.set_mode((int(display_width), int(display_height)))
    game_intro()


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

        screen.fill(WHITE)
        largeText = pygame.font.SysFont("comicsansms",90)
        TextSurf, TextRect = text_objects("Main menu", largeText)
        TextRect.center = ((display_width/2),100)
        screen.blit(TextSurf, TextRect)

        button("Level 1",(display_width/2)-50,200,100,50,GREEN,RED,level1)
        button("Level 2",(display_width/2)-50,260,100,50,GREEN,RED,level2)
        button("About",(display_width/2)-50,320,100,50,GREEN,RED,about)
        button("Level 3",(display_width/2)-50,380,100,50,GREEN,RED,level3)
        #button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

 

# -------- Main Program Loop -----------
def level1():

	pygame.key.set_repeat(1,15)

	#Variaveis importantes 
        B=-5 #campo magnetico default
        Ex=4
        Ey=0.
        vel=0
	s = shoot(display_height)


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


        ##Criar objecto resize
        rs = resize_screen(display_width,display_height,Ox,Oy,c_vec)

        scale = rs.get_scale()
        srx = rs.get_srx() #screen ratio em x em relacao ao default
        sry = rs.get_sry() #screen ratio em y em relacao ao default
        tc_x = rs.get_charge_transform_x()
        tc_y = rs.get_charge_transform_y()
        trans_x = rs.get_trans_x()
        trans_y = rs.get_trans_y()
        
        ##Usado dentro do loop principal para escalar a velocidade
        if(srx==1):
            vel_scale=1
        else:
            vel_scale=0.948*srx


        c1.create_charge(screen,1000*srx*srx,Ox+trans_x,Oy+tc_y[0]+trans_y,DARK_RED)
        c2.create_charge(screen,-1000*srx*srx,Ox+tc_x[1]+trans_x,Oy+tc_y[1]+trans_y,DARK_BLUE)
        c3.create_charge(screen,-2000*srx*srx,Ox+tc_x[2]+trans_x,Oy+tc_y[2]+trans_y,DARK_BLUE)



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
                    if srx==1:
                        bg = pygame.image.load("bg.png") 
                        screen.blit(bg, (0, 0)) 
                    else:
                        screen.fill(BLACK)
                    #bg = pygame.image.load("bg.png")                
                    #screen.blit(bg, (0, 0))



                # Explicacao do objectivo ##########################
                button("Menu",0,0,50,30,WHITE,GREEN,game_intro)
                pygame.draw.rect(screen,AQUA,(180,0,225,30))
                font = pygame.font.Font(None, 20)
                text = font.render("Objective: Collide until it stops!!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (300,15)
                screen.blit(text, textpos)

                ##Informacao sobre o angulo de inclinacao
                pygame.draw.rect(screen,AQUA,(display_width/2+100,15,300,30))
                font = pygame.font.SysFont("comicsansms", 20)
                info_shooter_angle= "Angle: " + str(shooter_angle)
                text = font.render(info_shooter_angle, 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (display_width/2+200,30)
                screen.blit(text, textpos)

                ###Origem do referencial
                Ox=display_width/2
                Oy=display_height/2


		# --- Criar efectivamente as cargas no screen ######
                c1.draw_charge(screen)
                font = pygame.font.SysFont("comicsansms", int(srx*30))
                text = font.render("+", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c1.get_pos()[0]),(c1.get_pos()[1]-5))
                screen.blit(text, textpos)
                

                c2.draw_charge(screen)
                font = pygame.font.SysFont("comicsansms", int(srx*30))
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((c2.get_pos()[0]),(c2.get_pos()[1]))
                screen.blit(text, textpos)

                c3.draw_charge(screen)
                font = pygame.font.SysFont("comicsansms", int(srx*50))
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
                pos_patamar=(Ox+270*srx+trans_x,Oy-sry*20+trans_y)
                width_patamar=20*srx
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
                    
                        vel = 10*vel_scale#scale*1.166 # mudar depois para tornar interativo
                        s.motion_in_field(screen,shot,c_vec,vel)

			shot = False
			
			pos = s.get_ball_pos()

                        # verificar se a bola acertou no patamar pretendido
                        if pos_patamar[0]<pos[0]<pos_patamar[0]+width_patamar and pos_patamar[1]-2<pos[1]<pos_patamar[1]+2:
                            victory(level1)

                        # verificar as tentativas efectuadas
                        if(n_tries==3):
                            lost(level1)

                        #Verificar se a bola colide com as cargas
                        """
                        pos_c1 = c1.get_pos()
                        r1 = 6*c1.get_radius()
                        pos_c2 = c2.get_pos()
                        r2 = 6*c2.get_radius()
                        pos_c3 = c3.get_pos()
                        r3 = 6*c3.get_radius()
                        """
                        
                        #if((pos_c1[0]-r1<pos[0]<pos_c1[0]+r1 and pos_c1[1]-r1<pos[1]<pos_c1[1]+r1) or (pos_c2[0]-r2<pos[0]<pos_c2[0]+r2 and pos_c2[1]-r2<pos[1]<pos_c2[1]+r2) or (pos_c3[0]-r3<pos[0]<pos_c3[0]+r3 and pos_c3[1]-r3<pos[1]<pos_c3[1]+r3)):
                            #lost()
                        

			
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



def level2():

	pygame.key.set_repeat(1,10)

	#Variaveis importantes 
        Ex=4
        Ey=0.
        vel=0
	s = shoot(display_height)


        # Criacao de cargas ########################

        c1 = elec_charge()
        c2 = elec_charge()
        c3 = elec_charge()

        c1.create_charge(screen,800,display_width/2-150,display_height/2-100,DARK_RED)
        c2.create_charge(screen,-1000,display_width/2-200,display_height/2+100,DARK_BLUE)
        c3.create_charge(screen,-2000,display_width/2+100,display_height/2-20,DARK_BLUE)


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
                    screen.fill(BLACK)


                button("Menu",0,0,50,30,WHITE,GREEN,game_intro)
                pygame.draw.rect(screen,AQUA,(180,0,225,30))
                font = pygame.font.Font(None, 20)
                text = font.render("Objective: Collide until it stops!!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (300,15)
                screen.blit(text, textpos)

                ###E dificil com o background porque temos de apagar a carga anterior RESOLVER!!!!
                #if ball_on_screen == False:)
                    #bg = pygame.image.load("bg.png")               
                    #screen.blit(bg, (0, 0))



		# --- Criar efectivamente as cargas no screen ######
                c1.erase_charge(screen)

                font = pygame.font.SysFont("comicsansms", 30)
                text = font.render("-", 1, BLACK)
                textpos = text.get_rect()
                c1_pos=c1.get_pos()
                textpos.center = c1_pos
                screen.blit(text, textpos)

                ##mover a carga
                c1.move_charge(-0.09,0.09)
                # Desenhar a carga e o sinal - depois de movidos
                c1.draw_charge(screen)

                font = pygame.font.SysFont("comicsansms", 30)
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                c1_pos=c1.get_pos()
                textpos.center = c1_pos
                screen.blit(text, textpos)


                #######A carga c2 esta agora em movimento!!!############################################################################
                #apagar o desenho da carga anterior e da fonte(sinal -)
                c2.erase_charge(screen)

                font = pygame.font.SysFont("comicsansms", 30)
                text = font.render("-", 1, BLACK)
                textpos = text.get_rect()
                c2_pos=c2.get_pos()
                textpos.center = c2_pos
                screen.blit(text, textpos)

                ##mover a carga
                c2.move_charge(0.01,0.005)
                # Desenhar a carga e o sinal - depois de movidos
                c2.draw_charge(screen)

                font = pygame.font.SysFont("comicsansms", 30)
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                c2_pos=c2.get_pos()
                textpos.center = c2_pos
                screen.blit(text, textpos)
                
                #verificar se a carga em movimento sai do ecra. Se sair, o jogador perde
                if 0<c2_pos[0]< display_width and  0<c2_pos[1]<display_height: 
                    c2_pos=c2_pos # So para ter alguma coisa no if, nao faz nada, pode continuar
                else:
                    #quer dizer que esta fora do ecra e nao pode continuar
                    lost(level2)

                ########################################################################################################################
            
                c3.draw_charge(screen)
                font = pygame.font.SysFont("comicsansms", 50)
                text = font.render("-", 1, WHITE)
                textpos = text.get_rect()
                textpos.center = ((display_width/2+100),(display_height/2-22))
                screen.blit(text, textpos)


                c_vec=[]
                c_vec.append(c1)
                c_vec.append(c2)
                c_vec.append(c3)
                ####################################################

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
                            victory(level2)
                        

			
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


def level3():

	pygame.key.set_repeat(1,15)

	s = shoot(display_height)


        # Criacao de cargas ########################

        c1 = elec_charge()
        c2 = elec_charge()
        c3 = elec_charge()

        ###Origem do referencial
        Ox=display_width/2
        Oy=display_height/2


        # --- Criar efectivamente as cargas no screen ######
        c1.create_charge(screen,-700,Ox,Oy-100,DARK_BLUE)
        c2.create_charge(screen,-700,Ox,Oy,DARK_BLUE)
        c3.create_charge(screen,-700,Ox,Oy+100,DARK_BLUE)

        c_vec=[]
        c_vec.append(c1)
        c_vec.append(c2)
        c_vec.append(c3)



        ###############################################

        n_tries=0 #para contar o nr de tentativas do user
	shooter_angle=0
	ball_on_screen=False

        c1_move=False ##indica se a carga c1 se esta a movimentar
        collision=False ## da-me informacao sobre se esta ou nao a haver colisao entre fotao e eletrao
        first_entrance=True #Variavel auiliar para definir a trajectoria do fotao apos o choque

        ##ponto em torno do qual se da a rotacao
        Orotx = 0
        Oroty = 0

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
				elif event.key == pygame.K_s:
					shot=True
					ball_on_screen=True
                                        s.reset_wavepos() #para que a posicao inicial da onda nao seja a do tiro anterior
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



                # Explicacao do objectivo ##########################
                button("Menu",0,0,50,30,WHITE,GREEN,game_intro)
                pygame.draw.rect(screen,AQUA,(180,0,225,30))
                font = pygame.font.Font(None, 20)
                text = font.render("Use Compton scattering to reach both thresholds!!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (300,15)
                screen.blit(text, textpos)

                ##Informacao sobre o angulo de inclinacao
                pygame.draw.rect(screen,AQUA,(display_width/2+100,15,300,30))
                font = pygame.font.SysFont("comicsansms", 20)
                info_shooter_angle= "Angle: " + str(shooter_angle)
                text = font.render(info_shooter_angle, 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (display_width/2+200,30)
                screen.blit(text, textpos)

                ###Origem do referencial
                Ox=display_width/2
                Oy=display_height/2


		# --- Criar efectivamente as cargas no screen ######
                c1.draw_charge(screen)
                c2.draw_charge(screen)
                c3.draw_charge(screen)


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

                        if(collision==False):
                            angle = s.get_sh_angle() #angulo da trajectoria da onda
                        if(collision==True and first_entrance==True):
                            angle = s.get_sh_angle() - 0.5

                            ##ponto em torno do qual se da a rotacao
                            Orotx = pos[0]/cos(s.get_sh_angle())*(cos(s.get_sh_angle())-cos(angle))#-40*cos(s.get_sh_angle())
                            Oroty = pos[0]/cos(s.get_sh_angle())*(sin(s.get_sh_angle())-sin(angle))
                            first_entrance=False

                        s.wave_motion(screen,shot,vel,angle,Orotx,Oroty)

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

                        if c1_pos[0]-10<pos[0]<c1_pos[0]+10 and c1_pos[1]-10<pos[1]<c1_pos[1]+10:
                            c1_move=True #variavel definida no inicio do codigo do nivel
                            collision=True #variavel definida no inciio do nivel


                        ## NAO ESQUECER DE TESTAR DEPOIS SE A CARGA SAI DO SCREEN!!!
                        if c1_move==True:
                            c1.move_charge(0.2,-1)

			
 
		# --- Wrap-ups
		# Limit to 180 frames per second
		clock.tick(180)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()





def victory(level):
    
    lost = True 

    while lost:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.draw.rect(screen,AQUA,((display_width/2)-100,(display_height/2)-50,200,50))
        font = pygame.font.SysFont("comicsansms", 50)
        text = font.render("   You win!   ", 1, (20, 20, 20))
        textpos = text.get_rect()
        textpos.center = ((display_width/2),(display_height/2)-20)
        screen.blit(text, textpos)
        button("Again",(display_width/2)-100,(display_height/2),100,50,WHITE,GREEN,level)
        button("Menu",(display_width/2),(display_height/2),100,50,WHITE,GREEN,game_intro)

        pygame.display.update()
        clock.tick(10)


def lost(level):
    
    lose = True 

    while lose:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.draw.rect(screen,AQUA,((display_width/2)-100,(display_height/2)-50,200,50))
        font = pygame.font.SysFont("comicsansms", 50)
        text = font.render("   You lost!   ", 1, (20, 20, 20))
        textpos = text.get_rect()
        textpos.center = ((display_width/2),(display_height/2)-20)
        screen.blit(text, textpos)
        button("Again",(display_width/2)-100,(display_height/2),100,50,WHITE,GREEN,level)
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
        font = pygame.font.SysFont("comicsansms", 26)
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
#game_screen()
game_intro()
pygame.quit()
quit()

