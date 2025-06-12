import pandas as pd
import os

def get_data(folder_path):
    """
    Load and combine Excel files from a folder containing age-range data by year.

    Parameters:
    folder_path (str): Path to the folder containing Excel files. Files must start with 
                       'reference-person-age-ranges-' and end with '.xlsx'.

    Returns:
    pd.DataFrame: A single concatenated DataFrame with an added 'Year' column, cleaned of newline characters in column headers.
    """
    all_dataframes = []

    try:
        if not os.path.isdir(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

        matched_files = [
            f for f in os.listdir(folder_path)
            if f.startswith('reference-person-age-ranges-') and f.endswith('.xlsx')
        ]

        if not matched_files:
            raise FileNotFoundError("No matching Excel files found in the specified folder.")

        for filename in matched_files:
            file_path = os.path.join(folder_path, filename)
            try:
                df = pd.read_excel(file_path)
                df['Year'] = filename[-9:-5]  # Extract year from filename
                all_dataframes.append(df)
            except Exception as e:
                print(f"Error reading file '{filename}': {e}")

        if not all_dataframes:
            raise ValueError("No dataframes were loaded successfully.")

        df = pd.concat(all_dataframes, ignore_index=True)
        df.columns = [col.replace('\n', ' ') for col in df.columns]
        return df

    except Exception as e:
        print(f"Error in get_data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on failure

def get_item(df, text, offset=1):
    """
    Retrieve rows from the DataFrame that are located a fixed number of rows after rows
    where the 'Item' column matches a specified value.

    Parameters:
    df (pd.DataFrame): The DataFrame to search.
    text (str): The text to match in the 'Item' column.
    offset (int, optional): The number of rows to offset from the matching row. Default is 1.

    Returns:
    list: A list of Series objects representing the retrieved rows.
    """
    try:
        if 'Item' not in df.columns:
            raise KeyError("The DataFrame does not contain an 'Item' column.")

        matching_indices = df[df['Item'].str.strip() == text].index
        result = []

        for i in matching_indices:
            if i + offset < len(df):
                result.append(df.iloc[i + offset])
            else:
                print(f"Index {i + offset} out of bounds. Skipping.")

        if not result:
            print(f"No matching items found with offset '{offset}' for '{text}'.")

        return result

    except Exception as e:
        print(f"Error in get_item: {e}")
        return []

def get_helper(data, text, offset=1):
    """
    Extract and format specific rows from a DataFrame for time-series analysis.

    Parameters:
    data (pd.DataFrame): The source DataFrame containing yearly data.
    text (str): The value to search for in the 'Item' column.
    offset (int, optional): Number of rows to skip after the matched row to retrieve target data. Default is 1.

    Returns:
    pd.DataFrame: A cleaned DataFrame with 'Year' as the index and the 'Item' column removed.
    Only the first instance of each year is retained.
    """
    try:
        items = get_item(data, text, offset)
        if not items:
            raise ValueError("No rows extracted using get_item.")

        df = pd.DataFrame(items)
        if 'Year' not in df.columns:
            raise KeyError("The extracted data does not contain a 'Year' column.")

        df = df.loc[df.drop_duplicates(subset=['Year']).index]
        df.set_index('Year', inplace=True)

        if 'Item' in df.columns:
            df = df.drop('Item', axis=1)

        return df

    except Exception as e:
        print(f"Error in get_helper: {e}")
        return pd.DataFrame()
