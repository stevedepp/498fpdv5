import json
import logging
import pprint
import boto3
from botocore.exceptions import ClientError

# https://docs.aws.amazon.com/code-samples/latest/catalog/python-iam-iam_basics-role_wrapper.py.html

logger = logging.getLogger(__name__)
iam = boto3.resource('iam')

def create_role(role_name, allowed_services):
    """
    Creates a role that lets a list of specified services assume the role.
    :param role_name: The name of the role.
    :param allowed_services: The services that can assume the role.
    :return: The newly created role.
    """
    trust_policy = {
        'Version': '2012-10-17',
        'Statement': [{
                'Effect': 'Allow',
                'Principal': {'Service': service},
                'Action': 'sts:AssumeRole'
            } for service in allowed_services
        ]
    }

    try:
        role = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy))
        logger.info("Created role %s.", role.name)
    except ClientError:
        logger.exception("Couldn't create role %s.", role_name)
        raise
    else:
        return role


def delete_role(iam_role_name):
    """
    Deletes a role.

    :param role_name: The name of the role to delete.
    """
    try:
        iam.Role(iam_role_name).delete()
        logger.info("Deleted role %s.", iam_role_name)
        print(f"Deleted {iam_role_name}.")

    except ClientError:
        logger.exception("Couldn't delete role %s.", iam_role_name)
        raise


def attach_policy(role_name, policy_arn):
    """
    Attaches a policy to a role.

    :param role_name: The name of the role. **Note** this is the name, not the ARN.
    :param policy_arn: The ARN of the policy.
    """
    try:
        iam.Role(role_name).attach_policy(PolicyArn=policy_arn)
        logger.info("Attached policy %s to role %s.", policy_arn, role_name)
    except ClientError:
        logger.exception("Couldn't attach policy %s to role %s.", policy_arn, role_name)
        raise


def detach_policy(iam_role_name, policy_arn):
    """
    Detaches a policy from a role.

    :param role_name: The name of the role. **Note** this is the name, not the ARN.
    :param policy_arn: The ARN of the policy.
    """
    try:
        iam.Role(iam_role_name).detach_policy(PolicyArn=policy_arn)
        logger.info("Detached policy %s from role %s.", policy_arn, iam_role_name)
        print(f"Detached policy {policy_arn} from {iam_role_name}.")

    except ClientError:
        logger.exception(
            "Couldn't detach policy %s from role %s.", policy_arn, iam_role_name)
        raise


def iam_create_role_with_policy(iam_role_name, allowed_services_list, policy_arn):
    """
    allowed services = list e.g. ['lambda.amazonaws.com', 'batchoperations.s3.amazonaws.com']
    policy_arn e.g. arn:aws:iam::aws:policy/AdministratorAccess
    """
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    print('-'*88)
    print("Welcome to the AWS Identity and Account Management.")
    role = create_role(iam_role_name, allowed_services_list)
    print(f"Created role {role.name}, with trust policy:")
    pprint.pprint(role.assume_role_policy_document)
    attach_policy(role.name, policy_arn)
    print(f"Attached policy {policy_arn} to {role.name}.")

