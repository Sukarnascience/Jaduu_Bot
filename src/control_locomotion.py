import rospy
from std_msgs.msg import String

def callback(data):
    # process the data received from the input topic
    output_data = str(data)

    # publish the processed data to the output topic
    pub.publish(output_data)

if __name__ == '__main__':
    rospy.init_node('locomotion_control', anonymous=True)

    # create a subscriber to the input topic
    rospy.Subscriber("/move", String, callback)

    # create a publisher to the output topic
    pub = rospy.Publisher("/control_loco", String, queue_size=10)

    # spin the node to receive and process the input data and publish to the output topic
    rospy.spin()
