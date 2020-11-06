# BMI-Calculator
Building a BMI Calculator

//Import Libraries 
#include <Keypad.h>
#include <LiquidCrystal.h>

//Set up OUTPUT Pins to the LCD (Liquid Crystal Display)
const int rs = 13, en = 8, d4 = 9, d5 = 10, d6 = 11, d7 = 12;

// Create the LCD object by communicating the order of the pins)
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
//define the cymbols on the buttons of the keypads
char hexaKeys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','N'},
  {'C','0','E','D'}
};
byte rowPins[ROWS] = {3, 2, 1, 0}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {7, 6, 5, 4}; //connect to the column pinouts of the keypad

//initialize an instance of class NewKeypad
Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 


boolean enterWeight = false;
boolean enterHeight = false;
boolean final = false;

String num1, num2;
int answer;

float Umass;
float Uheight;
float BMI;

int dt0=1000;
int dt1=3000;
int dt2=5000;


void setup() {
  // put your setup code here, to run once:
lcd.begin (16,2);
lcd.setCursor (0,0);
lcd.print("Are you fit?");
delay (dt0);
lcd.setCursor (0,1);
lcd.print("BMI Calculator");
delay (dt1);
lcd.clear();
delay (dt1);

digitalWrite (key('E'), HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:

//Start first question
lcd.setCursor(0,0);
lcd.print("Input Your");
lcd.setCursor(0,1);
lcd.print("Weight (lbs)");

char key = myKeypad.getKey();

if (key != NO_KEY && (key=='1'||key=='2'||key=='3'||key=='4'||key=='5'||key=='6'||key=='7'||key=='8'||key=='9'||key=='0'))
  {
if (enterWeight!= true){
    lcd.clear();
    lcd.setCursor(0,0);
  
    char key = myKeypad.getKey();

    if (key != NO_KEY && (key=='1'||key=='2'||key=='3'||key=='4'||key=='5'||key=='6'||key=='7'||key=='8'||key=='9'||key=='0')){
        if (presentValue != true)
        {
         Umass = num1 + key;
          int numLength = num1.length();
          lcd.print(num1);
        }
      }
    else if (key != NO_KEY && key == 'C'){
        lcd.clear();
        presentValue = false;
        final = false;
        num1 = "";
        num2 = "";
      }

    else if (final == true && key != NO_KEY && 'E' == 0){
        lcd.clear();
          if (enterHeight== true){
            lcd.setCursor(0,0);
            lcd.print("Input Your");
            lcd.setCursor(0,1);
            lcd.print("Height (inches)");
            char key = myKeypad.getKey();
           
              if (key != NO_KEY && (key=='1'||key=='2'||key=='3'||key=='4'||key=='5'||key=='6'||key=='7'||key=='8'||key=='9'||key=='0')){
                  if (presentValue != true)
                {
                    Uweight = num2 + key;
                    int numLength = num2.length();
                    lcd.print(num2);
                }
           }
              else if (key != NO_KEY && key == 'C'){
                   lcd.clear();
                   presentValue = false;
                   final = false;
                   num2 = "";
            }
          }
    }
      if (final == true && key != NO_KEY && key == 'E'==0){
                   lcd.clear();
                   lcd.setCursor(0,0);
                   BMI=(Umass*0.454)/sq(Uheight*0.0254);
                   lcd.print("Your BMI = ");
                    lcd.print(BMI);
                    lcd.setCursor(0,1);
                    lcd.print(" Thank You! ");
                    delay(dt2);
                    lcd.clear();
               }         
      }
}
