import pygame
from math import cos,sin
import ctypes 
from ctypes import *
import random
from charge import elec_charge

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255,165,0)
AQUA = (127,255,212)
DSBLUE = (0,191,255)
BLUE = (0,0,255)
LGRAY = (119,136,153)
BROWN = (255,228,181)
GRAY = (211,211,211)
GOLD = (255,215,0)

lib = cdll.LoadLibrary('./ElecMag.so') # carrega-se a biblioteca partilhada, sendo possivel usar as funcoes presentes nela

a = ctypes.CDLL('ElecMag.so')

#a=ctypes.WinDLL('EleMag.dll')

#a = lib['myFunc']#my func is double myFunc(double);


a.ElectricField.argtypes = [ ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]

a.ElectricFieldWire.argtypes = [ ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double] 

# o mesmo, mas agora para o retorno da funcao
a.ElectricField.restype = ctypes.POINTER(ctypes.c_double)

a.ElectricFieldWire.restype = ctypes.POINTER(ctypes.c_double)

a.charge_field.argtypes = [ ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
a.charge_field.restype = ctypes.POINTER(ctypes.c_double)

class shoot:
        
	def __init__(self):
	
		# ---- caracteristicas do shooter ------------------------------------#
		self.sh_angle=0
		self.sh_width=4
		self.sh_length=40
		
		#posicoes do ponto onde comeca a linha do shooter
		self.sh_pos_x=0
		self.sh_pos_y=495
		
		# ---- condicoes iniciais da bola ---- #
		self.ball_pos_x=0
		self.ball_pos_y=0
                self.ball_vx=0
                self.ball_vy=0;
		self.ball_pos_x0=0
		self.ball_pos_y0=0
                self.ball_vx0=0
                self.ball_vy0=0;
		self.ball_angle=0
                self.ball_m=1 # massa da particula lancada
                self.ball_q=10 # carga da particula lancada
		self.t=0
		
	def get_ball_pos(self):
		position = (self.ball_pos_x,self.ball_pos_y)
		return position

        def get_ball_vel(self):
                velocity = (self.ball_vx,self.ball_vy)
		return velocity

	
	def draw_shooter(self,screen,angle):
		self.sh_angle = angle
		end_point_x = self.sh_length*cos(angle)
		end_point_y = self.sh_length*sin(angle)
		pygame.draw.line(screen, WHITE, (self.sh_pos_x, self.sh_pos_y), (self.sh_pos_x+end_point_x, self.sh_pos_y-end_point_y),self.sh_width)
		
	def draw_ball(self,screen,shot):

		end_point_x = self.sh_length*cos(self.sh_angle)
		end_point_y = self.sh_length*sin(self.sh_angle)
		
		# faz-se o teste de se a bola acabou de ser disparada, ou seja, para ver se e a primeira vez que a funcao esta a ser chamada de forma 
		# a actualizar a posicao da bola dependendo do angulo do shooter
		if(shot==True):
			self.ball_pos_x0 = self.sh_pos_x + end_point_x 
			self.ball_pos_y0 = self.sh_pos_y - end_point_y
			self.t=0
			
		pygame.draw.circle(screen, GREEN, (int(self.ball_pos_x), int(self.ball_pos_y)), 5, 5)
		
		self.t=self.t+0.05
		v0=70
		g=9.8
		self.ball_pos_x = self.ball_pos_x0 + v0*cos(self.sh_angle)*self.t
		self.ball_pos_y = self.ball_pos_y0 - v0*sin(self.sh_angle)*self.t + 0.5*g*self.t*self.t
		
	
        def motion_in_field(self,screen,shot,Ex,Ey):

                vel=4;
                if(shot==True):
			self.ball_pos_x0 = self.sh_pos_x + end_point_x 
			self.ball_pos_y0 = self.sh_pos_y - end_point_y
                        self.ball_pos_x = self.ball_pos_x0
                        self.ball_pos_y = self.ball_pos_y0
                        self.ball_vx = vel*cos(self.sh_angle)
                        self.ball_vy = vel*sin(self.sh_angle)
			self.t=0

               	pygame.draw.circle(screen, GREEN, (int(self.ball_pos_x), int(self.ball_pos_y)), 10, 5)

                pos = a.ElectricField(self.t,self.ball_pos_x,self.ball_pos_y,self.ball_vx,self.ball_vy,Ex,Ey)

                ht = .05;
		self.t=self.t+ht
		self.ball_pos_x = pos[0] 
		self.ball_pos_y = pos[1]
                self.ball_vx= pos[2]
                self.ball_vy=pos[3]




        def draw_detector(self,screen):
                #camadas up
                pygame.draw.rect(screen,WHITE,(100,75,520,5))
                pygame.draw.rect(screen,LGRAY,(120,80,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,85,480,10))
                pygame.draw.rect(screen,LGRAY,(120,95,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,100,480,10))
                pygame.draw.rect(screen,LGRAY,(120,110,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,115,480,10))

                #separadores up
                pygame.draw.rect(screen,LGRAY,(210,80,2,45))
                pygame.draw.rect(screen,LGRAY,(270,80,2,45))
                pygame.draw.rect(screen,LGRAY,(330,80,2,45))
                pygame.draw.rect(screen,LGRAY,(390,80,2,45))
                pygame.draw.rect(screen,LGRAY,(450,80,2,45))
                pygame.draw.rect(screen,LGRAY,(510,80,2,45)) 

                #inner detector
                pygame.draw.rect(screen,GRAY,(120,125,480,175))
                pygame.draw.rect(screen,GOLD,(120,170,480,90))
                pygame.draw.rect(screen,BLACK,(120,212.5,480,5))

                #camadas down
                pygame.draw.rect(screen,DSBLUE,(120,300,480,10))
                pygame.draw.rect(screen,LGRAY,(120,310,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,315,480,10))
                pygame.draw.rect(screen,LGRAY,(120,325,480,5))
                pygame.draw.rect(screen,DSBLUE,(120,330,480,10))
                pygame.draw.rect(screen,LGRAY,(120,340,480,5))
                pygame.draw.rect(screen,WHITE,(100,345,520,5))

                #separadores down
                pygame.draw.rect(screen,LGRAY,(210,300,2,45))
                pygame.draw.rect(screen,LGRAY,(270,300,2,45))
                pygame.draw.rect(screen,LGRAY,(330,300,2,45))
                pygame.draw.rect(screen,LGRAY,(390,300,2,45))
                pygame.draw.rect(screen,LGRAY,(450,300,2,45))
                pygame.draw.rect(screen,LGRAY,(510,300,2,45)) 
                 
                #barreiras left
                pygame.draw.rect(screen,WHITE,(0,180,100,60))

                pygame.draw.rect(screen,LGRAY,(115,80,5,265))
                pygame.draw.rect(screen,WHITE,(110,75,5,270))
                pygame.draw.rect(screen,LGRAY,(105,80,5,265))
                pygame.draw.rect(screen,WHITE,(100,75,5,270))

                #barreiras right
                pygame.draw.rect(screen,WHITE,(620,180,90,60))

                pygame.draw.rect(screen,LGRAY,(600,80,5,265))
                pygame.draw.rect(screen,WHITE,(605,75,5,270))
                pygame.draw.rect(screen,LGRAY,(610,80,5,265))
                pygame.draw.rect(screen,WHITE,(615,75,5,270))
                

        def motion_in_charge_field(self,screen,shot,charge,vel):
                

		end_point_x = self.sh_length*cos(self.sh_angle)
		end_point_y = self.sh_length*sin(self.sh_angle)

                #vel=10;
                if(shot==True):
			self.ball_pos_x0 = self.sh_pos_x + end_point_x 
			self.ball_pos_y0 = self.sh_pos_y - end_point_y
                        self.ball_pos_x = self.ball_pos_x0
                        self.ball_pos_y = self.ball_pos_y0
                        self.ball_vx = vel*cos(self.sh_angle)
                        self.ball_vy = -vel*sin(self.sh_angle)
			self.t=0

               	pygame.draw.circle(screen, GREEN, (int(self.ball_pos_x), int(self.ball_pos_y)), 2, 2)

                i=0
                Ex=[]
                Ey=[]
                for ch in charge:
                        E = ch.get_E_field(self.ball_pos_x,self.ball_pos_y)
                        Ex.append(E[0])
                        Ey.append(E[1])
                        i = i+1

                """
                E = charge[0].get_E_field(self.ball_pos_x,self.ball_pos_y)
                #print E[0] Se imprimir os valores de E novamente depois de declarar o E2, eles ficam com os valores iguais ao E2. WTF??????????????????????????????????????????????????????????? Por isso tenho de os guardar logo no Ex e Ey antes de declarar o E2
                Ex = E[0]
                Ey = E[1]

                E2 = charge[1].get_E_field(self.ball_pos_x,self.ball_pos_y) 
                Ex2 =E2[0]
                Ey2 =E2[1]
"""


                # ball's charge
                qm = self.ball_q/self.ball_m


                # agora tenho de somar as contribuicoes de cada carga para o campo aplicado na bola
                j=0
                sum_Ex=0
                sum_Ey=0
                while(j<i):
                        sum_Ex = sum_Ex + Ex[j]
                        sum_Ey = sum_Ey + Ey[j]
                        j = j+1

                
                h = .05
                self.ball_vx= self.ball_vx + qm*sum_Ex*h
                self.ball_vy= self.ball_vy + qm*sum_Ey*h
		self.ball_pos_x = self.ball_pos_x + self.ball_vx*h
		self.ball_pos_y = self.ball_pos_y + self.ball_vy*h

	
        def kutta(self, screen, shot,B,Ex,Ey):
 
                """

                # temos de relacionar os data types do c++ com os do python, entao identifica-se abaixo o tipo de cada argumento enviado para a funcao FullRK4 da biblioteca a para fazer esta conexao
                # ----> Ver data-types em: https://docs.python.org/2/library/ctypes.html#fundamental-data-types !!
                a.MagField.argtypes = [ ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double] 

                # o mesmo, mas agora para o retorno da funcao
                a.MagField.restype = ctypes.POINTER(ctypes.c_double)
                """

		end_point_x = self.sh_length*cos(self.sh_angle)
		end_point_y = self.sh_length*sin(self.sh_angle)
		
		# faz-se o teste de se a bola acabou de ser disparada, ou seja, para ver se e a primeira vez que a funcao esta a ser chamada de forma 
		# a actualizar a posicao da bola dependendo do angulo do shooter
                """             
                vel = 4
		if(shot==True):
			self.ball_pos_x0 = self.sh_pos_x + end_point_x 
			self.ball_pos_y0 = self.sh_pos_y - end_point_y
                        self.ball_pos_x = self.ball_pos_x0
                        self.ball_pos_y = self.ball_pos_y0
                        self.ball_vx = vel*cos(self.sh_angle)
                        self.ball_vy = vel*sin(self.sh_angle)
			self.t=0
			
		pygame.draw.circle(screen, GREEN, (int(self.ball_pos_x), int(self.ball_pos_y)), 5, 5)
		

                # chamar a funcao do c++

                h = 0.1 #step
                pos = a.MagField(h,self.ball_pos_x,self.ball_pos_y,self.ball_vx,self.ball_vy,B)

		self.t=self.t+h
		self.ball_pos_x = pos[0] 
		self.ball_pos_y = pos[1]
                self.ball_vx= pos[2]
                self.ball_vy=pos[3]
                """


                vel=4;
                if(shot==True):
			self.ball_pos_x0 = self.sh_pos_x + end_point_x 
			self.ball_pos_y0 = self.sh_pos_y - end_point_y
                        self.ball_pos_x = self.ball_pos_x0
                        self.ball_pos_y = self.ball_pos_y0
                        self.ball_vx = vel*cos(self.sh_angle)
                        self.ball_vy = vel*sin(self.sh_angle)
			self.t=0

               	pygame.draw.circle(screen, GREEN, (int(self.ball_pos_x), int(self.ball_pos_y)), 5, 5)

                pos = a.ElectricField(self.t,self.ball_pos_x,self.ball_pos_y,self.ball_vx,self.ball_vy,Ex,Ey)

                ht = .05;
		self.t=self.t+ht
		self.ball_pos_x = pos[0] 
		self.ball_pos_y = pos[1]
                self.ball_vx= pos[2]
                self.ball_vy=pos[3]

        def ElectricFieldWire(self, screen, shot,B,Ex,Ey,w_pos):

		end_point_x = self.sh_length*cos(self.sh_angle)
		end_point_y = self.sh_length*sin(self.sh_angle)
	
                vel=4;
                if(shot==True):
			self.ball_pos_x0 = self.sh_pos_x + end_point_x 
			self.ball_pos_y0 = self.sh_pos_y - end_point_y
                        self.ball_pos_x = self.ball_pos_x0
                        self.ball_pos_y = self.ball_pos_y0
                        self.ball_vx = vel*cos(self.sh_angle)
                        self.ball_vy = vel*sin(self.sh_angle)
			self.t=0

               	pygame.draw.circle(screen, GREEN, (int(self.ball_pos_x), int(self.ball_pos_y)), 5, 5)

                pos = a.ElectricFieldWire(self.t,self.ball_pos_x,self.ball_pos_y,self.ball_vx,self.ball_vy,Ex,Ey,w_pos)

                ht = .05;
		self.t=self.t+ht
		self.ball_pos_x = pos[0] 
		self.ball_pos_y = pos[1]
                self.ball_vx= pos[2]
                self.ball_vy=pos[3]

                
        def collisions(self, screen, shot, hcol,velcol):
                
                if(shot==True):
			self.t=0
          
                tcol = self.t
                #velcol = 0.2*hcol-20
                htcol = 4
                #self.t=self.t+htcol
                tcol = tcol + htcol
                pygame.draw.circle(screen, RED, (int(600-velcol*tcol), int(hcol)), 5, 5)
                col_pos = 600-velcol*tcol
                return col_pos
        
        def simulation(self, screen):
                
                rpos = random.randint(0,1)
                hpos = random.randint(100,330)
                xpos = random.randint(150,600)
                hpos2 = random.randint(100,330)
                xpos2 = random.randint(150,600)
                hpos3 = random.randint(100,330)
                xpos3 = random.randint(150,600)
                p = 2
                i=0

                while i<20:
                        pygame.draw.circle(screen, RED, (int(xpos-p*rpos), int(hpos)), 3, 3)
                        pygame.draw.circle(screen, BLUE, (int(xpos2-p*rpos), int(hpos2)), 3, 3)
                        pygame.draw.circle(screen, GREEN, (int(xpos3-p*rpos), int(hpos3)), 3, 3)
                        simpos = [(xpos-p*rpos),hpos,(xpos2-p*rpos),hpos2,(xpos3-p*rpos),hpos3]
                        #print str(simpos[0]) + " , " + str(simpos[1])
                        i=i+1

                #print str(simpos[0]) + " , " + str(simpos[1])

                return simpos

        def col_recoil(self,screen, spos1,spos2,stop):

                if stop:
                        self.ball_vx=0;
                        self.ball_vy=0;

                tcol = self.t
                velcol = 10
                htcol = 4
                #self.t=self.t+htcol
                tcol = tcol + htcol
                self.ball_vx=0.2*self.ball_vx;
                self.ball_vy=0.2*self.ball_vy;
                #pygame.draw.circle(screen, AQUA, (int(spos1), int(spos2+velcol*tcol)), 10, 10)
                pygame.draw.rect(screen,AQUA,(400,0,205,30))
                font = pygame.font.Font(None, 20)
                text = font.render("Objective: Collision!!", 1, BLACK)
                textpos = text.get_rect()
                textpos.center = (300,15)
                screen.blit(text, textpos)


        def counter(self,shot,detect):
                
                count=self.t
                #base=7
                if(shot==True):
			self.t=0
                        #base=0

                if detect:
                        count=count+1
                        #print count
                        #print base

                return count


        def magkutta(self, screen, shot,B,Ex,Ey):
                        
                

                # temos de relacionar os data types do c++ com os do python, entao identifica-se abaixo o tipo de cada argumento enviado para a funcao FullRK4 da biblioteca a para fazer esta conexao
                # ----> Ver data-types em: https://docs.python.org/2/library/ctypes.html#fundamental-data-types !!
                a.MagField.argtypes = [ ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double] 

                # o mesmo, mas agora para o retorno da funcao
                a.MagField.restype = ctypes.POINTER(ctypes.c_double)
                

		end_point_x = self.sh_length*cos(self.sh_angle)
		end_point_y = self.sh_length*sin(self.sh_angle)
		
		# faz-se o teste de se a bola acabou de ser disparada, ou seja, para ver se e a primeira vez que a funcao esta a ser chamada de forma 
		# a actualizar a posicao da bola dependendo do angulo do shooter
        
                vel = 4
		if(shot==True):
			self.ball_pos_x0 = self.sh_pos_x + end_point_x 
			self.ball_pos_y0 = self.sh_pos_y - end_point_y
                        self.ball_pos_x = self.ball_pos_x0
                        self.ball_pos_y = self.ball_pos_y0
                        self.ball_vx = vel*cos(self.sh_angle)
                        self.ball_vy = vel*sin(self.sh_angle)
			self.t=0
			
		pygame.draw.circle(screen, GREEN, (int(self.ball_pos_x), int(self.ball_pos_y)), 5, 5)
		

                # chamar a funcao do c++

                h = 0.1 #step
                pos = a.MagField(h,self.ball_pos_x,self.ball_pos_y,self.ball_vx,self.ball_vy,B)

		self.t=self.t+h
		self.ball_pos_x = pos[0] 
		self.ball_pos_y = pos[1]
                self.ball_vx= pos[2]
                self.ball_vy=pos[3]
                
