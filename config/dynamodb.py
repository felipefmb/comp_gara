import boto3
import os

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb',
                          region_name=os.environ.get('AWS_REGION', 'us-east-1'),
                          aws_access_key_id=os.environ.get('AKIA4T4OCHOVAAKF5SQZ'),
                          aws_secret_access_key=os.environ.get('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')
                          )


def save(entity, table_name):
    """
    Persist an entity to a DynamoDB table.

    :param entity: A dictionary representing the item to be saved
    :param table_name: The name of the DynamoDB table
    :return: The response from DynamoDB
    """
    table = dynamodb.Table(table_name)

    try:
        response = table.put_item(Item=entity)
        print(f"Successfully saved item to {table_name}")
        return response
    except Exception as e:
        print(f"Error saving item to {table_name}: {str(e)}")
        raise
