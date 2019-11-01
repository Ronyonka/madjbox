#!/usr/bin/env python3
# import pandas
# from cartoframes.auth import set_default_credentials
# from cartoframes.data import Dataset
# from cartoframes.viz import Map, Layer

# set_default_credentials(username='wstf', api_key='532f87940a1834e8e3172afc0c1f4f89f9ac1601')

# remote_file_path = 'http://data.sfgov.org/resource/wg3w-h783.csv'

# df = pandas.read_csv(remote_file_path)

# df = df[df.longitude == df.longitude]
# df = df[df.latitude == df.latitude]

# df.head()

# ds = Dataset(df)
# def create_table(ds):
#     table_name='sustainable_palm_oil_production_mills'
#     ds.upload(
#         table_name= table_name,
#         with_lnglat=('longitude', 'latitude'),
#         if_exists=Dataset.IF_EXISTS_REPLACE
#     )

# def change_dataset_privacy(ds):
#     create_table(ds)
#     ds.update_dataset_info(privacy=Dataset.PRIVACY_PUBLIC)
#     Map(Layer(ds))   

# change_dataset_privacy(ds)
