const int piezometer0 = A0, piezometer1 = A1;
const int READS = 50;
const int N_FRACO = 3;
const int N_MEDIO = 3;
const int N_FORTE = 3;
const int OUT_0 = 3, OUT_1 = 4;

void setup() {
  //Set piezometers as pullup input
  analogReference(INTERNAL);
  //Start the serial
  Serial.begin(9600);

  //Set digital output (2 pins)
  pinMode(OUT_0, OUTPUT);
  pinMode(OUT_1, OUTPUT);

}

int out_val = 0x00;
int real_val = 0;
int count = 0;
int count_fraco = 0, count_medio = 0, count_forte = 0;
int estado = 0;

void loop() {
  // put your main code here, to run repeatedly:
  int val0 = analogRead(piezometer0);
  int val1 = analogRead(piezometer1);
  
  if (val0 >= 20 || val1 >= 20) {
    count_fraco++;
    if (val0 >= 20 && val1 >= 0)
      count_medio++;
 }
 else {
   /* Serial.println("Sem apertar");*/
 }
 count++;

 if (count == READS) {
    if (count_fraco >= N_FRACO) {
          if (count_medio >= N_MEDIO) {
            Serial.println(2);
          }
          else {
            Serial.println(1);
          }
    }
    else {
      Serial.println(0);
      
    }
    
    count = count_fraco = count_medio = count_forte = 0;
 }
  delay(20);
}
