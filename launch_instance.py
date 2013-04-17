#!bin/python

instance_type = 't1.micro'
key_name = 'boto'
group_name = 'boto'
tag = 'boto'

from ec2_launch_instance import launch_instance

launch_instance(instance_type, key_name, group_name, tag)
