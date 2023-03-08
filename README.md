# Jaduu_Bot
```
<launch>
    <node name="node1" pkg="jaduu_Bot" type="control_locomotion.py" output="screen"/>
    <node name="node2" pkg="jaduu_Bot" type="face_detection.py" output="screen"/>
    <node name="node3" pkg="jaduu_Bot" type="facial_expression.py" output="screen"/>
    <node name="node4" pkg="jaduu_Bot" type="talking_nlp.py" output="screen"/>
    <node name="node5" pkg="jaduu_Bot" type="telegram_bot.py" output="screen"/>
</launch>
TestRUN
multi_node_launch.launch
```