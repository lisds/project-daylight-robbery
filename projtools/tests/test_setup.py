""" Setup.py tests
"""

from projtools import setup

LSOA_CRIME_21_23_HASH = "8057ba79256769903b91b084e1ed0affd8e85277"

def test_data_hash():
    """ Test that the data hash is correct"""
    assert setup.get_data_hash("LSOA_Crime_21-23.csv") == LSOA_CRIME_21_23_HASH
