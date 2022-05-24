# sample-python-lambda

Simple POC with a Python AWS Lambda.
Uses poetry for package management and building; localstack Docker container and custom scripts for local deployments.

# How the project was initialized 
1. `poetry init`

2. Set poetry virtualenvs property to keep dependencies inside project folder (.venv)
```
[virtualenvs] 
in-project = true
```

# Poetry 101

Add package: `poetry add pandas`
Run custom command: `poetry run <cmd>`
(not applicable for lambdas) `poetry build`

# Packing Lambda

Create lambda zip
`poetry run pack`

# Deploying

```
docker-compose up -d
poetry run localdeploy
```

# Ad-hoc Invoking

`awslocal lambda invoke --function-name sample-python-lambda --payload '{}' result.json`

# Testing

`pytest tests`

# Checking logs

`awslocal logs tail /aws/lambda/sample-python-lambda --follow` 
(or without `--follow`)