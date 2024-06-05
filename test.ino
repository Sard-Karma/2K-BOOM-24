void setup() {
  Serial.begin(9600);
  Serial1.begin(115200);
}

void loop() {  
  // Envoyer un message à l'Arduino MEGA
  // afficher le message envoyé sur le moniteur serie
  Serial1.println("1");
  delay(10000);
  Serial1.println("3");
  delay(10000);
  Serial1.println("4");
  delay(10000);
  Serial1.println("5");
  delay(10000);
  Serial1.println("h");
  delay(5000);
  Serial1.println("b");
  delay(5000);
  Serial1.println("g");
  delay(5000);
  Serial1.println("d");
  delay(5000);
  Serial1.println("p");
  delay(5000);
  Serial1.println("6");
  delay(10000);
  Serial1.println("r");
  delay(5000);
  Serial1.println("a");
  delay(5000);
  Serial1.println("v");
  delay(5000);
  Serial1.println("w");
  delay(5000);
  Serial1.println("2");
  delay(10000);
  Serial1.println("7");
  delay(10000);
}