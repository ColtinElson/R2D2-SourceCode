#include <AFMotor.h>

AF_DCMotor motor(1, MOTOR12_64KHZ);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode( 2, OUTPUT );
}

void loop() {
  // put your main code here, to run repeatedly:
  char key = Serial.read();
  if (key == 'w') {
    motor.run(RELEASE);
    delay(100);
    motor.run(FORWARD);
    motor.setSpeed(250);
  }
  else if (key == 's') {
    motor.run(RELEASE);
    delay(100);
    motor.run(BACKWARD);
    motor.setSpeed(200);
  }
  else if (key == 'a' || key == 'd') {
    motor.run(RELEASE);
  }
  
  delay(500);
}
