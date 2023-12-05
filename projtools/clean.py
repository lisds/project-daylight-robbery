# instruction manual on how to use the data class stuff
import pandas as pd
from projtools.data import Data # pylint: disable=no-name-in-module

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
