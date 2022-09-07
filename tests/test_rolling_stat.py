import numpy as np
import pandas as pd
import cfg_col_names
import pytest
from pandas.testing import assert_frame_equal
from src.logic import add_rolling_stat
import cfg_col_names

GROUPBY_COLS = [cfg_col_names.LOC_NAME_COL]
GROUPBY_COLS_2 = [cfg_col_names.LOC_NAME_COL, cfg_col_names.SORTING_MACHINE_COL]

@pytest.mark.parametrize(
    "input_df, func, window, groupby_cols, expected_output_df",
    [pytest.param(
        # input df containing some arbitrary values
        pd.DataFrame({
            cfg_col_names.PROCESS_DATE_COL: [
                pd.to_datetime('2020-01-01'), pd.to_datetime('2020-01-02'),
                pd.to_datetime('2020-01-03'), pd.to_datetime('2020-01-04')] * 2,
            cfg_col_names.LOC_NAME_COL: [
                'Rotterdam', 'Rotterdam', 'Rotterdam', 'Rotterdam',
                'Amsterdam', 'Amsterdam', 'Amsterdam', 'Amsterdam'],
            cfg_col_names.TARGET_COL: [
                10, 20, 30, 40, 40, 30, 20, 10]
            }),
        (np.mean,),
        2,
        GROUPBY_COLS,
        # expected output df
        pd.DataFrame({
            cfg_col_names.PROCESS_DATE_COL: pd.Series([
                '2020-01-01', '2020-01-01', '2020-01-02', '2020-01-02',
                '2020-01-03', '2020-01-03', '2020-01-04', '2020-01-04'
                ], dtype='datetime64[ns]'),
            cfg_col_names.LOC_NAME_COL: [
                'Rotterdam', 'Amsterdam', 'Rotterdam', 'Amsterdam',
                'Rotterdam', 'Amsterdam', 'Rotterdam', 'Amsterdam'],
            cfg_col_names.TARGET_COL: [10, 40, 20, 30, 30, 20, 40, 10],
            f'{cfg_col_names.TARGET_COL}_{cfg_col_names.LOC_NAME_COL}_2_mean':
                [10.0, 40.0, 15.0, 35.0, 25.0, 25.0, 35.0, 15.0]
                }),
        id='returns_df_plus_rolling_mean_of_target_col'),

     pytest.param(
         # input df containing some arbitrary values
        pd.DataFrame({
            cfg_col_names.PROCESS_DATE_COL: [
                pd.to_datetime('2020-01-01'), pd.to_datetime('2020-01-04'),
                pd.to_datetime('2020-01-02'), pd.to_datetime('2020-01-03'),
                pd.to_datetime('2020-01-03'), pd.to_datetime('2020-01-02'),
                pd.to_datetime('2020-01-04'), pd.to_datetime('2020-01-01')],
            cfg_col_names.LOC_NAME_COL: [
                'Rotterdam', 'Rotterdam', 'Rotterdam', 'Rotterdam',
                'Amsterdam', 'Amsterdam', 'Amsterdam', 'Amsterdam'],
            cfg_col_names.TARGET_COL: [10, 40, 20, 30, 20, 30, 10, 40]
            }),
        (np.mean,),
        2,
        GROUPBY_COLS,
        # expected output df
        pd.DataFrame({
            cfg_col_names.PROCESS_DATE_COL: [
                pd.to_datetime('2020-01-01'), pd.to_datetime('2020-01-01'),
                pd.to_datetime('2020-01-02'), pd.to_datetime('2020-01-02'),
                pd.to_datetime('2020-01-03'), pd.to_datetime('2020-01-03'),
                pd.to_datetime('2020-01-04'), pd.to_datetime('2020-01-04')],
            cfg_col_names.LOC_NAME_COL: [
                'Rotterdam', 'Amsterdam', 'Rotterdam', 'Amsterdam',
                'Rotterdam', 'Amsterdam', 'Rotterdam', 'Amsterdam'],
            cfg_col_names.TARGET_COL: [10, 40, 20, 30, 30, 20, 40, 10],
            f'{cfg_col_names.TARGET_COL}_{cfg_col_names.LOC_NAME_COL}_2_mean':
                [10.0, 40.0, 15.0, 35.0, 25.0, 25.0, 35.0, 15.0]
                }),
        id='returns_df_plus_rolling_mean_of_target_col_from_unsorted'),

     pytest.param(
        # input df containing some arbitrary values
        pd.DataFrame({
            cfg_col_names.PROCESS_DATE_COL: [
                pd.to_datetime('2020-01-01'), pd.to_datetime('2020-01-02'),
                pd.to_datetime('2020-01-03'), pd.to_datetime('2020-01-04')] * 2,
            cfg_col_names.LOC_NAME_COL: [
                'Rotterdam', 'Rotterdam', 'Rotterdam', 'Rotterdam',
                'Amsterdam', 'Amsterdam', 'Amsterdam', 'Amsterdam'],
            cfg_col_names.SORTING_MACHINE_COL: [
                'SMK', 'SMX',
                'SMK', 'SMX',
                'SMK', 'SMX',
                'SMK', 'SMX'],
            cfg_col_names.TARGET_COL: [10, 20, 30, 40, 40, 30, 20, 10]
            }),
        (np.mean,),
        2,
        GROUPBY_COLS_2,
        # expected output df
        # expected output df
        pd.DataFrame({
            cfg_col_names.PROCESS_DATE_COL: [
                pd.to_datetime('2020-01-01'), pd.to_datetime('2020-01-01'),
                pd.to_datetime('2020-01-02'), pd.to_datetime('2020-01-02'),
                pd.to_datetime('2020-01-03'), pd.to_datetime('2020-01-03'),
                pd.to_datetime('2020-01-04'), pd.to_datetime('2020-01-04')],
            cfg_col_names.LOC_NAME_COL: [
                'Rotterdam', 'Amsterdam', 'Rotterdam', 'Amsterdam',
                'Rotterdam', 'Amsterdam', 'Rotterdam', 'Amsterdam'],
            cfg_col_names.SORTING_MACHINE_COL: [
                'SMK', 'SMK',
                'SMX', 'SMX',
                'SMK', 'SMK',
                'SMX', 'SMX'],
            cfg_col_names.TARGET_COL: [10, 40, 20, 30, 30, 20, 40, 10],
            f'{cfg_col_names.TARGET_COL}_{cfg_col_names.LOC_NAME_COL}'
            f'_{cfg_col_names.SORTING_MACHINE_COL}_2_mean':
                [10.0, 40.0, 20.0, 30.0, 20.0, 30.0, 30.0, 20.0]
                }
                     ),
        id='returns_df_plus_rolling_mean_of_target_col_with_2_groupby_levels'),
     ]
    )


def test_add_rolling_stat(input_df, func, window, groupby_cols, expected_output_df):
    output_df, _ = add_rolling_stat(
        input_df,
        groupby_cols=groupby_cols,
        func=func,
        rolling_window=window,
        measure_col=cfg_col_names.TARGET_COL,
        min_periods=1,
        date_col=cfg_col_names.PROCESS_DATE_COL)

    output_df.reset_index(drop=True, inplace=True)
    expected_output_df.reset_index(drop=True, inplace=True)

    print(' Expected:\n', expected_output_df)
    print(expected_output_df.dtypes)
    print(' Calculated:\n', output_df)
    print(output_df.dtypes)

    assert_frame_equal(expected_output_df, output_df, check_dtype=True)
