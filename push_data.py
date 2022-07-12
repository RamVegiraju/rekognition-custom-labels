import os
import glob
import boto3

s3 = boto3.resource('s3')

##Data Source: https://www.kaggle.com/competitions/dogs-vs-cats/overview

def upload_data(data):
    for file in os.listdir(data):
        if "cat" in file:
            catResponse = s3.meta.client.upload_file(f'{data}/{file}', 'rekog-sample-mars', f'cat/{file}')
        else:
            dogResponse = s3.meta.client.upload_file(f'{data}/{file}', 'rekog-sample-mars', f'dog/{file}')
    print("Uploaded")


if __name__ == "__main__":
    #replace this with your data folder with the training dataset
    upload_data("train")