#include <Arduino.h>
#include <Tone.h>
#include <math.h>

#define POTENTIOMETER 0
#define SPEAKER 11

Tone freq1;

void setup()
{
  Serial.begin(9600);
  freq1.begin(SPEAKER);
}

int potentiometer;
int multiplier;
int last_multiplier = 0;

void loop()
{
  potentiometer = analogRead(POTENTIOMETER);

  multiplier = (int)(((float)potentiometer - 0.0)*(12.0 - 0.0)/(1023.0 - 0.0) + 0.0);

  int freq = pow(2, (float)multiplier/12.0)*440;
  freq1.play(freq, 500);

  if (multiplier != last_multiplier)
  {
      Serial.println(freq);
      Serial.println(multiplier);
      last_multiplier = multiplier;
  }

  delay(10);
}

/*
Tone freq1;
Tone freq2;

const int DTMF_freq1[] = { 1336, 1209, 1336, 1477, 1209, 1336, 1477, 1209, 1336, 1477 };
const int DTMF_freq2[] = {  941,  697,  697,  697,  770,  770,  770,  852,  852,  852 };

void setup()
{
  Serial.begin(9600);
  freq1.begin(11);
  freq2.begin(12);
}

void playDTMF(uint8_t number, long duration)
{
  freq1.play(DTMF_freq1[number], duration);
  freq2.play(DTMF_freq2[number], duration);
}


void loop()
{
  int i;
  uint8_t phone_number[] = { 8, 6, 7, 5, 3, 0 ,9 };

  for(i = 0; i < sizeof(phone_number); i ++)
  {
    Serial.print(phone_number[i], 10);
    Serial.print(' ');
    playDTMF(phone_number[i], 500);
    delay(600);
  }

  Serial.println();
  delay(4000);
}
*/
