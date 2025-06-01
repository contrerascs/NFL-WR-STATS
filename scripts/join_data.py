import pandas as pd
import os

def join_data(year):
    inputfile1 = f'data/data_csv/wr_standard_stats_{year}.csv'
    inputfile2 = f'data/data_csv/wr_advanced_stats_{year}.csv'
    outputfile = f'data/data_csv/wr_complete_stats_season_{year}.csv'

    