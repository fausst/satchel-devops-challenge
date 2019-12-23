# ansible_test

The following structure has been created to resolve the execrise:
ansible_test:
- site.yml
- ansible.cfg
- group_vars:
    - all
- addkey:
    - public_keys:
    	- ubuntu.pub
    - tasks:
        - main.yml
- config:
    - templates:
    	- gunicorn_start
	- nginx.conf
	- production.j2
	- supervisor.conf
    - tasks:
        - main.yml
- packages:
    - tasks:
        - main.yml
- postgresql:
    - tasks:
        - main.yml
- django:
    - tasks:
        - main.yml


In the site.yml (main playbook yaml), ansible do the following:

- Create a security group for the ec2 instances. It will receive request in ports 22,80 and 443, and will send to anywhere (all)

- Create 2 ec2 Ubuntu 14.04 TLS instances

- Install required packages for the deploy to work

- Generate and add our local host public key and adding to authorized_keys file on remote servers

- Pull the django application code from the public github repo fausst/django_test to the servers

- Install django requirements with pip

- Create postgresql database and user for the django app

- Deploy django app (collect stats, migrate database)

- Generate a new AWS load balancer in a default security group listening 80 port and add both web servers to it.

- Copy/substitute neccessary config files for Nginx,Supervisor,Gunicorn,Django

- Restart supervisor and nginx


Some considerations to keep in mind:

- A dynamic inventory has been used (ec2.py,ec2.ini)

- Application writted in Django

- Launch command: ansible-playbook site.yml --private-key /home/ubuntu/my_key_pair.pem

- Result: a welcome messagge will be displayed if ELB DNS Name is requested (http://awselbdemo-455991089.us-east-2.elb.amazonaws.com): 

Hello world FROM SERVER 3.135.185.189!
Hello world FROM SERVER 3.133.154.43!

Depending on which server the ELB are pointing one or the other will be printed (F5 many times to see it changing).

This playbook has been tested in a empty execution (dropping ec2 instances) and it works.

#update_playbook.yml

It will make a pull of code in the servers, will modify the required django files, and will restart supervisor and nginx.
