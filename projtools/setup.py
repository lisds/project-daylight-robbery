""" Setup code

This file sets up the initial environment.
"""

import pandas as pd
import hashlib
from pathlib import Path

crime_summary_hash = "347719448c0a591ca0426f089b8ca0b741d23708"

def import_data(filename = "LSOA_Crime_21-23.csv"):
    """ An example function, returning `a` * 10 + b

    Parameters
    ----------
    a : number
    b : number

    Returns
    -------
    res : number
        Result of ``a * 10 + b``.
    """
    return pd.read_csv(filename)

def check_data_hash(filename = "LSOA_Crime_21-23.csv"):
    base = Path(__file__).parent.parent
    filename = base / "data" / filename
    return hashlib.sha1(filename.read_bytes()).hexdigest()
