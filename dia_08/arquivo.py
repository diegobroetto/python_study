import boto3, csv



ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        
        if 'BlockDeviceMappings' in instance:
            for listar in instance['BlockDeviceMappings']:
                status = listar['Ebs']['Status']
                volume_id = listar['Ebs']['VolumeId']
                print(f"Instance ID: {instance['InstanceId']} Public IP: {instance['PublicIpAddress']} Status: {status} Vol ID: {volume_id}")

response =  ec2.describe_volumes()

with open('./teste.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['VolumeID', 'Status', 'Volume Type', 'Size'])

    for volume in response['Volumes']:
        volume_id = volume['VolumeId']
        status = volume['State']
        volume_type = volume['VolumeType']
        size = volume['Size']
        
        writer.writerow([volume_id, status, volume_type, size])
    
