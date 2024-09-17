import pandas as pd

def get_range(series: list) -> list:
  """Returns a list of the max and min values for a series

  Args:
      series (list): List of numerical values

  Returns:
      list: list containing min and max values
  """
  return [series.max(), series.min()]

def groupby_count(df, col):
  return df.group_by(col).count()