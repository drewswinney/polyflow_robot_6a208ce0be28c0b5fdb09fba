import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n6a208d27be28c0b5fdb0a15c",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "6a208d27be28c0b5fdb0a15c",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"6a208d02be28c0b5fdb0a047","mode":"speed","max_speed":31.4159,"reverse":false,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e541cd15153dec61d7af:state","name":"state","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a208d45be28c0b5fdb0a190","source_node_id":"6a208d35be28c0b5fdb0a17a","source_pin_id":"rear_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n6a208d29be28c0b5fdb0a162",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "6a208d29be28c0b5fdb0a162",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"6a208d06be28c0b5fdb0a06c","mode":"speed","max_speed":31.4159,"reverse":false,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e541cd15153dec61d7af:state","name":"state","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a208d44be28c0b5fdb0a18c","source_node_id":"6a208d35be28c0b5fdb0a17a","source_pin_id":"front_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n6a208d2bbe28c0b5fdb0a168",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "6a208d2bbe28c0b5fdb0a168",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"6a208d0ebe28c0b5fdb0a092","mode":"speed","max_speed":31.4159,"reverse":true,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e541cd15153dec61d7af:state","name":"state","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a208d47be28c0b5fdb0a194","source_node_id":"6a208d35be28c0b5fdb0a17a","source_pin_id":"front_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n6a208d2dbe28c0b5fdb0a16e",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "6a208d2dbe28c0b5fdb0a16e",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"6a208d10be28c0b5fdb0a0b0","mode":"speed","max_speed":31.4159,"reverse":true,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e541cd15153dec61d7af:state","name":"state","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a208d48be28c0b5fdb0a198","source_node_id":"6a208d35be28c0b5fdb0a17a","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="differential_drive",
            executable="differential_drive_node",
            name="differential_drive_n6a208d35be28c0b5fdb0a17a",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "6a208d35be28c0b5fdb0a17a",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"wheel_radius":0.05,"wheel_separation":0.3,"max_wheel_speed":1,"teleop_timeout_s":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e71bcd15153dec61d7f8:cmd_vel_teleop","name":"cmd_vel_teleop","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3e71bcd15153dec61d7f8:cmd_vel_automated","name":"cmd_vel_automated","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3e71bcd15153dec61d7f8:front_left_motor","name":"front_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:rear_left_motor","name":"rear_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:front_right_motor","name":"front_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:rear_right_motor","name":"rear_right_motor","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a208d42be28c0b5fdb0a188","source_node_id":"6a208d3abe28c0b5fdb0a182","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel_teleop"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a208d44be28c0b5fdb0a18c","target_node_id":"6a208d29be28c0b5fdb0a162","source_pin_id":"front_left_motor","target_pin_id":"command"},{"connection_id":"6a208d45be28c0b5fdb0a190","target_node_id":"6a208d27be28c0b5fdb0a15c","source_pin_id":"rear_left_motor","target_pin_id":"command"},{"connection_id":"6a208d47be28c0b5fdb0a194","target_node_id":"6a208d2bbe28c0b5fdb0a168","source_pin_id":"front_right_motor","target_pin_id":"command"},{"connection_id":"6a208d48be28c0b5fdb0a198","target_node_id":"6a208d2dbe28c0b5fdb0a16e","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="gamepad",
            executable="gamepad_node",
            name="gamepad_n6a208d3abe28c0b5fdb0a182",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "6a208d3abe28c0b5fdb0a182",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"device_index":0,"poll_rate_hz":60,"deadzone":0.05,"max_linear_speed":1,"max_angular_speed":2,"wheel_separation":0.3,"output_mode":"diff_drive"}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":60,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e702cd15153dec61d7da:axes","name":"axes","direction":"output","msg_type":"polyflow_msgs/GamepadAxes"},{"pin_id":"69a3e702cd15153dec61d7da:buttons","name":"buttons","direction":"output","msg_type":"polyflow_msgs/GamepadButtons"},{"pin_id":"69a3e702cd15153dec61d7da:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a208d42be28c0b5fdb0a188","target_node_id":"6a208d35be28c0b5fdb0a17a","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel_teleop"}]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
    ])