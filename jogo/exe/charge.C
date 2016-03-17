#include <iostream>
#include <cmath>

using namespace std;

extern "C" double* charge_field(double q, double q_pos_x, double q_pos_y, double coord_x, double coord_y){

  //Definir o r*r usado depois no calculo do campo eletrico
  double r2 = (coord_x-q_pos_x)*(coord_x-q_pos_x) + (coord_y-q_pos_y)*(coord_y-q_pos_y); 

  double Er = q/r2;

  double Ex = (coord_x-q_pos_x)/sqrt(r2)*Er;
  double Ey = (coord_y-q_pos_y)/sqrt(r2)*Er;

  static double E[2];
  E[0] = Ex;
  E[1] = Ey;

  return E;
}
