// definition des variables
int bouton = 2;
int led = 5;
int buzzer = 8;
void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);     // configuration du pin 5 en mode OUTPUT
  pinMode(buzzer, OUTPUT);   // configuration du pin 8 en mode OUTPUT
  pinMode(bouton, INPUT_PULLUP);  // configuration du pin en mode INPUT avec activation PULLUP
}
void loop() {
  // lire l'etat du bouton
  int etat_bouton = digitalRead(bouton);
  //si le bouton est appuye, cad etat = LOW
  if (etat_bouton == LOW){
    digitalWrite(led, HIGH);//allumer les LED
    digitalWrite(buzzer, HIGH);//activer le buzzer
    
  }
  //sinon
  else{
    digitalWrite(led, LOW);//etindre le LED
    digitalWrite(buzzer, LOW);//desactiver le buzzer
  }
}
