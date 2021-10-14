# read the data from data source
# save it in the data/raw for further process

import os
from get_data import read_params,get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    # here we are replacing some space with underscore in columns
    new_cols = [col.replace(' ','_') for col in df.columns]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    #to save maked changes in the data file as raw file
    df.to_csv(raw_data_path,sep=',',index=False,header=new_cols)
    print(new_cols)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    os.chdir(r'C:/Users/knora/PycharmProjects/simple_app')
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)
