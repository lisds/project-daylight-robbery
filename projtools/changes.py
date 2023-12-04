from data import Data # pylint: disable=import-error disable=no-name-in-module

data = Data()

borough_10_21 = data.borough_crime_10_21
borough_10_21 = borough_10_21.rename(columns={"MajorText": "Category",
                               "MinorText": "Offence",
                               "LookUp_BoroughName": "Borough"}) #renaming columns to make them more legible
borough_21_23 = data.borough_crime_21_23
borough_21_23 = borough_21_23.rename(columns={"MajorText": "Category",
                               "MinorText": "Offence",
                               "LookUp_BoroughName": "Borough"}) #renaming columns to make them more legible
lsoa_10_21 = data.lsoa_crime_10_21
lsoa_10_21 = lsoa_10_21.rename(columns={"Major Category": "Category",
                                        "Minor Category": "Offence"}) #renaming columns to make them more legible
lsoa_21_23 = data.lsoa_crime_21_23
lsoa_21_23 = lsoa_21_23.rename(columns={"Major Category": "Category",
                                        "Minor Category": "Offence"}) #renaming columns to make them more legible
ward_10_21 = data.ward_crime_10_21
ward_10_21 = ward_10_21.rename(columns={"MajorText": "Category",
                                        "MinorText": "Offence",
                                        "LookUp_BoroughName": "Borough"}) #renaming columns to make them more legible
ward_21_23 = data.ward_crime_21_23
ward_21_23 = ward_21_23.rename(columns={"MajorText": "Category",
                                        "MinorText": "Offence",
                                        "LookUp_BoroughName": "Borough"}) #renaming columns to make them more legible
print(borough_10_21.Category.list())