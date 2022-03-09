#!/bin/bash
aws cloudtrail validate-logs --start-time 2015-08-27T00:00:00Z --trail-arn arn:aws:cloudtrail:eu-west-1:903077646177:trail/DemoTrail --verbose --profile aws-devops --region eu-west-1
