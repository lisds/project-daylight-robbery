from projtools import clean

def test_ward():
    """Test that the sum of crimes in the ward datasets are correct"""
    assert clean.ward.iloc[:,5:].sum().sum() == 10701946
    assert clean.ward_10_21.iloc[:,5:].sum().sum() == 8988243
    assert clean.ward_21_23.iloc[:,5:].sum().sum() == 1713703
