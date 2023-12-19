"""Setup.py tests
"""

from projtools import data_hash

BOROUGH_10_21_HASH = "6249aad9c5f8d039f709f083470b1157d5917a93"
BOROUGH_21_23_HASH = "4d702ed26a1291cdd1f12a62da2a04b4cba8cfe9"
LSOA_10_21_HASH = "505e5a58d1fab62f73fb2232cb3ed802b7c1f4d8"
LSOA_21_23_HASH = "5f17d817d45d63efdf776df87908b2f8ecc8f5a5"
WARD_10_21_HASH = "5c131d68434cbb0c013f3028d8d2bae8a944c3c4"
WARD_21_23_HASH = "018daac5cb312f8b7c628f98d689ab0f3ce43820"

def test_data_hash():
    """ Test that the data hash is correct"""
    assert data_hash.get_data_hash("lsoa_21_23.csv") == LSOA_21_23_HASH
    assert data_hash.get_data_hash("borough_10_21.csv") == BOROUGH_10_21_HASH
    assert data_hash.get_data_hash("borough_21_23.csv") == BOROUGH_21_23_HASH
    assert data_hash.get_data_hash("lsoa_10_21.csv") == LSOA_10_21_HASH
    assert data_hash.get_data_hash("ward_10_21.csv") == WARD_10_21_HASH
    assert data_hash.get_data_hash("ward_21_23.csv") == WARD_21_23_HASH
