import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def get_line_plot(df, text, columns):
    """
    Generate a line plot for the specified columns in the DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame with time-series data.
    text (str): Title and y-axis label for the plot.
    columns (list): List of column names to plot.
    """
    try:
        if df.empty:
            raise ValueError("Input DataFrame is empty.")
        if not all(col in df.columns for col in columns):
            missing = [col for col in columns if col not in df.columns]
            raise KeyError(f"The following columns are missing from DataFrame: {missing}")
        
        x = df.index.astype(int)
        plt.figure(figsize=(10, 6))
        for i in columns:
            plt.plot(x, df[i], marker='o', label=i)
        plt.title(text + " Over Time")
        plt.xlabel("Year")
        plt.ylabel(text)
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Error in get_line_plot: {e}")

def get_heat_plot(df, text):
    """
    Generate a heatmap for the values in the DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing numeric values.
    text (str): Title of the heatmap.
    """
    try:
        if df.empty:
            raise ValueError("Input DataFrame is empty.")
        if not pd.api.types.is_numeric_dtype(df.dtypes).all():
            raise TypeError("All values in DataFrame must be numeric for heatmap.")
        
        plt.figure(figsize=(6, 4))
        sns.heatmap(df, cmap='coolwarm', linewidths=0.5)
        plt.title(text)
        plt.show()

    except Exception as e:
        print(f"Error in get_heat_plot: {e}")

def get_bar_plot(df, text, values):
    """
    Generate a bar plot using the DataFrame index as x-axis and provided values as bar heights.

    Parameters:
    df (pd.DataFrame): DataFrame whose index will be used for x-axis values.
    text (str): Title of the bar plot.
    values (list or pd.Series): Heights of the bars corresponding to the DataFrame index.
    """
    try:
        if df.empty:
            raise ValueError("Input DataFrame is empty.")
        if len(values) != len(df):
            raise ValueError("Length of 'values' must match the number of rows in DataFrame.")
        
        plt.bar(df.index.astype(int), values, color='skyblue')
        plt.title(text + " Over Time")
        plt.show()

    except Exception as e:
        print(f"Error in get_bar_plot: {e}")

def graph_all(df, text, columns):
    """
    Display both a line plot and heatmap for the given DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data to visualize.
    text (str): Title and label used for the plots.
    columns (list): List of column names to include in the line plot.
    """
    try:
        get_line_plot(df, text, columns)
        get_heat_plot(df, text)
    except Exception as e:
        print(f"Error in graph_all: {e}")
