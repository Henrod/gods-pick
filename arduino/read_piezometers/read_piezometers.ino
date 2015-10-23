const int piezometer0 = A0, piezometer1 = A1;
const int READS = 50;
const int N_FRACO = 4;
const int N_MEDIO = 4;
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
  int val = analogRead(piezometer0);/* + analogRead(piezometer1);*/
  int out = 0;
  if (val >= 400)
    out++;
  if (val >= 700)
    out++;
  if (val >= 900)
    out++;
 
 /* Serial.println(val);*/
 if (val >= 4) {
    count_fraco++;
    if (val >= 9)
      count_medio++;
 }
 else {
   /* Serial.println("Sem apertar");*/
 }
 count++;

 if (count == READS) {
    if (count_fraco >= N_FRACO) {
       if (count_medio >= N_MEDIO)
          Serial.println("Medio apertado");
       else
          Serial.println("Pouco Apertado");
    }
   
    else
      Serial.println("NAO APERTADO");
    count = count_fraco = count_medio = count_forte = 0;
 }
  delay(10);
}
