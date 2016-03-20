#!/usr/bin/env python

# Simple Custom Module for checking whether an instance with
# a specified name exists or not in the us-east-1 region

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
                            "named_instance_present": True
                          }
                      })
                    sys.exit(0)

print json.dumps({
  "ansible_facts": {
    "named_instance_present": False
  }
})
sys.exit(0)
