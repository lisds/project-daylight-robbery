# instruction manual on how to use the data class stuff
import pandas as pd
from projtools.data import Data

data = Data()

#renaming columns to make them more legible
column_names = {"MajorText": "category",
                "MinorText": "offence",
                "LookUp_BoroughName": "borough",
                "Major Category": "category",
                "Minor Category": "offence",
                "Borough": "borough",
                "WardName": "ward_name",
                "WardCode": "ward_code",
                "LSOA Name": "lsoa_name",
                "LSOA Code": "lsoa_code"}

borough_10_21 = data.borough_10_21.rename(columns=column_names)
borough_21_23 = data.borough_21_23.rename(columns=column_names)

lsoa_10_21 = data.lsoa_10_21.rename(columns=column_names)
lsoa_21_23 = data.lsoa_21_23.rename(columns=column_names)

ward_10_21 = data.ward_10_21.rename(columns=column_names)
ward_21_23 = data.ward_21_23.rename(columns=column_names)

common_columns = ["ward_name", "ward_code", "category", "offence", "borough"]
ward = pd.merge(ward_10_21, ward_21_23, on = common_columns, how = "outer")

common_columns = ["lsoa_name", "lsoa_code", "category", "offence", "borough"]
lsoa = pd.merge(lsoa_10_21, lsoa_21_23, on = common_columns, how = "outer")

common_columns = ["borough", "category", "offence"]
borough = pd.merge(borough_10_21, borough_21_23, on = common_columns, how = "outer")

ward = ward.rename(columns=data.change_date_cols(ward.columns[5:]))
lsoa = lsoa.rename(columns=data.change_date_cols(lsoa.columns[5:]))
borough = borough.rename(columns=data.change_date_cols(borough.columns[3:]))
