"""Module provides methods for interacting with the filesystem.""" # pylint: disable=invalid-name
from pathlib import Path
import pandas as pd

class Data:
    """The Data class contains methods for loading the data.
    """
    #borough_crime_10-21, borough_crime_21-23 = (None, None)

    base = Path(__file__).parent.parent
    data_folder = base / "data"

    def __init__(self):
        """Load the dataframes"""
        base = Path(__file__).parent.parent
        for filename in base.glob("data/*.csv"):
            setattr(self, filename.stem, pd.read_csv(filename))
