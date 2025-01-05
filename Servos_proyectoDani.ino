#include <Servo.h>
Servo servoa;
Servo servob;
Servo servoEmpuje;

void setup() {

  Serial.begin(9600);
  pinMode(13, OUTPUT);
  servoa.attach(7);
  servob.attach(3);
  servoEmpuje.attach(10);
  // Para inicializar en una posicion espefica de 
  // de los servos.
  servoa.write(0);
  servob.write(0);
  servoEmpuje.write(90);
  
}
void loop() {
// Manejo de los servos
 if (Serial.available() > 0) {
  char op = Serial.read();
  

// para el servo a
  if (op == 's') 
  {
    servoa.write(65);
    delay(3000);
    servoa.write(0);
  }
  //para el servo b
  else if (op == 'b')
  {
    servob.write(65); 
    delay(3000);
    servob.write(0);
  }
  // Servo para el empuje de los materiales.
  else if(op == 'h')
  {
    servoEmpuje.write(180);
    delay(1000);
    servoEmpuje.write(90);
  }

  else if (op == 'g')
  {
    servoa.write(0);
     servob.write(0);
    servoEmpuje.write(90);
  }
  op == 'z';

 }

}
