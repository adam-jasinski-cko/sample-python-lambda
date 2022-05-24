__version__ = '0.1.0'
#https://docs.datadoghq.com/serverless/installation/python/?tab=awscdk
#https://www.datadoghq.com/blog/python-logging-best-practices/
#'apm' refers obviously to Application Performance Monitoring :)
#from datadog_cdk_constructs import Datadog
from pythonjsonlogger import jsonlogger
import logging

# datadog = Datadog(self, "Datadog",
#     python_layer_version=57,
#     extension_layer_version=21,
#     api_key=<DATADOG_API_KEY>
# )
# datadog.add_lambda_functions(['adam_sample_python_lambda'])


logger = logging.getLogger()
logger.setLevel(logging.INFO)
# logHandler = logging.StreamHandler()
# formatter = jsonlogger.JsonFormatter()
# logHandler.setFormatter(formatter)
# logger.addHandler(logHandler)

# class CustomJsonFormatter(jsonlogger.JsonFormatter):
#     def add_fields(self, log_record, record, message_dict):
#         super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
#         if not log_record.get('timestamp'):
#             # this doesn't use record.created, so it is slightly off
#             now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
#             log_record['timestamp'] = now
#         if log_record.get('level'):
#             log_record['level'] = log_record['level'].upper()
#         else:
#             log_record['level'] = record.levelname

# formatter = CustomJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')