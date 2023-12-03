from pathlib import Path
import pandas as pd

base = Path(__file__).parent.parent
filepath = base / "data" / "Borough_Crime_10-21.csv"
pd.read_csv(filepath)