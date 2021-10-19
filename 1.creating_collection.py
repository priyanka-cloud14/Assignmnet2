# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:39:19 2021

@author: PRIYANKA REDDY
"""


import boto3
import csv

# Create client 
client  = boto3.client('rekognition',
                       aws_access_key_id = "AKIAWIHVMFXLBSLBFDNL",
                       aws_secret_access_key = "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",
                                             region_name = 'us-east-1'
                       )

def create_collection(collection_id): 

    #Create a collection
    print('Creating collection:' + collection_id)
    
    #Using inbuilt function within rekognition client
    response=client.create_collection(CollectionId=collection_id) 
    
    #Printing the collection details, save the printed output in a text file.
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')
    
def main():
    collection_id='students123' #Assign Collection ID Name
    create_collection(collection_id) # Creation of Collection ID

if __name__ == "__main__":
    
    main() 
    
    
    