
# import libraries
import sys
import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# load messages dataset
def load_data(messages_filepath, categories_filepath):
    '''
    INPUT:
        messages_filepath - path to the messages file
        categories_filepath - path to the categories file

    OUTPUT:
        df - data frame with merged messages data and categories data
    '''
    
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on='id')
    
    return df 

def clean_data(df):
    '''
    INPUT:
        df - merged messages and categories data
    OUTPUT:
        df - merged messages and categories data with clean category columns
    '''
    
    categories = df['categories'].str.split(pat=';', expand=True)
    row = categories.iloc[0]
    category_colnames = row.apply(lambda x:x[:-2])
    categories.columns = category_colnames

    for column in categories:
        categories[column] = categories[column].astype(str).str[-1]
        categories[column] =  categories[column].astype(int)
    
    df = df.drop('categories',axis=1)
    df = pd.concat([df,categories],axis=1)
    df = df.drop_duplicates()

    # value 2 in the related column is invalid
    # I will replace the value 2 to 1, which is the majority class in the filed
    df['related'] = df['related'].map(lambda x: 1 if x == 2 else x)

    return df

def save_data(df, database_filename):
    '''
    INPUT:
        df - cleaned data frame
        database_filename - path to SQLite database 
    '''

    engine = create_engine('sqlite:///'+ database_filename)
    table_name = os.path.basename(database_filename).replace('.db','') + '_table'
    df.to_sql(table_name, engine, index=False, if_exists='replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
