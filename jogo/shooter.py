import pygame
from math import cos,sin
import ctypes 
from ctypes import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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
		self.t=0
		
	def get_ball_pos(self):
		position = (self.ball_pos_x,self.ball_pos_y)
		return position
	
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
		
		
        def kutta(self, screen, shot,B,Ex,Ey):
                lib = cdll.LoadLibrary('./ElecMag.so') # carrega-se a biblioteca partilhada, sendo possivel usar as funcoes presentes nela

                a = ctypes.CDLL('ElecMag.so')


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


                pos = a.MagField(t,self.ball_pos_x,self.ball_pos_y,self.ball_vx,self.ball_vy,Ex,Ey)

                if(shot==True):
			self.ball_pos_x0 = self.sh_pos_x + end_point_x 
			self.ball_pos_y0 = self.sh_pos_y - end_point_y
                        self.ball_pos_x = self.ball_pos_x0
                        self.ball_pos_y = self.ball_pos_y0
                        self.ball_vx = vel*cos(self.sh_angle)
                        self.ball_vy = vel*sin(self.sh_angle)
			self.t=0

                ht = 0.5;
		self.t=self.t+ht
		self.ball_pos_x = pos[0] 
		self.ball_pos_y = pos[1]
                self.ball_vx= pos[2]
                self.ball_vy=pos[3]
                
		
		
		
		
		
