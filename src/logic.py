from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
import pandas as pd


def roman_string_to_date_parser(roman_string: str) -> pd.Timestamp:
    pass


def distance_between_points(point1, point2):
    """Calculate the distance between two points.

    Args:
        point1 (??): ???
        point2 (??): ???
    
    Returns:
        np.float: distance between point1 and point2
    """
    return np.sqrt(
        (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
        )


@dataclass
class Stop:
    name: str
    x: int
    y: int

    @property
    def coords(self):
        return (self.x, self.y)


class Route:
    
    def __init__(self, id: int, stops: List[Stop]):
        self.id = id
        self.stops = stops
        self.stop_names = [stop.name for stop in stops]
        self.total_distance = [
            distance_between_points(point1, point2)
            for point1, point2 in zip(stops[0:], stops[1:])
            ].sum()

    def add_point(self, stop: Stop):
        self.stops.append(stop)

    def remove_point(self, stop: Stop):
        self.stops.remove(stop)

    def recalculate_distance(self):
        self.total_distance = [
            distance_between_points(point1, point2)
            for point1, point2 in zip(self.stops[0:], self.stops[1:])
            ].sum()


def replace_value(
    df: pd.DataFrame,
    col: str,
    value: str, 
    replace_with: str):
    """Replace value in col with replace_with.

    Args:
        df (pd.DataFrame): target data
        col (str): column name
        value (str): value to replace
        replace_with (str): value to replace with
    """
    df.loc[df[col] == value, col] = replace_with
    return df


def add_rolling_stat(
    df: pd.DataFrame,
    groupby_cols: list,
    func: tuple,
    rolling_window: int,
    measure_col: str,
    min_periods: int,
    date_col: str) -> Tuple[pd.DataFrame, str]:
    """Add rolling func of a target col per unique groups in
    groupby_cols to df.

    Args:
        df (pd.DataFrame): target data
        groupby_cols (list): columns to group on
        func (tuple): function to apply as first element.
            Additional elements will be passed as parameters to
            this function.
        rolling_window (int): rolling window size
        measure_col (str): name of the measure column to apply func to
        min_periods (int): minimum number of observations in window
        date_col (str): name of the date column

    Returns:
        df: pd.DataFrame with rolling feature added
        colname_rolling (str): new column name for rolling feature
    """
    str_groupby_list = "_".join(groupby_cols)
    colname_rolling = (
        f'{measure_col}_{str_groupby_list}_{rolling_window}_'
        f'{func[0].__name__}')

    if len(func) > 1:
        colname_rolling = f'{colname_rolling}_{"_".join(map(str, func[1:]))}'

    df.sort_values(date_col, inplace=True)
    df['groupby_dummy_col'] = 0
    df[colname_rolling] = (df
        .groupby(groupby_cols + ['groupby_dummy_col'])
        .rolling(rolling_window, min_periods=min_periods)[measure_col]
        .apply(func[0], args=func[1:])
        .reset_index(groupby_cols + ['groupby_dummy_col'], drop=True)
        )

    df.drop(columns=['groupby_dummy_col'], inplace=True)
    return df, colname_rolling
