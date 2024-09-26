from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    # aws_sqs as sqs,
)
from constructs import Construct

class TasksApiCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        tasks_table = dynamodb.Table(
            self, "TasksTable",
            partition_key=dynamodb.Attribute(name="taskId", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST  
        )
       
        # Função Lambda para criar tarefas
        create_task_function = lambda_.Function(
            self, "CreateTaskFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="create_task.handler",
            code=lambda_.Code.from_asset("lambda"),
            environment={
                "TABLE_NAME": tasks_table.table_name
            }
        )
        
        # Função Lambda para obter tarefas
        get_task_function = lambda_.Function(
            self, "GetTaskFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="get_task.handler",
            code=lambda_.Code.from_asset("lambda"),
            environment={
                "TABLE_NAME": tasks_table.table_name
            }
        )
        
        # Função Lambda para atualizar tarefas
        update_task_function = lambda_.Function(
            self, "UpdateTaskFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="update_task.handler",
            code=lambda_.Code.from_asset("lambda"),
            environment={
                "TABLE_NAME": tasks_table.table_name
            }
        )
        
        # Função Lambda para excluir tarefas
        delete_task_function = lambda_.Function(
            self, "DeleteTaskFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="delete_task.handler",
            code=lambda_.Code.from_asset("lambda"),
            environment={
                "TABLE_NAME": tasks_table.table_name
            }
        )

        tasks_table.grant_read_write_data(create_task_function)
        tasks_table.grant_read_write_data(get_task_function)
        tasks_table.grant_read_write_data(update_task_function)
        tasks_table.grant_read_write_data(delete_task_function)

        
         # Criar a API REST
        api = apigateway.RestApi(self, "TasksApi",
            rest_api_name="Tasks Service",
            description="This service serves tasks."
        )

        # Recurso /tasks
        tasks = api.root.add_resource("tasks")

        # POST /tasks
        tasks.add_method(
            "POST",
            apigateway.LambdaIntegration(create_task_function)
        )

        # Recurso /tasks/{taskId}
        task = tasks.add_resource("{taskId}")

        # GET /tasks/{taskId}
        task.add_method(
            "GET",
            apigateway.LambdaIntegration(get_task_function)
        )

        # PUT /tasks/{taskId}
        task.add_method(
            "PUT",
            apigateway.LambdaIntegration(update_task_function)
        )

        # DELETE /tasks/{taskId}
        task.add_method(
            "DELETE",
            apigateway.LambdaIntegration(delete_task_function)
        )



