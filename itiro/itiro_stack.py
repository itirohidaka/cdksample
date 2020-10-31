from aws_cdk import (
    aws_ec2 as ec2,
    core,
)

class ItiroStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc(self, "VPC",
            nat_gateways=1,
            subnet_configuration=[ec2.SubnetConfiguration(name="public",subnet_type=ec2.SubnetType.PUBLIC),ec2.SubnetConfiguration(name="private",subnet_type=ec2.SubnetType.PRIVATE)],
            )