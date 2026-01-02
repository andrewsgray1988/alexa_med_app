import boto3
from botocore.exceptions import ClientError

TABLE_NAME = "MedicationLogs"

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def save_medication(user_id, person, medication, timestamp):
    try:
        table.put_item(
            Item={
                "UserId": user_id,
                "PersonMedication": f"{person}#{medication}",
                "LastTakenAt": timestamp
            }
        )
    except ClientError as e:
        raise RuntimeError(f"DynamoDB error: {e}")

def load_last_taken(user_id, person, medication):
    try:
        response = table.get_item(
            Key={
                "UserId": user_id,
                "PersonMedication": f"{person}#{medication}"
            }
        )
    except ClientError as e:
        raise RuntimeError(f"DynamoDB read failed: {e}")

    item = response.get("Item")
    if not item:
        return None

    return item.get("LastTakenAt")
