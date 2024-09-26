import os
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):
    try:
        task_id = event['pathParameters']['taskId']
        body = json.loads(event['body'])
        response = table.update_item(
            Key={'taskId': task_id},
            UpdateExpression="set #t = :t, description = :d, #s = :s",
            ExpressionAttributeNames={
                '#t': 'title',
                '#s': 'status'
            },
            ExpressionAttributeValues={
                ':t': body['title'],
                ':d': body['description'],
                ':s': body['status']
            },
            ReturnValues="ALL_NEW"
        )
        item = response.get('Attributes')
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
