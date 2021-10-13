import boto3_helper

session = boto3_helper.init_aws_session()
creds = session.get_credentials()
print ('Access key: ', creds.access_key)
print ('Secret key: ', creds.secret_key)
print ('Region: ', session.region_name)
print ('Profile: ', session.profile_name)
iam = session.client('iam')
print ('User: ', iam.get_user())
