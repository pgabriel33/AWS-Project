import aws_cdk as core
import aws_cdk.assertions as assertions

from tasks_api_cdk.tasks_api_cdk_stack import TasksApiCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in tasks_api_cdk/tasks_api_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TasksApiCdkStack(app, "tasks-api-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
