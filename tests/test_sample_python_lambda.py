#from src.sample_python_lambda import __version__
import pytest
from tools import localdeploy
from io import StringIO, BytesIO

def test_version():
    response = localdeploy.invoke_lambda('sample-python-lambda')
    print(response)
    assert response is not None
    assert isinstance(response, dict)
    assert response["StatusCode"] >= 200 and response["StatusCode"] <= 202
    #assert response["FunctionError"] != "Unhandled"
    #assert response["Payload"] == ""
    #s = StringIO(response["Payload"].read().decode('utf8'))
    # obj = BytesIO(response["Payload"].read())
    # print(s)
    # for line in s: 
    #     assert line == 'aaa'
    #     print(line)


