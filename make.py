import boto3
import sqs
import ddb
import iam
import L
import event
import s3

def s3b():
    response = s3.delete(name = 'aws-sam-cli-managed-default-samclisourcebucket-g8yh0dei4jqb')
    return response

def q():

    response = sqs.create_q('producer')
    return response

def ddbt():
    response = ddb.table_make('fang')
    return response

def ddbi():
    response = ddb.add_items(name='fang')
    return response 

def i():
    response = iam.create_role_with_policy('admin4lambda498')
    return response

#def lapps():
#    import subprocess
#    subprocess.getoutput("zsh -c './lambda.sh'")

def roles():
    responses = L.update_roles()
    return responses

def rule():
    response = event.make_rule(name='5minutetimer')




#response = sqs.delete_q('producer')
#response = ddb.delete_table('fang')
#response = iam.delete_role('admin4lambda498')