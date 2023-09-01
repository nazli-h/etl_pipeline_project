import os

from src.extract import extract_transactional_data
from src.transform import drop_duplicates
from src.load_data_to_s3 import df_to_s3
# this code works for only local execution
from dotenv import load_dotenv
load_dotenv()

dbname = os.getenv('dbname')
host = os.getenv('host')
port = os.getenv('port')
user = os.getenv('user')
password = os.getenv('password')
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key_id = os.getenv('aws_secret_access_key_id')

print("Extracting the data form redshift")
online_trans_cleaned = extract_transactional_data(dbname, host, port, user, password)

print("Identifying and removing duplicates")
online_trans_cleaned = drop_duplicates(online_trans_cleaned)

print("Loading data to the s3 bucket...")
s3_bucket = "july-bootcamp"
key = "etl_pipeline/docker/ne_online_transactions_v2.pkl"

df_to_s3(online_trans_cleaned, key, s3_bucket, aws_access_key_id, aws_secret_access_key_id)

