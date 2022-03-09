#!/bin/bash

# replace where needed

aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric-name CPUUtilization --dimensions Name=InstanceId,Value=i-06e91bf508fd3bf9f --statistics Maximum --start-time 2019-09-10T00:00:00 --end-time 2019-09-11T00:00:00 --period 360 --profile aws-devops --region eu-west-1