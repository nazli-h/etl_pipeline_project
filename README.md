## ETL Pipeline 

### Introduction
Building an ETL pipline that does the following steps
- Extracts transactional data of 400k invoices from Redshift
- Identifies and removes any duplicates
- Loads the data to the bootcamp' s s3 bucket

### Requirements
- Python3+

### Instructions on how to execute the code
Make sure you are executing the code from the etl_pipeline folder.

1-) Install all the libraries you will need to execute main.py. 
    Please add python-dotenv to the requirements.txt.
  
  pip3 install -r requirements.txt
  
2-) Copy the .env.example file to .env and fill out the environment vars.

3-) Run the main.py script. You will need to import dotenv and load the environment variables.

  python3 main.py

