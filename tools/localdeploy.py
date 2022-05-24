import os
import logging
import json
import shutil
import boto3
import botocore.exceptions
from . import utils, packer

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = 'http://localhost:4566' #os.environ.get('LOCALSTACK_ENDPOINT_URL')
LAMBDA_ZIP = os.path.join(utils.REPO_ROOT, 'artifacts/lambda.zip')
LOCALSTACK_MOUNT_TMP = os.path.join(utils.REPO_ROOT, 'localstack_tmp')
# boto3.setup_default_session(profile_name=AWS_PROFILE)
localstack_session = boto3.session.Session(aws_access_key_id='XXX', aws_secret_access_key='XXX', aws_session_token='XXX')

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')


def get_boto3_client(service):
    """
    Initialize Boto3 Lambda client.
    """
    try:
        lambda_client = localstack_session.client(service, region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)
    except Exception as err:
        logger.exception('Error while connecting to LocalStack.')
        raise err
    else:
        return lambda_client


# def create_lambda_zip(function_name):
#     """
#     Generate ZIP file for lambda function.
#     """
#     try:
#         with ZipFile(LAMBDA_ZIP, 'w') as zip:
#             zip.write(function_name + '.py')
#     except Exception as e:
#         logger.exception('Error while creating ZIP file.')
#         raise e

def deploy_to_localstack():
    """
    Deploys lambda to localstack
    """
    # Ensure the lambda package has been built
    if not os.path.exists(LAMBDA_ZIP):
        raise Exception(f"{LAMBDA_ZIP} doesn't exist; make sure that 'poetry run pack' has been run")

    # Unzips the pack in Localstack mounted directory
    #TODO - clear the directory first

    dest_dir = os.path.join(LOCALSTACK_MOUNT_TMP, 'lambda')
    #shutil.rmtree(dest_dir)

    packer.unpack_lambda(LAMBDA_ZIP, dest_dir)
    
    create_lambda('sample-python-lambda')


def create_lambda(function_name):
    """
    Creates a Lambda function in LocalStack.
    """
    try:
        lambda_client = get_boto3_client('lambda')
        #_ = create_lambda_zip(function_name)

        # create zip file for lambda function.
        # with open(LAMBDA_ZIP, 'rb') as f:
        #     zipped_code = f.read()
        info = None
        try:
            info = lambda_client.get_function(FunctionName=function_name)
        except lambda_client.exceptions.ResourceNotFoundException as err:
             print('Function does not exist yet; continuing')
        # except Exception as err:
        #     print('Caught error!')
        #     print(type(err))
        #     if 'ResourceNotFoundException' in type(err).__name__:
        #         pass
        #     else:
        #         raise err

        if info is not None and 'Configuration' in info:
            # Update lambda
            print('Updating lambda')
            lambda_client.update_function_code(
                FunctionName=function_name,
                S3Bucket='__local__',
                S3Key='/tmp/localstack/lambda',
                Publish=True
                #Code=dict(ZipFile=zipped_code)
            )
        else:
            print('Creating lambda')
            lambda_client.create_function(
                FunctionName=function_name,
                Runtime=f'python{utils.PYTHON_VERSION}',
                Role='role',
                #Handler=function_name + '.handler',
                Handler='handler.lambda_handler',
                Code=dict(S3Bucket='__local__',S3Key='/tmp/localstack/lambda'),
                PackageType='Zip'
                #Code=dict(ZipFile=zipped_code)
            )
            # except ResourceConflictException:
            #     logger('Function already exists. Ignoring')
    except Exception as err:
        logger.exception('Error while creating function.')
        raise err

def create_lambda_default():
    create_lambda('sample-python-lambda')

def invoke_lambda(function_name):
    """
    Invokes a Lambda function in LocalStack.
    """
    lambda_client = get_boto3_client('lambda')

    response = lambda_client.invoke(
        FunctionName = function_name, 
        InvocationType = 'Event',
        LogType = 'Tail',
        Payload = '{}'
    )
    return response
