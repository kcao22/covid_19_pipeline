import boto3
import configparser


def create_session():
    '''
    RETURNS:
        boto3 session used for creating clients. Defaults to AdminUser IAM user and correspondong credentials along with us-west-2 region.
    '''
    # Config parser to read credentials from config 
    parser = configparser.ConfigParser()
    parser.read_file(open('credentials.config'))
    key = parser.get('AWS', 'KEY')
    secret = parser.get('AWS', 'SECRET')

    # Instantiate boto3 s3 API client
    session = boto3.Session(
        aws_access_key_id=key,
        aws_secret_access_key=secret,
        region_name='us-west-2'
    )
    return session