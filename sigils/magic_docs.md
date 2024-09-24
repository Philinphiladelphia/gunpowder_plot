# Running turtlesim

ros2 run turtlesim turtlesim_node

ros2 run turtlesim turtle_teleop_key

# Running talker/listener

ros2 run demo_nodes_py talker
or
ros2 run demo_nodes_cpp talker

ros2 run demo_nodes_py listener

# The way I should be using ros:

Note: this is not a typical workflow / setup, so you could run into some issues. There will also not be many people able to help you, as I believe 98% of ROS (1) users would be doing the regular Catkin based approach combined with my suggestion (calling into libraries from ROS nodes).

I need to call powdersim libraries from an external ROS node. Basically make a ROS node that wraps the powdersim libraries.