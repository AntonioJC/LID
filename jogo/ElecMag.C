#include <iostream>
#include <cmath>

using namespace std;

extern "C" double* MagField(double h, double x_0, double y_0, double vx_0, double vy_0, double Bz){

  //SO quero movimento no plano xy

  double B[3];
  double vz_0 = 0;
  double z_0 = 0;
  B[0] = 0;
  B[1] = 0;
  B[2] = Bz;


  double v = sqrt(vx_0*vx_0+vy_0*vy_0);

  double qm = 0.01;

  double V1_x, V1_y, V1_z, V1_vx, V1_vy, V1_vz;
  double V2_x, V2_y, V2_z, V2_vx, V2_vy, V2_vz;
  double V3_x, V3_y, V3_z, V3_vx, V3_vy, V3_vz;
  double V4_x, V4_y, V4_z, V4_vx, V4_vy, V4_vz;
 
  ////Calculo dos V1////////////////////////

  V1_x = h*vx_0;
  V1_y = h*vy_0;
  V1_z = h*vz_0;

  V1_vx = h*qm*(-vy_0*B[2] + vz_0*B[1]);

  V1_vy = h*qm*(-vz_0*B[0]+vx_0*B[2]);

  V1_vz = h*qm*(-vx_0*B[1]+vy_0*B[0]);
    
  ////V2////////////////////////

  V2_x = h*(vx_0 + V1_vx/2);
  V2_y = h*(vy_0 + V1_vy/2);
  V2_z = h*(vz_0 + V1_vz/2);

  V2_vx = h*qm*(-(vy_0 + V1_vy/2)*B[2] + (vz_0 + V1_vz/2)*B[1]);

  V2_vy = h*qm*(-(vz_0 + V1_vz/2)*B[0] + (vx_0 + V1_vx/2)*B[2]);

  V2_vz = h*qm*(-(vx_0 + V1_vx/2)*B[1] + (vy_0 + V1_vy/2)*B[0]);

  ////V3////////////////////////

  V3_x = h*(vx_0 + V2_vx/2);
  V3_y = h*(vy_0 + V2_vy/2);
  V3_z = h*(vz_0 + V2_vz/2);
    
  V3_vx = h*qm*(-(vy_0 + V2_vy/2)*B[2] + (vz_0 + V2_vz/2)*B[1]);

  V3_vy = h*qm*(-(vz_0 + V2_vz/2)*B[0] + (vx_0 + V2_vx/2)*B[2]);

  V3_vz = h*qm*(-(vx_0 + V2_vx/2)*B[1] + (vy_0 + V2_vy/2)*B[0]);

  ////V4////////////////////////

  V4_x = h*(vx_0 + V3_vx);
  V4_y = h*(vy_0 + V3_vy);
  V4_z = h*(vz_0 + V3_vz);

  V4_vx = h*qm*(-(vy_0 + V3_vy)*B[2] + (vz_0 + V3_vz)*B[1]);

  V4_vy = h*qm*(-(vz_0 + V3_vz)*B[0] + (vx_0 + V3_vx)*B[2]);

  V4_vz = h*qm*(-(vx_0 + V3_vx)*B[1] + (vy_0 + V3_vy)*B[0]);

  ///Calculo de t(n+1) a partir de t(n)///////////////////////

  x_0 = x_0 + (V1_x + 2*V2_x + 2*V3_x + V4_x)/6;
  y_0 = y_0 + (V1_y + 2*V2_y + 2*V3_y + V4_y)/6;
  z_0 = z_0 + (V1_z + 2*V2_z + 2*V3_z + V4_z)/6;

  vx_0 = vx_0 + (V1_vx + 2*V2_vx + 2*V3_vx + V4_vx)/6;
  vy_0 = vy_0 + (V1_vy + 2*V2_vy + 2*V3_vy + V4_vy)/6;
  vz_0 = vz_0 + (V1_vz + 2*V2_vz + 2*V3_vz + V4_vz)/6;


  //Vamos ver depois se esta correcao vai ser precisa

  ///Correçao///////////////////////////////
  /*
  if(CORRECTION == true){
    double crc = v/sqrt(vx_0*vx_0+vy_0*vy_0+vz_0*vz_0);//v(n)/v(n-1)

    vx_0 = crc*vx_0;
    vy_0 = crc*vy_0;
    vz_0 = crc*vz_0;
    }
  */


  static double pos[4];

  pos[0] = x_0;
  pos[1] = y_0;
  pos[2] = vx_0;
  pos[3] = vy_0;


  return pos;

}

extern "C" double* ElectricField(double t, double x_0, double y_0, double vx_0, double vy_0, double Ex, double Ey){

  //double qm=0.01;
  double qm = 0;

  x_0 = qm*Ex*t*t*0.5+vx_0*t+x_0;
  vx_0 = qm*Ex*t+vx_0;
  
  y_0 = -qm*Ey*t*t*0.5-vy_0*t+y_0;
  vy_0 = qm*Ey*t+vy_0;
  
  static double pose[4];
  
  pose[0] = x_0;
  pose[1] = y_0;
  pose[2] = vx_0;
  pose[3] = vy_0;


  return pose;

}

extern "C" double* ElectroMagField(double h, double x_0, double y_0, double vx_0, double vy_0, double Bz, double Ex, double Ey){

  //SO quero movimento no plano xy

  double B[3];
  double vz_0 = 0;
  double z_0 = 0;
  B[0] = 0;
  B[1] = 0;
  B[2] = Bz;

  double v = sqrt(vx_0*vx_0+vy_0*vy_0);

  double qm = 0.01;

  double V1_x, V1_y, V1_z, V1_vx, V1_vy, V1_vz;
  double V2_x, V2_y, V2_z, V2_vx, V2_vy, V2_vz;
  double V3_x, V3_y, V3_z, V3_vx, V3_vy, V3_vz;
  double V4_x, V4_y, V4_z, V4_vx, V4_vy, V4_vz;
 
  ////Calculo dos V1////////////////////////

  V1_x = h*vx_0;
  V1_y = h*vy_0;
  V1_z = h*vz_0;

  V1_vx = h*qm*(-vy_0*B[2] + vz_0*B[1]+Ex);

  V1_vy = h*qm*(-vz_0*B[0]+vx_0*B[2]+Ey);

  V1_vz = h*qm*(-vx_0*B[1]+vy_0*B[0]);
    
  ////V2////////////////////////

  V2_x = h*(vx_0 + V1_vx/2);
  V2_y = h*(vy_0 + V1_vy/2);
  V2_z = h*(vz_0 + V1_vz/2);

  V2_vx = h*qm*(-(vy_0 + V1_vy/2)*B[2] + (vz_0 + V1_vz/2)*B[1] +Ex);

  V2_vy = h*qm*(-(vz_0 + V1_vz/2)*B[0] + (vx_0 + V1_vx/2)*B[2] +Ey);

  V2_vz = h*qm*(-(vx_0 + V1_vx/2)*B[1] + (vy_0 + V1_vy/2)*B[0]);

  ////V3////////////////////////

  V3_x = h*(vx_0 + V2_vx/2);
  V3_y = h*(vy_0 + V2_vy/2);
  V3_z = h*(vz_0 + V2_vz/2);
    
  V3_vx = h*qm*(-(vy_0 + V2_vy/2)*B[2] + (vz_0 + V2_vz/2)*B[1] +Ex);

  V3_vy = h*qm*(-(vz_0 + V2_vz/2)*B[0] + (vx_0 + V2_vx/2)*B[2] +Ey);

  V3_vz = h*qm*(-(vx_0 + V2_vx/2)*B[1] + (vy_0 + V2_vy/2)*B[0]);

  ////V4////////////////////////

  V4_x = h*(vx_0 + V3_vx);
  V4_y = h*(vy_0 + V3_vy);
  V4_z = h*(vz_0 + V3_vz);

  V4_vx = h*qm*(-(vy_0 + V3_vy)*B[2] + (vz_0 + V3_vz)*B[1] +Ex);

  V4_vy = h*qm*(-(vz_0 + V3_vz)*B[0] + (vx_0 + V3_vx)*B[2] +Ey);

  V4_vz = h*qm*(-(vx_0 + V3_vx)*B[1] + (vy_0 + V3_vy)*B[0]);

  ///Calculo de t(n+1) a partir de t(n)///////////////////////

  x_0 = x_0 + (V1_x + 2*V2_x + 2*V3_x + V4_x)/6;
  y_0 = y_0 + (V1_y + 2*V2_y + 2*V3_y + V4_y)/6;
  z_0 = z_0 + (V1_z + 2*V2_z + 2*V3_z + V4_z)/6;

  vx_0 = vx_0 + (V1_vx + 2*V2_vx + 2*V3_vx + V4_vx)/6;
  vy_0 = vy_0 + (V1_vy + 2*V2_vy + 2*V3_vy + V4_vy)/6;
  vz_0 = vz_0 + (V1_vz + 2*V2_vz + 2*V3_vz + V4_vz)/6;


  //Vamos ver depois se esta correcao vai ser precisa

  ///Correçao///////////////////////////////
  /*
  if(CORRECTION == true){
    double crc = v/sqrt(vx_0*vx_0+vy_0*vy_0+vz_0*vz_0);//v(n)/v(n-1)

    vx_0 = crc*vx_0;
    vy_0 = crc*vy_0;
    vz_0 = crc*vz_0;
    }
  */


  static double pos[4];

  pos[0] = x_0;
  pos[1] = y_0;
  pos[2] = vx_0;
  pos[3] = vy_0;


  return pos;

}


extern "C" double* ElectricFieldWire(double t, double x_0, double y_0, double vx_0, double vy_0, double Ex, double qEy, double wpos){

  double qm=0.01;
  double Ey;

  Ey = qEy/abs(wpos-y_0);
  //cout << Ey << endl;

  x_0 = qm*Ex*t*t*0.5+vx_0*t+x_0;
  vx_0 = qm*Ex*t+vx_0;
  
  y_0 = -qm*Ey*t*t*0.5-vy_0*t+y_0;
  vy_0 = qm*Ey*t+vy_0;
  
  static double pose[4];
  
  pose[0] = x_0;
  pose[1] = y_0;
  pose[2] = vx_0;
  pose[3] = vy_0;


  return pose;

}


/*
extern "C" double* FullRK4(double t_f, double h, double a, double x_0, double y_0, double vy_0){
  
  double sa = sin(a);
  double ca = cos(a);
  double g = 9.8;
  double b = 0.1;
  double **Data;

  double V1_x, V1_y, V1_vx, V1_vy;
  double V2_x, V2_y, V2_vx, V2_vy;
  double V3_x, V3_y, V3_vx, V3_vy;
  double V4_x, V4_y, V4_vx, V4_vy;
 
  double t=0;
  double x = x_0;
  double y = y_0;
  
  double vx = 0;
  double vy = vy_0;

  int N = t_f/h;
  //cout << N << endl;
  Data = new double *[4];
  for(int i=0;i<4;i++)
    Data[i] = new double [N];

  for(int n=0;n<N;n++){

  ////Calculo dos V1////////////////////////

    V1_x = h*vx;
    V1_y = h*vy;

    V1_vx = h*(sa*sa*vy*vy*x - g*ca);
    V1_vy = h*(-2*vx*vy/x - b*sa*x*vy);
    
  ////V2////////////////////////

    V2_x = h*(vx + V1_vx/2);
    V2_y = h*(vy + V1_vy/2);

    V2_vx = h*(sa*sa*(vy + V1_vy/2)*(vy + V1_vy/2)*(x + V1_x/2) - g*ca);
    V2_vy = h*(-2*(vx + V1_vx/2)*(vy + V1_vy/2)/(x + V1_x/2) - b*sa*(vy + V1_vy/2)*(x + V1_x/2));

  ////V3///////////////////////

    V3_x = h*(vx + V2_vx/2);
    V3_y = h*(vy + V2_vy/2);

    V3_vx = h*(sa*sa*(vy + V2_vy/2)*(vy + V2_vy/2)*(x + V2_x/2) - g*ca);
    V3_vy = h*(-2*(vx + V2_vx/2)*(vy + V2_vy/2)/(x + V2_x/2) - b*sa*(vy + V2_vy/2)*(x + V2_x/2));

  ////V4////////////////////////

    V4_x = h*(vx + V3_vx);
    V4_y = h*(vy + V3_vy);

    V4_vx = h*(sa*sa*(vy + V3_vy)*(vy + V3_vy)*(x + V3_x) - g*ca);
    V4_vy = h*(-2*(vx + V3_vx)*(vy + V3_vy)/(x + V3_x) - b*sa*(vy + V3_vy)*(x + V3_x));

    ///Calculo de t(n+1) a partir de t(n)///////////////////////

    t = t + h;

    x = x + (V1_x + 2*V2_x + 2*V3_x + V4_x)/6;
    y = y + (V1_y + 2*V2_y + 2*V3_y + V4_y)/6;

    vx = vx + (V1_vx + 2*V2_vx + 2*V3_vx + V4_vx)/6;
    vy = vy + (V1_vy + 2*V2_vy + 2*V3_vy + V4_vy)/6;

    Data[0][n] = t;
    Data[1][n] = x*sa*cos(y);
    Data[2][n] = x*sa*sin(y);
    Data[3][n] = x*ca;

    //cout << Data[1][n]*Data[1][n]+Data[2][n]*Data[2][n]-Data[3][n]*Data[3][n]*tan(a)*tan(a) << endl; // da 0 por isso esta certo
  }

  static double arr[4];
  arr[0] = Data[0][0];
  arr[1] = Data[1][0];
  arr[2] = Data[2][0];
  arr[3] = Data[3][0];

  for(int i=0;i<4;i++)
    delete [] Data[i];

  return arr;

}

*/
