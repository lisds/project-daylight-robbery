"""Module provides methods for interacting with the filesystem.""" # pylint: disable=invalid-name
from pathlib import Path
import pandas as pd

class Data:
    """The Data class contains methods for loading the data."""

    # pylint: disable=too-many-instance-attributes

    __base = Path(__file__).parent.parent
    __data_folder = __base / "data"

    def __init__(self):
        """Load the dataframes"""
        base = Path(__file__).parent.parent / "data"
        self.__borough_10_21 = pd.read_csv(base / "borough_10_21.csv")
        self.__borough_21_23 = pd.read_csv(base / "borough_21_23.csv")
        self.__lsoa_10_21 = pd.read_csv(base / "lsoa_10_21.csv")
        self.__lsoa_21_23 = pd.read_csv(base / "lsoa_21_23.csv")
        self.__ward_10_21 = pd.read_csv(base / "ward_10_21.csv")
        self.__ward_21_23 = pd.read_csv(base / "ward_21_23.csv")
        self.__ward_01_10_oldward = pd.read_csv(base / "ward_01_10_oldward.csv") # pylint: disable=unused-private-member

        self.clean()

    def clean(self):
        """Clean the data"""
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

        self.__borough_10_21 = self.__borough_10_21.rename(columns=column_names)
        self.__borough_21_23 = self.__borough_21_23.rename(columns=column_names)

        self.__lsoa_10_21 = self.__lsoa_10_21.rename(columns=column_names)
        self.__lsoa_21_23 = self.__lsoa_21_23.rename(columns=column_names)

        self.__ward_10_21 = self.__ward_10_21.rename(columns=column_names)
        self.__ward_21_23 = self.__ward_21_23.rename(columns=column_names)

        common_columns = ["ward_name", "ward_code", "category", "offence", "borough"]
        self.ward = pd.merge(self.__ward_10_21, self.__ward_21_23, on = common_columns, how = "outer")

        common_columns = ["lsoa_name", "lsoa_code", "category", "offence", "borough"]
        self.lsoa = pd.merge(self.__lsoa_10_21, self.__lsoa_21_23, on = common_columns, how = "outer")

        common_columns = ["borough", "category", "offence"]
        self.borough = pd.merge(self.__borough_10_21, self.__borough_21_23, on = common_columns, how = "outer")

        self.ward = self.ward.rename(columns=self.__change_date_cols(self.ward.columns[5:]))
        self.lsoa = self.lsoa.rename(columns=self.__change_date_cols(self.lsoa.columns[5:]))
        self.borough = self.borough.rename(columns=self.__change_date_cols(self.borough.columns[3:]))

    def __change_date_cols(self, date_cols):
        """Improve formatting of date columns"""
        date_cols = list(date_cols)
        return dict((date, f"{date[:4]}-{date[4:]}") for date in date_cols)
