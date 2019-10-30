import os

from carto.datasets import DatasetManager
from carto.auth import APIKeyAuthClient
# from carto.auth import NoAuthClient

# write here the path to a local file or remote URL
# prefix_path = ""
LOCAL_FILE_OR_URL = open(
    "/home/ron/Desktop/doodles/madjbox/files/csv/wstf_2018_shortended_data_H54U6EC.csv")
USERNAME = "wstf"
API_KEY = "532f87940a1834e8e3172afc0c1f4f89f9ac1601"
BASE_URL = "https://{}.carto.com/api/v1/imports/?api_key={}".format(
    USERNAME, API_KEY)
USR_BASE_URL = "https://{}.carto.com/".format(USERNAME)
# auth_client = NoAuthClient(base_url=USR_BASE_URL)

# dataset_manager = DatasetManager(auth_client)
# dataset = dataset_manager.create(LOCAL_FILE_OR_URL)
USR_BASE_URL = "https://{}.carto.com/".format(USERNAME)
# to use the DatasetManager you need an enterprise account
auth_client = APIKeyAuthClient(
    api_key="532f87940a1834e8e3172afc0c1f4f89f9ac1601", base_url=USR_BASE_URL)


def upload_dataset(auth_client, LOCAL_FILE_OR_URL):
    dataset_manager = DatasetManager(auth_client)
    dataset = dataset_manager.create(LOCAL_FILE_OR_URL)
    print('-------------------------------file uploaded-------------------------------------')


# upload_dataset(auth_client, LOCAL_FILE_OR_URL)
# curl -v -F file=@/home/ron/Desktop/doodles/csv_manipulation/wstf_2018_cleaned_data.csv "https://wstf.carto.com/api/v1/imports/?api_key=532f87940a1834e8e3172afc0c1f4f89f9ac1601"
