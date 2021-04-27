
from stacker.blueprints.base import Blueprint

from stacker.blueprints.variables.types import (
    CFNString
)

from troposphere import (
    AWS_REGION,
    AWSHelperFn,
    Condition,
    Equals,
    If,
    Output,
    Ref,
    Sub,
    Tag,
    ec2,
    elasticloadbalancingv2 as alb
)

class EC2(Blueprint):
    VARIABLES = {
        'ImageId': {
            'type': CFNString,
            'description': 'ID of the AMI to use as the controller node'
        },
        'InstanceType': {
            'type': CFNString,
            'description': 'The instance type and size for the controller'
        },
        'UserData': {
            'type': AWSHelperFn,
            'description': 'base64 encoded string of the userdata for the instance',
            'default': Ref('AWS::NoValue')
        },
        'WebServerSgId': {
            'type': CFNString,
            'description': 'ID of the security group to connect prometheus instances'
        },
    }

    def create_conditions(self):
        pass

    def create_security_groups(self):
        t = self.template

        self.http_sg = t.add_resource(ec2.SecurityGroup(
            'EC2HTTPSG',
            GroupDescription='Allow all HTTP requests',
            SecurityGroupIngress=[
                ec2.SecurityGroupRule(
                    CidrIp='0.0.0.0/0',
                    FromPort='80',
                    ToPort='80',
                    IpProtocol='tcp'
                )
            ]
        ))

    def create_ec2_instances(self):
        t = self.template

        self.controller_instance = t.add_resource(ec2.Instance(
            'EC2Instance',
            ImageId=Ref('ImageId'),
            InstanceType=Ref('InstanceType'),
            UserData=self.get_variables()['UserData'],
            SecurityGroupIds=[self.http_sg.Ref()],
            Tags=[
                Tag('Name', 'Web Server'),
            ]
        ))

    def create_target_groups(self):
        pass

    def create_alb_listener_rules(self):
        pass

    def create_outputs(self):
        pass

    def create_template(self):
        self.create_conditions()
        self.create_security_groups()
        self.create_ec2_instances()
        self.create_target_groups()
        self.create_alb_listener_rules()
        self.create_outputs()
