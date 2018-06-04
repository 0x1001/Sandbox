#include <Arduino.h>

#define POTENTIOMETER_1 0
#define POTENTIOMETER_2 1

#define AVERAGE 20

void setup()
{
  Serial.begin(9600);
  delay(100);
  Serial.println("Hello Audio 1.0");
}

int potentiometer_1;
int potentiometer_2;

int last_potentiometer_1 = 0;
int last_potentiometer_2 = 0;

void loop()
{
  unsigned int avg_potentiometer_1 = 0;
  unsigned int avg_potentiometer_2 = 0;

  for (int i=0; i < AVERAGE; i++)
  {
    avg_potentiometer_1 += analogRead(POTENTIOMETER_1);
    avg_potentiometer_2 += analogRead(POTENTIOMETER_2);
  }

  potentiometer_1 = avg_potentiometer_1 / AVERAGE;
  potentiometer_2 = avg_potentiometer_2 / AVERAGE;

  if (potentiometer_1 != last_potentiometer_1)
  {
      Serial.print("A");
      Serial.println(potentiometer_1);
      last_potentiometer_1 = potentiometer_1;
  }

  if (potentiometer_2 != last_potentiometer_2)
  {
      Serial.print("B");
      Serial.println(potentiometer_2);
      last_potentiometer_2 = potentiometer_2;
  }

  delay(1);
}
