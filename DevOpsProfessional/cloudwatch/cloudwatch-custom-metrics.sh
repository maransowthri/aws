#!/bin/bash

# Publish a custom metric
aws cloudwatch put-metric-data --metric-name FunnyMetric --namespace Custom --value 1243 --dimensions InstanceId=1-23456789,InstanceType=m1.small --profile aws-devops --region eu-west-1