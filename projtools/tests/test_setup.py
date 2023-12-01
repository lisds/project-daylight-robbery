""" Projcode tests
"""

from projtools import setup

def test_data_hash():
    assert setup.check_data_hash("LSOA_Crime_21-23.csv") == "8057ba79256769903b91b084e1ed0affd8e85277"