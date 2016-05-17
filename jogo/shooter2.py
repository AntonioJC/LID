import pygame
from math import cos,sin
import math
import ctypes 
from ctypes import *
from charge import elec_charge

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255,215,0)
BLUE = (0,0,255)
DARK_RED = (178,34,34)

lib = cdll.LoadLibrary('./ElecMag.so') # carrega-se a biblioteca partilhada, sendo possivel usar as funcoes presentes nela

a = ctypes.CDLL('ElecMag.so')

# Campo magnetico ##########################################
a.MagField.argtypes = [ ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double] 

# o mesmo, mas agora para o retorno da funcao
a.MagField.restype = ctypes.POINTER(ctypes.c_double)
###########################################################


#Campo eletrico ########################################
a.ElectricField.argtypes = [ ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double] 

# o mesmo, mas agora para o retorno da funcao
a.ElectricField.restype = ctypes.POINTER(ctypes.c_double)
############################################################

# Campo de carga #############################################
a.charge_field.argtypes = [ ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
a.charge_field.restype = ctypes.POINTER(ctypes.c_double)

class shoot:
        
	def __init__(self,display_height):
	
		# ---- caracteristicas do shooter ------------------------------------#
		self.sh_angle=0
		self.sh_width=4
		self.sh_length=40
		
		#posicoes do ponto onde comeca a linha do shooter
		self.sh_pos_x=0
		self.sh_pos_y=display_height-5
		
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
		
                # ---- Posicao da onda -------#
		self.wave_pos_x=0
		self.wave_pos_y=0
                self.xrot=0
                self.yrot=0
                self.wave_init=0


                # variaveis uteis de teste
                self.first_entry=0
                self.last_entry=0
                self.wit=0
                self.pos_step=0

        def reset_wavepos(self):
                self.wave_pos_x=0
		self.wave_pos_y=0
                self.xrot=0
                self.yrot=0
                self.wave_init=0
                self.first_entry=0
                self.last_entry=0
                self.wit=0
		self.t=0


	def get_ball_pos(self):
		position = (self.ball_pos_x,self.ball_pos_y)
		return position
                
        def get_sh_angle(self):
                return self.sh_angle
	
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
			
		pygame.draw.circle(screen, GREEN, (int(self.ball_pos_x), int(self.ball_pos_y)), 1, 1)
		
		self.t=self.t+0.05
		v0=70
		g=9.8
		self.ball_pos_x = self.ball_pos_x0 + v0*cos(self.sh_angle)*self.t
		self.ball_pos_y = self.ball_pos_y0 - v0*sin(self.sh_angle)*self.t + 0.5*g*self.t*self.t



        def motion_in_field(self,screen,shot,charge,vel):

		end_point_x = self.sh_length*cos(self.sh_angle)
		end_point_y = self.sh_length*sin(self.sh_angle)

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


        def wave_motion(self,screen,shot,Ox,Oy,ki,wi,angle,theta,eta):

		end_point_x = self.sh_length*cos(self.sh_angle)
		end_point_y = self.sh_length*sin(self.sh_angle)

                if(shot==True):
			self.ball_pos_x0 = self.sh_pos_x + end_point_x 
			self.ball_pos_y0 = self.sh_pos_y - end_point_y
                        self.ball_pos_x = self.ball_pos_x0
                        self.ball_pos_y = self.ball_pos_y0
                        self.ball_vx = vel*cos(self.sh_angle)
                        self.ball_vy = -vel*sin(self.sh_angle)
			self.t=0


                amplitude = 5 # amplitude da onda

                y=0
                low_lim=0
                if(angle==self.sh_angle):
                        self.wave_init=self.sh_length
                
                else:
                        self.first_entry=1
                if(self.first_entry==1 and self.last_entry==0):
                        self.wave_init=self.wave_pos_x

                        self.first_entry=0
                        self.last_entry=1

                if self.last_entry==0:
                        self.wit=self.sh_length
                        while(self.wit>=self.sh_length and self.wit<=self.wave_pos_x):
                                x = self.wit
                                y = amplitude*math.sin(ki*(x-self.sh_length)-wi*self.t)

                                ###Rotacao
                                self.xrot = x*cos(-angle)-y*sin(-angle)
                                self.yrot = x*sin(-angle)+y*cos(-angle)


                                self.xrot = self.xrot + Ox
                                self.yrot = self.yrot + self.sh_pos_y-Oy
                
                                #screen.set_at((x, y), GREEN)
                                pygame.draw.circle(screen, BLUE, (int(self.xrot),int(self.yrot)), 2, 1)
                                self.wit+=0.5
 

                if self.last_entry==1:
                        self.wit = self.sh_length

                        w = wi/(1+eta*(1-cos(theta)))##calcula-se um novo w correspondente a frequencia do fotao difundido. 

                        k = w/wi*ki #numero de onda da onda difundida

                        while(self.wit>=self.sh_length and self.wit<=self.wave_init):
                                x = self.wit
                                y = amplitude*math.sin(k*(x-self.sh_length)-w*self.t)


                                ###Rotacao
                                self.xrot = x*cos(-self.sh_angle)-y*sin(-self.sh_angle)
                                self.yrot = x*sin(-self.sh_angle)+y*cos(-self.sh_angle)

                                self.xrot = self.xrot 
                                self.yrot = self.yrot + self.sh_pos_y
                
                                #screen.set_at((x, y), GREEN)
                                pygame.draw.circle(screen, DARK_RED, (int(self.xrot),int(self.yrot)), 2, 1)
                                self.wit+=0.5



                        self.wit=self.wave_init
                        while(self.wit>=self.wave_init and self.wit<=self.wave_pos_x):
                                x = self.wit
                                y = amplitude*math.sin(k*(x-self.sh_length)-w*self.t)

                                angle = theta+self.sh_angle
                                ###Rotacao
                                self.xrot = x*cos(-angle)-y*sin(-angle)
                                self.yrot = x*sin(-angle)+y*cos(-angle)


                                self.xrot = self.xrot + Ox 
                                self.yrot = self.yrot + self.sh_pos_y-Oy
                
                                #screen.set_at((x, y), GREEN)
                                pygame.draw.circle(screen, DARK_RED, (int(self.xrot),int(self.yrot)), 2, 1)
                                self.wit+=0.5


                self.t = self.t + 0.8
                h = 2
		self.wave_pos_x = self.wave_pos_x + wi/ki*h
                self.pos_step=wi/ki*h
		#self.ball_pos_y = self.ball_pos_y + self.ball_vy*h

        def get_wave_pos(self):#funcao que retorna a posicao da onda
                return(self.xrot,self.yrot)

        def get_wave_before_rot(self):
                return self.wave_pos_x

        def get_pos_step(self):
                return self.pos_step



		
        def kutta(self, screen, shot,B,Ex,Ey):
                # temos de relacionar os data types do c++ com os do python, entao identifica-se abaixo o tipo de cada argumento enviado para a funcao FullRK4 da biblioteca a para fazer esta conexao
                # ----> Ver data-types em: https://docs.python.org/2/library/ctypes.html#fundamental-data-types !!
                
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
                
"""
                a.ElectricField.argtypes = [ ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double] 

                # o mesmo, mas agora para o retorno da funcao
                a.ElectricField.restype = ctypes.POINTER(ctypes.c_double)

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
"""
        
		
		
		
