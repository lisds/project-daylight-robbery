"""Module provides methods for interacting with the filesystem.""" # pylint: disable=invalid-name
from pathlib import Path
import pandas as pd

class Data:
    """The Data class contains methods for loading the data."""

    borough_10_21 = None
    borough_21_23 = None
    lsoa_10_21 = None
    lsoa_21_23 = None
    ward_10_21 = None
    ward_21_23 = None
    ward_01_10_oldward = None

    __base = Path(__file__).parent.parent
    __data_folder = __base / "data"

    def __init__(self):
        """Load the dataframes"""
        base = Path(__file__).parent.parent / "data"
        self.borough_10_21 = pd.read_csv(base / "borough_10_21.csv")
        self.borough_21_23 = pd.read_csv(base / "borough_21_23.csv")
        self.lsoa_10_21 = pd.read_csv(base / "lsoa_10_21.csv")
        self.lsoa_21_23 = pd.read_csv(base / "lsoa_21_23.csv")
        self.ward_10_21 = pd.read_csv(base / "ward_10_21.csv")
        self.ward_21_23 = pd.read_csv(base / "ward_21_23.csv")
        self.ward_01_10_oldward = pd.read_csv(base / "ward_01_10_oldward.csv")

    def clean(self):
        """Clean the data"""

    def change_date_cols(self, date_cols):
        """Improve formating of date columns"""
        date_cols = list(date_cols)
        return dict((date, f"{date[:4]}-{date[4:]}") for date in date_cols)
