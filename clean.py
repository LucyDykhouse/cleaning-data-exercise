"""
A simple script to clean up the Tate artwork dataset.
"""


# Library imports
import pandas as pd


def process_file(path):
    data = pd.read_csv(path, low_memory=False)
    return data


def understand_data(df):
    print('\n**** Understanding Data Section ****')
    print('\nData head:\n', df.head())
    print('\nData types of columns:\n', df.dtypes)
    df.year = pd.to_numeric(df.year, errors='coerce')
    df.height = pd.to_numeric(df.height, errors='coerce')
    print('\nData types following conversion:\n', df.dtypes)
    print('\nMin year: ', df['year'].min())
    print('\nMax year: ', df['year'].max())
    print('\nAvg year: ', df['year'].mean())
    print('\nStats across all columns:\n', df.agg(['min', 'max', 'mean', 'std']))
    print('\nMean of height column per artist:\n', df.groupby('artist')['height'].transform('mean'))
    print('\nExamine columns with word artist:\n', df.filter(like='artist'))
    print('\nExamine columns with word year (case insensitive):\n', df.filter(regex="(?i)year"))


def adjust_columns(df):
    print('\n\n**** Removing and Fixing Columns Section ****')
    print('\nDrop first row (Not in place):\n', df.drop(0))
    print('\nDrop id column:\n', df.drop('id', axis=1))
    print('\nDrop multiple columns:\n', df.drop(columns=['id', 'year', 'height', 'artistRole', 'creditLine']))
    print('\nDrop multiple rows:\n', df.drop(labels=[0, 1, 2]))
    print('\nData columns:\n', df.columns)
    print('\nData columns to lower (Not in place):\n', df.columns.str.lower())
    data1 = pd.read_csv('artwork_sample.csv')
    data1.columns = map(lambda x: x.lower(), data1.columns)
    print('\nColumns to lowercase using function:\n', data1.columns)
    data1.rename({"thumbnailUrl":"thumbnail"}, axis=1, inplace=True)
    data1.columns = ['id', 'accessionNumber', 'artist', 'artistRole', 'artistId', 'title', 'dateText', 'medium', 'creditLine', 'year', 'acquisitionYear', 'dimensions', 'width', 'height', 'depth', 'units', 'inscription', 'thumbnailCopyright', 'thumbnail', 'url']
    print('\nRenamed columns:\n', data1.columns)


def main():
    data = process_file('artwork_sample.csv')
    understand_data(data)
    adjust_columns(data)


main()
