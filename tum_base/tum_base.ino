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

  Serial.begin(9600);
  Serial.println("Hello from tum_base");
  Serial.println("palse:100");
}

void loop() {
   if (Serial.available()) { // if there's data coming in from the serial connection
    String inputString = Serial.readStringUntil('\n'); // read the incoming data until a newline character is received
    int colonIndex = inputString.indexOf(':'); // find the index of the colon character
    if (colonIndex >= 0) { // if the colon character is found
      String command = inputString.substring(0, colonIndex); // extract the command from the input string
      int time = inputString.substring(colonIndex + 1).toInt(); // extract the time from the input string and convert it to an integer
      // do something with the command and time variables
      Serial.print("running with recieved input:");
      Serial.println(inputString);            
      char control_char = command[0]; 
      switch(control_char) {
        case 'f':
          forward(time);
          palse(10);
          break;
        case 'b':
          backward(time);
          palse(10);
          break;
        case 'r':
          right(time);
          palse(10);
          break;
        case 'l':
          left(time);
          palse(10);
          break;
        case '>':
          rightDia(time);
          palse(10);
          break;
        case '<':
          leftDia(time);
          palse(10);
          break;
        case '-':
          turnaround(time);
          palse(10);
          break;
        case 't':
          turn(time);
          palse(10);
          break;
        case 'p':
          palse(time);
          break;
        default:
          // handle unknown command
          break;
      }       
    }
  }
}

void leftUpControl(int rpm){
  lum.write(map(rpm,-100,100,1000,2000));
}
void leftDownControl(int rpm){
  ldm.write(map(rpm,-100,100,1000,2000));
}
void rightUpControl(int rpm){
  rum.write(map(rpm,-100,100,1000,2000));
}
void rightDownControl(int rpm){
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

