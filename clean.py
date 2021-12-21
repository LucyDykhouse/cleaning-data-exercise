"""
A simple script to clean up the Tate artwork dataset.
"""


# Library imports
import pandas as pd


def process_file(path):
    data = pd.read_csv(path, low_memory=False)
    return data


def understand_data(df):
    print('\nUnderstanding Data Section')
    print('\n', df.head())
    print('\n', df.dtypes)
    df.year = pd.to_numeric(df.year, errors='coerce')
    df.height = pd.to_numeric(df.height, errors='coerce')
    print('\n', df.dtypes)
    print('\nMin year: ', df['year'].min())
    print('\nMax year: ', df['year'].max())
    print('\nAvg year: ', df['year'].mean())
    print('\nStats across all columns:\n', df.agg(['min', 'max', 'mean', 'std']))
    print('\nMean of height column per artist:\n', df.groupby('artist')['height'].transform('mean'))
    print('\nExamine columns with word artist:\n', df.filter(like='artist'))
    print('\nExamine columns with word year (case insensitive):\n', df.filter(regex="(?i)year"))


def main():
    data = process_file('artwork_sample.csv')
    understand_data(data)


main()
