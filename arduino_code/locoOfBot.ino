/**
 * @Author : Sukarna Jana
 * @Date   : 08/12/2022
 * @Title  : Control Locomotion 
 * @Device : Arduino UNO R3
 * @ROS Ver: ROS1 Noetic
 */
 
#include <ros.h>
#include <std_msgs/String.h>
#include <Servo.h>

#define ltServoPin 3
#define rtServoPin 5
#define lhServoPin 6
#define rhServoPin 9

Servo leftFoot;
Servo rightFoot;
Servo leftHip;
Servo rightHip;

ros::NodeHandle nh;
void doTask(const std_msgs::String& movementMsg);
ros::Subscriber<std_msgs::String> sub("control_loco", &doTask);

void setupServo(){
  leftFoot.attach(ltServoPin);
  leftHip.attach(lhServoPin);
  rightFoot.attach(rtServoPin);
  rightHip.attach(rhServoPin);

  leftFoot.write(90);
  rightFoot.write(90);
  leftHip.write(90);
  rightHip.write(90);
}

void moveFront(){}
void moveBack(){}
void moveLeft(){}
void moveRight(){}
void dance(String moveMode){}

void setup(){
  nh.initNode();
  nh.subscribe(sub);  
  setupServo();
}
void loop(){
  nh.spinOnce();
  delay(10);
}

void doTask(const std_msgs::String& movementMsg){
  if(movementMsg.data=="move_front"){
    moveFront();
  }
  else if(movementMsg.data=="move_back"){
    moveBack();
  }
  else if(movementMsg.data=="move_left"){
    moveLeft();
  }
  else if(movementMsg.data=="move_right"){
    moveRight();
  }
  else if(movementMsg.data=="dance1"){
    dance(movementMsg.data);
  }
}
