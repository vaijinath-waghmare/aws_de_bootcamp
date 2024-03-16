import json

def lambda_handler(event, context):
    # TODO implement
    print("Event is:",event)
    print("S3 Bucket name :",event['Records'][0]['s3']['bucket']['name'])
    print("Name of file uplosded is:",event['Records'][0]['s3']['object']['key'])
    size_of_file=event['Records'][0]['s3']['object']['size']
    
    print("Size of File uploaded is:",size_of_file)
    
    if size_of_file>102400:
        print("File size is greater then 100MB")
    else:
        print("File size is less than 100MB")
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
