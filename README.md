
# API CRUD SERVELESS USING AWS CDK, LAMBDA, DYNAMODB AND API GATEWAY!

This project run a cdk template to provide Lambda functions to create API CRUD using Dynamo tables on AWS.

Steps to run the project. 

On terminal you need to create the virtual env on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you need install the required dependencies.

```
$ pip install -r requirements.txt
```
On virtualenv you need install the other depedencie for Dynamo DB on python file called boto3. Try this:

```
$ pip install boto3
```
Prepare your AWS account to receive CDK deployments. Use this:

```
$ cdk bootstrap
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can deploy the CloudFormation template at your AWS account with this command:

```
$ cdk deploy
```

After all the resources have been provisioned on AWS, you can test using the Curl tool on terminal with this command for:

Create task

```
$ curl -X POST https://{api-id}.execute-api.{your-region-on-AWS}.amazonaws.com/prod/tasks \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Task 1",
    "description": "This is task 1",
    "status": "pending"
  }'
```

List task

```
$ curl -X GET https://{api-id}.execute-api.{your-region-on-AWS}.amazonaws.com/prod/tasks/{task-id}
```

Update task

```
$ curl -X PUT https://{api-id}.execute-api.{your-region-on-AWS}.amazonaws.com/prod/tasks/{task-id} \                      
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Updated Task 1",
    "description": "This task has been updated",
    "status": "completed"
  }'
```

Delete task

```
$ curl -X DELETE https://{api-id}.execute-api.{your-region-on-AWS}.amazonaws.com/prod/tasks/{task-id}
```

OBS: Don't forget to create the policy for allow your AWS user read, list and write about the services API Gateway, Lambda, Dynamo DB, S3, STS, IAM and CloudFormation.
