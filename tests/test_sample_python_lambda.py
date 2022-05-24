import pytest
from tools import localdeploy
import json

def test_version():
    response = localdeploy.invoke_lambda('sample-python-lambda')
    print(response)
    assert response is not None
    assert isinstance(response, dict)
    assert response["StatusCode"] == 200

    payload = json.loads(response['Payload'].read())
    assert "body" in payload
    body = json.loads(payload["body"])
    assert "Region" in body
    assert body["Region"] == "us-east-1"
    assert body["Greeting"] == "Hello, world!"