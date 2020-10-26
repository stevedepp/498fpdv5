import boto3
import L
import iam
client = boto3.client('events')

lambda_name = 'server'
rule_name = '5minutetimer'
rule = 'rate(5 minutes)'
rule_description = 'plays every 5 minutes'

def make_rule(
    name=rule_name,
    rule=rule,
    description=rule_description):
    
    response = client.put_rule(
        Name = name,
        ScheduleExpression = rule,
        Description = description)
    return response


def attach_rule(name='5minutetimer', lambda_name='server'):
    lid, larn = L.name_2_arn_id(lambda_name)
    #return lid, larn
    client = boto3.client('events')
    response = client.put_targets(Rule=name, Targets=[{'Arn': larn, 'Id': lid}])
    return response

def list():
    return client.list_rules()

def disable(name='5minutetimer'):
    response = client.disable_rule(Name=name)

def enable(name='5minutetimer'):
    response = client.enable_rule(Name=name)

def delete(name='5minutetimer'):
    response = client.delete_rule(Name=name)
