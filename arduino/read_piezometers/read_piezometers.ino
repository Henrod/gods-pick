const int piezometer0 = A0, piezometer1 = A1;
const int OUT_0 = 3, OUT_1 = 4;
const int READS = 20;
int pula_leituras = 0;
void setup() {
  //Set piezometers as pullup input
  analogReference(INTERNAL);
  //Start the serial
  Serial.begin(9600);

  //Set digital output (2 pins)
  pinMode(OUT_0, OUTPUT);
  pinMode(OUT_1, OUTPUT);

}

int segurando = 0;
int count = 0;

void loop() {
  // put your main code here, to run repeatedly:
  int val0 = analogRead(piezometer0);
  int val1 = analogRead(piezometer1);
    if ((val0 >= 150 || val1 >= 150) && pula_leituras == 0) {
      segurando = !segurando;
      pula_leituras = 200;
    }
    if ( pula_leituras > 0)
      pula_leituras--;
 
 
   /* Serial.println("Sem apertar");*/
 
 count++;

   if (count == READS) {
      Serial.println(segurando ? 2 : 0);
      count = 0;
    }
    
   
  delay(20);
}
