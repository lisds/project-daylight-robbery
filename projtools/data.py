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
        self.__ward = pd.merge(self.__ward_10_21, self.__ward_21_23, on = common_columns, how = "outer")

        common_columns = ["lsoa_name", "lsoa_code", "category", "offence", "borough"]
        self.__lsoa = pd.merge(self.__lsoa_10_21, self.__lsoa_21_23, on = common_columns, how = "outer")

        common_columns = ["borough", "category", "offence"]
        self.__borough = pd.merge(self.__borough_10_21, self.__borough_21_23, on = common_columns, how = "outer")

        self.__ward = self.__change_date_cols(self.__ward, 5)
        self.__lsoa = self.__change_date_cols(self.__lsoa, 5)
        self.__borough = self.__change_date_cols(self.__borough, 3)

        self.ward = self.__make_multi_index(self.__ward, 5)
        self.lsoa = self.__make_multi_index(self.__lsoa, 5)
        self.borough = self.__make_multi_index(self.__borough, 3)

        # This changes the borough codes in the lsoa dataframe to borough names as in the borough and ward dataframes
        df = pd.read_excel(self.__data_folder / "LAD_DEC_2021_UK_NC.xlsx")
        map_dict = df.set_index("Code").to_dict()["borough"]
        self.lsoa.index = self.lsoa.index.set_levels(self.lsoa.index.levels[2].map(map_dict), level=2)

    def __change_date_cols(self, df: pd.DataFrame, num_index_cols: int): #an artefact of earlier cleaning
        """Improve formatting of date columns.

        Parameters
        ----------
            df: pd.DataFrame
                DataFrame to change
            num_index_cols: int
                number of columns to keep as index  (dont change)
            
        Returns
        ----------
            df: pd.DataFrame 
                DataFrame with date columns changed
        """
        date_cols = list(df.columns[num_index_cols:])
        df = df.rename(columns=dict((date, f"{date[:4]}-{date[4:]}") for date in date_cols))
        return df

    def __make_multi_index(self, df: pd.DataFrame, num_index_cols: int) -> pd.DataFrame:
        """Make a multi-index dataframe.
        
        Parameters
        ----------
            df: pd.DataFrame
                DataFrame to change
            num_index_cols: int
                number of columns to set as the index
                
        Returns
        ----------
            df: pd.DataFrame 
                DataFrame with multi-index
        """
        df = df.set_index(df.columns[:num_index_cols].tolist())
        df.columns = pd.MultiIndex.from_tuples([tuple(col.split("-")) for col in df.columns], names=["year", "month"])
        return df
