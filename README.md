# sample-python-lambda

Simple POC with a Python AWS Lambda.
Uses poetry for package management and building; Localstack Docker container for testing and custom scripts for local deployments.

# Pre-requisites

- [Poetry](https://python-poetry.org/)
- Docker CLI
- [AWS CLI local](https://github.com/localstack/awscli-local) (optional)

Please run `poetry install` first.

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

Create lambda zip:

`poetry run pack`

# Running Localstack

`docker-compose up -d`

# Deploying to Localstack

`poetry run localdeploy`

Note: The script unpacks Lambda zip into a directory mounted inside Localstack. See also Localstack [Lambda configuration](https://docs.localstack.cloud/localstack/configuration/) and [Hot swapping](https://docs.localstack.cloud/tools/lambda-tools/hot-swapping/).

# Ad-hoc Invoking on Localstack

Requires [awslocal](https://github.com/localstack/awscli-local)

`awslocal lambda invoke --function-name sample-python-lambda --payload '{}' result.json`

# Testing

`pytest tests`

# Checking logs

`awslocal logs tail /aws/lambda/sample-python-lambda`  (optionally with `--follow`)

# Caveats

Logging from Lambda (e.g. with `logger.info`) doesn't seem to propagate to Localstack Cloudwatch. However, `print` output is captured in Localstack Cloudwatch.

To verify: if standard logging is available in actual AWS Cloudwatch.