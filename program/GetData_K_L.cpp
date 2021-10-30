/******************************************************************************\
GET CHINESE SIGN LANGUAGE RAW DATA BY USING KINECT V2 + LEAP MOTION
GREATED BY Raindrop Zheng, April 2020
SHANGHAI UNIVERSITY
\******************************************************************************/

#include <string>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <cstring>
#include <future>
#include <chrono>
#include <thread>
#include "Leap.h"
#include <Kinect.h>


using namespace Leap;
using namespace std;


class SampleListener : public Listener {
public:
	virtual void onInit(const Controller&);
	virtual void onConnect(const Controller&);
	virtual void onDisconnect(const Controller&);
	virtual void onExit(const Controller&);
	virtual void onFrame(const Controller&);
	virtual void onFocusGained(const Controller&);
	virtual void onFocusLost(const Controller&);
	virtual void onDeviceChange(const Controller&);
	virtual void onServiceConnect(const Controller&);
	virtual void onServiceDisconnect(const Controller&);

private:
};

const std::string fingerNames[] = { "Thumb", "Index", "Middle", "Ring", "Pinky" };
const std::string boneNames[] = { "Distal" };
const std::string stateNames[] = { "STATE_INVALID", "STATE_START", "STATE_UPDATE", "STATE_END" };

void SampleListener::onInit(const Controller& controller) {
	std::cout << "Initialized" << std::endl;
}

void SampleListener::onConnect(const Controller& controller) {
	std::cout << "Connected" << std::endl;
	controller.enableGesture(Gesture::TYPE_CIRCLE);
	controller.enableGesture(Gesture::TYPE_KEY_TAP);
	controller.enableGesture(Gesture::TYPE_SCREEN_TAP);
	controller.enableGesture(Gesture::TYPE_SWIPE);
}

void SampleListener::onDisconnect(const Controller& controller) {
	// Note: not dispatched when running in a debugger.
	std::cout << "Disconnected" << std::endl;
}

void SampleListener::onExit(const Controller& controller) {
	std::cout << "Exited" << std::endl;
}

void SampleListener::onFrame(const Controller& controller) {
	ofstream dataFileL;
	dataFileL.open("添加文件储存地址及文件名", ofstream::app);//Bixu Canlan Baowei Bu Bolang Binglie Anzhao
	// Get the most recent frame and report some basic information
	const Frame frame = controller.frame();
	//dataFileL << "Frame id: " << frame.id()
		//<< "  ";

	HandList hands = frame.hands();
	for (HandList::const_iterator hl = hands.begin(); hl != hands.end(); ++hl) {
		// Get the first hand
		const Hand hand = *hl;
		std::string handType = hand.isLeft() ? "Left hand" : "Right hand";
		//std::cout << std::string(2, ' ') << handType << ", id: " << hand.id()
			//<< ", palm position: " << hand.palmPosition() << std::endl;
		// Get the hand's normal vector and direction
		const Vector normal = hand.palmNormal();
		const Vector direction = hand.direction();
		cout << "LLL" << endl;
		dataFileL << hand.palmPosition() << "  ";
		// Calculate the hand's pitch, roll, and yaw angles


		// Get the Arm bone
		Arm arm = hand.arm();


		// Get fingers
		const FingerList fingers = hand.fingers();
		for (FingerList::const_iterator fl = fingers.begin(); fl != fingers.end(); ++fl) {
			const Finger finger = *fl;


			// Get finger bones
			for (int b = 0; b < 1; ++b) {
				Bone::Type boneType = static_cast<Bone::Type>(b);
				Bone bone = finger.bone(boneType);
				dataFileL << bone.prevJoint() << string(2, ' ');
			}
		}
		
	}
    dataFileL << "\n";
	// Get tools
	const ToolList tools = frame.tools();
	for (ToolList::const_iterator tl = tools.begin(); tl != tools.end(); ++tl) {
		const Tool tool = *tl;
		std::cout << std::string(2, ' ') << "Tool, id: " << tool.id()
			<< ", position: " << tool.tipPosition()
			<< ", direction: " << tool.direction() << std::endl;
	}

	// Get gestures
	const GestureList gestures = frame.gestures();
	for (int g = 0; g < gestures.count(); ++g) {
		Gesture gesture = gestures[g];

		switch (gesture.type()) {
		case Gesture::TYPE_CIRCLE:
		{
			CircleGesture circle = gesture;
			std::string clockwiseness;

			if (circle.pointable().direction().angleTo(circle.normal()) <= PI / 2) {
				clockwiseness = "clockwise";
			}
			else {
				clockwiseness = "counterclockwise";
			}

			// Calculate angle swept since last frame
			float sweptAngle = 0;
			if (circle.state() != Gesture::STATE_START) {
				CircleGesture previousUpdate = CircleGesture(controller.frame(1).gesture(circle.id()));
				sweptAngle = (circle.progress() - previousUpdate.progress()) * 2 * PI;
			}
			std::cout << std::string(2, ' ')
				<< "Circle id: " << gesture.id()
				<< ", state: " << stateNames[gesture.state()]
				<< ", progress: " << circle.progress()
				<< ", radius: " << circle.radius()
				<< ", angle " << sweptAngle * RAD_TO_DEG
				<< ", " << clockwiseness << std::endl;
			break;
		}
		case Gesture::TYPE_SWIPE:
		{
			SwipeGesture swipe = gesture;
			std::cout << std::string(2, ' ')
				<< "Swipe id: " << gesture.id()
				<< ", state: " << stateNames[gesture.state()]
				<< ", direction: " << swipe.direction()
				<< ", speed: " << swipe.speed() << std::endl;
			break;
		}
		case Gesture::TYPE_KEY_TAP:
		{
			KeyTapGesture tap = gesture;
			std::cout << std::string(2, ' ')
				<< "Key Tap id: " << gesture.id()
				<< ", state: " << stateNames[gesture.state()]
				<< ", position: " << tap.position()
				<< ", direction: " << tap.direction() << std::endl;
			break;
		}
		case Gesture::TYPE_SCREEN_TAP:
		{
			ScreenTapGesture screentap = gesture;
			std::cout << std::string(2, ' ')
				<< "Screen Tap id: " << gesture.id()
				<< ", state: " << stateNames[gesture.state()]
				<< ", position: " << screentap.position()
				<< ", direction: " << screentap.direction() << std::endl;
			break;
		}
		default:
			std::cout << std::string(2, ' ') << "Unknown gesture type." << std::endl;
			break;
		}
	}

	if (!frame.hands().isEmpty() || !gestures.isEmpty()) {
		std::cout << std::endl;
	}
	dataFileL.close();
}

void SampleListener::onFocusGained(const Controller& controller) {
	std::cout << "Focus Gained" << std::endl;
}

void SampleListener::onFocusLost(const Controller& controller) {
	std::cout << "Focus Lost" << std::endl;
}

void SampleListener::onDeviceChange(const Controller& controller) {
	std::cout << "Device Changed" << std::endl;
	const DeviceList devices = controller.devices();

	for (int i = 0; i < devices.count(); ++i) {
		std::cout << "id: " << devices[i].toString() << std::endl;
		std::cout << "  isStreaming: " << (devices[i].isStreaming() ? "true" : "false") << std::endl;
	}
}

void SampleListener::onServiceConnect(const Controller& controller) {
	std::cout << "Service Connected" << std::endl;
}

void SampleListener::onServiceDisconnect(const Controller& controller) {
	std::cout << "Service Disconnected" << std::endl;
}

template <class Interface>
inline void SafeRelease(Interface &pInterfaceToRelease)
{
	if (pInterfaceToRelease != NULL) {
		pInterfaceToRelease->Release();   //clear cache
		pInterfaceToRelease = NULL;
	}
}

const   string  get_name(int n);    //此函数判断出关节点的名字

const   string  get_name(int n)
{
	switch (n)
	{
	case    5:return    "elbowleft"; break;
	case    6:return    "wristleft"; break;
	case    9:return    "elbowright"; break;
	case    10:return    "wristright"; break;
	default:return "NULL";
	}
}

void GetLP()
{
	// Create a sample listener and controller
	SampleListener listener;
	Controller controller;

	// Have the sample listener receive events from the controller
	controller.addListener(listener);

	//if (argc > 1 && strcmp(argv[1], "--bg") == 0)
		controller.setPolicy(Leap::Controller::POLICY_BACKGROUND_FRAMES);

	// Keep this process running until Enter is pressed
	std::cout << "Press Enter to quit..." << std::endl;
	std::cin.get();

	// Remove the sample listener when done
	controller.removeListener(listener);
}

void GetK()
{

	HRESULT hr;
	IKinectSensor *sensor = nullptr;
	GetDefaultKinectSensor(&sensor);
	sensor->Open();                  //open sensor
									 //1:think how to control open or close sensor

	IFrameDescription *description = nullptr;

	int depthHeight = 0, depthWidth = 0;

	IDepthFrameSource *depthSource = nullptr;
	IDepthFrameReader *depthReader = nullptr;
	sensor->get_DepthFrameSource(&depthSource);
	depthSource->get_FrameDescription(&description);
	description->get_Height(&depthHeight);
	description->get_Width(&depthWidth);
	depthSource->OpenReader(&depthReader);

	ICoordinateMapper *mapper = nullptr;
	sensor->get_CoordinateMapper(&mapper);

	IBodyFrameSource *bodySource = nullptr;
	IBodyFrame *bodyFrame = nullptr;
	IBodyFrameReader *bodyReader = nullptr;
	sensor->get_BodyFrameSource(&bodySource);
	bodySource->OpenReader(&bodyReader);


	while (1)
	{
		while (bodyReader->AcquireLatestFrame(&bodyFrame) != S_OK);
		IBody *pbody[BODY_COUNT] = { 0 };//count the number of people
		hr = bodyFrame->GetAndRefreshBodyData(BODY_COUNT, pbody);   //catch people
		if (SUCCEEDED(hr))
		{

			for (int i = 0; i < BODY_COUNT; i++)
			{
				BOOLEAN isTracked = false;
				pbody[i]->get_IsTracked(&isTracked);
				if (SUCCEEDED(hr) && isTracked)
				{
					ofstream dataFileK;
					dataFileK.open("C:\\Users\\Administrator\\Desktop\\Gproject\\datasets\\train\\K_Anzhao_ZSJ_1.txt", ofstream::app);
					Joint joints[JointType_Count];
					hr = pbody[i]->GetJoints(JointType_Count, joints);
					if (SUCCEEDED(hr))
					{
						for (int j = 0; j < JointType_Count; j++)
						{
							int i = joints[j].JointType;
							if (i == 5 || i == 6 || i == 9 || i == 10)
							{
								string rt = get_name(joints[j].JointType);
								cout << "KKK" << endl;
								//cout << "Joint name: " << rt << "  " << joints[j].Position.X << "  " << joints[j].Position.Y << "  " << joints[j].Position.Z;
								dataFileK << joints[j].Position.X << "  " << joints[j].Position.Y << "  " << joints[j].Position.Z << "  ";

							}

						}
						//cout << endl;
						dataFileK << "\n";

					}
					dataFileK.close();
				}

			}
			SafeRelease(bodyFrame);

		}
	}
	sensor->Close();

}

int main() {

	thread lp(GetLP);
	thread k(GetK);
	lp.join();
	k.join();

	return 0;
}

/*python接口转换
extern "C"
{
	int cmain()
	{
		main();
		return 0;
	}
}*/