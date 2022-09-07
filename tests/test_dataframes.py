import os

import pandas as pd
import pandas.testing
import pytest
from src.logic import replace_value


# Create a pytest fixture for a pd.DataFrame
@pytest.fixture(scope='session')
# scope='session' means the fixture is created once per session. Do we want this?
def df():
    return pd.DataFrame({'a': [1, 2, 3],
                         'b': [4, 5, 6],
                         'c': pd.Series([
                             '2020-01-01',
                             '2020-01-02',
                             '2020-01-03'], dtype='datetime64[ns]'),
                         'd': [pd.NA, 0, '1']})


# Test the fixture
def test_fixture(df):
    assert df.shape == (3, 4)
    assert df.dtypes['a'] == 'int64'
    assert df.dtypes['b'] == 'int64'
    assert df.dtypes['c'] == 'datetime64[ns]'
    assert df.dtypes['d'] == 'object'


# Quickly testing a function with multiple in and outputs without 
# boilerplate using parameterize and the fixture
@pytest.mark.parametrize(
    "col, value, replace_with, expected_output_df", 
    [pytest.param(
        'a', 1, 100,
        pd.DataFrame({'a': [100, 2, 3],
                      'b': [4, 5, 6],
                      'c': pd.Series(['2020-01-01',
                                      '2020-01-02',
                                      '2020-01-03'],
                                     dtype='datetime64[ns]'),
                      'd': [pd.NA, 0, '1']}), id='value_is_replaced')
     ]
    )

def test_replace_value(df, value, replace_with, col, expected_output_df):
    # We can leverage built in pandas testing asserts, which can be
    # configured to be less or more strict with dtypes, indexes, etc.
    pandas.testing.assert_frame_equal(
        replace_value(
            df=df,
            col=col,
            value=value,
            replace_with=replace_with
            ),
        expected_output_df)


# A test can also read from a csv file (can become useful for larger 
# data). This lies more in the realm of integration testing.
# In this case you can prepare and save a csv file with the 
# expected output (and of course also input). For now we use the fixture
# and test if we can only keep the row where the date is 2020-01-01.
file_path = os.path.dirname(__file__)
output_path = f'{file_path}/test_data'

def test_keep_only_jan_first(df):
    output_df = df.loc[df['c'] == '2020-01-01']
    expected_output_df = pd.read_csv(f'{output_path}/test_out',
                                     parse_dates=['c'],
                                     date_parser=pd.to_datetime)

    # Sometimes with reading/writing from csv you have to do some manual 
    # type casting can you think of a solution for this?
    expected_output_df['d'] = expected_output_df['d'].astype('object') 
    pandas.testing.assert_frame_equal(output_df, expected_output_df)