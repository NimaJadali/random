#define utm_input 8
#define led_output 13

void setup() {
  // put your setup code here, to run once:
  pinMode(utm_input, INPUT_PULLUP);
  pinMode(led_output, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
//  if (digitalRead(utm_input)) {
//    digitalWrite(ledPin, HIGH);
//    delay(50);
//  } else {
//    digitalWrite(ledPin, LOW);
//  } 

  digitalWrite(led_output, digitalRead(utm_input));
  delay(20);
}
