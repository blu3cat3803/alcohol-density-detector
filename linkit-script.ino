void setup() {
    Serial.begin(9600);
}

void loop() {

    int sensorValue[5];
    int i;
    
    sensorValue[0] = analogRead(A0);
    sensorValue[1] = analogRead(A1);
    sensorValue[2] = analogRead(A2);
    sensorValue[3] = analogRead(A3);
    sensorValue[4] = analogRead(A4);

    for (i = 0; i < 5; i++) {
        Serial.print(sensorValue[i]);
        if (i != 4) Serial.print(":");
        else Serial.println();
    }
    delay(1000);

}
