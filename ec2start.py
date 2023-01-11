import boto3
region = "us-east-1"
instances = ['i-0c75610112a24dd73', 'i-037f14606ec524a4e']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print("start instances your instances")
