## read params
## Process
## return DataFrame

import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path,'r') as yaml_file:
        print(yaml_file)

        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    print(config)
    data_path = config["data_source"]["s3_source"]  #here we are providing winequality dataset path
    df = pd.read_csv(data_path,sep=',',encoding='utf-8')
    return df

if __name__ =="__main__":
    args = argparse.ArgumentParser()
    os.chdir(r'C:/Users/knora/PycharmProjects/simple_app')
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path = parsed_args.config)