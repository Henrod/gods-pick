//Number of input pins
const int IN_PINS = 1;
//Number of output pins
const int OUT_PINS = 2;
//Delay between reads in ms
const int DELAY = 10;
//Needed reads
const int N_READS = 10;

//First analogic input pin used
const int INITIAL_IN_PIN = A0;
//which output pin is the least signficative
const int INITIAL_OUT_PIN = 3;
//Min analog value
const int MIN_VALUE = 0;
//Max analog value
const int MAX_VALUE = IN_PINS*1023;
const int STEP = (MAX_VALUE - MIN_VALUE) / (2 << OUT_PINS);

void setup() {
  //Set piezometers as pullup input
  //pinMode(piezometer0, INPUT);
  //pinMode(piezometer1, INPUT);
  
  //Start the serial
  Serial.begin(9600);

  //Set digital output (2 pins)
  for (int i = 0; i < OUT_PINS; i++)
    pinMode(INITIAL_OUT_PIN + i, OUTPUT);

}

int out_val = 0x00;
int count = 0;
void loop() {
  // put your main code here, to run repeatedly:
  int val = 0;
  int digital_val = 0;
  for (int i = 0; i < IN_PINS; i++)
    val += analogRead(INITIAL_IN_PIN + i);
  
  for (digital_val = 0; digital_val < (2 << OUT_PINS); digital_val++)
    if ((digital_val == 0 && val <= STEP) 
        || (val >= STEP * digital_val && val <= (STEP * (digital_val + 1)))
        || val >= (STEP * (digital_val + 1)))
        break;
  if (digital_val == out_val || count == 0) {
    count++;
    out_val = digital_val;
    if (count == N_READS) {
      count = 0;
      for (int i = 0; i < OUT_PINS; i++) {
        digitalWrite(INITIAL_OUT_PIN + i, out_val & (1 << i));
      }
    }
  }
  else {
    count = 0;
    out_val = digital_val;
  }
  Serial.println(val);
  
  delay(DELAY);
}
