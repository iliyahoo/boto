#!bin/python

instance_type = 't1.micro'
ami = 'ami-3fec7956' # ubuntu 12.04 lts x86_64
key_name = 'boto'
group_name = 'boto'
tag = 'boto'

from ec2_launch_instance import launch_instance

launch_instance(instance_type, ami, key_name, group_name, tag)
