#!/bin/python
import boto3
import botocore
ec2client = boto3.client('ec2')
# Find instances with the following tag and value
tagkey='GW_TomcatVersion'
tagvalue='7_Latest'
# Send request to AWS
response = ec2client.describe_instances(Filters=[ {'Name': 'tag:'+tagkey,'Values': [tagvalue] }])
# Find the instanceId and hostname
for i in range(len(response["Reservations"])):
    ec2instance= response["Reservations"][i]['Instances'][0]["InstanceId"]
    print "InstanceID: ",ec2instance
    for  j in range(len(response["Reservations"][i]['Instances'][0]["Tags"])):
        if response["Reservations"][i]['Instances'][0]["Tags"][j]['Key'] == 'Hostname':
            print  "Hostname: ",response["Reservations"][i]['Instances'][0]["Tags"][j]['Value']
            #Uncomment the following to disable termination protection and terminate the instance
            #ec2client.modify_instance_attribute(DisableApiTermination={'Value': False},InstanceId=ec2instance)
            #ec2client.terminate_instances(InstanceIds=[ec2instance])
