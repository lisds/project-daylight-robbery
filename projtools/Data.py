from pathlib import Path
import pandas as pd

class Data:
  #borough_crime_10-21, borough_crime_21-23 = (None, None)

  base = Path(__file__).parent.parent
  data_folder = base / "data"

  def __init__(self):
    base = Path(__file__).parent.parent
    dataframes = {}
    for filename in base.glob("data/*.csv"):
        setattr(self, filename.stem, pd.read_csv(filename))
    
  # def __init__(self):
  #   base = Path(__file__).parent.parent
  #   dataframes = {}
  #   for filename in base.glob("data/*.csv"):
  #       dataframes[filename.stem] = pd.read_csv(filename)
  #   self.dataframes = dataframes
  
  # def __init__(self, borough_crime_10_21, borough_crime_21_23):
  #   self.borough_crime_10_21 = pd.read_csv(self.data_folder / "Borough_Crime_10-21.csv")
  #   self.borough_crime_21_23 = pd.read_csv(self.data_folder / "Borough_Crime_21-23.csv")
