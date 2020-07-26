#define RIGHTtrigPIN 2
#define RIGHTechoPIN 3
#define LEFTtrigPIN 4
#define LEFTechoPIN 5
#define MIDtrigPIN 6
#define MIDechoPIN 7
#define MOTOR_LEFT_BACK_PIN 8
#define MOTOR_LEFT_FRONT_PIN 9
#define MOTOR_RIGHT_FRONT_PIN 10
#define MOTOR_RIGHT_BACK_PIN 11

//8번전진 9번후진
 

//변수를 설정합니다. 



 

void setup() {
  
  pinMode(MOTOR_LEFT_BACK_PIN, OUTPUT);     //전진핀
  pinMode(MOTOR_LEFT_FRONT_PIN, OUTPUT);     //후진핀
  pinMode(MOTOR_RIGHT_FRONT_PIN, OUTPUT);     //전진핀
  pinMode(MOTOR_RIGHT_BACK_PIN, OUTPUT);     //후진핀  

  pinMode(RIGHTtrigPIN, OUTPUT); // trigPin을 출력으로 

  pinMode(RIGHTechoPIN, INPUT); // echoPin을 입력이다.

  pinMode(LEFTtrigPIN, OUTPUT); // trigPin을 출력으로 

  pinMode(LEFTechoPIN, INPUT); // echoPin을 입력이다.

  pinMode(MIDtrigPIN, OUTPUT); // trigPin을 출력으로 

  pinMode(MIDechoPIN, INPUT); // echoPin을 입력이다.

  Serial.begin(9600); // 시리얼 포트를 시작합니다.

}
int getUltraRight();
int getUltraLeft();
int getUltraMid();
void goLeft();
void goRight();
void goFront();
void goBack();
void stopMotor();



//////////////////////////////////////////////////////////////////////MAINㅜ

 
void loop() {
//////////////////////////////////////////////////////////////////////////RIGHT센서 부분
  
  int Right = getUltraRight();
  int Left = getUltraLeft();
  int Mid = getUltraMid();

  
  if(Right<=100&&Right>=0||Left<=100&&Left>=0||Mid<=100&&Mid>=0){
    Serial.println("front");
    //라즈베리파이로 시리얼 통신을 해준다
    //라즈베리파이 카메라 켜기
       if(Right<=30&&Right>=0||Left<=30&&Left>=0||Mid<=30&&Mid>=0){
        //너무 가까이 있으므로 카메라를 켜도 사람인지 아닌지 구분 못함
        //뒤로 이동 후 확인 사람이면 스피커 아닐 경우 턴
        
        goBack();
        delay(1500);
        //신호 보내기
        //사람일 경우 스피커 아닐경우 턴

        
        goRight();
        if(getUltraRight()<=30&&getUltraRight()>=0||getUltraLeft()<=30&&getUltraLeft()>=0||getUltraMid()<=30&&getUltraMid()>=0)
          goLeft();
          //180도 만큼 왼쪽으로 이동
          delay(1400);
       }
    
    
  }
  else{
    Serial.println("e");
    delay(800);
    stopMotor();
  }
  ////motor test
  if(Serial.available()>0){
    char c = Serial.read();
      if(c=='l'){
        goLeft();
        //delay(2000);
      }
      else if(c=='r'){
        goRight();
        //delay(2000);
      }
      else if(c=='b'){
        goBack();
        //delay(2000);
      }
      else if(c=='f'){
        goFront();
        //delay(2000);
      }
      else {
        stopMotor();
        //delay(2000);
      }
  }
  /////motor test
   
  //Serial.print(Right); Serial.print(" ");Serial.print(Mid); Serial.print(" ");Serial.print(Left); Serial.print("\n");
  delay(1000);
//////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////MAINㅗ




}

void stopMotor(){
  digitalWrite(MOTOR_LEFT_FRONT_PIN, LOW);  //전진 활성화
  digitalWrite(MOTOR_LEFT_BACK_PIN, LOW);   //전진 비활성화
  digitalWrite(MOTOR_RIGHT_FRONT_PIN, LOW);  //전진 활성화
  digitalWrite(MOTOR_RIGHT_BACK_PIN, LOW);   //전진 비활성화
}

void goFront(){
  digitalWrite(MOTOR_LEFT_FRONT_PIN, HIGH);  //전진 활성화
  digitalWrite(MOTOR_LEFT_BACK_PIN, LOW);   //전진 비활성화
  digitalWrite(MOTOR_RIGHT_FRONT_PIN, HIGH);  //전진 활성화
  digitalWrite(MOTOR_RIGHT_BACK_PIN, LOW);   //전진 비활성화
  
}

void goRight(){
  digitalWrite(MOTOR_LEFT_FRONT_PIN, HIGH);  //전진 활성화
  digitalWrite(MOTOR_LEFT_BACK_PIN, LOW);   //전진 비활성화
  digitalWrite(MOTOR_RIGHT_FRONT_PIN, LOW);  //전진 활성화
  digitalWrite(MOTOR_RIGHT_BACK_PIN, HIGH);   //전진 비활성화
}

void goLeft(){
  digitalWrite(MOTOR_LEFT_FRONT_PIN, LOW);  //전진 활성화
  digitalWrite(MOTOR_LEFT_BACK_PIN, HIGH);   //전진 비활성화
  digitalWrite(MOTOR_RIGHT_FRONT_PIN, HIGH);  //전진 활성화
  digitalWrite(MOTOR_RIGHT_BACK_PIN, LOW);   //전진 비활성화
}

void goBack(){
  digitalWrite(MOTOR_LEFT_FRONT_PIN, LOW);  //전진 활성화
  digitalWrite(MOTOR_LEFT_BACK_PIN, HIGH);   //전진 비활성화
  digitalWrite(MOTOR_RIGHT_FRONT_PIN, LOW);  //전진 활성화
  digitalWrite(MOTOR_RIGHT_BACK_PIN, HIGH);   //전진 비활성화
}

int getUltraRight(){
  long duration, distance;
  digitalWrite(RIGHTtrigPIN, LOW); //초음파 센서를 초기화 하는 과정입니다.

  delayMicroseconds(2);

  digitalWrite(RIGHTtrigPIN, HIGH);

  delayMicroseconds(10);

  digitalWrite(RIGHTtrigPIN, LOW);

  duration = pulseIn(RIGHTechoPIN, HIGH); // 트리거 핀에서 나온 펄스를 받아서 

  distance= duration*0.034/2; // 거리를 측정합니다. 
  if (distance >= 500 || distance <= 0){ //500보다 크거나, 0보다 작으면 측정이 불가하다는 것을 프린트합니다.

    return -1;

  }

  else {
    return distance;
  }

  //delay(500); //0.5초마다 , 그리고 아래의 과정은 모두 동일합니다.   
}

int getUltraLeft(){
  long duration, distance;
  digitalWrite(LEFTtrigPIN, LOW);

  delayMicroseconds(2);

  digitalWrite(LEFTtrigPIN, HIGH);

  delayMicroseconds(10);

  digitalWrite(LEFTtrigPIN, LOW);

  duration = pulseIn(LEFTechoPIN, HIGH);

  distance= duration*0.034/2;

 

  if (distance >= 500 || distance <= 0){
    return -1;
  }

  else {
    return distance;
  }

  //delay(500);  
}

int getUltraMid(){
  long duration, distance;
  digitalWrite(MIDtrigPIN, LOW);

  delayMicroseconds(2);

  digitalWrite(MIDtrigPIN, HIGH);

  delayMicroseconds(10);

  digitalWrite(MIDtrigPIN, LOW);

  duration = pulseIn(MIDechoPIN, HIGH);

  distance= duration*0.034/2;

 

  if (distance >= 500 || distance <= 0){
    return -1;

  }

  else {
    return distance;
  }

  //delay(500);  
}
