#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>
#include <Servo.h>

// Set these to run example.

#define FIREBASE_HOST "//firebase id"
#define FIREBASE_AUTH "project secret"
#define WIFI_SSID "wifi name"
#define WIFI_PASSWORD "wifi password"
Servo scam;
void setup() {
  Serial.begin(9600);
  // pinMode(2, OUTPUT);

  // connect to wifi.
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.set("dir", 3);
  scam.attach(2); //D4
  scam.write(90);
}

int n=3, ang=45;


void loop() {
  // get value
  n = Firebase.getInt("dir"); {
    // handle error
//    if (n2 - n1 > 0) { //clockwise
//      Serial.println("clockwise");
//      scam.write(ang*(n2-n1));
//      delay(10 * (n2 - n1));
//      n2 = n1;
//    }
//
//    else if (n2 - n1 < 0) {
//      Serial.println("anticlockwise");
//      scam.write(ang*(n1-n2));
//      delay(10 * (n1 - n2));
//      n2 = n1;
//    }

    if (n == 1) {
      Serial.println("1");
      scam.write(0);
      delay(20);
    }

    if (n == 2) {
      Serial.println("2");
      scam.write(45);
      delay(20);
    }

    if (n == 3) {
      Serial.println("3");
      scam.write(90);
      delay(20);
    }

    if (n == 5) {
      Serial.println("180");
      scam.write(180);
      delay(20);
    }

    if (n == 4) {//south west
      Serial.println("135");
      scam.write(135);
      delay(20);
    }
  }

}
