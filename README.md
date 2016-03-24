DevOps Test
-----------

Ansible Playbooks for setting up an EC2 instance, Installing Docker & Running a Nginx enabled container that serves up static pages behind a HTTP Auth.

### Requirements

* Ansible ~> 2.0
* Python ~> 2.7
* Boto ~> 2.34

### Pre Setup - AWS

1. Playbook assumes that the Instance will be launched in the us-east-1 region. (TODO: Make it configurable)
2. Import your ssh key into EC2 with the name "Devops_Test" (Mandatory, other names will not work.)

### Pre Setup - Local Machine (Ubuntu 14.04)

1. Install required packages
    ```
    sudo apt-get install software-properties-common
    
    sudo apt-add-repository ppa:ansible/ansible
    
    sudo apt-get update
    
    sudo apt-get install ansible python-pip
    
    sudo pip install boto
    ```

### Usage

1. Clone the Repo
    ```
    git clone https://github.com/vinay-nadig-0042/DevOps-Test.git
    ```

2. Export AWS Keys - Make sure the keys corresponding to the IAM user has sufficient privilages to launch & administer EC2 Intances.
    ```
    export AWS_ACCESS_KEY_ID='AKIXXX'
    export AWS_SECRET_ACCESS_KEY='AKIXXX'
    ```

3. Run the Playbook
    ```
    ansible-playbook -i ./inventory master.yaml -vvvv
    ```

4. Access the Default Page - http://&lt;public-ip-of-launched-instance&gt;/ - IP has to be accessed from the EC2 Console. TODO: Output Public IP at the end of the playbook execution.

### References

1. https://github.com/electroniceagle/ansible-dc-ec2-tutorial
2. http://docs.ansible.com/ansible/intro_dynamic_inventory.html
3. http://docs.ansible.com/ansible/developing_modules.html
4. Docker Installation & Configuration - https://github.com/angstwad/docker.ubuntu

### TODOS
1. Display EC2 Public IP at the end of the playbook execution
2. Make region configurable(Currently only us-east-1 is supported)

### Notes

1. EC2 IP Address extracted through the [EC2 Dynamic Inventory](http://docs.ansible.com/ansible/intro_dynamic_inventory.html#example-aws-ec2-external-inventory-script) Script.
2. The check on whether an instance exists or not is checked through a custom module located at [library/check_named_instance.py](https://github.com/vinay-nadig-0042/DevOps-Test/blob/master/library/check_named_instance.py)

