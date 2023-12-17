import numpy as np
import pandas as pd
from projtools.data import Data

data = Data()

# pylint: disable=protected-access disable=line-too-long

def test_ward():
    """Test that the ward datasets are in the expected format,
    with the expected columns and the expected sum of crimes"""
    assert data._Data__ward.iloc[:,5:].sum().sum() == 10701946
    assert data._Data__ward_10_21.iloc[:,5:].sum().sum() == 8988243
    assert data._Data__ward_21_23.iloc[:,5:].sum().sum() == 1713703
    assert len(data._Data__ward.columns) == 168
    assert data._Data__ward.columns.equals(pd.Index(['ward_name', 'ward_code', 'category', 'offence', 'borough', '2010-04', '2010-05', '2010-06', '2010-07', '2010-08', '2010-09', '2010-10', '2010-11', '2010-12', '2011-01', '2011-02', '2011-03', '2011-04', '2011-05', '2011-06', '2011-07', '2011-08', '2011-09', '2011-10', '2011-11', '2011-12', '2012-01', '2012-02', '2012-03', '2012-04', '2012-05', '2012-06', '2012-07', '2012-08', '2012-09', '2012-10', '2012-11', '2012-12', '2013-01', '2013-02', '2013-03', '2013-04', '2013-05', '2013-06', '2013-07', '2013-08', '2013-09', '2013-10', '2013-11', '2013-12', '2014-01', '2014-02', '2014-03', '2014-04', '2014-05', '2014-06', '2014-07', '2014-08', '2014-09', '2014-10', '2014-11', '2014-12', '2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06', '2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12', '2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12', '2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12', '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12', '2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12', '2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06', '2021-07', '2021-08', '2021-09', '2021-10', '2021-11', '2021-12', '2022-01', '2022-02', '2022-03', '2022-04', '2022-05', '2022-06', '2022-07', '2022-08', '2022-09', '2022-10', '2022-11', '2022-12', '2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09', '2023-10'])) # pylint: disable=line-too-long

def test_lsoa():
    """Test that the sum of crimes in the lsoa datasets are correct"""
    assert data._Data__lsoa.iloc[:,5:].sum().sum() == 10414629
    assert data._Data__lsoa_10_21.iloc[:,5:].sum().sum() == 8747261
    assert data._Data__lsoa_21_23.iloc[:,5:].sum().sum() == 1667368
    assert len(data._Data__lsoa.columns) == 168
    assert data._Data__lsoa.columns.equals(pd.Index(['lsoa_code', 'lsoa_name', 'borough', 'category', 'offence', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12', '2020-01', '2020-02', '2019-01', '2019-02', '2010-04', '2010-05', '2010-06', '2010-07', '2010-08', '2010-09', '2010-10', '2010-11', '2010-12', '2011-01', '2011-02', '2011-03', '2011-04', '2011-05', '2011-06', '2011-07', '2011-08', '2011-09', '2011-10', '2011-11', '2011-12', '2012-01', '2012-02', '2012-03', '2012-04', '2012-05', '2012-06', '2012-07', '2012-08', '2012-09', '2012-10', '2012-11', '2012-12', '2013-01', '2013-02', '2013-03', '2013-04', '2013-05', '2013-06', '2013-07', '2013-08', '2013-09', '2013-10', '2013-11', '2013-12', '2014-01', '2014-02', '2014-03', '2014-04', '2014-05', '2014-06', '2014-07', '2014-08', '2014-09', '2014-10', '2014-11', '2014-12', '2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06', '2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12', '2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12', '2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12', '2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06', '2021-07', '2021-08', '2021-09', '2021-10', '2021-11', '2021-12', '2022-01', '2022-02', '2022-03', '2022-04', '2022-05', '2022-06', '2022-07', '2022-08', '2022-09', '2022-10', '2022-11', '2022-12', '2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09', '2023-10'])) # pylint: disable=line-too-long

def test_borough():
    """Test that the sum of crimes in the borough datasets are correct"""
    assert data._Data__borough.iloc[:,3:].sum().sum() == 10928170
    assert data._Data__borough_10_21.iloc[:,3:].sum().sum() == 9146913
    assert data._Data__borough_21_23.iloc[:,3:].sum().sum() == 1781257
    assert len(data._Data__borough.columns) == 166
    assert data._Data__borough.columns.equals(pd.Index(['category', 'offence', 'borough', '2010-04', '2010-05', '2010-06', '2010-07', '2010-08', '2010-09', '2010-10', '2010-11', '2010-12', '2011-01', '2011-02', '2011-03', '2011-04', '2011-05', '2011-06', '2011-07', '2011-08', '2011-09', '2011-10', '2011-11', '2011-12', '2012-01', '2012-02', '2012-03', '2012-04', '2012-05', '2012-06', '2012-07', '2012-08', '2012-09', '2012-10', '2012-11', '2012-12', '2013-01', '2013-02', '2013-03', '2013-04', '2013-05', '2013-06', '2013-07', '2013-08', '2013-09', '2013-10', '2013-11', '2013-12', '2014-01', '2014-02', '2014-03', '2014-04', '2014-05', '2014-06', '2014-07', '2014-08', '2014-09', '2014-10', '2014-11', '2014-12', '2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06', '2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12', '2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12', '2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12', '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12', '2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12', '2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06', '2021-07', '2021-08', '2021-09', '2021-10', '2021-11', '2021-12', '2022-01', '2022-02', '2022-03', '2022-04', '2022-05', '2022-06', '2022-07', '2022-08', '2022-09', '2022-10', '2022-11', '2022-12', '2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09', '2023-10'])) # pylint: disable=line-too-long

def test_change_date_cols():
    """Test that the date columns are changed correctly"""
    change_date_cols = data._Data__change_date_cols
    df = pd.DataFrame({"201001": [1,2,3], "202108": [1,2,3]})
    assert change_date_cols(df, 0).equals(pd.DataFrame({"2010-01": [1,2,3], "2021-08": [1,2,3]}))
    assert change_date_cols(df, 1).equals(pd.DataFrame({"201001": [1,2,3], "2021-08": [1,2,3]}))
    assert change_date_cols(df, 2).equals(pd.DataFrame({"201001": [1,2,3], "202108": [1,2,3]}))

def test_make_multi_index():
    """Test that the multi-index is made correctly"""
    make_multi_index = data._Data__make_multi_index
    df = pd.DataFrame({"2010-01": [1,2,3], "2021-08": [4,5,6], "2021-09": [7,8,9], "2021-10": [10,11,12], "2021-11": [13,14,15], "2021-12": [16, 17, 18]})
    assert list(make_multi_index(df, 1).columns) == [('2021', '08'),('2021', '09'),('2021', '10'),('2021', '11'),('2021', '12')]
    assert list(make_multi_index(df, 1).index) == [1,2,3]
    assert list(make_multi_index(df, 3).columns) == [('2021', '10'),('2021', '11'),('2021', '12')]
    assert list(make_multi_index(df, 3).index) == [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

def test_ward_multi():
    """Test that the ward MultiIndex is correct"""
    assert list(data.ward.columns) == [('2010', '04'), ('2010', '05'), ('2010', '06'), ('2010', '07'), ('2010', '08'), ('2010', '09'), ('2010', '10'), ('2010', '11'), ('2010', '12'), ('2011', '01'), ('2011', '02'), ('2011', '03'), ('2011', '04'), ('2011', '05'), ('2011', '06'), ('2011', '07'), ('2011', '08'), ('2011', '09'), ('2011', '10'), ('2011', '11'), ('2011', '12'), ('2012', '01'), ('2012', '02'), ('2012', '03'), ('2012', '04'), ('2012', '05'), ('2012', '06'), ('2012', '07'), ('2012', '08'), ('2012', '09'), ('2012', '10'), ('2012', '11'), ('2012', '12'), ('2013', '01'), ('2013', '02'), ('2013', '03'), ('2013', '04'), ('2013', '05'), ('2013', '06'), ('2013', '07'), ('2013', '08'), ('2013', '09'), ('2013', '10'), ('2013', '11'), ('2013', '12'), ('2014', '01'), ('2014', '02'), ('2014', '03'), ('2014', '04'), ('2014', '05'), ('2014', '06'), ('2014', '07'), ('2014', '08'), ('2014', '09'), ('2014', '10'), ('2014', '11'), ('2014', '12'), ('2015', '01'), ('2015', '02'), ('2015', '03'), ('2015', '04'), ('2015', '05'), ('2015', '06'), ('2015', '07'), ('2015', '08'), ('2015', '09'), ('2015', '10'), ('2015', '11'), ('2015', '12'), ('2016', '01'), ('2016', '02'), ('2016', '03'), ('2016', '04'), ('2016', '05'), ('2016', '06'), ('2016', '07'), ('2016', '08'), ('2016', '09'), ('2016', '10'), ('2016', '11'), ('2016', '12'), ('2017', '01'), ('2017', '02'), ('2017', '03'), ('2017', '04'), ('2017', '05'), ('2017', '06'), ('2017', '07'), ('2017', '08'), ('2017', '09'), ('2017', '10'), ('2017', '11'), ('2017', '12'), ('2018', '01'), ('2018', '02'), ('2018', '03'), ('2018', '04'), ('2018', '05'), ('2018', '06'), ('2018', '07'), ('2018', '08'), ('2018', '09'), ('2018', '10'), ('2018', '11'), ('2018', '12'), ('2019', '01'), ('2019', '02'), ('2019', '03'), ('2019', '04'), ('2019', '05'), ('2019', '06'), ('2019', '07'), ('2019', '08'), ('2019', '09'), ('2019', '10'), ('2019', '11'), ('2019', '12'), ('2020', '01'), ('2020', '02'), ('2020', '03'), ('2020', '04'), ('2020', '05'), ('2020', '06'), ('2020', '07'), ('2020', '08'), ('2020', '09'), ('2020', '10'), ('2020', '11'), ('2020', '12'), ('2021', '01'), ('2021', '02'), ('2021', '03'), ('2021', '04'), ('2021', '05'), ('2021', '06'), ('2021', '07'), ('2021', '08'), ('2021', '09'), ('2021', '10'), ('2021', '11'), ('2021', '12'), ('2022', '01'), ('2022', '02'), ('2022', '03'), ('2022', '04'), ('2022', '05'), ('2022', '06'), ('2022', '07'), ('2022', '08'), ('2022', '09'), ('2022', '10'), ('2022', '11'), ('2022', '12'), ('2023', '01'), ('2023', '02'), ('2023', '03'), ('2023', '04'), ('2023', '05'), ('2023', '06'), ('2023', '07'), ('2023', '08'), ('2023', '09'), ('2023', '10')] # pylint: disable=line-too-long
    assert list(data.ward.index.names) == ['ward_name', 'ward_code', 'category', 'offence', 'borough']
    assert data.ward.sum().sum() == 10701946
    assert len(data.ward.columns) == 163
    assert len(data.ward.index) == 30121
    assert list(data.ward.index[0:20]) == [('Heathrow Villages', 'E05013570', 'Arson and Criminal Damage', 'Criminal Damage', 'Aviation Security (SO18)'), ('Heathrow Villages', 'E05013570', 'Miscellaneous Crimes Against Society', 'Other Notifiable Offences', 'Aviation Security (SO18)'), ('Heathrow Villages', 'E05013570', 'Theft', 'Other Theft', 'Aviation Security (SO18)'), ('Heathrow Villages', 'E05013570', 'Theft', 'Shoplifting', 'Aviation Security (SO18)'), ('Heathrow Villages', 'E05013570', 'Vehicle Offences', 'Theft from a Motor Vehicle', 'Aviation Security (SO18)'), ('Heathrow Villages', 'E05013570', 'Violence Against the Person', 'Violence with Injury', 'Aviation Security (SO18)'), ('Heathrow Villages', 'E05013570', 'Violence Against the Person', 'Violence without Injury', 'Aviation Security (SO18)'), ('Abbey', 'E05014053', 'Arson and Criminal Damage', 'Arson', 'Barking and Dagenham'), ('Abbey', 'E05014053', 'Arson and Criminal Damage', 'Criminal Damage', 'Barking and Dagenham'), ('Abbey', 'E05014053', 'Burglary', 'Burglary Business and Community', 'Barking and Dagenham'), ('Abbey', 'E05014053', 'Burglary', 'Domestic Burglary', 'Barking and Dagenham'), ('Abbey', 'E05014053', 'Drug Offences', 'Drug Trafficking', 'Barking and Dagenham'), ('Abbey', 'E05014053', 'Drug Offences', 'Possession of Drugs', 'Barking and Dagenham'), ('Abbey', 'E05014053', 'Historical Fraud and Forgery', 'Historical Fraud and Forgery', 'Barking and Dagenham'), ('Abbey', 'E05014053', 'Miscellaneous Crimes Against Society', 'Bigamy', 'Barking and Dagenham'), ('Abbey', 'E05014053', 'Miscellaneous Crimes Against Society', 'Dangerous Driving', 'Barking and Dagenham'), ('Abbey', 'E05014053', 'Miscellaneous Crimes Against Society', 'Exploitation of Prostitution', 'Barking and Dagenham'), ('Abbey', 'E05014053', 'Miscellaneous Crimes Against Society', 'Forgery or Use of Drug Prescription', 'Barking and Dagenham'), ('Abbey', 'E05014053', 'Miscellaneous Crimes Against Society', 'Fraud or Forgery Associated with Driver Records', 'Barking and Dagenham'), ('Abbey', 'E05014053', 'Miscellaneous Crimes Against Society', 'Going Equipped for Stealing', 'Barking and Dagenham')] # pylint: disable=line-too-long

def test_lsoa_multi():
    """Test that the lsoa MultiIndex is correct"""
    assert list(data.lsoa.columns) == [('2019', '03'), ('2019', '04'), ('2019', '05'), ('2019', '06'), ('2019', '07'), ('2019', '08'), ('2019', '09'), ('2019', '10'), ('2019', '11'), ('2019', '12'), ('2020', '01'), ('2020', '02'), ('2019', '01'), ('2019', '02'), ('2010', '04'), ('2010', '05'), ('2010', '06'), ('2010', '07'), ('2010', '08'), ('2010', '09'), ('2010', '10'), ('2010', '11'), ('2010', '12'), ('2011', '01'), ('2011', '02'), ('2011', '03'), ('2011', '04'), ('2011', '05'), ('2011', '06'), ('2011', '07'), ('2011', '08'), ('2011', '09'), ('2011', '10'), ('2011', '11'), ('2011', '12'), ('2012', '01'), ('2012', '02'), ('2012', '03'), ('2012', '04'), ('2012', '05'), ('2012', '06'), ('2012', '07'), ('2012', '08'), ('2012', '09'), ('2012', '10'), ('2012', '11'), ('2012', '12'), ('2013', '01'), ('2013', '02'), ('2013', '03'), ('2013', '04'), ('2013', '05'), ('2013', '06'), ('2013', '07'), ('2013', '08'), ('2013', '09'), ('2013', '10'), ('2013', '11'), ('2013', '12'), ('2014', '01'), ('2014', '02'), ('2014', '03'), ('2014', '04'), ('2014', '05'), ('2014', '06'), ('2014', '07'), ('2014', '08'), ('2014', '09'), ('2014', '10'), ('2014', '11'), ('2014', '12'), ('2015', '01'), ('2015', '02'), ('2015', '03'), ('2015', '04'), ('2015', '05'), ('2015', '06'), ('2015', '07'), ('2015', '08'), ('2015', '09'), ('2015', '10'), ('2015', '11'), ('2015', '12'), ('2016', '01'), ('2016', '02'), ('2016', '03'), ('2016', '04'), ('2016', '05'), ('2016', '06'), ('2016', '07'), ('2016', '08'), ('2016', '09'), ('2016', '10'), ('2016', '11'), ('2016', '12'), ('2017', '01'), ('2017', '02'), ('2017', '03'), ('2017', '04'), ('2017', '05'), ('2017', '06'), ('2017', '07'), ('2017', '08'), ('2017', '09'), ('2017', '10'), ('2017', '11'), ('2017', '12'), ('2018', '01'), ('2018', '02'), ('2018', '03'), ('2018', '04'), ('2018', '05'), ('2018', '06'), ('2018', '07'), ('2018', '08'), ('2018', '09'), ('2018', '10'), ('2018', '11'), ('2018', '12'), ('2020', '03'), ('2020', '04'), ('2020', '05'), ('2020', '06'), ('2020', '07'), ('2020', '08'), ('2020', '09'), ('2020', '10'), ('2020', '11'), ('2020', '12'), ('2021', '01'), ('2021', '02'), ('2021', '03'), ('2021', '04'), ('2021', '05'), ('2021', '06'), ('2021', '07'), ('2021', '08'), ('2021', '09'), ('2021', '10'), ('2021', '11'), ('2021', '12'), ('2022', '01'), ('2022', '02'), ('2022', '03'), ('2022', '04'), ('2022', '05'), ('2022', '06'), ('2022', '07'), ('2022', '08'), ('2022', '09'), ('2022', '10'), ('2022', '11'), ('2022', '12'), ('2023', '01'), ('2023', '02'), ('2023', '03'), ('2023', '04'), ('2023', '05'), ('2023', '06'), ('2023', '07'), ('2023', '08'), ('2023', '09'), ('2023', '10')] # pylint: disable=line-too-long
    assert list(data.lsoa.index.names) == ['lsoa_code', 'lsoa_name', 'borough', 'category', 'offence']
    assert data.lsoa.sum().sum() == 10414629
    assert len(data.lsoa.columns) == 163
    assert len(data.lsoa.index) == 157959
    assert list(data.lsoa.index[0:20]) == [('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Arson and Criminal Damage', 'Arson'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Arson and Criminal Damage', 'Criminal Damage'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Burglary', 'Burglary Business and Community'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Burglary', 'Domestic Burglary'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Drug Offences', 'Drug Trafficking'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Drug Offences', 'Possession of Drugs'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Miscellaneous Crimes Against Society', 'Handling Stolen Goods'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Miscellaneous Crimes Against Society', 'Making, Supplying or Possessing Articles for use i'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Miscellaneous Crimes Against Society', 'Obscene Publications'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Miscellaneous Crimes Against Society', 'Other Forgery'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Miscellaneous Crimes Against Society', 'Other Notifiable Offences'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Miscellaneous Crimes Against Society', 'Perverting Course of Justice'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Miscellaneous Crimes Against Society', 'Possession of False Documents'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Miscellaneous Crimes Against Society', 'Threat or Possession With Intent to Commit Crimina'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Possession of Weapons', 'Possession of Article with Blade or Point'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Possession of Weapons', 'Possession of Firearms Offences'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Public Order Offences', 'Other Offences Against the State, or Public Order'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Public Order Offences', 'Public Fear Alarm or Distress'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Public Order Offences', 'Racially or Religiously Aggravated Public Fear, Al'), ('E01000006', 'Barking and Dagenham 016A', 'E09000002', 'Robbery', 'Robbery of Personal Property')] # pylint: disable=line-too-long

def test_borough_multi():
    """Test that the borough MultiIndex is correct"""
    assert list(data.borough.columns) == [('2010', '04'), ('2010', '05'), ('2010', '06'), ('2010', '07'), ('2010', '08'), ('2010', '09'), ('2010', '10'), ('2010', '11'), ('2010', '12'), ('2011', '01'), ('2011', '02'), ('2011', '03'), ('2011', '04'), ('2011', '05'), ('2011', '06'), ('2011', '07'), ('2011', '08'), ('2011', '09'), ('2011', '10'), ('2011', '11'), ('2011', '12'), ('2012', '01'), ('2012', '02'), ('2012', '03'), ('2012', '04'), ('2012', '05'), ('2012', '06'), ('2012', '07'), ('2012', '08'), ('2012', '09'), ('2012', '10'), ('2012', '11'), ('2012', '12'), ('2013', '01'), ('2013', '02'), ('2013', '03'), ('2013', '04'), ('2013', '05'), ('2013', '06'), ('2013', '07'), ('2013', '08'), ('2013', '09'), ('2013', '10'), ('2013', '11'), ('2013', '12'), ('2014', '01'), ('2014', '02'), ('2014', '03'), ('2014', '04'), ('2014', '05'), ('2014', '06'), ('2014', '07'), ('2014', '08'), ('2014', '09'), ('2014', '10'), ('2014', '11'), ('2014', '12'), ('2015', '01'), ('2015', '02'), ('2015', '03'), ('2015', '04'), ('2015', '05'), ('2015', '06'), ('2015', '07'), ('2015', '08'), ('2015', '09'), ('2015', '10'), ('2015', '11'), ('2015', '12'), ('2016', '01'), ('2016', '02'), ('2016', '03'), ('2016', '04'), ('2016', '05'), ('2016', '06'), ('2016', '07'), ('2016', '08'), ('2016', '09'), ('2016', '10'), ('2016', '11'), ('2016', '12'), ('2017', '01'), ('2017', '02'), ('2017', '03'), ('2017', '04'), ('2017', '05'), ('2017', '06'), ('2017', '07'), ('2017', '08'), ('2017', '09'), ('2017', '10'), ('2017', '11'), ('2017', '12'), ('2018', '01'), ('2018', '02'), ('2018', '03'), ('2018', '04'), ('2018', '05'), ('2018', '06'), ('2018', '07'), ('2018', '08'), ('2018', '09'), ('2018', '10'), ('2018', '11'), ('2018', '12'), ('2019', '01'), ('2019', '02'), ('2019', '03'), ('2019', '04'), ('2019', '05'), ('2019', '06'), ('2019', '07'), ('2019', '08'), ('2019', '09'), ('2019', '10'), ('2019', '11'), ('2019', '12'), ('2020', '01'), ('2020', '02'), ('2020', '03'), ('2020', '04'), ('2020', '05'), ('2020', '06'), ('2020', '07'), ('2020', '08'), ('2020', '09'), ('2020', '10'), ('2020', '11'), ('2020', '12'), ('2021', '01'), ('2021', '02'), ('2021', '03'), ('2021', '04'), ('2021', '05'), ('2021', '06'), ('2021', '07'), ('2021', '08'), ('2021', '09'), ('2021', '10'), ('2021', '11'), ('2021', '12'), ('2022', '01'), ('2022', '02'), ('2022', '03'), ('2022', '04'), ('2022', '05'), ('2022', '06'), ('2022', '07'), ('2022', '08'), ('2022', '09'), ('2022', '10'), ('2022', '11'), ('2022', '12'), ('2023', '01'), ('2023', '02'), ('2023', '03'), ('2023', '04'), ('2023', '05'), ('2023', '06'), ('2023', '07'), ('2023', '08'), ('2023', '09'), ('2023', '10')] # pylint: disable=line-too-long
    assert list(data.borough.index.names) == ['category', 'offence', 'borough']
    assert data.borough.sum().sum() == 10928170
    assert len(data.borough.columns) == 163
    assert len(data.borough.index) == 1745
    assert list(data.borough.index[0:20]) == [('Arson and Criminal Damage', 'Arson', 'Barking and Dagenham'), ('Arson and Criminal Damage', 'Criminal Damage', 'Barking and Dagenham'), ('Burglary', 'Burglary Business and Community', 'Barking and Dagenham'), ('Burglary', 'Domestic Burglary', 'Barking and Dagenham'), ('Drug Offences', 'Drug Trafficking', 'Barking and Dagenham'), ('Drug Offences', 'Possession of Drugs', 'Barking and Dagenham'), ('Historical Fraud and Forgery', 'Historical Fraud and Forgery', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Absconding from Lawful Custody', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Bail Offences', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Bigamy', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Dangerous Driving', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Disclosure, Obstruction, False or Misleading State', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Exploitation of Prostitution', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Forgery or Use of Drug Prescription', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Fraud or Forgery Associated with Driver Records', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Going Equipped for Stealing', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Handling Stolen Goods', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Making, Supplying or Possessing Articles for use i', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Obscene Publications', 'Barking and Dagenham'), ('Miscellaneous Crimes Against Society', 'Other Forgery', 'Barking and Dagenham')] # pylint: disable=line-too-long

def test_data_consistency():
    """Tests that the data is the same between the different data sets"""
    # This test checks that the borough and ward data sets have the same categories for offences
    assert list(np.sort(data.borough.index.get_level_values(0).unique())) == list(np.sort(data.ward.index.get_level_values(2).unique()))
    # This test checks that the LSOA and ward datasets have the same categories for offences. Two of the missing categories (Historical Fraud and Forgery and Sexual Offences) are added to the LSOA list
    assert list(np.sort(np.append(data.lsoa.index.get_level_values(3).unique().to_numpy(), ['Sexual Offences', 'Historical Fraud and Forgery']))) == list(np.sort(data.ward.index.get_level_values(2).unique()))
    #This test checks that the borough and ward data sets have the same list of offences
    assert list(np.sort(data.borough.index.get_level_values(1).unique())) == list(np.sort(data.ward.index.get_level_values(3).unique()))
    #This test checks that the LSOA and ward datasets have the same list of offences. Three of the missing offences (Rape, Other Sexual Offences and Historical Fraud and Forgery) are added to the LSOA list.
    assert list(np.sort(np.append(data.lsoa.index.get_level_values(4).unique().to_numpy(), ['Rape', 'Other Sexual Offences', 'Historical Fraud and Forgery']))) == list(np.sort(data.ward.index.get_level_values(3).unique()))
