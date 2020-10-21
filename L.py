import boto3
import iam
import event

def list_functions():
    '''list of all lambda functions'''
    client = boto3.client('lambda')
    functions = client.list_functions() 
    return functions

def list_arns():
    '''get a list of all lambda arns'''
    client = boto3.client('lambda')
    functions = client.list_functions() 
    function_list = list_functions()['Functions']
    arns = []
    for function in function_list:
        arns.append(function['FunctionArn'])
    return arns

def list_ids():
    '''get a list of all lambda names aka ids'''
    client = boto3.client('lambda')
    functions = client.list_functions() 
    function_list = list_functions()['Functions']
    ids = []
    for function in function_list:
        ids.append(function['FunctionName'])
    return ids

def name_2_arn_id(lambda_name):
    id = [id for id in list_ids() if lambda_name in id]
    arn = [arn for arn in list_arns() if lambda_name in arn]
    return id[0], arn[0]

def update_iam(function_arn, iam_role):
    '''update a function arn's iam role value'''
    client = boto3.client('lambda')
    response = client.update_function_configuration(
        FunctionName=function_arn, 
        Role=iam_role)
    return response

def update_roles():
    responses = []
    iam_role = iam.name2arn('adminfordev498')[0]
    for arn in list_arns():
        responses.append(update_iam(arn, iam_role))
    return responses 
