#Import packages
import pandas as pd ## import pandas for general file types 
import json ## imoprt json for json files
import bs4 ## import bs4 for html files
import requests ## import requests for web requests
import sqlalchemy ## import sqlalchemy for sql queries
import xlrd ## import xlrd for excel files, tab names 


#Section 1 Opened Kaggle dataset
#Bring in tabs 
'''
tab1 = pd.read_excel('data/combined_aug.xlsx', sheet_name='aug_train')
tab2 = pd.read_excel('data/combined_aug.xlsx', sheet_name='sample_submission')

#Section 2 
#Bring in open source json API using requests package
data = requests.get('https://data.cms.gov/data-api/v1/dataset/b35c77ac-26e2-4320-91e1-ba71c4d7ff2c/data')
data = data.json()
data
'''
#Section 3
from google.cloud import bigquery #Imported missing package
client = bigquery.Client.from_service_account_json('/Users/Sarah/-hha-data-ingestion-sarah/json1.json')
bigquery1 = client.query("SELECT * FROM `chc-nih-chest-xray.nih_chest_xray.nih_chest_xray` LIMIT 100")
results = bigquery1.result()
df = pd.DataFrame(results.to_dataframe())

bigquery2 = client.query("SELECT * FROM `bigquery-public-data.genomics_cannabis.MNPR01_201703` LIMIT 100")
results = bigquery2.result()
df2 = pd.DataFrame(results.to_dataframe())
print(df)