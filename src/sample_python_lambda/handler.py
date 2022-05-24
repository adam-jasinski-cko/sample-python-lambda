import os
import json
import datetime
#from apmlogging import logger
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
        
def lambda_handler(event, context):
    logger.info('Inside lambda function (via Logger) %s', 'Sample lambda')
    print('Inside lambda function (via print) ' + 'Sample lambda')
    print('Printing out logging handlers:')
    print(logging.handlers)

    json_region = os.environ['AWS_REGION']
    home_dir = os.environ['HOME']
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Status": "Healthy",
            "Region": json_region,
            "Home": home_dir,
            "Greeting": "Hello, world!"
        })
    }