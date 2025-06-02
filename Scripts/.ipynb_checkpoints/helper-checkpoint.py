import pandas as pd
import os

def get_data(folder_path):
    all_dataframes = []

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.startswith('reference-person-age-ranges-') and filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_excel(file_path)
            df['Year'] = filename[-9:-5]  # Extract year from filename
            all_dataframes.append(df)

    # Concatenate all dataframes into one and clean up
    df = pd.concat(all_dataframes, ignore_index=True)
    df.columns = [col.replace('\n', ' ') for col in df.columns]
    return df

def get_item(df, text, offset = 1):
    all_dataframes = []
    index = df[df['Item'].str.strip() == text].index
    for i in index:
        all_dataframes.append(df.iloc[i + offset])
    return all_dataframes

def get_helper(data, text, offset = 1):
    df = pd.DataFrame(get_item(data, text, offset))
    df = df.loc[df.drop_duplicates(subset=['Year']).index]
    df.set_index('Year', inplace=True)
    return df.drop('Item', axis=1)