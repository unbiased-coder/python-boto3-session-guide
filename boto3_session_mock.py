from unittest import mock
import boto3

@mock.patch('boto3.session.Session')
def test_session_iam(test_val):
    mock_session_obj = mock.Mock()
    mock_iam_client = mock.Mock()
    
    creds = mock_session_obj.get_credentials()
    print ('Access key: ', creds.access_key)
    print ('Secret key: ', creds.secret_key)
    print ('Region: ', mock_session_obj.region_name)
    print ('Profile: ', mock_session_obj.profile_name)
    print ('User: ', mock_iam_client.get_user())

test_session_iam()
