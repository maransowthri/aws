from stacker.blueprints.base import Blueprint

from stacker.blueprints.variables.types import (
    CFNCommaDelimitedList,
    CFNString
)

from troposphere import (
    AWS_REGION,
    Equals,
    If,
    Output,
    Ref,
    Sub,
    ec2,
    elasticloadbalancingv2 as alb
)

class ALB(Blueprint):
    def create_conditions(self):
        pass

    def create_security_groups(self):
        t = self.template

        self.http_sg = t.add_resource(ec2.SecurityGroup(
            'ALBHTTPSG',
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

    def create_load_balancers(self):
        t = self.template

        self.load_balancer = t.add_resource(alb.LoadBalancer(
            f"PrimaryAlb",
            SecurityGroups=[],
        ))

    def create_listeners(self):
        t = self.template

        # Require that a host header matches in order to forward data
        https_listner = t.add_resource(alb.Listener(
            'AlbHTTPSListener',
            DefaultActions=[alb.Action(
                Type='fixed-response',
                FixedResponseConfig=alb.FixedResponseConfig(
                    StatusCode='404',
                    MessageBody='Not Found'
                )
            )],
            LoadBalancerArn=self.load_balancer.Ref(),
            Port=80,
            Protocol='HTTP',
        ))

        self.outputs['AlbHTTPSListenerArn'] = https_listner.Ref()

    def create_outputs(self):
        pass

    def create_template(self):
        self.outputs = {}
        self.create_conditions()
        self.create_security_groups()
        self.create_load_balancers()
        self.create_listeners()
        self.create_outputs()
