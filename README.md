# create file 
# with appropriate keys

    vim ~/.boto 

[Credentials]
aws_access_key_id = xxxxxxxxxxxxxxxxxxxx
aws_secret_access_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

[Boto]
ec2_region_name = us-east-1a
http_socket_timeout = 5


==================================================


chmod 600 ~/.boto

sudo apt-get install python-dev
virtualenv boto
cd boto
source bin/activate
sudo bin/pip install boto
sudo bin/pip install Crypto
sudo bin/pip install paramiko


===========================================
    vim launch_instance.py
instance_type = 't1.micro'
ami = 'ami-3fec7956' # ubuntu 12.04 lts x86_64
key_name = 'boto'
group_name = 'boto'
tag = 'boto'
=============================================

    and 

./launch_instance.py
