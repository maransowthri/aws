#!/bin/bash

aws autoscaling complete-lifecycle-action --lifecycle-action-result CONTINUE --lifecycle-hook-name LaunchHook --auto-scaling-group-name demo-asg-launch-template --instance-id i-XXXXXXXXXXXX --region eu-west-1 --profile aws-devops

# lifecycle token can also be used instead of --instance-id if Lambda is used for example