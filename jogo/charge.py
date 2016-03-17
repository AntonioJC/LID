import pygame
from math import cos,sin
import ctypes 
from ctypes import *

DARK_RED = (178,34,34)

lib = cdll.LoadLibrary('./ElecMag.so') # carrega-se a biblioteca partilhada, sendo possivel usar as funcoes presentes nela

a = ctypes.CDLL('ElecMag.so')

# Campo de carga #############################################
a.charge_field.argtypes = [ ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
a.charge_field.restype = ctypes.POINTER(ctypes.c_double)

class elec_charge:

    def __init__(self):

        self.pos_x = 0
        self.pos_y = 0
        self.q = 1000
        self.radius=0
        self.mass=1

    def create_charge(self,screen,q,x,y,color):
        self.pos_x = x
        self.pos_y = y
        self.q = q
        self.radius=q*0.01
        pygame.draw.circle(screen, color, (int(self.pos_x), int(self.pos_y)), int(abs(q*0.01)), int(abs(q*0.01)))

    def get_mass_q(self):
        return (self.mass,self.q)

    def get_pos(self):
        return (self.pos_x,self.pos_y)

    def get_radius(self):
        return self.radius
        

    def get_E_field(self,x,y): #as variaveis dao a posicao em que se quer calcular o campo

        E = a.charge_field(self.q,self.pos_x,self.pos_y,x,y)
        return E

    def get_pos(self):
        return (self.pos_x,self.pos_y)

        
