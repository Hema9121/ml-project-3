import logging 
import os 
from datetime import datetime
import pandas as pd

logs_file_name=f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",logs_file_name)

os.makedirs(logs_path,exist_ok=True)

logs_file_path=os.path.join(logs_path,logs_file_name)

logging.basicConfig(filename="logs_file_path",
                    filemode="w",
                    format="[%(asctime)s]_%(levelname)s_%(lineno)d_%(filename)s_%(funcName)s()_%(message)s",
                    level=logging.INFO)

data=[]

def get_logs_dataframe(file_path:str):
    with open(file_path) as f:
        for i in f.readlines():
            data.append(i.split("_"))

    logs_df=pd.DataFrame(data)

    columns=["time_stamp","level","line_num","file_name","dunc_name","message"]

    logs_df.columns=columns

    logs_df["log_message"] = logs_df['time_stamp'].astype(str) +":$"+ logs_df["message"]

    return logs_df[["log_message"]] 


