import rospy
from std_msgs.msg import String

def publishData():
    rospy.init_node("listenMe")
    pub = rospy.Publisher("u_listen", String, queue_size=10)

    i = 0
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        pub.publish("it's my : " + str(i))
        i += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        print("Publisher Started")
        publishData()

    except rospy.ROSInterruptException:
        print("Publisher Stoped")