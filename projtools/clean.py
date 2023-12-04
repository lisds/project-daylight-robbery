# instruction manual on how to use the data class stuff
from data import Data # pylint: disable=no-name-in-module

data = Data()

#renaming columns to make them more legible
column_names = {"MajorText": "Category",
                "MinorText": "Offence",
                "LookUp_BoroughName": "Borough",
                "Major Category": "Category",
                "Minor Category": "Offence"}

borough_10_21 = data.borough_crime_10_21
borough_10_21 = borough_10_21.rename(columns=column_names)

borough_21_23 = data.borough_crime_21_23
borough_21_23 = borough_21_23.rename(columns=column_names)

lsoa_10_21 = data.lsoa_crime_10_21
lsoa_10_21 = lsoa_10_21.rename(columns=column_names)

lsoa_21_23 = data.lsoa_crime_21_23
lsoa_21_23 = lsoa_21_23.rename(columns=column_names)

ward_10_21 = data.ward_crime_10_21
ward_10_21 = ward_10_21.rename(columns=column_names)

ward_21_23 = data.ward_crime_21_23
ward_21_23 = ward_21_23.rename(columns=column_names)

