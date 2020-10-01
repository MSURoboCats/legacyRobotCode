#include <Servo.h>
#include <ctype.h>
#include <ros.h>
#include <robosub2018/Depth.h>
#include <robosub2018/MotorCommands.h>
#include <robosub2018/PneumaticCommand.h>
#include <robosub2018/Arm.h>
#include <std_msgs/Header.h>

ros::NodeHandle nh;
robosub2018::Depth depthMsg;
robosub2018::Arm armMsg;

ros::Publisher pubDepth("sensors/depth", &depthMsg);
ros::Publisher pubArm("borbcat/arm", &armMsg);

const int numMotors = 8;
const float maxThrust = 0.65
const int neutral = 1500;
const int scale = 400;

const float surfacePSI = 10.44;

/***** Start Pin Definitions *****/
const int depthPin = 0; // A0
const armPin = 33;
const handPin = 35;
const dropLeft = 37;
const dropRight = 39;
const leftTorpedo = 41;
const rightTorpedo = 43;

int motorPins[numMotors] = {
	2, // Port Forward
	3, // Starboard Forward
	4, // Fore Strafe
	5, // Aft Strafe
	6, // Fore Port Depth
	7, // Fore Starboard Depth
	8, // Aft Port Depth
	9  // Aft Starboard Depth
};

bool armDown = false;
bool handOpen = false;
/***** End Pin Definitions *****/

Servo motors[numMotors];

float directions[numMotors] = {1, 1, 1, 1, 1, 1, 1, 1};
int motorCommands[numMotors] = {neutral, neutral, neutral, neutral, neutral, neutral, neutral, neutral};

ros::Subscriber<robosub2018::MotorCommands> subMotorCommands("command/motor", &motorCommandCallback);
ros::Subscriber<robosub2018::PneumaticCommands> subPneuCommand("command/pneumatics" &pneumaticCommandCallback);


/***** Start Function Definitions *****/

void motorCommandCallback(const robosub2018::MotorCommands& commands) {
	for(int i = 0; i < numMotors; i++) {
		motorCommands[i] = percentToThrottle(commands.command[i], i);
	}
}


void motorUpdate() {
	for(int i = 0; i < numMotors; i++) {
		motors[i].writeMicroseconds(motorCommands[i]);
	}
}


int percentToThrottle(float t, int motor) {
	t = constrain(t, -1, 1);
	return int(1500 + t * scale * maxThrust * directions[motor]);
}


// There may be a better way to do this ...
void pneumaticCommandCallback(const robosub2018::PneumaticCommand& command) {
	switch(command.valve) {
		case 33:
			if(armDown) {
				digitalWrite(armPin, HIGH); // Double check high/low
			}
			else {
				digitalWrite(armPin, LOW);
			}
			armDown = !armDown;
			armUpdate();
			break;
		case 35:
			if(handOpen) {
				digitalWrite(handPin, HIGH); // double check
			}
			else {
				digitalWrite(handPin, LOW);
			}
			handOpen = !handOpen;
			armUpdate();
			break;
		case 37:
			digitalWrite(dropLeft, HIGH);
			delay(1000);
			digitalWrite(dropLeft, LOW);
			break;
		case 39:
			digitalWrite(dropRight, HIGH);
			delay(1000);
			digitalWrite(dropRight, LOW);
			break;
		case 41:
			digitalWrite(leftTorpedo, HIGH);
			delay(1000);
			digitalWrite(leftTorpedo, LOW);
			break;
		case 43:
			digitalWrite(rightTorpedo, HIGH);
			delay(1000);
			digitalWrite(rightTorpedo, LOW);
			break;
		default:
			// Probably log

	}	
}


void armUpdate() {
	armMsg.header = getHeader(armMsg.header);
	armMsg.armDown = armDown;
	armMsg.handOpen = handOpen;

	pubArm.publish(&armMsg);
}


void sensorUpdate() {
	depthMsg.header = getHeader(depthMsg.header);
	depthMsg.psi = (analogRead(depthPin) * 0.0048828125 - 1) * 12.5;

	if(surfacePSI == -1) {
		surfacePSI = depthMsg.psi;
	}

	// 12.5 max voltage
	// current is signal (depthPin)
	depthMsg.depth = ((analogRead(depthPin) * 0.0048828125 - 1) * 12.5 - surfacePSI) * 0.13197839577;
	pubDepth.publish(&depthMsg);
}


std_msgs::Header getHeader(std_msgs::Header h) {
	std_msgs::Header updated = std_msgs::Header();
	updated.seq = h.seq + 1;
	updated.stamp = nh.now();
	updated.frame_id = h.frame_id;
	return updated;
}

std_msgs::Header getHeader() {
	std_msgs::Header updated = std_msgs::Header();
	updated.seq = 0;
	updated.stamp = nh.now();
	updated.frame_id = "0";
	return updated;
}

/***** End Function Definitions *****/


/***** setup && loop *****/

void setup() {
	nh.initNode();
	nh.subscribe(subMotorCommand);
	nh.advertise(pubDepth);

	depthMsg.header = getHeader();
	depthMsg.header.frame_id = "depth";

	for(int i = 0; i < numMotors; i++) {
		motors[i].attach(motorPins[i]);
		motors[i].writeMicroseconds(neutral);
	}
	pinMode(armPin, OUTPUT);
	pinMode(handPin, OUTPUT);
	pinMode(dropLeft, OUTPUT);
	pinMode(dropRight, OUTPUT);
	pinMode(leftTorpedo, OUTPUT);
	pinMode(rightTorpedo, OUTPUT);
	//delay(1000);
}


void loop() {
	sensorUpdate();
	motorUpdate();
	nh.spinOnce();
}


