#!/bin/bash

# create role for CW Logs
aws iam create-role --profile aws-devops \
      --role-name CWLtoKinesisFirehoseRole \
      --assume-role-policy-document file://./cloudwatch/trust-policy-cwsubscription.json

# create the subscription filter to Kinesis Data Firehose
aws logs put-subscription-filter \
    --log-group-name "access_log" \
    --filter-name "Destination" \
    --filter-pattern "" \
    --destination-arn "arn:aws:firehose:eu-west-1:903077646177:deliverystream/DemoFirehose" \
    --role-arn "arn:aws:iam::903077646177:role/CWLtoKinesisFirehoseRole" --region eu-west-1 --profile aws-devops