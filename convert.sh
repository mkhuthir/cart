#! /bin/bash

xacro xacro/cart_position.xacro > urdf/cart_position.urdf
xacro xacro/cart_velocity.xacro > urdf/cart_velocity.urdf
xacro xacro/cart_effort.xacro  > urdf/cart_effort.urdf
xacro xacro/gripper_mimic_joint.xacro > urdf/gripper_mimic_joint.urdf

echo "Done"
