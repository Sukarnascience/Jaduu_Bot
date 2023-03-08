import rospy
from std_msgs.msg import String

def processWhatisSaid(data):
    print("Msg says : " + str(data))

def subcribe_listen():
    rospy.init_node("hareMe")
    rospy.Subscriber("u_listen",String, processWhatisSaid)

if __name__ == '__main__':
    subcribe_listen()
    rospy.spin()