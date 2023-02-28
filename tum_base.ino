#include <Servo.h>

int leftup = 2;
int leftdown = 4;
int rightup = 13;
int rightdown = 11;
Servo lum;
Servo rum;
Servo ldm;
Servo rdm;

void setup() {
  pinMode(leftup, OUTPUT);
  pinMode(leftdown, OUTPUT);
  pinMode(rightup, OUTPUT);
  pinMode(rightdown, OUTPUT);
  lum.attach(leftup);
  ldm.attach(leftdown);
  rum.attach(rightup);
  rdm.attach(rightdown);

}

void loop() {
  forward(5000);
  palse(5000);
}

int leftUpControl(int rpm){
  lum.write(map(rpm,-100,100,1000,2000));
}
int leftDownControl(int rpm){
  ldm.write(map(rpm,-100,100,1000,2000));
}
int rightUpControl(int rpm){
  rum.write(map(rpm,-100,100,1000,2000));
}
int rightDownControl(int rpm){
  rdm.write(map(rpm,-100,100,1000,2000));
}

void forward(int msec){
  leftUpControl(95);//left positive
  leftDownControl(95);
  rightUpControl(-100);//right negative
  rightDownControl(-100);
  delay(msec); 
}

void backward(int msec){
  leftUpControl(-100);
  leftDownControl(-100);
  rightUpControl(100);
  rightDownControl(100);
  delay(msec); 
}

void right(int msec){
  leftUpControl(100);
  leftDownControl(-100);
  rightUpControl(100);
  rightDownControl(-100);
  delay(msec);
}

void left(int msec){
  leftUpControl(-100);
  leftDownControl(100);
  rightUpControl(-100);
  rightDownControl(100);
  delay(msec);
}

void rightDia(int msec){
  leftUpControl(100);
  rightDownControl(-100);
  delay(msec);  
}

void leftDia(int msec){
  leftDownControl(100);
  rightUpControl(-100);
  delay(msec); 
}

void turnaround(int msec){
  leftUpControl(100);
  leftDownControl(100);
  rightUpControl(100);
  rightDownControl(100);
  delay(msec);
}

void turn(int msec){
  leftUpControl(100);
  rightUpControl(100);
  delay(msec);  
}

void palse(int msec){
  leftUpControl(0);
  leftDownControl(0);
  rightUpControl(0);
  rightDownControl(0);
  delay(msec);
}
