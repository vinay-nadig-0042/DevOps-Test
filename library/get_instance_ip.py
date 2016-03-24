#!/usr/bin/env python

# Simple Custom Module to wait for an EC2 instance with specific tag to be up

# TODO: Make region configurable.

import boto.ec2, json, sys, shlex

args_file = sys.argv[1]
args_data = file(args_file).read()

arguments = shlex.split(args_data)

for arg in arguments:
    if "=" in arg:
        (key, value) = arg.split("=")
        if key == "name":
            conn = boto.ec2.connect_to_region("us-east-1")
            instances = conn.get_only_instances()
            for instance in instances:
                if instance.tags['Name'] == value and instance.state != 'terminated':
                    print json.dumps({
                        "ansible_facts": {
                            "next_ip": instance.ip_address
                          }
                      })
                    sys.exit(0)

print json.dumps({
  "ansible_facts": {
    "next_ip": None
  }
})
sys.exit(0)
