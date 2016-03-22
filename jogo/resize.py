
class resize_screen:

    def __init__(self,display_width,display_height,Ox_in,Oy_in,c_vec_in):
        #O screen de referencia neste caso vai ser o com as dimensoes (700,500) que foi para as quais o nivel foi feito e por isso e preciso escalar para outras dimensoes e as quantidades definidas de seguida sao uteis para isso
        self.srx=display_width/700.  #sr de screen ratio
        self.sry=display_height/500.
        self.scale=(self.srx+self.sry)/2 #grosseiramente, fiz a media


        self.Ox=Ox_in
        self.Oy=Oy_in
        self.c_vec=c_vec_in
        self.c_x = [] #coordenadas x das cargas utilizadas
        self.c_y = []
        self.tc_x= []
        self.tc_y= []
        

    def get_scale(self):
        return self.scale

    def get_srx(self):
        return self.srx

    def get_sry(self):
        return self.sry

    def get_charge_transform_x(self):

        i=0
        for c in self.c_vec:
             self.c_x.append(c.get_pos()[0])

             #No ref O (do centro do screen)
             self.c_x[i]=self.c_x[i]-self.Ox
             
             #Novas coordenadas no ref O
             self.tc_x.append(self.scale*self.c_x[i])
             i=i+1

        return self.tc_x

    def get_charge_transform_y(self):

        i=0
        for c in self.c_vec:
             self.c_y.append(c.get_pos()[1])

             #No ref O (do centro do screen)
             self.c_y[i]=self.c_y[i]-self.Oy
             
             #Novas coordenadas no ref O
             self.tc_y.append(self.scale*self.c_y[i])
             i=i+1


        return self.tc_y

    def get_trans_x(self):
        w=self.Ox+self.c_x[1]
        trans_x = -(w-self.Ox-self.tc_x[1])

        return trans_x

    def get_trans_y(self):
        h=self.Oy+self.c_y[1]
        trans_y = (h-self.Oy-self.tc_y[1])

        return trans_y

