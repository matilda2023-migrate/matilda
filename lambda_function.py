import os
import csv
#import boto3
import json

def lambda_handler(event, context):
    # Create file and store in /tmp
    f = open("/tmp/csv_file.csv", "w+")
    temp_csv_file = csv.writer(f) 
    temp_csv_file.writerow(["Account Name", "Month", "Cost"])

    # writing rows in to the CSV file
    temp_csv_file.writerow(['computer', 'printer', 'tablet', 'monitor'])
    f.close()
    print("created CSV file in tmp")
    
    # List files stored in /tmp
    print("files stored in /tmp ")
    files_in_tmp = os.listdir('/tmp')
    print(files_in_tmp)
    
    #upload file to S3 (OPTIONAL)
    print("uploading file to S3")
    #s3_client = boto3.client('s3')
    #s3_client.upload_file('/tmp/csv_file.csv', 'sahithilambdatest','csv_file.csv')
    print("successfully uploaded file to S3")
    return "Lambda executed successfully"